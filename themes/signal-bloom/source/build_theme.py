# Portions Copyright 2026 The Hollycast Authors
# SPDX-License-Identifier: GPL-2.0-or-later
"""Build the Signal Bloom theme manifest and deterministic ZIP package."""

import argparse
import json
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT.parent
INK = "e8f2ff"
MUTED = "a2b7d0"
CYAN = "43e8f2"
CORAL = "ff627f"
NAVY = "070b18"


def element(kind, rect, **fields):
    return {"type": kind, "rect": rect, **fields}


def text(rect, label, size, **fields):
    fields.setdefault("color", INK)
    fields.setdefault("wrap", False)
    fields.setdefault("zIndex", 2)
    return element("text", rect, text=label, fontSize=size, **fields)


def metadata(rect, source, size, **fields):
    fields.setdefault("color", INK)
    fields.setdefault("zIndex", 2)
    return element("metadata", rect, source=source, fontSize=size, **fields)


def play_button(rect):
    return element(
        "button", rect, action="activate", text="PLAY", fontSize=0.04,
        bold=True, color=INK, background="ff627f", borderColor=CYAN, rounding=0.18,
        zIndex=5,
    )


def backdrop(filename):
    return [
        element("image", [0, 0, 1, 1], source=filename, fit="stretch",
                zIndex=-100, bleed=True),
        # Independent empty fallbacks avoid ever enlarging a cover as background art.
        # Fanart draws over the screenshot when both exist; otherwise the static art remains.
        element("artwork", [0, 0, 1, 1], source="screenshot", fallback="none",
                fit="cover", zIndex=-99, bleed=True),
        element("artwork", [0, 0, 1, 1], source="fanart", fallback="none",
                fit="cover", zIndex=-98, bleed=True),
        element("panel", [0, 0, 1, 1], color="070b188c", endColor="070b18e8",
                zIndex=-97, bleed=True),
        element("panel", [0, 0, 1, 0.105], color="050919e8",
                endColor="050919b0", zIndex=-90, bleed=True),
        element("panel", [0, 0.103, 1, 0.002], color="258ca0aa",
                zIndex=-80, bleed=True),
    ]


def info_elements(title_rect, date_rect, overview_label_rect,
                  overview_rect, button_rect, date_label_width=0.082):
    return [
        metadata(title_rect, "title", 0.043, bold=True, wrap=False,
                 text="SELECT A GAME"),
        text([date_rect[0], date_rect[1], date_label_width, date_rect[3]],
             "RELEASED", 0.016, color=MUTED),
        metadata([date_rect[0] + date_label_width + 0.01, date_rect[1],
                 date_rect[2] - date_label_width - 0.01, date_rect[3]],
                "releaseDate", 0.019, color=CYAN, wrap=False),
        text(overview_label_rect, "OVERVIEW", 0.017, color=CYAN, bold=True),
        metadata(overview_rect, "description", 0.018, color=INK, wrap=True),
        play_button(button_rect),
    ]


def wide_gallery():
    layout = {
        "id": "signal-gallery",
        "name": "Signal Gallery",
        "mode": "carousel",
        "browser": [0.04, 0.205, 0.92, 0.43],
        "columns": 5,
        "itemAspect": 0.78,
        "spacing": 14,
        "showTitles": False,
        "fontSize": 0.021,
        "minItemWidth": 80,
        "inactiveOpacity": 0.94,
        "canvasAspect": 16 / 9,
        "narrowLayout": "signal-portrait",
        "narrowAspect": 1.15,
    }
    layout.update(common_layout())
    layout["selectorStyle"] = "outline"
    elements = backdrop("assets/signal-bloom-landscape.png")
    elements += [
        text([0.05, 0.125, 0.38, 0.047], "COLLECTION", 0.032, bold=True),
        element("stat", [0.84, 0.133, 0.073, 0.027], source="gameCount",
                fontSize=0.019, color=CYAN, align="right", zIndex=2),
        text([0.92, 0.133, 0.045, 0.027], "GAMES", 0.016, color=MUTED),
    ]
    elements += info_elements(
        [0.06, 0.684, 0.62, 0.057],
        [0.06, 0.754, 0.33, 0.032],
        [0.06, 0.802, 0.26, 0.027],
        [0.06, 0.837, 0.65, 0.112],
        [0.79, 0.766, 0.155, 0.082],
    )
    layout["elements"] = elements
    return layout


