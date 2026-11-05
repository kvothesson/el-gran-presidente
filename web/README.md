# Web

- `decretos.html`: fuente de la página (sin `<html>`/`<head>`; `build_site.py` la envuelve).
- `build_site.py <directorio de salida>`: genera `index.html` con meta de SEO y vista previa, y copia `og.png`, directo en ese directorio. En cada push a `main`, `.github/workflows/pages.yml` lo corre con `_site` y lo publica en GitHub Pages: https://kvothesson.com/el-gran-presidente/
- `marca.css`: colores y fuentes de la marca común de las apps de Kvothesson. Es un archivo generado: no editarlo a mano. La página solo suma la letra serif del texto y los tonos suaves de hielo y ámbar.
- `make_post.py`: regenera `post_1080x1350.png` y `og_1200x630.png` (usa fuentes de Windows: Bahnschrift, Georgia, Consolas).
