# Content-Element: Search

## Beschreibung
Suchfeld mit optionaler Autosuggest-Funktion.

## Warum dieses Element?
- Produktsuche in Shops oder Verzeichnissen.
- Suche in Knowledge-Bases oder Blogs.
- Trade-off: Schlechte Ergebnisse oder langsame Suggests schaden Vertrauen.

## Anforderungen & Besonderheiten
- **Responsiveness:** Eingabefeld volle Breite, Suggest-Panel adaptiv.
- **Accessibility:** `aria-expanded`, `aria-controls`, Tastaturnavigation im Suggest.
- **SEO:** Interne Suche kann für Site-Search-Snippets genutzt werden.
- **Design-Guidelines:** Lupe-Icon, deutlicher Fokus, Loading-Indicator für Suggests.
- **Rechtliches:** Suchlogs datenschutzkonform speichern und anonymisieren.

## Umsetzung – Technische Leitplanken
- **Mobile First:** Fullscreen-Suche mit On-Screen-Keyboard, History-Vorschläge.
- **Accessibility:** Ergebnisse in `role=listbox`, Items mit `role=option` versehen.
- **SEO:** Suchseiten indexieren oder bewusst ausschließen (noindex).
- **Best Practices:**
  - Fehlertoleranz (Fuzzy Search) anbieten.
  - Analytics zur Suchnutzung integrieren.
  - Leere Ergebnisse mit Hilfestellungen versehen.

## Checkliste
- [ ] Darstellung auf allen Breakpoints geprüft
- [ ] Barrierefreiheit (Fokus, ARIA, Kontrast) OK
- [ ] Semantik korrekt (HTML)
- [ ] Performance optimiert (Lazyload/Kompression)

## Abhängigkeiten / Überschneidungen
- Search-API, Analytics, Autosuggest-Service

## Akzeptanzkriterien
- Technische Funktion OK
- Konsistenz zum Designsystem
- A11y & rechtliche Vorgaben erfüllt

## Beispiel / Code
```html
<!-- Minimales, valides HTML-Beispiel -->
<form role="search">
  <label for="search" class="sr-only">Suche</label>
  <input id="search" name="q" type="search" placeholder="Suche">
  <button type="submit">Suchen</button>
</form>
```

Bewertung der Relevanz 2025

⭐⭐⭐⭐⭐ Suche bleibt zentral für Nutzerzufriedenheit und Conversions.
