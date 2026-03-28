# Style and Tool Defaults

## Recommended Models

### Nano Banana / Nano Banana 2

Use first for:

- flowcharts
- architecture diagrams
- process diagrams
- academic structure diagrams

Why:

- strongest fit for clean diagram-style outputs
- usually better for publication-oriented organization and readability

Current production default in this skill:

- OpenRouter model id: `google/gemini-3.1-flash-image-preview`

### DALL-E 3

Use for:

- complex concept maps
- framework diagrams with many labeled relationships
- diagrams that require better interpretation of dense descriptions

Why:

- stronger prompt understanding for complex structures

### Midjourney

Use for:

- visually expressive concept visuals
- stylized cover-like framework illustrations

Avoid as the first choice when the user needs the cleanest academic labeling.

## Color Palettes

### Nature or Science-Inspired Palette

- blue: `#2E86AB`
- rose: `#A23B72`
- orange: `#F18F01`
- brick red: `#C73E1D`
- yellow-green: `#95C623`

### Minimal Academic Palette

- deep blue: `#1D3557`
- medium blue: `#457B9D`
- light blue: `#A8DADC`
- off-white: `#F1FAEE`
- brick red: `#E63946`

## Color Usage Rules

- blue family: inputs, sources, or general modules
- orange family: core processing or focal mechanism
- gray family: auxiliary steps
- red dashed outline: innovation or emphasis
- green family: outputs, outcomes, or completion states

## Readability Rules

Always ask for:

- clear label legibility
- balanced whitespace
- uncluttered composition
- consistent iconography or box style
- arrow direction that is easy to follow

## Language Rules

If the user requests an English academic figure, keep:

- node labels in English
- style descriptors in English
- concise wording for all labels

If the figure will be used in a paper, avoid decorative or poster-like effects unless the user explicitly asks for them.
