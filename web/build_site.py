"""Arma decretos/index.html para kvothesson.com a partir de decretos.html (formato artifact).

Uso: python build_site.py <ruta al clon de kvothesson/kvothesson.github.io>
Después: commit con el mail noreply de Kvothesson y push.
"""
import re
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).parent
URL = "https://kvothesson.com/decretos/"
DESC = ("Dos propuestas abiertas para Argentina: regalías en cómputo por los data centers de IA "
        "e inteligencia artificial de uso diario para cada ciudadano. Firma: Kvothesson.")

site = Path(sys.argv[1])
src = (HERE / "decretos.html").read_text(encoding="utf-8")
head, body = src.split("</style>", 1)
head = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{DESC}">', head)
meta = f"""<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="robots" content="index, follow">
<link rel="canonical" href="{URL}">
<meta property="og:type" content="article">
<meta property="og:title" content="Los Decretos del Gran Presidente">
<meta property="og:description" content="{DESC}">
<meta property="og:url" content="{URL}">
<meta property="og:locale" content="es_AR">
<meta property="og:image" content="{URL}og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="{URL}og.png">
"""
out = f'<!doctype html>\n<html lang="es">\n<head>\n{meta}{head}\nbody{{margin:0}}\n</style>\n</head>\n<body>{body}\n</body>\n</html>\n'
(site / "decretos").mkdir(exist_ok=True)
(site / "decretos" / "index.html").write_text(out, encoding="utf-8", newline="\n")
shutil.copy(HERE / "og_1200x630.png", site / "decretos" / "og.png")
print("ok:", site / "decretos")
