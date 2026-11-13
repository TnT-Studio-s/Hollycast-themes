# Blue Hour

A cinematic Hollycast library theme with a midnight-blue palette, spacious cover row and full-screen game artwork.

## Install

Once listed in the community catalogue, open Settings > Library > Browse themes, select Blue Hour, choose Download and install, then Use theme.

For manual installation, extract blue-hour-1.0.0.zip into a new library-themes/blue-hour/ folder in Hollycast's data directory. theme.json must be directly inside that folder. Restart Hollycast, select Blue Hour in Settings > Library, and choose Cinema. The folder and manifest ID must both be blue-hour. Installation never requires replacing app files.

Cinema automatically switches to Portrait below an available width/height ratio of 1.2. Portrait can also be selected explicitly. Library Scale changes how many covers fit on a page. Both layouts use the full window, without the standard app headers or a centred fixed-aspect canvas.

## Controls

- Click or tap a cover to preview it. Double-click or confirm to launch through Hollycast's normal launch path and configured save-loading preferences.
- Use arrows or the D-pad to browse. Page Up / Page Down, the mouse wheel, or the visible arrow buttons move between cover pages.
- The star toggles the selected game's persistent favourite state. All Games, Continue Playing, Favourites, DCnet, Settings and search are in the slim theme-authored navigation bar. DCnet keeps the theme's navigation and artwork around Hollycast's live dashboard. Choose All Games, Continue Playing or Favourites to return to the library. The Hollycast wordmark also opens the app menu.
- Resume loads the latest available manual state or autosave. It is disabled when no save is available. Start Fresh explicitly starts without loading a state, preserving the user's automatic-save preferences.
- Open a game's normal context menu (right-click, long press, or the platform's game-menu input) for explicit Resume and Start Fresh actions.

## Artwork and metadata

All game art and metadata are loaded from the user's library. Fanart is preferred for the full-screen background; a screenshot shows underneath it when fanart is unavailable. Without either, the theme uses its own navy/blue gradient. Missing covers use the included original disc placeholder. The right-hand card shows the actual latest save-state thumbnail and date when a state is available, otherwise gameplay artwork. Game/page counts and the clock use real app/system data. Missing metadata stays blank.

The package contains no ROMs, game artwork, mockup imagery, external fonts, scripts, remote URLs or account data. No Sonic artwork is built into the theme. Configure local ES-DE media or Hollycast's artwork providers to populate the selected-game backgrounds.

## Compatibility

Requires the shared renderer support in [Hollycast PR #69](https://github.com/nexus382/Hollycast/pull/69), commit `aeddc1441`. That support must be merged and included in a build before installing this theme on an ordinary Hollycast release.

Requires the shared theme extensions implemented alongside this package: theme-authored library navigation actions; DCnet page layouts; clock elements; single-row pagedGrid.selectedScale; resume and startFresh button actions; saved/unsaved visibility; savestate artwork and saveDate metadata. The theme uses the same layered elements and image-backed controls as Demo Disc. The app-side implementation adds reusable actions and data bindings; it contains no theme-specific layout, colors or IDs. Older Hollycast builds reject these fields; include the renderer changes in a Hollycast release before advertising this theme as compatible with that release. Tested in a native macOS arm64 Debug/OpenGL build of that commit, with wide and portrait library/DCnet layouts, mouse selection, search and navigation. Actual emulation was not launched during visual checks; the shared renderer's launch intent is covered by automated tests.

The cover row pages rather than scrolling continuously. The profile symbol is a neutral local icon; Hollycast does not expose an online player avatar. Save files do not provide level names, so the save card displays the real save date instead of invented location text.

## Licence and credits

Copyright 2026 The Hollycast Authors. Theme manifest, documentation and original UI assets: GPL-2.0-or-later; see LICENSE. The placeholder, navigation states and neutral profile icon were drawn procedurally for this theme. Game artwork displayed by the app remains the property of its respective owners and is not distributed with the package. This is an unofficial visual homage and is not affiliated with Sony or PlayStation.

## Rebuilding the repository contribution

From the Hollycast-themes repository root, regenerate the original UI shapes with `python3 tools/generate_blue_hour_assets.py`, then run `python3 build_catalog.py` and `python3 build_catalog.py --check`. The package does not include the generator or catalogue screenshots.
