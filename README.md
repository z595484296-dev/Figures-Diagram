# Figures Diagram

Codex skill for academic non-numeric diagram generation and OpenRouter-backed rendering.

This repository packages a reusable workflow for turning diagram ideas into polished English prompts for image models and, when requested, directly rendering publication-oriented draft figures.

## Highlights

- Prompt engineering for flowcharts, frameworks, concept maps, taxonomies, and timelines
- Academic defaults for layout, readability, color usage, and labeling
- Prompt-only mode for reusable figure ideation
- Production mode for direct OpenRouter image rendering
- Environment-variable based credential handling instead of hardcoded secrets

## Best Fit

Use this skill for:

- flowcharts
- process diagrams
- architecture diagrams
- model structure diagrams
- concept maps
- theoretical framework diagrams
- organization charts
- taxonomy diagrams
- timelines

Do not use it for numeric charts such as line charts, bar charts, scatterplots, or heatmaps.

## Workflow

1. Classify the figure type
2. Gather or infer the minimum inputs
3. Choose prompt-only or production mode
4. Build a polished academic prompt
5. Render through OpenRouter when direct generation is requested

## Repository Layout

```text
SKILL.md
agents/
  openai.yaml
references/
  openrouter-production.md
  prompt-templates.md
  style-and-tools.md
scripts/
  render_via_openrouter.py
```

## Quick Start

Install into your Codex skills directory:

```text
$CODEX_HOME/skills/figures-diagram
```

Typical Windows path:

```text
C:\Users\<your-user>\.codex\skills\figures-diagram
```

Example prompts:

- `Use $figures-diagram to create an academic concept map prompt for my theoretical framework.`
- `Use $figures-diagram to generate a methodology flowchart prompt.`
- `Use $figures-diagram to render a research-process figure now.`

## Production Rendering

The bundled script renders prompts through OpenRouter and saves:

- the generated image
- the original prompt text
- the raw JSON response
- any assistant text returned by the model

Example:

```bash
python scripts/render_via_openrouter.py --prompt "Draw a publication-ready academic flowchart illustrating the proposed research process from data collection to model evaluation." --aspect-ratio 4:3 --output-dir output/figures
```

Default production model:

- `google/gemini-3.1-flash-image-preview`

User-facing aliases may refer to this as:

- `Nano Banana`
- `Nano Banana 2`

## Environment Variables

- `OPENROUTER_API_KEY`
- `OPENROUTER_IMAGE_MODEL`

The rendering script also supports Windows user environment variables.

## Companion Repository

- `Thesis-Pipeline` for proposal drafting, literature retrieval, and methodology planning

## Design Principles

- Keep labels crisp and readable
- Prefer uncluttered academic composition over decorative effects
- Use explicit layout and relationship instructions
- Keep prompts drawable and production-oriented
- Use prompt-only mode when direct rendering is unnecessary

## License

MIT
