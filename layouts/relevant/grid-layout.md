# Layout: Responsive Grid

## Beschreibung
Ein modularer Kartenraster erlaubt flexible Inhalte wie Produktkacheln, Team-Profile oder News. Das Layout nutzt CSS Grid für unterschiedliche Spaltenkonfigurationen.

## Warum dieses Layout?
- Skalierbar für unterschiedlich viele Karten.
- Bietet konsistente Darstellung über diverse Viewports.
- Erfordert sorgfältige Breakpoint-Definitionen und Bildoptimierung.

## Anforderungen & Besonderheiten
- **Responsiveness:** Grid-Spalten passen sich über auto-fit/minmax() dynamisch an.
- **Accessibility:** Lesereihenfolge folgt der DOM-Struktur, Karten erhalten eindeutige Überschriften.
- **SEO:** Jede Karte nutzt semantische Elemente wie <article> und sprechende Links.
- **Design-Guidelines:** Konsistente Kartenhöhen, klare Abstände und definierte Schatten oder Umrandungen.

## Umsetzung – Technische Leitplanken
- **Mobile First:** Startet einspaltig und erweitert sich schrittweise auf mehr Spalten.
- **Accessibility:** Fokuszustände klar hervorheben und Karten interaktiv gestalten.
- **SEO:** Primäre Links in Karten prominent platzieren und strukturierte Daten erwägen.
- **Best Practices:** minmax() zur Breitensteuerung, Lazy Loading für Medien, Grid-Gaps gemäß Spacing-Scale

## Checkliste
- [ ] Kartenhöhen bleiben visuell ausgerichtet.
- [ ] LCP-relevante Bilder optimiert.
- [ ] Tastaturnavigation durch Karten getestet.
- [ ] Performance- und Accessibility-Review erfolgt.

## Abhängigkeiten / Überschneidungen
- Card-Komponenten
- Design-Tokens für Abstände

## Akzeptanzkriterien
- Grid passt sich nahtlos an 1–4 Spalten an.
- Screenreader können jede Karte separat ankündigen.
- Lazy Loading reduziert Initial-Ladezeit messbar.

## Beispiel / Code
```html
<section class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
  <article class="card">…</article>
</section>
```

Bewertung der Relevanz 2025

⭐⭐⭐⭐⭐ Grundlage für produkt- und contentlastige Übersichten.
