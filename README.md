# Figures Diagram

`figures-diagram` is a Codex skill for academic non-numeric diagram generation.

It converts a user's diagram idea into a polished English prompt for image models and can optionally render the figure directly through an OpenRouter-backed production workflow.

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

Do not use this skill for charts that depend on exact numeric values, such as line charts, bar charts, scatterplots, or heatmaps.

## Core Capabilities

- Classify the requested academic diagram type
- Infer missing figure details when the request is incomplete
- Generate publication-oriented English prompts for image models
- Recommend the most suitable generation model for the figure type
- Render the figure directly through OpenRouter when production mode is requested

## Workflow

The skill follows a compact figure workflow:

1. Classify the figure
2. Gather the minimum inputs
3. Decide prompt-only vs production mode
4. Build a polished academic prompt
5. Render the image directly when credentials are available

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

## Included References

- `references/prompt-templates.md`
  Reusable prompt skeletons for flowcharts, architecture diagrams, concept maps, taxonomies, and timelines
- `references/style-and-tools.md`
  Color palettes, readability defaults, and model recommendations
- `references/openrouter-production.md`
  Production rendering rules, model defaults, and environment setup

## Included Script

`scripts/render_via_openrouter.py` renders diagram prompts through OpenRouter and saves:

- the generated image file
- the original prompt text
- the raw JSON response
- any assistant text returned by the model

Example:

```bash
python scripts/render_via_openrouter.py --prompt "Draw a publication-ready academic flowchart illustrating the proposed research process from data collection to model evaluation." --aspect-ratio 4:3 --output-dir output/figures
```

## Production Model

The default production model is:

- `google/gemini-3.1-flash-image-preview`

The skill may refer to this in user-facing language as:

- `Nano Banana`
- `Nano Banana 2`

## Environment Variables

For production rendering, configure:

- `OPENROUTER_API_KEY`
- `OPENROUTER_IMAGE_MODEL`

The script also supports reading Windows user environment variables.

## Installation

Copy this folder into your Codex skills directory:

```text
$CODEX_HOME/skills/figures-diagram
```

On Windows, this is typically:

```text
C:\Users\<your-user>\.codex\skills\figures-diagram
```

## Example Usage

- `Use $figures-diagram to create an academic concept map prompt for my theoretical framework.`
- `Use $figures-diagram to generate a flowchart for my methodology section.`
- `Use $figures-diagram to render a research-process figure now.`

## Design Principles

- Keep labels crisp and readable
- Prefer uncluttered academic composition over decorative effects
- Use explicit layout and relationship instructions
- Keep prompts drawable and production-oriented
- Use prompt-only mode when direct rendering is unnecessary

## Who This Repository Is For

- Codex users who want a reusable academic figure skill
- thesis and paper writers who need framework and process diagrams
- research workflow builders who want prompt generation plus optional rendering

## License

MIT
