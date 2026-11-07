# Portions Copyright 2026 The Hollycast Authors
# SPDX-License-Identifier: GPL-2.0-or-later
"""Build Harvest Afterglow's manifest, design preview and deterministic ZIP."""

import argparse
import json
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo


ROOT = Path(__file__).resolve().parents[1]
IVORY = "fff1d7"
GOLD = "e6bd72"
MUTED = "d8bea0"
CRANBERRY = "782e40"


def element(kind, rect, **fields):
    return {"type": kind, "rect": rect, **fields}


def text(rect, label, size, **fields):
    return element("text", rect, text=label, fontSize=size, color=IVORY,
                   wrap=False, **fields)


def panel(rect):
    x, y, w, h = rect
    # A thin brass edge surrounds a translucent walnut surface. All browser
    # decoration stays behind native items and their input regions.
    return [
        element("panel", rect, color="b37b455e", rounding=14, zIndex=-80),
        element("panel", [x + .001, y + .0018, w - .002, h - .0036],
                color="24160fe8", endColor="140f0df2", rounding=13, zIndex=-79),
    ]


def button(rect, action, label, size=.021, **fields):
    return element("button", rect, action=action, text=label, fontSize=size,
                   color=IVORY, background="302018ed", borderColor="b7824c",
                   rounding=.15, **fields)


def favourite(rect, size):
    return button(rect, "favourite", "Favourite", size, icon="star",
                  selectedIcon="star-filled", selectedText="Saved",
                  selectedBackground=GOLD, selectedColor="21150f",
                  selectedBorderColor=GOLD)


def art_buttons(x, y, width, height, size):
    result = []
    for index, (source, label) in enumerate([
        ("cover", "Cover"), ("screenshot", "Screenshot"), ("disc", "Disc")
    ]):
        result.append(button([round(x + index * width / 3, 6), y,
                              round(width / 3 - .006, 6), height],
                             "artwork", label, size, source=source,
                             selectedBackground=GOLD,
                             selectedColor="21150f", selectedBorderColor=GOLD))
    return result


def decorations(portrait=False):
    image = "harvest-portrait.png" if portrait else "harvest-lodge.png"
    result = [element("image", [0, 0, 1, 1], source="assets/" + image,
                      fit="stretch", zIndex=-100),
              element("panel", [0, 0, 1, .105], color="1b110bbc",
                      endColor="1b110b00", zIndex=-90)]
    # Native sweep animation is clipped to the margins, never over games or
    # controls. Only two sprites animate; there is no script or particle engine.
    for x, seconds in ((.012, 23), (.958, 31)):
        result.append(element("image", [x, .23, .03, .55],
                              source="assets/maple-leaf.png", color="ffffff94",
                              sweepSeconds=seconds, zIndex=-20))
    result.append(element("panel", [0, 0, 1, 1], color="24160f",
                          when="launching", launchFadeFrom=0, zIndex=90, bleed=True))
    return result


COMMON = {
    "activation": "doubleClick", "toolbar": "compact",
    "toolbarSelectedTextColor": IVORY, "background": "21150f",
    "textColor": IVORY, "selectedTextColor": IVORY,
    "selectorColor": "782e40ec", "selectorBorderColor": GOLD,
    "separatorColor": "b7824c40", "rounding": 8,
    "artworkSource": "cover", "showItemActions": False,
    "showFavouriteMarker": True, "hoverDetails": False,
    "showInfoTooltip": False, "previewSource": "screenshot",
    "placeholder": "assets/storybook-cover.png", "launch": {"seconds": .32},
}


