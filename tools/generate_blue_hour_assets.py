#!/usr/bin/env python3
"""Generate this theme's original UI shapes without third-party assets using the standard library."""
from pathlib import Path
import math
import struct
import zlib

ASSETS = Path(__file__).resolve().parents[1] / "themes/blue-hour/assets"


def png(name, width, height, pixel):
    raw = bytearray()
    for y in range(height):
        raw.append(0)
        for x in range(width):
            raw.extend(pixel(x, y))

    def chunk(kind, data):
        return struct.pack(">I", len(data)) + kind + data + struct.pack(">I", zlib.crc32(kind + data) & 0xffffffff)

    ASSETS.mkdir(parents=True, exist_ok=True)
    (ASSETS / name).write_bytes(
        b"\x89PNG\r\n\x1a\n"
        + chunk(b"IHDR", struct.pack(">IIBBBBB", width, height, 8, 6, 0, 0, 0))
        + chunk(b"IDAT", zlib.compress(raw, 9)) + chunk(b"IEND", b""))


for selected in (False, True):
    for hovered in (False, True):
        name = "nav-selected" if selected else "nav"
        name += "-hover" if hovered else ("" if selected else "-idle")
        png(name + ".png", 256, 96,
            lambda x, y, s=selected, h=hovered:
                (245, 250, 255, 255) if s and 90 <= y <= 94 and 12 <= x <= 244
                else (255, 255, 255, 14 if h else 0))


def profile(x, y):
    radius = math.hypot(x - 63.5, y - 63.5)
    head = math.hypot(x - 63.5, y - 45)
    shoulders = ((x - 63.5) / 32) ** 2 + ((y - 101) / 29) ** 2
    ink = 59 <= radius <= 63 or head <= 16 or (shoulders <= 1 and y < 110)
    return (244, 249, 255, 255 if ink else 0)


png("profile.png", 128, 128, profile)
