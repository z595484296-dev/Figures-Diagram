#!/usr/bin/env python
from __future__ import annotations

import argparse
import base64
import json
import os
from pathlib import Path
from typing import Any, Iterable

import requests


OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
DEFAULT_MODEL = "google/gemini-3.1-flash-image-preview"


def read_windows_user_env(name: str) -> str | None:
    if os.name != "nt":
        return None
    try:
        import winreg

        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Environment") as key:
            value, _ = winreg.QueryValueEx(key, name)
            return value
    except Exception:
        return None


def get_config(name: str, default: str | None = None) -> str | None:
    return os.environ.get(name) or read_windows_user_env(name) or default


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Render an academic diagram prompt through OpenRouter image generation."
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--prompt", help="Direct prompt text to send.")
    group.add_argument("--prompt-file", help="Path to a UTF-8 text file containing the prompt.")
    parser.add_argument("--output-dir", default="output/figures", help="Directory for saved outputs.")
    parser.add_argument("--output-prefix", default="diagram", help="Filename prefix for saved images.")
    parser.add_argument("--model", default=None, help="Override model id.")
    parser.add_argument("--aspect-ratio", default="4:3", help="Aspect ratio, for example 1:1, 4:3, or 16:9.")
    parser.add_argument("--image-size", default=None, help="Optional image size such as 2K or 4K.")
    parser.add_argument("--site-url", default="https://openai.com", help="Optional HTTP-Referer header.")
    parser.add_argument("--site-name", default="Codex Figures Diagram Skill", help="Optional X-Title header.")
    parser.add_argument("--timeout", type=int, default=180, help="Request timeout in seconds.")
    return parser.parse_args()


def load_prompt(args: argparse.Namespace) -> str:
    if args.prompt:
        return args.prompt.strip()
    return Path(args.prompt_file).read_text(encoding="utf-8").strip()


def build_payload(prompt: str, model: str, aspect_ratio: str | None, image_size: str | None) -> dict[str, Any]:
    payload: dict[str, Any] = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "modalities": ["image", "text"],
    }
    image_config: dict[str, str] = {}
    if aspect_ratio:
        image_config["aspect_ratio"] = aspect_ratio
    if image_size:
        image_config["image_size"] = image_size
    if image_config:
        payload["image_config"] = image_config
    return payload


def extract_text(message: dict[str, Any]) -> str:
    content = message.get("content")
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        parts: list[str] = []
        for item in content:
            if isinstance(item, dict) and item.get("type") == "text" and item.get("text"):
                parts.append(str(item["text"]))
        return "\n".join(parts).strip()
    return ""


def iter_image_urls(message: dict[str, Any]) -> Iterable[str]:
    images = message.get("images")
    if isinstance(images, list):
        for image in images:
            if not isinstance(image, dict):
                continue
            image_url = image.get("image_url") or image.get("imageUrl")
            if isinstance(image_url, dict) and image_url.get("url"):
                yield str(image_url["url"])
    content = message.get("content")
    if isinstance(content, list):
        for item in content:
            if not isinstance(item, dict):
                continue
            if item.get("type") != "image_url":
                continue
            image_url = item.get("image_url") or item.get("imageUrl")
            if isinstance(image_url, dict) and image_url.get("url"):
                yield str(image_url["url"])


def save_data_url(url: str, path: Path) -> None:
    header, encoded = url.split(",", 1)
    if ";base64" not in header:
        raise ValueError("Only base64 data URLs are supported.")
    raw = base64.b64decode(encoded)
    path.write_bytes(raw)


def save_remote_image(url: str, path: Path, timeout: int) -> None:
    response = requests.get(url, timeout=timeout)
    response.raise_for_status()
    path.write_bytes(response.content)


def main() -> int:
    args = parse_args()
    api_key = get_config("OPENROUTER_API_KEY")
    if not api_key:
        raise SystemExit("OPENROUTER_API_KEY is not configured.")

    model = args.model or get_config("OPENROUTER_IMAGE_MODEL", DEFAULT_MODEL) or DEFAULT_MODEL
    prompt = load_prompt(args)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    payload = build_payload(prompt, model, args.aspect_ratio, args.image_size)
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": args.site_url,
        "X-Title": args.site_name,
    }

    response = requests.post(
        OPENROUTER_URL,
        headers=headers,
        json=payload,
        timeout=args.timeout,
    )
    response.raise_for_status()
    result = response.json()

    response_path = output_dir / f"{args.output_prefix}_response.json"
    response_path.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")

    choices = result.get("choices") or []
    if not choices:
        raise SystemExit("OpenRouter returned no choices.")
    message = choices[0].get("message") or {}

    prompt_path = output_dir / f"{args.output_prefix}_prompt.txt"
    prompt_path.write_text(prompt, encoding="utf-8")

    assistant_text = extract_text(message)
    if assistant_text:
        (output_dir / f"{args.output_prefix}_assistant.txt").write_text(
            assistant_text, encoding="utf-8"
        )

    image_urls = list(iter_image_urls(message))
    if not image_urls:
        raise SystemExit("OpenRouter returned no images.")

    saved_paths: list[Path] = []
    for index, image_url in enumerate(image_urls, start=1):
        path = output_dir / f"{args.output_prefix}_{index}.png"
        if image_url.startswith("data:image/"):
            save_data_url(image_url, path)
        else:
            save_remote_image(image_url, path, args.timeout)
        saved_paths.append(path)

    print(f"model={model}")
    print(f"prompt_file={prompt_path}")
    print(f"response_file={response_path}")
    for path in saved_paths:
        print(f"image_file={path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
