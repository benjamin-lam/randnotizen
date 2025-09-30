# Layout: Asymmetric Layout

## Beschreibung
Eine asymmetrische Grid-Struktur kombiniert große und kleine Kacheln für dynamische Seitenaufteilung. Perfekt für Editorials, Portfolio-Highlights oder Kampagnen.

## Warum dieses Layout?
- Erzeugt visuelle Spannung und lenkt Fokus gezielt.
- Erlaubt flexible Kombination verschiedener Content-Typen.
- Erfordert sorgfältige A11y-Prüfung der Lesereihenfolge.

## Anforderungen & Besonderheiten
- **Responsiveness:** Grid Areas reorganisieren sich auf mobilen Geräten zu logischer Reihenfolge.
- **Accessibility:** DOM-Reihenfolge bleibt konsistent, aria-labelledby für große Hero-Kacheln.
- **SEO:** Wichtige Inhalte in prominenten Bereichen semantisch hervorheben.
- **Design-Guidelines:** Konsistente Spacing-Scale, Bildzuschnitt und Farbkontraste.

## Umsetzung – Technische Leitplanken
- **Mobile First:** Startet als lineare Liste und erweitert sich zu komplexen Grids.
- **Accessibility:** Alternative Reihenfolge über CSS Grid Areas ohne DOM-Manipulation.
- **SEO:** Sektionen mit passenden Überschriften strukturieren.
- **Best Practices:** Grid Areas definieren, Bildfokuspunkte beachten, Hover/Fokus-Effekte synchronisieren

## Checkliste
- [ ] Lesereihenfolge bleibt nachvollziehbar.
- [ ] Kacheln skalieren ohne Bildverzerrung.
- [ ] Hover/Fokus-Zustände klar sichtbar.
- [ ] Performance- und A11y-Prüfung erfolgt.

## Abhängigkeiten / Überschneidungen
- Grid-System
- Medien- und Text-Module

## Akzeptanzkriterien
- Layout reorganisiert sich ohne Inhaltssprünge.
- Screenreader geben Reihenfolge logisch aus.
- Visuelle Hierarchie unterstützt Content-Ziele.

## Beispiel / Code
```html
<section class="grid md:grid-cols-3 gap-6">
  <article class="md:col-span-2">Highlight</article>
  <article>Teaser</article>
  <article>Teaser</article>
</section>
```

Bewertung der Relevanz 2025

⭐⭐⭐⭐☆ Setzt Kampagnen und Stories aufmerksamkeitsstark in Szene.