def wide_list():
    layout = {
        "id": "signal-index",
        "name": "Signal Index",
        "mode": "list",
        "browser": [0.045, 0.185, 0.46, 0.77],
        "showArtwork": True,
        "rowHeight": 0.071,
        "fontSize": 0.023,
        "canvasAspect": 16 / 9,
        "narrowLayout": "signal-portrait",
        "narrowAspect": 1.15,
        "list": {"selectOnHover": False},
    }
    layout.update(common_layout())
    layout["selectorStyle"] = "outline"
    elements = backdrop("assets/signal-bloom-landscape.png")
    elements += [
        text([0.05, 0.125, 0.38, 0.047], "COLLECTION", 0.032, bold=True),
        element("stat", [0.84, 0.133, 0.073, 0.027], source="gameCount",
                fontSize=0.019, color=CYAN, align="right", zIndex=2),
        text([0.92, 0.133, 0.045, 0.027], "GAMES", 0.016, color=MUTED),
    ]
    elements += info_elements(
        [0.56, 0.215, 0.37, 0.072],
        [0.56, 0.305, 0.37, 0.04],
        [0.56, 0.38, 0.30, 0.034],
        [0.56, 0.425, 0.36, 0.34],
        [0.56, 0.84, 0.36, 0.075],
    )
    layout["elements"] = elements
    return layout


def portrait_list():
    layout = {
        "id": "signal-portrait",
        "name": "Signal Pocket",
        "mode": "list",
        "browser": [0.055, 0.515, 0.89, 0.385],
        "showArtwork": True,
        "rowHeight": 0.046,
        "fontSize": 0.017,
        "canvasAspect": 2 / 3,
        "toolbarLogoHeight": 44,
        "list": {"selectOnHover": False},
    }
    layout.update(common_layout(logo_height=44))
    layout["selectorStyle"] = "outline"
    elements = backdrop("assets/signal-bloom-portrait.png")
    elements += [
        text([0.07, 0.035, 0.60, 0.045], "COLLECTION", 0.028, bold=True),
        element("stat", [0.78, 0.044, 0.10, 0.027], source="gameCount",
                fontSize=0.018, color=CYAN, align="right", zIndex=2),
        text([0.89, 0.044, 0.075, 0.027], "GAMES", 0.015, color=MUTED),
    ]
    elements += info_elements(
        [0.08, 0.125, 0.83, 0.056],
        [0.08, 0.192, 0.83, 0.032],
        [0.08, 0.239, 0.40, 0.027],
        [0.08, 0.272, 0.82, 0.192],
        [0.27, 0.918, 0.46, 0.058],
        date_label_width=0.16,
    )
    layout["elements"] = elements
    return layout


def common_layout(logo_height=64):
    return {
        "activation": "doubleClick",
        "toolbar": "compact",
        "toolbarLogo": "assets/hollycast-banner.png",
        "toolbarLogoHeight": logo_height,
        "toolbarSelectedTextColor": INK,
        "background": NAVY,
        "textColor": INK,
        "selectedTextColor": INK,
        "selectorColor": "102338aa",
        "selectorBorderColor": CYAN,
        "separatorColor": "23899b77",
        "rounding": 9,
        "artworkSource": "cover",
        "requiredMedia": ["cover", "fanart", "screenshot"],
        "showItemActions": False,
        "showFavouriteMarker": False,
        "hoverDetails": False,
        "showInfoTooltip": False,
    }


