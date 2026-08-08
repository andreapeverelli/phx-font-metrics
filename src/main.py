import sys
import json
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont

def badArguments():
    sys.stdout.write("""\
Bad arguments.
Try 'phx-font-metrics --help' for command structure.
""")

    sys.exit(1)

if len(sys.argv) < 2:
    badArguments()

if sys.argv[1] == "--help":
    sys.stdout.write("""\
PHX-FONT-METRICS
Extract metrics from a TTF font file for generating a custom Material You typescale.

Command structure:
    phx-font-metrics TTF_FONT_FILE [WEIGHT_AXIS_NAME] [WEIGHT_AXIS_VALUE]
    phx-font-metrics --version
    phx-font-metrics --help
""")

    sys.exit(0)

if sys.argv[1] == "--version":
    sys.stdout.write("PHX-FONT-METRICS v1.0.1\n")

    sys.exit(0)

if len(sys.argv) < 3:
    badArguments()

def glyphBbox(font, char):
    cmap = font.getBestCmap()
    glyph_name = cmap.get(ord(char))

    if not glyph_name:
        return None

    glyph = font["glyf"][glyph_name]

    if glyph.isComposite():
        glyph.recalcBounds(font["glyf"])

    return (
        glyph.xMin,
        glyph.yMin,
        glyph.xMax,
        glyph.yMax,
    )

def loadFont(path):
    font = TTFont(path)

    if "fvar" not in font:
        return font

    if len(sys.argv) < 4:
        badArguments()

    axes = {}

    for axis in font["fvar"].axes:
        tag = axis.axisTag

        if tag == sys.argv[2]:
            axes[tag] = int(sys.argv[3])
        else:
            axes[tag] = axis.defaultValue

    return instantiateVariableFont(
        font,
        axes,
        inplace=False,
    )

def getMetrics(path):
    font = loadFont(path)

    upm = font["head"].unitsPerEm
    hmtx = font["hmtx"]

    # x-height
    x_box = glyphBbox(font, "x")
    x_height = x_box[3]

    # cap height
    h_box = glyphBbox(font, "H")
    cap_height = h_box[3]

    # ascender
    ascender_chars = "bdfhklt"
    ascender = max(
        glyphBbox(font, c)[3]
        for c in ascender_chars
        if glyphBbox(font, c)
    )

    # descender
    descender_chars = "gjpqy"
    descender = min(
        glyphBbox(font, c)[1]
        for c in descender_chars
        if glyphBbox(font, c)
    )

    # average advance
    cmap = font.getBestCmap()

    sample = (
        "abcdefghijklmnopqrstuvwxyz"
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    )

    advances = []

    for c in sample:
        glyph = cmap.get(ord(c))
        if glyph:
            advances.append(
                hmtx[glyph][0]
            )

    avg_advance = sum(advances) / len(advances)

    natural_line_height = ascender + abs(descender)

    return {
        "x_ratio": x_height / upm,
        "cap_ratio": cap_height / upm,
        "natural_line_ratio": natural_line_height / upm,
        "advance_ratio": avg_advance / upm,
    }


json.dump(getMetrics(sys.argv[1]), sys.stdout)

sys.exit(0);