def landscape(mode):
    grid = mode == "grid"
    layout = {
        **COMMON, "id": "harvest-gallery" if grid else "fireside-list",
        "name": "Harvest Gallery" if grid else "Fireside List", "mode": mode,
        # With no fixed canvas aspect, these rectangles follow the full library width.
        "browser": [.040, .176, .569, .691],
        "fontSize": .024, "spacing": 10 if grid else 0,
        "narrowLayout": "pocket-harvest", "narrowAspect": 1.15,
    }
    if grid:
        layout.update(columns=4, itemAspect=.95, minItemWidth=96,
                      inactiveOpacity=.94, showTitles=True,
                      pagedGrid={"rows": 2, "padding": 7})
    else:
        layout.update(showArtwork=True, rowHeight=.064,
                      list={"systemBadge": True, "favouriteBadge": True,
                            "favouriteColor": GOLD, "selectOnHover": False})
    elements = decorations() + panel([.025, .112, .600, .843])
    elements += panel([.641, .112, .334, .843])
    elements += [
        text([.040, .025, .68, .063], "Harvest Afterglow", .047, bold=True),
        text([.040, .127, .40, .032], "Your collection" if grid else "Fireside collection", .025),
        element("stat", [.523, .131, .039, .026], source="gameCount",
                fontSize=.021, color=GOLD, align="right"),
        text([.570, .131, .041, .025], "games", .019),
        element("metadata", [.661, .127, .294, .068], source="title",
                fontSize=.031, color=IVORY, bold=True),
        element("metadata", [.661, .205, .294, .028], fields=["system", "genre"],
                separator="  /  ", fontSize=.019, color=GOLD, wrap=False),
        element("panel", [.659, .249, .298, .251], color="b7824c88", rounding=8),
        element("panel", [.660, .251, .296, .247], color="100d0b", rounding=7),
        element("artwork", [.663, .254, .290, .241], source="preview",
                fit="contain", fallbackImage="assets/storybook-cover.png", rounding=5),
    ]
    elements += art_buttons(.661, .519, .300, .042, .019)
    elements += [
        # The native fitter wraps the full synopsis into the enlarged region.
        element("details", [.661, .578, .294, .287], fields=["description"],
                columns=1, autoFit=True, fontSize=.020, color=MUTED),
        {**button([.661, .892, .170, .043], "activate", "Play", .026),
         "background": CRANBERRY, "borderColor": GOLD},
        favourite([.843, .892, .112, .043], .019),
        button([.040, .892, .092, .042], "previousPage" if grid else "previous", "Previous"),
        button([.516, .892, .092, .042], "nextPage" if grid else "next", "Next"),
        text([.194, .903, .084, .026], "PAGE" if grid else "SELECTED", .018),
        element("stat", [.286, .898, .050, .033], source="page" if grid else "position",
                fontSize=.025, color=GOLD, align="right"),
    ]
    if grid:
        elements += [
            text([.343, .898, .023, .033], "/", .023, align="center"),
            element("stat", [.372, .898, .075, .033], source="pageCount",
                    fontSize=.025, color=MUTED),
        ]
    layout["elements"] = elements
    return layout


def portrait():
    layout = {
        **COMMON, "id": "pocket-harvest", "name": "Pocket Harvest (portrait)",
        "mode": "list",
        "browser": [.060, .484, .880, .392], "fontSize": .018,
        "rowHeight": .048, "spacing": 0, "showArtwork": True,
        "list": {"favouriteBadge": True, "favouriteColor": GOLD, "selectOnHover": False},
    }
    elements = decorations(True) + panel([.040, .112, .920, .864])
    elements += [
        text([.055, .025, .890, .063], "Harvest Afterglow", .039, bold=True, align="center"),
        element("panel", [.055, .129, .310, .244], color="b7824c88", rounding=8),
        element("panel", [.057, .131, .306, .240], color="100d0b", rounding=7),
        element("artwork", [.060, .134, .300, .234], source="preview", fit="contain",
                fallbackImage="assets/storybook-cover.png", rounding=5),
        element("metadata", [.398, .130, .542, .049], source="title",
                fontSize=.023, color=IVORY, bold=True),
        element("metadata", [.398, .189, .542, .029], fields=["system", "genre"],
                separator="  /  ", fontSize=.016, color=GOLD),
        element("details", [.398, .230, .542, .138], fields=["description"],
                columns=1, autoFit=True, fontSize=.017, color=MUTED),
    ]
    elements += art_buttons(.060, .389, .886, .037, .016)
    elements += [
        text([.060, .443, .650, .026], "Your collection", .019),
        element("stat", [.860, .443, .080, .026], source="gameCount",
                fontSize=.019, color=GOLD, align="right"),
        {**button([.060, .907, .470, .052], "activate", "Play", .026),
         "background": CRANBERRY, "borderColor": GOLD},
        favourite([.550, .907, .390, .052], .020),
    ]
    layout["elements"] = elements
    return layout