THEME = {
    "formatVersion": 1,
    "id": "signal-bloom",
    "name": "Signal Bloom",
    "author": "The Hollycast Authors",
    "description": 'A midnight-neon cover carousel with selected-game backgrounds, cyan selection and coral PLAY controls. Requires the new carousel-enabled Hollycast development build.',
    "baseTheme": 0,
    "fonts": {"bold": "assets/Jura-wght.ttf"},
    "colors": {
        "Text": INK,
        "TextDisabled": MUTED,
        "WindowBg": NAVY,
        "ChildBg": "081020",
        "PopupBg": "0b1427",
        "Border": "287184",
        "BorderShadow": "00000066",
        "FrameBg": "101a30",
        "FrameBgHovered": "172a47",
        "FrameBgActive": "1d3958",
        "TitleBg": NAVY,
        "TitleBgActive": "101a30",
        "TitleBgCollapsed": NAVY,
        "MenuBarBg": "081020",
        "ScrollbarBg": "050918",
        "ScrollbarGrab": "246477",
        "ScrollbarGrabHovered": "34a0b0",
        "ScrollbarGrabActive": CYAN,
        "CheckMark": CYAN,
        "SliderGrab": "328da4",
        "SliderGrabActive": CYAN,
        "Button": "132844",
        "ButtonHovered": "1d4162",
        "ButtonActive": CORAL,
        "Header": "102d43",
        "HeaderHovered": "17455e",
        "HeaderActive": "ff627f",
        "Separator": "27839766",
        "SeparatorHovered": "32b8ca",
        "SeparatorActive": CYAN,
        "ResizeGrip": "43e8f255",
        "ResizeGripHovered": "43e8f2aa",
        "ResizeGripActive": CYAN,
        "InputTextCursor": CYAN,
        "Tab": "111e34",
        "TabHovered": "1d3b56",
        "TabSelected": "17394f",
        "TabSelectedOverline": CORAL,
        "TabDimmed": "0b1424",
        "TabDimmedSelected": "13243a",
        "TabDimmedSelectedOverline": "287184",
        "PlotLines": CYAN,
        "PlotLinesHovered": INK,
        "PlotHistogram": CORAL,
        "PlotHistogramHovered": "ff94a6",
        "TableHeaderBg": "102038",
        "TableBorderStrong": "287184",
        "TableBorderLight": "28718455",
        "TableRowBg": "00000000",
        "TableRowBgAlt": "43e8f20d",
        "TextLink": CYAN,
        "TextSelectedBg": "32d9e055",
        "TreeLines": "287184",
        "DragDropTarget": CYAN,
        "DragDropTargetBg": "43e8f233",
        "UnsavedMarker": CORAL,
        "NavCursor": CYAN,
        "NavWindowingHighlight": "e8f2ffcc",
        "NavWindowingDimBg": "050918aa",
        "ModalWindowDimBg": "050918bb",
    },
    "layouts": [wide_gallery(), wide_list(), portrait_list()],
}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, default=OUTPUT)
    output_dir = parser.parse_args().output_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    manifest = json.dumps(THEME, ensure_ascii=False, indent=2) + "\n"
    (ROOT / "theme.json").write_text(manifest, encoding="utf-8", newline="\n")

    files = sorted(path for path in ROOT.rglob("*") if path.is_file()
                   and "__pycache__" not in path.parts)
    total_size = sum(path.stat().st_size for path in files)
    if len(files) > 256 or total_size > 64 * 1024 * 1024:
        raise ValueError("Theme exceeds Hollycast package limits")

    destination = output_dir / "signal-bloom-1.0.0.zip"
    with ZipFile(destination, "w", compression=ZIP_DEFLATED, compresslevel=9) as archive:
        for path in files:
            entry = ZipInfo(path.relative_to(ROOT).as_posix(), (2026, 11, 9, 0, 0, 0))
            entry.compress_type = ZIP_DEFLATED
            entry.create_system = 3
            entry.external_attr = 0o100644 << 16
            archive.writestr(entry, path.read_bytes(), compresslevel=9)
    print(f"Created {destination} ({destination.stat().st_size:,} bytes; {len(files)} files)")


if __name__ == "__main__":
    main()
