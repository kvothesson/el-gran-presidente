"""Genera las imágenes para difundir Los Decretos del Gran Presidente.

post_1080x1350.png  -> X / Instagram / comunidad de YouTube
og_1200x630.png     -> vista previa al compartir el link (og:image)
"""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

OUT = Path(__file__).parent
F = "C:/Windows/Fonts/"

BG = (11, 20, 26)
FG = (219, 231, 236)
MUTED = (143, 166, 178)
ICE = (108, 193, 221)
ICE_SOFT = (22, 50, 62)
AMBER = (230, 162, 76)


def font(name, size, bold=False):
    f = ImageFont.truetype(F + name, size)
    if bold and name == "bahnschrift.ttf":
        f.set_variation_by_axes([700, 100])
    return f


def wrap(draw, text, fnt, width):
    lines, line = [], ""
    for word in text.split():
        test = f"{line} {word}".strip()
        if draw.textlength(test, font=fnt) <= width:
            line = test
        else:
            lines.append(line)
            line = word
    lines.append(line)
    return lines


def block(draw, xy, text, fnt, fill, width, leading=1.18):
    x, y = xy
    for ln in wrap(draw, text, fnt, width):
        draw.text((x, y), ln, font=fnt, fill=fill)
        y += int(fnt.size * leading)
    return y


def bars(draw, x, y, w, scale):
    """Regalía conservadora / uso real / regalía optimista, en millones de personas por día."""
    rows = [
        ("Regalía 5%, escenario conservador", 13, ICE),
        ("Uso real esperado (1 de cada 3 por día)", 15, AMBER),
        ("Toda la población", 46, AMBER),
        ("Regalía 5%, escenario optimista", 87, ICE),
    ]
    lab = font("consola.ttf", int(22 * scale))
    num = font("bahnschrift.ttf", int(26 * scale), bold=True)
    h = int(20 * scale)
    for label, v, color in rows:
        draw.text((x, y), label, font=lab, fill=MUTED)
        val = f"{v} M"
        draw.text((x + w - draw.textlength(val, font=num), y - 4), val, font=num, fill=FG)
        y += int(34 * scale)
        draw.rounded_rectangle((x, y, x + w, y + h), radius=3, fill=ICE_SOFT)
        draw.rounded_rectangle((x, y, x + max(int(w * v / 87), h), y + h), radius=3, fill=color)
        y += h + int(22 * scale)
    return y


def post():
    W, H, M = 1080, 1350, 84
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    tw = W - 2 * M

    d.text((M, 80), "DECRETO 001 · EL GRAN PRESIDENTE", font=font("consola.ttf", 26), fill=MUTED)
    y = block(d, (M, 150), "El que saca petróleo de la Argentina paga regalías.",
              font("bahnschrift.ttf", 76, bold=True), FG, tw)
    y0 = y + 24
    y = block(d, (M + 34, y0), "El que usa nuestro frío para hacer funcionar IA, ¿por qué no?",
              font("bahnschrift.ttf", 58), ICE, tw - 34)
    d.rectangle((M, y0 + 8, M + 6, y - 6), fill=AMBER)
    y += 70
    d.text((M, y), "5% del cómputo de un solo data center alcanza para:",
           font=font("georgia.ttf", 32), fill=FG)
    d.text((M, y + 44), "millones de personas usando IA por día",
           font=font("consola.ttf", 22), fill=MUTED)
    y = bars(d, M, y + 110, tw, 1.3)

    d.line((M, H - 150, W - M, H - 150), fill=FG, width=2)
    d.text((M, H - 120), "kvothesson.com/el-gran-presidente", font=font("bahnschrift.ttf", 44, bold=True), fill=ICE)
    d.text((M, H - 62), "La cuenta, los supuestos y las fuentes. Sin presupuesto público.",
           font=font("georgia.ttf", 24), fill=MUTED)
    im.save(OUT / "post_1080x1350.png")


def og():
    W, H, M = 1200, 630, 64
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    left = 620
    d.text((M, 56), "LOS DECRETOS DEL GRAN PRESIDENTE", font=font("consola.ttf", 20), fill=MUTED)
    y = block(d, (M, 100), "El que saca petróleo de la Argentina paga regalías.",
              font("bahnschrift.ttf", 50, bold=True), FG, left - M)
    y0 = y + 18
    y = block(d, (M + 26, y0), "El que usa nuestro frío para hacer funcionar IA, ¿por qué no?",
              font("bahnschrift.ttf", 34), ICE, left - M - 26)
    d.rectangle((M, y0 + 6, M + 5, y - 4), fill=AMBER)
    d.text((left + 40, 100), "5% de un data center =", font=font("georgia.ttf", 26), fill=FG)
    d.text((left + 40, 136), "millones de personas usando IA por día", font=font("consola.ttf", 17), fill=MUTED)
    bars(d, left + 40, 186, W - left - 40 - M, 0.8)
    d.text((M, H - 74), "kvothesson.com/el-gran-presidente", font=font("bahnschrift.ttf", 34, bold=True), fill=ICE)
    im.save(OUT / "og_1200x630.png")


if __name__ == "__main__":
    post()
    og()
