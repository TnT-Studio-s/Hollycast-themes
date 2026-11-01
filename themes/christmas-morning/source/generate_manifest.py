#!/usr/bin/env python3
"""Build the standalone Christmas Morning manifest; preserve generated PNGs."""
# Copyright 2026 The Hollycast Authors
# SPDX-License-Identifier: GPL-2.0-or-later

import json
from pathlib import Path

PACKAGE = Path(__file__).resolve().parents[1]
GREEN, CREAM, GOLD = "08251c", "fff0cf", "e7bf69"
MUTED, RED = "d1c5a2", "850c20"


def e(kind, rect, **values):
    return dict(type=kind, rect=rect, **values)


def text(rect, value, size, color=CREAM, **values):
    return e("text", rect, text=value, fontSize=size, color=color, **values)


def image(rect, source, **values):
    values.setdefault("fit", "contain")
    return e("image", rect, source="assets/" + source, **values)


def metadata(rect, source, size, **values):
    return e("metadata", rect, source=source, fontSize=size, color=CREAM, **values)


def button(rect, action, value, size=0.024, **values):
    result = e("button", rect, action=action, text=value, fontSize=size,
               color=CREAM, background="061b14e8", borderColor=GOLD, rounding=0.2)
    result.update(values)
    return result


def play(rect, size=0.032):
    return button(rect, "activate", "\u25b6  Play", size,
                  background=RED, borderColor="e7bf69", rounding=0.2)


def favourite(rect, size=0.024):
    return button(rect, "favourite", "Favourite", size, icon="star",
                  selectedIcon="star-filled", selectedText="Favourited",
                  selectedBackground=GOLD, selectedColor=GREEN,
                  selectedBorderColor=GOLD)


def choices(x, y, widths, height, size):
    total = sum(widths)
    # One shared gold rim gives the three native buttons a segmented silhouette.
    result = [
        e("panel", [x, y, total, height], color="c9a758", rounding=22),
        e("panel", [x + 0.001, y + 0.0018, total - 0.002, height - 0.0036],
          color="041b14f4", rounding=22),
    ]
    for source, label, width in zip(("cover", "screenshot", "disc"),
                                    ("Cover", "Screenshot", "Disc"), widths):
        result.append(button([x, y, width, height], "artwork", label, size,
                             source=source, background="00000000",
                             borderColor="00000000", rounding=0.5,
                             selectedColor="1b1a10", selectedBackground=GOLD,
                             selectedBorderColor=GOLD))
        x = round(x + width, 6)
    return result


def common():
    return dict(
        mode="list", activation="doubleClick", toolbar="compact",
        toolbarLogo="assets/hollycast-christmas.png", toolbarLogoHeight=32,
        toolbarSelectedTextColor=CREAM, background=GREEN,
        textColor=CREAM, selectedTextColor=CREAM, selectorColor="850c20f5",
        selectorBorderColor=GOLD, separatorColor="d9b77735", rounding=8,
        showArtwork=True, artworkSource="cover", showItemActions=False,
        showFavouriteMarker=True, hoverDetails=False, showInfoTooltip=False,
        previewSource="screenshot", spacing=0,
        list=dict(systemBadge=True, favouriteBadge=True, favouriteColor=GOLD,
                  selectOnHover=False),
        launch=dict(seconds=0.55),
    )


def background(filename):
    return image([0, 0, 1, 1], filename, zIndex=-100, fit="stretch")


def screen(rect):
    # The renderer starts on Screenshot when available and falls back to Cover.
    return e("artwork", rect, source="preview", fit="contain", rounding=8)


def crt(rect):
    # Existing generic selection timers keep this nonblocking and package-only.
    return [
        image(rect, "crt-glass.png", fit="stretch", rounding=8, zIndex=1),
        image(rect, "crt-retune.png", tileSeconds=0.5,
              onSelection=0.65, zIndex=2),
    ]


def synopsis(rect, size):
    # Description-only details retain scrolling without adding table labels.
    return e("details", rect, fields=["description"], columns=1, fontSize=size,
             color=MUTED)


def flash():
    return e("panel", [0, 0, 1, 1], color=CREAM, when="launching",
             launchFadeFrom=0.45, zIndex=90, bleed=True)


