# Visual Identity Assets

This directory contains the original visual identity created for Python Study Guide.

![Python Study Guide banner](banner.png)

## Available assets

| File | Purpose | Recommended use |
|---|---|---|
| `banner.png` | Current project banner with the name and motto | Main README and project pages |
| `logo.png` | Primary logo with emblem and wordmark on a transparent background | Light backgrounds and presentations |
| `logo-mark.png` | Compact emblem on a transparent background | Avatars, icons, diagrams, and small spaces |
| `repository-preview.png` | Current social preview image | GitHub repository sharing preview |
| `banner.svg` | Editable banner composition that embeds the raster emblem as Base64 data | Layout adjustments at the original design size |
| `repository-preview.svg` | Editable social-preview composition that references `logo-mark.png` as a local file | Layout adjustments at the original design size |

The SVG compositions are not fully vector artwork. `banner.svg` embeds a PNG copy of the emblem, while `repository-preview.svg` links to the local `logo-mark.png` file. They should not be treated as infinitely scalable sources. Use the current PNG exports at their intended dimensions and avoid enlarging new raster placements beyond their source resolution.

## Meaning of the identity

The visual system combines four ideas:

- the geometric serpent represents Python and a continuous learning path;
- the braces represent code and structured ideas;
- the open book represents study and accessible knowledge;
- the connected nodes represent relationships between concepts and progress through practice.

The emblem is an original project mark. It does not reproduce the official Python logo and must not be used to imply affiliation, sponsorship, or endorsement by the Python Software Foundation or another organization.

## Color palette

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
- Prefer `logo.png` on light backgrounds and `banner.png` on dark presentation surfaces.
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
