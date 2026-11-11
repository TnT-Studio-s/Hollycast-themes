<!-- Portions Copyright 2026 The Hollycast Authors -->
# Play Archive

An antique library reading room with wood framing, an olive collection sidebar,
parchment game index, burgundy selection and a large scraped case-art preview.
The official Hollycast banner replaces the concept's Dreamcast name and swirl.

The native sidebar provides All Games, Favourites, Recent, By Year, Search and Settings.
The game index supports wheel, touch, keyboard and controller selection. PLAY
launches the selected game. Metadata and artwork come from the user's library;
no game artwork is redistributed. Missing case art falls back to its cover.

Use the accompanying Play Archive test build. This package requires the native
navigation rectangle, release-year list column and hidden toolbar extensions.
Extract into data/library-themes/play-archive next to the executable and restart.

Run python source/build_theme.py to regenerate the manifest and deterministic ZIP.

Compatibility: requires the renderer support on nexus382/Hollycast branch
`codex/play-archive-signal-bloom`. Older releases cannot load these extensions.
Restart Hollycast after changing themes to refresh the theme fonts.
