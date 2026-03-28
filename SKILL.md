---
name: figures-diagram
description: Generate polished English prompts for academic flowcharts, structure diagrams, concept maps, organization charts, and timelines for image-generation models. Use when Codex needs to turn a non-numeric diagram idea into a professional prompt for thesis figures, paper figures, framework diagrams, process illustrations, or model structure visuals. Do not use for charts with exact numeric values such as line charts, bar charts, scatterplots, heatmaps, or other statistical graphics.
---

# Figures Diagram

Convert a user's diagram idea into a clean, publication-oriented English prompt for an image model, and render it directly when production image generation is requested and credentials are available.

Treat this skill as a prompt-engineering and optional production workflow for non-numeric academic figures.

## Fit Check

Use this skill only for diagram-like visuals:

- flowcharts
- process diagrams
- architecture or model structure diagrams
- concept maps
- organization or taxonomy diagrams
- timelines

Do not use this skill for data charts that depend on precise values or axes. In those cases, use a code-based plotting workflow instead.

## Workflow

### 1. Classify the figure

Identify the requested figure type:

- flowchart for step-by-step processes or algorithms
- structure or architecture diagram for models, systems, or layered designs
- concept map for theoretical relationships or knowledge frameworks
- organization chart for hierarchy or classification
- timeline for chronological development or staged progression

If the type is ambiguous, infer the most likely type from the user's purpose.

### 2. Gather the minimum inputs

Collect or infer:

- figure purpose
- figure type
- main elements or nodes
- relationships between elements
- layout direction
- language of labels
- target venue or style if provided

If the user does not specify all of these, make reasonable academic defaults and state them briefly.

### 3. Decide prompt-only vs production mode

Use prompt-only mode when the user wants:

- a reusable prompt for another image tool
- prompt iteration without spending API credits
- a draft concept before rendering

Use production mode when the user wants:

- the image generated now
- a ready-to-save figure draft
- an OpenRouter-backed render using the configured model

## Default Assumptions

Unless the user says otherwise, use these defaults:

- language: English
- background: white
- style: clean academic style
- resolution: 450 DPI
- typography: readable sans-serif labels
- arrows: clear directional arrows where relevant
- annotation: include concise labels only

Preferred layout defaults:

- top-to-bottom for workflows with stages
- left-to-right for linear processes and pipelines
- center-radial for concept maps

## Output Format

When using this skill, produce four parts when useful:

1. `Figure Type`
2. `Assumptions`
3. `Final Prompt`
4. `Recommended Model`

If the user already gave enough detail, keep `Assumptions` short.

In production mode, also return:

5. `Render Output`

This should briefly state which script was used, which model was used, and where the image was saved.

## Prompt Construction Rules

Build prompts that include:

- the academic purpose of the figure
- the full set of elements and their relationships
- layout instructions
- visual styling instructions
- color palette guidance
- labeling requirements
- readability requirements

Prefer explicit, drawable instructions over abstract advice. Describe every major box, arrow, layer, cluster, or branch that should appear.

## Model Recommendation Rules

Recommend:

- `google/gemini-3.1-flash-image-preview` on OpenRouter as the default production model when direct rendering is requested
- `Nano Banana` or `Nano Banana 2` wording only as a user-facing alias when helpful
- `DALL-E 3` for complex conceptual or multi-relationship diagrams
- `Midjourney` only when the user wants a more stylized conceptual visual rather than the cleanest academic diagram

If the user asks for actual generation through this skill, prefer the configured OpenRouter production path over external tool recommendations.

## Production Rendering

If direct generation is requested, read [references/openrouter-production.md](./references/openrouter-production.md) and use:

- [scripts/render_via_openrouter.py](./scripts/render_via_openrouter.py)

Do not hardcode API secrets into prompts, Markdown, or skill files.

## Template References

Load only what you need:

- For reusable prompt skeletons, read [references/prompt-templates.md](./references/prompt-templates.md).
- For color schemes, styling defaults, and model recommendations, read [references/style-and-tools.md](./references/style-and-tools.md).
- For OpenRouter-based rendering details, read [references/openrouter-production.md](./references/openrouter-production.md).

## Quality Bar

Ensure the final prompt asks for:

- crisp readable text
- uncluttered spacing
- clearly separated levels or stages
- consistent color usage
- publication-ready composition

If the requested figure is too dense to render well in one image, suggest splitting it into two figures before generating the prompt.
