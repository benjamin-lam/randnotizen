# Layout: Portfolio Layout

## Beschreibung
Projekte oder Referenzen werden als visuelle Kacheln und Fallstudien präsentiert. Ideal für Kreativschaffende, Agenturen oder Produktteams.

## Warum dieses Layout?
- Hebt Projekte visuell hervor und erlaubt kuratiertes Storytelling.
- Unterstützt Filter und Tags für zielgerichtete Navigation.
- Erfordert konsequente Bildpflege und aktuelle Inhalte.

## Anforderungen & Besonderheiten
- **Responsiveness:** Flexible Grids, die je nach Viewport von einer auf mehrere Spalten wechseln.
- **Accessibility:** Karten als klickbare Elemente mit klaren Alternativtexten und Fokuszuständen.
- **SEO:** Jede Referenz nutzt sprechende Titel, Metadaten und strukturierte Daten (CreativeWork).
- **Design-Guidelines:** Konsistente Bildformate, Abstände und typografische Gewichtung für Projektinfos.

## Umsetzung – Technische Leitplanken
- **Mobile First:** Startet einspaltig mit priorisiertem Projekt-Highlight.
- **Accessibility:** Verwendet <figure>/<figcaption> für Medien und sichtbare Fokusrahmen.
- **SEO:** Filteroptionen ohne Duplicate-Content-Fallen implementieren.
- **Best Practices:** Lazy Loading von Bildern, Tag-basierte Filter klar kennzeichnen, Hover-Effekte mit Fokus synchronisieren

## Checkliste
- [ ] Bilder entsprechen vereinbarten Formaten.
- [ ] Filter funktionieren mit Tastatur und Screenreadern.
- [ ] Projekttexte sind aktuell und konsistent.
- [ ] Performance- und Accessibility-Audit durchgeführt.

## Abhängigkeiten / Überschneidungen
- Filter-/Tagging-System
- Card-Komponenten

## Akzeptanzkriterien
- Portfolio skaliert ohne Layout-Brüche.
- Filterbare Listen aktualisieren Inhalte barrierefrei.
- Jede Karte führt zu detaillierter Projektbeschreibung.

## Beispiel / Code
```html
<section class="grid sm:grid-cols-2 lg:grid-cols-3 gap-6">
  <article class="project-card">…</article>
</section>
```

Bewertung der Relevanz 2025

⭐⭐⭐⭐☆ Bewährtes Muster zur Präsentation kreativer Arbeiten.
