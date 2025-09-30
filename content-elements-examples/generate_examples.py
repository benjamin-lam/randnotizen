from __future__ import annotations

from pathlib import Path
import textwrap

from component_data import COMPONENTS

CONTENT_DIR = Path("../content-elements").resolve()
OUTPUT_DIR = Path(".").resolve()

TEMPLATE = """<!doctype html>
<html lang=\"de\">
  <head>
    <meta charset=\"utf-8\">
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">
    <title>{title} – Content Element Beispiel</title>
    <meta name=\"description\" content=\"Beispielimplementierung für das Content-Element {title}.\">
    <link rel=\"stylesheet\" href=\"assets/styles.css\">
  </head>
  <body>
    <a href=\"#main\" class=\"skip-link\">Zum Inhalt springen</a>
    <header class=\"site-header\">
      <p class=\"badge\">Content Element Beispiel</p>
      <h1 class=\"site-header__title\">{title}</h1>
    </header>
    <main id=\"main\" class=\"component-page\" tabindex=\"-1\">
      <article class=\"component-preview\">
        <header class=\"component-preview__header\">
          <h2 class=\"component-preview__title\">Live-Demo</h2>
          <p class=\"component-preview__description\">{description}</p>
          <div class=\"component-meta\" role=\"list\">
            {meta}
          </div>
        </header>
        <section class=\"component-preview__example\" aria-label=\"Beispiel\">
{example}
        </section>
        {notes}
      </article>
    </main>
    <script src=\"assets/scripts.js\" defer></script>
  </body>
</html>
"""


def read_title(md_path: Path) -> str:
    for line in md_path.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            return line.split(":", 1)[-1].strip()
    raise ValueError(f"Kein Titel in {md_path}")


def read_description(md_path: Path) -> str:
    lines = md_path.read_text(encoding="utf-8").splitlines()
    try:
        idx = lines.index("## Beschreibung") + 1
    except ValueError as exc:
        raise ValueError(f"Keine Beschreibung in {md_path}") from exc
    collected: list[str] = []
    for line in lines[idx:]:
        if not line.strip():
            break
        collected.append(line.strip())
    return " ".join(collected)


def build_meta(meta_items: list[str]) -> str:
    pills = []
    for item in meta_items:
        pills.append(
            f"<span class=\"meta-pill\" role=\"listitem\" aria-label=\"{item}\">" f"<span aria-hidden=\"true\">⚙️</span>{item}</span>"
        )
    return "".join(pills) if pills else "<span class=\"meta-pill\">Standard Best Practices</span>"


def indent(text: str, spaces: int = 10) -> str:
    return textwrap.indent(text.strip(), " " * spaces)


def main() -> None:
    for md_path in sorted(CONTENT_DIR.glob("*.md")):
        slug = md_path.stem
        if slug not in COMPONENTS:
            raise KeyError(f"Für {slug} wurde kein Beispiel definiert")
        entry = COMPONENTS[slug]
        title = entry.get("title") or read_title(md_path)
        description = entry.get("description") or read_description(md_path)
        meta = build_meta(entry.get("meta", []))
        example = indent(entry["example"], 10)
        notes_block = entry.get("notes")
        notes_html = ""
        if notes_block:
            notes_html = "          <footer class=\"component-meta\">" + notes_block + "</footer>"
        html = TEMPLATE.format(
            title=title,
            description=description,
            meta=meta,
            example=example,
            notes=notes_html,
        )
        output_path = OUTPUT_DIR / f"{slug}.html"
        output_path.write_text(html, encoding="utf-8")
        print(f"geschrieben: {output_path.name}")


if __name__ == "__main__":
    main()
