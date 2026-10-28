# Web

- `decretos.html`: fuente de la página (sin `<html>`/`<head>`; `build_site.py` la envuelve).
- `build_site.py <directorio de salida>`: genera `index.html` con meta de SEO y vista previa, y copia `og.png`, directo en ese directorio. En cada push a `main`, `.github/workflows/pages.yml` lo corre con `_site` y lo publica en GitHub Pages: https://kvothesson.com/el-gran-presidente/
- `make_post.py`: regenera `post_1080x1350.png` y `og_1200x630.png` (usa fuentes de Windows: Bahnschrift, Georgia, Consolas).
