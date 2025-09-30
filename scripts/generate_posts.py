import datetime
import textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
POSTS_DIR = ROOT / "_posts"
POSTS_DIR.mkdir(exist_ok=True)

SOURCE_DIRS = [
    ROOT / "layouts",
    ROOT / "content-elements",
    ROOT / "frontend",
]

def slugify_path(path: Path) -> str:
    relative = path.relative_to(ROOT)
    without_suffix = relative.with_suffix("")
    return "-".join(without_suffix.parts)

def human_title(segment: str) -> str:
    words = segment.replace("-", " ").replace("_", " ")
    return " ".join(word.capitalize() if word.islower() else word for word in words.split())

def build_text(name: str, category_title: str, original_path: Path, slug: str) -> str:
    today = datetime.date.today().isoformat()
    excerpt = f"Warum {name} unsere {category_title}-Notizen inspiriert.".replace('"', '\\"')

    intro = (
        f"Es fühlt sich an wie ein Fund in einer verstaubten Prototyp-Schublade: **{name}** "
        f"passte heute perfekt in unsere {category_title}-Gedanken, und plötzlich roch der Raum "
        "nach Whiteboard-Markern und frisch gebrühtem Kaffee."
    )
    technical = (
        f"Technisch betrachtet verlangt {name} nach klaren Leitplanken. Ich habe die ursprüngliche "
        f"Beschreibung unten angeheftet und mit Kommentaren versehen, damit der Transfer in das neue Blog "
        "sichtbar bleibt."
    )
    anecdotes = (
        f"Michael Crichton hätte wahrscheinlich eine komplette Katastrophensimulation um {name} gestrickt, "
        f"nur um zu zeigen, wie viele Dinge gleichzeitig schiefgehen können. Douglas Coupland würde dagegen "
        f"eine Slack-Konversation voller Insider-Gags daraus machen. Und irgendwo zwinkert eine alte RFC "
        "dazu, weil die Nerd-Fakten selten stillstehen."
    )
    best_practices = [
        f"A11y: {name} tastatur- und screenreader-freundlich gestalten.",
        f"Performance: {name} nur laden, wenn der Kontext es wirklich braucht.",
        f"Wartbarkeit: Entscheidungen zu {name} direkt neben dem Code dokumentieren."
    ]
    fazit = (
        f"{name} bleibt ein schönes Beispiel dafür, wie {category_title}-Elemente Geschichten erzählen können, "
        "wenn man sie ernst nimmt und trotzdem mit Humor betrachtet."
    )

    best_practices_md = "\n".join(f"- {line}" for line in best_practices)
    original_content = original_path.read_text(encoding="utf-8").strip()

    lines = [
        "---",
        f"title: \"{name}: Randnotiz\"",
        f"date: {today}",
        "tags: [UI, Komponente, Webentwicklung]",
        "excerpt: \"" + excerpt + "\"",
        "layout: post",
        f"categories: [{category_title.lower().replace(' ', '-')}]",
        f"slug: {slug}",
        f"original_path: {original_path.relative_to(ROOT).as_posix()}",
        "---",
        "",
        "## Einleitung",
        intro,
        "",
        "## Technischer Kern",
        technical,
        "",
        "### Originalnotizen",
        original_content,
        "",
        "## Anekdoten & Nerd-Zitate",
        anecdotes,
        "",
        "## Best Practices",
        best_practices_md,
        "",
        "## Fazit",
        fazit,
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    today = datetime.date.today().isoformat()
    for source_dir in SOURCE_DIRS:
        for path in sorted(source_dir.rglob("*.md")):
            slug = slugify_path(path)
            category = path.relative_to(ROOT).parts[0]
            category_title = category.replace("-", " ").title()
            name_segment = path.stem
            name = human_title(name_segment)
            content = build_text(name, category_title, path, slug)
            target_name = f"{today}-{slug}.md"
            target_path = POSTS_DIR / target_name
            if target_path.exists():
                continue
            target_path.write_text(content, encoding="utf-8")

if __name__ == "__main__":
    main()
