# Content-Element: Tags & Badges

## Beschreibung
Labels oder Chips zur Kennzeichnung von Kategorien, Status oder Highlights.

## Warum dieses Element?
- Produkte mit Attributen wie „Neu“ oder „Sale“ markieren.
- Blogartikel nach Themen filtern oder kategorisieren.
- Trade-off: Zu viele Tags wirken unübersichtlich und reduzieren Klarheit.

## Anforderungen & Besonderheiten
- **Responsiveness:** Chips umbrechen lassen, horizontale Scrollleisten für Tag-Listen.
- **Accessibility:** `aria-pressed` für toggelbare Chips, ausreichender Kontrast.
- **SEO:** Tags können Landingpages generieren, sollten aber gepflegt sein.
- **Design-Guidelines:** Farbcodierung, abgerundete Ecken, kleine Typografie, Hover-/Focus-States.
- **Rechtliches:** Keine speziellen Anforderungen.

## Umsetzung – Technische Leitplanken
- **Mobile First:** Tags als Scroll-Liste darstellen, wichtige Tags priorisieren.
- **Accessibility:** Chips per Tastatur steuerbar machen, Entfernen-Buttons beschriften.
- **SEO:** Tag-Seiten canonicalisieren, Duplicate Content vermeiden.
- **Best Practices:**
  - Maximale Tag-Anzahl pro Item begrenzen.
  - Farben aus Designsystem nutzen.
  - Optional Icons oder Prefixe für Status verwenden.

## Checkliste
- [ ] Darstellung auf allen Breakpoints geprüft
- [ ] Barrierefreiheit (Fokus, ARIA, Kontrast) OK
- [ ] Semantik korrekt (HTML)
- [ ] Performance optimiert (Lazyload/Kompression)

## Abhängigkeiten / Überschneidungen
- Filter-System, Design-Tokens

## Akzeptanzkriterien
- Technische Funktion OK
- Konsistenz zum Designsystem
- A11y & rechtliche Vorgaben erfüllt

## Beispiel / Code
[content-elements-examples/tags-badges.html](../content-elements-examples/tags-badges.html)

```html
<!-- Minimales, valides HTML-Beispiel -->
<ul class="tags">
  <li><span class="tag tag--new">Neu</span></li>
  <li><span class="tag tag--sale">Sale</span></li>
</ul>
```

Bewertung der Relevanz 2025

⭐⭐⭐⭐ Tags bleiben wichtig zur schnellen Kontextualisierung von Inhalten.
