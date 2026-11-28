# Visual Identity Assets

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

This directory preserves the six original canonical assets referenced by the immutable curriculum manifest. Do not overwrite or relocate those files during a presentation-only update. The approved Learning Hub V1 README banner is a separate 1280 × 400 PNG in `docs/assets/learning-hub/`, fitted without stretching. The original banner SVG remains paired with the original PNG; it is not the source of the new banner.

![Python Study Guide banner](../docs/assets/learning-hub/banner.png)

## Approved Learning Hub presentation exports

The following approved V1 files are stored separately from the immutable curriculum. The raster README banner remains the original approved artwork; the vector banner is a simplified adaptation, not its exact source. Vector exports use self-contained shapes, with no embedded raster images or external resources. Use the dark or light mark on its intended background. The card is for the Learning Hub catalogue; the social preview file is ready for upload in repository settings, but adding it here does not change those settings. All files follow the repository MIT license.

| Asset | SVG source | PNG export | Size |
| --- | --- | --- | --- |
| Vector banner adaptation | [banner-vector.svg](../docs/assets/learning-hub/banner-vector.svg) | [banner-vector-preview.png](../docs/assets/learning-hub/banner-vector-preview.png) | 1280 × 400 |
| Mark for light backgrounds | [logo-mark-light.svg](../docs/assets/learning-hub/logo-mark-light.svg) | [logo-mark-light.png](../docs/assets/learning-hub/logo-mark-light.png) | 512 × 512 |
| Mark for dark backgrounds | [logo-mark.svg](../docs/assets/learning-hub/logo-mark.svg) | [logo-mark.png](../docs/assets/learning-hub/logo-mark.png) | 512 × 512 |
| Horizontal logo | [logo.svg](../docs/assets/learning-hub/logo.svg) | [logo.png](../docs/assets/learning-hub/logo.png) | 1000 × 300 |
| Social preview | [repository-preview.svg](../docs/assets/learning-hub/repository-preview.svg) | [repository-preview.png](../docs/assets/learning-hub/repository-preview.png) | 1280 × 640 |
| Study Guide card | [study-guide-card.svg](../docs/assets/learning-hub/study-guide-card.svg) | [study-guide-card.png](../docs/assets/learning-hub/study-guide-card.png) | 640 × 400 |

## Available assets

| File | Purpose | Recommended use |
|---|---|---|
| [`docs/assets/learning-hub/banner.png`](../docs/assets/learning-hub/banner.png) | Current presentation banner, 1280 × 400 | Main README and localized READMEs |
| `banner.png` | Original canonical banner, 1200 × 400 | Immutable curriculum and historical presentation |
| `logo.png` | Primary logo with emblem and wordmark on a transparent background | Light backgrounds and presentations |
| `logo-mark.png` | Compact emblem on a transparent background | Avatars, icons, diagrams, and small spaces |
| `repository-preview.png` | Legacy social preview image | GitHub repository sharing preview |
| `banner.svg` | Legacy editable banner composition that embeds the raster emblem as Base64 data | Layout adjustments at the original design size |
| `repository-preview.svg` | Editable social-preview composition that references `logo-mark.png` as a local file | Layout adjustments at the original design size |

The SVG compositions are not fully vector artwork. `banner.svg` embeds a PNG copy of the emblem, while `repository-preview.svg` links to the local `logo-mark.png` file. They should not be treated as infinitely scalable sources. Use the current PNG exports at their intended dimensions and avoid enlarging new raster placements beyond their source resolution.

## Current banner identity

The approved banner uses the shared Learning Hub navy `#06111F`, cyan `#00D0C9` and off-white `#F1F5F9`, with Python-specific blue `#3776AB` and yellow `#FFD343` as design tokens. The geometric serpent, braces and book identify the guide; the hexagonal frame is part of the approved banner. The PNG is raster, not a vector master. The legacy palette, meanings and export limitations below describe the original assets only.

## Meaning of the legacy identity

The visual system combines four ideas:

- the geometric serpent represents Python and a continuous learning path;
- the braces represent code and structured ideas;
- the open book represents study and accessible knowledge;
- the connected nodes represent relationships between concepts and progress through practice.

The emblem is an original project mark. It does not reproduce the official Python logo and must not be used to imply affiliation, sponsorship, or endorsement by the Python Software Foundation or another organization.

## Legacy color palette

| Color | Hex | Role |
|---|---|---|
| Deep navy | `#06111F` | Primary dark background |
| Cyan | `#00D0C9` | Code, clarity, and connection |
| Green | `#17C964` | Progress and practice |
| Lime | `#A7F070` | Learning milestones and emphasis |
| Light cyan | `#59E1FF` | Highlights and accessible contrast |
| Slate | `#1F2937` | Supporting neutral tone |

The exported artwork may include smooth transitions between these colors.

## Usage guidance

- Preserve the original proportions.
- Do not stretch, rotate, recolor, or redraw the emblem.
- Keep enough clear space around the mark and wordmark.
- Use the Learning Hub presentation banner for README headers; the original logo and banner are historical assets.
- Use meaningful alternative text whenever an asset appears in documentation.
- Check readability at the final display size before publishing.
- Do not enlarge new raster placements beyond the resolution of their source images.
- Do not place private, personal, proprietary, or confidential information inside project artwork.

## Known non-blocking limitation

`logo-mark.png` is currently `384 × 384` pixels, while `repository-preview.svg` displays it at `440 × 440` pixels. This known upscale is documented for future export refinement and does not block the current repository foundation.

## Creation and review

The identity was created specifically for Python Study Guide with AI-assisted visual exploration and was selected, refined, and reviewed by the project maintainer, Ramon Estevez Rodriguez.

AI assistance does not replace the maintainer's responsibility for originality, suitability, accessibility, or final approval.

## License

Unless a future asset states otherwise, the files in this directory are distributed under the repository's [MIT License](../LICENSE).