wide = common()
wide.update(
    id="christmas-morning", name="Christmas Morning",
    canvasAspect=1672 / 941, browser=[0.022, 0.268, 0.432, 0.373],
    rowHeight=0.073, fontSize=0.0275,
    narrowLayout="christmas-morning-portrait", narrowAspect=1.15,
)
wide["elements"] = [
    background("christmas-room.png"),
    image([0.005, 0.027, 0.335, 0.226], "christmas-title.png"),
    screen([0.526, 0.266, 0.261, 0.308]),
    *crt([0.526, 0.266, 0.261, 0.308]),
    metadata([0.023, 0.653, 0.416, 0.074], "title", 0.060, bold=True, wrap=False),
    e("metadata", [0.024, 0.739, 0.414, 0.03],
      fields=["developer", "genre", "releaseDate", "players"], separator="   |   ",
      fontSize=0.019, color=MUTED, wrap=False),
    e("panel", [0.024, 0.781, 0.025, 0.0015], color=GOLD),
    synopsis([0.024, 0.793, 0.414, 0.049], 0.0195),
    play([0.023, 0.854, 0.179, 0.073]),
    favourite([0.211, 0.854, 0.170, 0.073]),
    text([0.023, 0.962, 0.425, 0.025],
         "Enter  Play     Arrows  Browse     Right-click  Game actions", 0.0155,
         MUTED, wrap=False),
    *choices(0.519, 0.903, [0.073, 0.098, 0.057], 0.043, 0.018),
    flash(),
]

portrait = common()
portrait.update(
    id="christmas-morning-portrait", name="Christmas Morning (portrait)",
    canvasAspect=2 / 3, browser=[0.06, 0.611, 0.88, 0.18],
    rowHeight=0.044, fontSize=0.019, toolbarLogoHeight=16,
)
portrait["elements"] = [
    background("christmas-room-portrait.png"),
    text([0.06, 0.049, 0.88, 0.045], "Christmas Morning", 0.034,
         bold=True, wrap=False),
    screen([0.261, 0.166, 0.365, 0.155]),
    *crt([0.261, 0.166, 0.365, 0.155]),
    *choices(0.19, 0.522, [0.16, 0.23, 0.14], 0.032, 0.015),
    metadata([0.06, 0.565, 0.88, 0.038], "title", 0.028, bold=True, wrap=False),
    e("metadata", [0.06, 0.806, 0.88, 0.023],
      fields=["developer", "genre", "releaseDate", "players"], separator="  |  ",
      fontSize=0.014, color=MUTED, wrap=False),
    synopsis([0.06, 0.841, 0.88, 0.041], 0.015),
    play([0.06, 0.905, 0.47, 0.051], 0.025),
    favourite([0.55, 0.905, 0.39, 0.051], 0.019),
    text([0.06, 0.974, 0.88, 0.018], "HOLLYCAST / CHRISTMAS EDITION",
         0.012, GOLD, align="center", wrap=False),
    flash(),
]

theme = dict(
    formatVersion=1, id="christmas-morning", name="Christmas Morning",
    author="Hollycast contributors",
    description="A nostalgic Christmas room with ivory serif type, a cover list, "
                "cranberry and gold controls, and a CRT preview. Requires Hollycast with list badges and keyboard preview support; see README.",
    baseTheme=0,
    fonts=dict(body="assets/ChristmasSerif-Regular.ttf",
               bold="assets/ChristmasSerif-Bold.ttf"),
    colors=dict(
        Text=CREAM, TextDisabled=MUTED, WindowBg=GREEN, ChildBg=GREEN,
        PopupBg="10291f", Border="a88c4e", Separator="78683b",
        FrameBg="16372a", FrameBgHovered="254c37", FrameBgActive="366244",
        Button="0e2c20", ButtonHovered="234734", ButtonActive=RED,
        Header=RED, HeaderHovered="a32535", HeaderActive="6a0617",
        CheckMark=GOLD, SliderGrab=GOLD, SliderGrabActive=CREAM,
        NavCursor=GOLD, ScrollbarBg="08251c00", ScrollbarGrab="a88c4e66",
        ScrollbarGrabHovered="d9b777aa", ScrollbarGrabActive=GOLD,
        TitleBg=GREEN, TitleBgActive="16372a", TableHeaderBg="16372a",
        TextLink=GOLD,
    ),
    layouts=[wide, portrait],
)

if __name__ == "__main__":
    (PACKAGE / "theme.json").write_text(json.dumps(theme, indent=2) + "\n", encoding="utf-8")
