#!/usr/bin/env python3
"""Generate original transparent CRT effect textures (Pillow; no image inputs)."""
# Copyright 2026 The Hollycast Authors
# SPDX-License-Identifier: GPL-2.0-or-later
from pathlib import Path
import math

from PIL import Image

ASSETS = Path(__file__).resolve().parents[1] / "assets"


def glass():
    width, height = 720, 480
    pixels = []
    for y in range(height):
        v = abs((y + 0.5) / height * 2 - 1)
        for x in range(width):
            u = abs((x + 0.5) / width * 2 - 1)
            edge = max(0, (u ** 4 + v ** 4 - 0.40) / 1.60)
            # A restrained dark raster and corner falloff leave the game readable.
            alpha = round(6 * edge ** 1.3) + (44 if y % 4 == 0 else 12 if y % 4 == 1 else 0)
            # A barely visible broad reflection across the upper-left glass.
            sheen = math.exp(-((x / width - 0.25) / 0.45) ** 2
                             - ((y / height - 0.02) / 0.20) ** 2)
            if alpha == 0:
                phosphor = ((180, 35, 35), (35, 180, 35), (35, 35, 180))[x % 3]
                pixels.append((*phosphor, 8))
            else:
                pixels.append((3, 11, 12, min(50, alpha)))
    texture = Image.new("RGBA", (width, height))
    texture.putdata(pixels)
    texture.save(ASSETS / "crt-glass.png", optimize=True)


def retune():
    # A loss of vertical sync: a dark tube with one clean luminous raster line.
    # Tiling this down the glass for one turn reads as tuning, without white noise.
    width, height = 720, 480
    pixels = []
    for y in range(height):
        distance = (y + 0.5 - height / 2) / height
        core = math.exp(-distance * distance / (2 * 0.0025 ** 2))
        bloom = math.exp(-distance * distance / (2 * 0.015 ** 2))
        for x in range(width):
            envelope = max(0, 1 - abs((x + 0.5) / width * 2 - 1) ** 8)
            brightness = min(1, (core + bloom * 0.21) * envelope)
            pixels.append((round(2 + 226 * brightness), round(5 + 240 * brightness),
                           round(4 + 227 * brightness), 248))
    texture = Image.new("RGBA", (width, height))
    texture.putdata(pixels)
    texture.save(ASSETS / "crt-retune.png", optimize=True)


if __name__ == "__main__":
    glass()
    retune()
