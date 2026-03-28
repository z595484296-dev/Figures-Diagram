# OpenRouter Production Mode

Use this reference when the user wants the figure rendered directly instead of receiving only a prompt.

## Default Production Model

- OpenRouter model id: `google/gemini-3.1-flash-image-preview`
- User-facing alias: `Nano Banana 2`

As of March 27, 2026, OpenRouter documents this model as an image-generation model that supports `modalities: ["image", "text"]` and optional `image_config` settings such as aspect ratio and image size.

## Credential Rule

Never store the API key inside the skill files.

Use:

- `OPENROUTER_API_KEY`
- `OPENROUTER_IMAGE_MODEL`

The bundled script also falls back to the Windows user environment if the process environment does not already include those values.

## Rendering Script

Use:

- `scripts/render_via_openrouter.py`

Typical usage:

```bash
python scripts/render_via_openrouter.py --prompt "Draw a publication-ready academic flowchart illustrating the proposed research process from data collection to model evaluation." --aspect-ratio 4:3 --output-dir output/figures
```

Or from a prompt file:

```bash
python scripts/render_via_openrouter.py --prompt-file prompt.txt --aspect-ratio 16:9 --output-dir output/figures
```

## What the Script Saves

The script saves:

- the generated image file
- the original prompt text
- the raw JSON response
- any assistant text returned by the model

This makes the workflow easier to audit and reproduce.

## When to Use Production Mode

Use production mode when:

- the user explicitly asks to generate the image now
- the user wants a first rendered draft for iteration
- the figure is conceptual enough that image generation is a good fit

Prefer prompt-only mode when:

- the figure contains dense text that may need manual vector cleanup later
- the user mainly wants a reusable prompt
- the user may send the prompt to another model manually
