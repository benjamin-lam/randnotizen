#!/usr/bin/env python3
"""Generate simple index.html files for directories lacking them."""

from __future__ import annotations

import argparse
import html
import os
from pathlib import Path
from typing import Iterable


def iter_directory_entries(directory: Path) -> tuple[list[str], list[str]]:
    subdirs: list[str] = []
    files: list[str] = []

    for entry in sorted(directory.iterdir(), key=lambda p: p.name.lower()):
        if entry.is_dir():
            subdirs.append(f'<li><a href="{entry.name}/index.html">{html.escape(entry.name)}/</a></li>')
        else:
            lower_name = entry.name.lower()
            if lower_name in {"index.html", "index.htm"}:
                continue
            if lower_name.endswith((".html", ".htm")):
                files.append(f'<li><a href="{entry.name}">{html.escape(entry.name)}</a></li>')
    return subdirs, files


def build_index(directory: Path, rel_display: str) -> str:
    subdirs, files = iter_directory_entries(directory)
    entries: list[str] = subdirs + files

    if not entries:
        entries = ["<li><em>Keine HTML-Inhalte in diesem Verzeichnis.</em></li>"]

    content = "\n".join(entries)
    return f"""<!doctype html>
<meta charset=\"utf-8\">
<title>Index von {html.escape(rel_display)}</title>
<meta name=\"viewport\" content=\"width=device-width,initial-scale=1\">
<style>
  body{{font:16px/1.5 system-ui,Segoe UI,Roboto,Helvetica,Arial,sans-serif;margin:2rem;max-width:72ch}}
  h1{{margin:0 0 1rem}}
  ul{{padding-left:1.2rem}}
  a{{word-break:break-word}}
  code{{background:#f6f8fa;padding:.1rem .3rem;border-radius:.25rem}}
</style>
<h1>Index von <code>{html.escape(rel_display)}</code></h1>
<ul>
{content}
</ul>
"""


def ensure_indexes(base_dir: Path) -> None:
    for current_dir, _, _ in os.walk(base_dir):
        directory = Path(current_dir)
        index_file = directory / "index.html"
        if index_file.exists():
            continue

        rel = directory.relative_to(base_dir)
        display = "/" if rel == Path('.') else f"/{rel.as_posix()}/"

        index_file.write_text(build_index(directory, display), encoding="utf-8")


def parse_args(argv: Iterable[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "directory",
        type=Path,
        nargs="?",
        default=Path("dist"),
        help="Base directory that should contain generated index.html files.",
    )
    return parser.parse_args(argv)


def main() -> None:
    args = parse_args()
    ensure_indexes(args.directory)


if __name__ == "__main__":
    main()