THEME = {
    "formatVersion": 1, "id": "harvest-afterglow", "name": "Harvest Afterglow",
    "author": "The Hollycast Authors",
    "description": "A candlelit Thanksgiving lodge with painted maple leaves, a harvest feast, "
                   "cranberry and brass controls, storybook typography, a full-width cover gallery, "
                   "a tall fireside list, fitted game descriptions, and a dedicated portrait layout.",
    "baseTheme": 0,
    "fonts": {"body": "assets/Alegreya-Regular.ttf", "bold": "assets/Alegreya-Bold.ttf"},
    "colors": {
        "Text": IVORY, "TextDisabled": MUTED, "WindowBg": "21150f", "ChildBg": "21150f",
        "PopupBg": "291b16", "Border": "a57449", "BorderShadow": "00000044",
        "FrameBg": "39251c", "FrameBgHovered": "583b2a", "FrameBgActive": "694631",
        "TitleBg": "21150f", "TitleBgActive": "38251c", "TitleBgCollapsed": "21150f",
        "MenuBarBg": "281a14", "ScrollbarBg": "21150f00", "ScrollbarGrab": "98674088",
        "ScrollbarGrabHovered": "bd8d57cc", "ScrollbarGrabActive": GOLD,
        "CheckMark": GOLD, "SliderGrab": "c28a50", "SliderGrabActive": GOLD,
        "Button": "3e291e", "ButtonHovered": "5d3a29", "ButtonActive": CRANBERRY,
        "Header": "672b39", "HeaderHovered": "874153", "HeaderActive": "782e40",
        "Separator": "9d6d405c", "SeparatorHovered": "bd8d57", "SeparatorActive": GOLD,
        "ResizeGrip": "b7824c55", "ResizeGripHovered": "b7824caa", "ResizeGripActive": GOLD,
        "InputTextCursor": GOLD, "Tab": "34231b", "TabHovered": "754736",
        "TabSelected": CRANBERRY, "TabSelectedOverline": GOLD, "TabDimmed": "291c17",
        "TabDimmedSelected": "51312b", "TabDimmedSelectedOverline": "b7824c",
        "PlotLines": GOLD, "PlotLinesHovered": IVORY,
        "PlotHistogram": "c88044", "PlotHistogramHovered": GOLD,
        "TableHeaderBg": "3c281e", "TableBorderStrong": "96643d",
        "TableBorderLight": "96643d44", "TableRowBg": "00000000", "TableRowBgAlt": "c08a4310",
        "TextLink": GOLD, "TextSelectedBg": "a44e6677", "TreeLines": "96643d",
        "DragDropTarget": GOLD, "DragDropTargetBg": "e6bd7233", "UnsavedMarker": GOLD,
        "NavCursor": GOLD, "NavWindowingHighlight": "fff1d7cc",
        "NavWindowingDimBg": "100b0aaa", "ModalWindowDimBg": "100b0ab8",
    },
    "layouts": [landscape("grid"), landscape("list"), portrait()],
}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, default=ROOT.parent)
    output_dir = parser.parse_args().output_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    manifest = json.dumps(THEME, ensure_ascii=False, indent=2) + "\n"
    (ROOT / "theme.json").write_text(manifest, encoding="utf-8", newline="\n")
    template = (ROOT / "source" / "preview-template.html").read_text(encoding="utf-8")
    preview = template.replace("/* THEME_DATA */", "const theme = " + manifest.strip() + ";")
    (output_dir / "harvest-afterglow-preview.html").write_text(preview, encoding="utf-8", newline="\n")
    # Theme ZIPs require theme.json at the root. A fixed timestamp and sorted
    # paths keep the archive reproducible; no machine-local paths are stored.
    destination = output_dir / "harvest-afterglow-1.0.0.zip"
    files = sorted(path for path in ROOT.rglob("*") if path.is_file()
                   and "__pycache__" not in path.parts and path.name != "listing.json")
    if len(files) > 256 or sum(path.stat().st_size for path in files) > 64 * 1024 * 1024:
        raise ValueError("Theme exceeds Hollycast's package limits")
    with ZipFile(destination, "w", compression=ZIP_DEFLATED, compresslevel=9) as archive:
        for path in files:
            entry = ZipInfo(path.relative_to(ROOT).as_posix(), (2026, 11, 6, 0, 0, 0))
            entry.compress_type = ZIP_DEFLATED
            entry.create_system = 3
            entry.external_attr = 0o100644 << 16
            archive.writestr(entry, path.read_bytes(), compresslevel=9)
    print(f"Created {destination} ({destination.stat().st_size:,} bytes; {len(files)} files)")


if __name__ == "__main__":
    main()
