# Christmas Morning

A standalone Hollycast library theme inspired by a nostalgic Christmas morning:
flat ivory serif lettering and holly, a straight cover list, cranberry selections,
brass-gold outlines, a Christmas-room CRT preview, and matching Play/Favourite and
artwork controls. A separate portrait composition is included.

## Install

1. Extract `christmas-morning-1.0.0.zip` into a new folder named
   `christmas-morning`. The ZIP has `theme.json` directly at its root.
2. Put that folder in `library-themes/` inside Hollycast's data directory, or
   import the extracted folder using Hollycast's theme installer.
3. Restart Hollycast. Choose **Settings > Library > Library Themes**, select
   **Christmas Morning**, and choose the **Christmas Morning** layout.

The final path must end in `christmas-morning/theme.json`, with `assets/` beside
it. This is Hollycast library theme format 1. Fonts and images are local to the
package; installing it needs no Python, font installation, network connection,
or plugin.

**Requires the Christmas Morning list-renderer update.** Verification used the
macOS arm64 build `ci-dev-41243457232-18-g01330d784` plus the shared list parser
and keyboard-preview changes described in [COMPATIBILITY.md](COMPATIBILITY.md).
The base version alone is insufficient. Older builds reject the optional `list`
field. No compatible published release is asserted; publish this listing only
when the renderer update is available to catalogue users. The catalogue does
not currently enforce a minimum app version.

## Use

- Click a cover/title to select a game. Scroll, drag, or use keyboard/controller
  navigation to browse. Double-click, confirm, or press **Play** to launch.
- The CRT starts on **Screenshot** when that game has one; otherwise it uses
  **Cover**. **Cover**, **Screenshot**, and **Disc** are live artwork controls.
  Missing artwork choices are disabled, and no artwork leaves the CRT empty.
- The television has fine scanlines and a subtle RGB phosphor mask, with no grain.
  Selecting another game produces a visible 0.65-second channel cut: the tube
  darkens to a luminous rolling raster line, then the new picture fades in. Browsing and Play
  remain responsive throughout; the effect never covers the surrounding UI.
- **Favourite** toggles the selected game's saved favourite and list star.
  All Games, Continue Playing, Favourites, Filter, and Settings remain native.
- Every row shows its actual system when known. Saved favourites get a filled
  gold **Favourite** badge with a dark star and label, so they stay identifiable
  without selecting them.
- The title, developer, genre, release date, player count and synopsis bind to
  real metadata. Unknown fields are omitted. The synopsis scrolls for long text.
- Narrow windows automatically use the portrait composition. Both layouts retain
  visible launch and favourite controls.
- Launch fades briefly to warm ivory; a fresh press skips the transition.

The decorative title, holly branding, and room are images. The game list, selected
game art, metadata, artwork choices, favourite state, and Play remain native and
interactive. Actual library content and native list behavior determine the
running screen. No game art or ROMs are bundled.

## Sources and rebuilding

The generated artwork uses the built-in imagegen tool; exact prompts and reference
roles are in [source/imagegen-prompts.md](source/imagegen-prompts.md).
The imagegen PNG alpha channels are retained unchanged. Original CRT effect
textures are generated procedurally with `python3 source/generate_crt.py` (Pillow
is needed only to rebuild those textures). The bundled fonts and their
reproducible preparation are documented in [source/FONTS.md](source/FONTS.md).

From this folder, rebuild the manifest with:

```sh
python3 source/generate_manifest.py
```

From the Hollycast-themes repository root, generate the catalogue package with:

```sh
python3 build_catalog.py
python3 build_catalog.py --check
```

FontTools is needed only to rebuild fonts from their retained upstream source.
Nothing in `source/` is executed by Hollycast.

The manifest, original artwork, CRT textures, authoring scripts and documentation
use [GPL-2.0-or-later](LICENSE.txt). Font software uses the bundled
[SIL Open Font License](assets/OFL-LibreBaskerville.txt). See
[ATTRIBUTION.md](ATTRIBUTION.md) for asset provenance and notices.
