#!/usr/bin/env python3
"""Build portable static OFL fonts from the retained upstream variable font.

Requires FontTools. This is an authoring tool; Hollycast loads only the saved TTFs.
"""
from pathlib import Path

from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools.pens.ttGlyphPen import TTGlyphPen

PACKAGE = Path(__file__).resolve().parents[1]
SOURCE = PACKAGE / "source/fonts/LibreBaskerville-variable.ttf"
FAMILY = "Hollycast Christmas Serif"

for weight, style in ((400, "Regular"), (700, "Bold")):
    font = instantiateVariableFont(TTFont(SOURCE, recalcTimestamp=False), {"wght": weight}, inplace=True,
                                   updateFontNames=True)
    # The upstream font reserves its family name. Static derivatives use a new one.
    names = {1: FAMILY, 2: style, 3: f"{FAMILY}-{style}-1.0",
             4: f"{FAMILY} {style}", 6: f"HollycastChristmasSerif-{style}",
             16: FAMILY, 17: style}
    for record in font["name"].names:
        if record.nameID in names:
            record.string = names[record.nameID].encode(record.getEncoding())
    for name_id, value in names.items():
        font["name"].setName(value, name_id, 3, 1, 0x409)
    # A native text button can include its play symbol without a system icon font.
    glyph_name = "christmasPlay"
    scale = font["head"].unitsPerEm / 1000
    pen = TTGlyphPen(None)
    for index, point in enumerate(((180, 30), (180, 670), (750, 350))):
        coordinates = tuple(round(v * scale) for v in point)
        (pen.moveTo if index == 0 else pen.lineTo)(coordinates)
    pen.closePath()
    font.setGlyphOrder(font.getGlyphOrder() + [glyph_name])
    font["glyf"][glyph_name] = pen.glyph()
    font["hmtx"].metrics[glyph_name] = (round(900 * scale), round(180 * scale))
    for table in font["cmap"].tables:
        if table.isUnicode():
            table.cmap[0x25B6] = glyph_name
    font.save(PACKAGE / "assets" / f"ChristmasSerif-{style}.ttf")
