<!-- Portions Copyright 2026 The Hollycast Authors -->
# Harvest Afterglow

A festive autumn and Thanksgiving library theme for Hollycast: a hand-painted
walnut lodge, copper maple garlands, warm lanterns, a harvest moon, velvet
pumpkins, cider, pie, a cornucopia and a little decorative turkey. Cream Alegreya
type, cranberry selections and brass outlines carry the same palette into menus.

## Install

Open **Settings > Library > Browse themes**, select **Harvest Afterglow**, choose
**Download and install**, then **Use theme**.

To install a downloaded ZIP manually:

1. Extract `harvest-afterglow-1.0.0.zip` into a folder named `harvest-afterglow`.
   The ZIP has `theme.json` at its root.
2. Copy that folder into `library-themes` inside the data directory used by your
   Hollycast executable. The final path is
   `library-themes/harvest-afterglow/theme.json`, with `assets` beside it.
3. Restart Hollycast. In **Settings > Library > Library Themes**, select
   **Harvest Afterglow** and a layout.

Keep the manifest, assets and fonts together when installing manually.

## Layouts and controls

- **Harvest Gallery:** a paged cover gallery, normally four columns by two rows,
  with Previous/Next page controls and a live selected-game preview.
- **Fireside List:** a scrolling cover list with system and favourite badges,
  selection by click or navigation, and the same preview and details.
- **Pocket Harvest (portrait):** a separately composed portrait scene, selected
  game preview above the list, and visible Play and Favourite controls. Both
  landscape layouts switch to it automatically in narrow windows.

All three layouts fill the available library width. The backdrop scales to
keep the entire painted scene visible. Game art retains its original proportions.

Cover, Screenshot and Disc select real library media. Unavailable choices follow
the app's disabled-control behavior. A gilded storybook illustration fills blank
preview regions and grid cards without artwork. Titles, descriptions, system,
genre, counts, favourites and page numbers come from the library. The taller
description areas use Hollycast's native text fitting to show the complete
synopsis without scrolling.

Two small maple leaves drift slowly along the outer margins, away from controls.
Launching uses a short, skippable 0.32-second fade into warm brown. All Games,
Continue Playing, Favourites, Filter, settings and input handling remain native.
No sounds, ROMs, game screenshots or game cover art are included.

## Compatibility and verification boundary

Authored against the documented theme format and parser in Nexus Hollycast
`dev` at `f9f8ec342695a2a96411e4a9e5f5f478825cae57` on 2026-11-06.
It uses the existing paged-grid, list-badge, portrait-fallback, font, artwork
selector and image-sweep features. Older builds without those fields can reject
the manifest; use a current build containing those features.

The accompanying `harvest-afterglow-preview.html` uses sample library content to
preview the responsive layout. The theme itself uses Hollycast's native controls.

## Rebuild

From this folder, run `python source/build_theme.py`. Python's standard library
is sufficient. It writes `theme.json`, the adjacent HTML design preview and the
adjacent deterministic `harvest-afterglow-1.0.0.zip`. The manifest is generated
from `source/build_theme.py`; make layout changes there before rebuilding.
Nothing in `source` runs inside Hollycast.

In the community catalogue checkout, use
`python themes/harvest-afterglow/source/build_theme.py --output-dir packages`,
then run `python build_catalog.py` from the repository root. This keeps authoring
exports inside the packages directory.

See `ATTRIBUTION.md`, `LICENSE.txt`, `assets/OFL-Alegreya.txt` and
`source/imagegen-prompts.md` for provenance, licences and generation prompts.
