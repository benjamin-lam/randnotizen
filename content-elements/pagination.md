# Content-Element: Pagination

## Beschreibung
Seitenweise Navigation für Listen und Suchergebnisse.

## Warum dieses Element?
- Produkt- oder Bloglisten seitenweise anzeigen.
- Suchergebnisse strukturieren und Crawlability verbessern.
- Trade-off: Paginierte Inhalte können Nutzerfluss unterbrechen und SEO-Herausforderungen erzeugen.

## Anforderungen & Besonderheiten
- **Responsiveness:** Nummern und Buttons vergrößern, auf Mobile simplifiziert (Vor/Zurück).
- **Accessibility:** `nav` mit `aria-label`, Fokusreihenfolge, `aria-current` für aktive Seite.
- **SEO:** `rel=next/prev` (wenn sinnvoll), canonical URLs, strukturierte Daten.
- **Design-Guidelines:** Kontrastreiche Buttons, Hover-/Focus-States, Platz für viele Seiten.
- **Rechtliches:** Keine speziellen Anforderungen.

## Umsetzung – Technische Leitplanken
- **Mobile First:** Vor/Zurück plus Seitenanzahl anzeigen, Infinite-Scroll-Alternative prüfen.
- **Accessibility:** Screenreader-Labels wie „Seite 2 von 10“ ergänzen.
- **SEO:** Indexierung steuern, Parameter konsistent halten.
- **Best Practices:**
  - Aktuelle Seite klar hervorheben.
  - First/Last optional ergänzen.
  - Paginierung auch am Seitenende platzieren.

## Checkliste
- [ ] Darstellung auf allen Breakpoints geprüft
- [ ] Barrierefreiheit (Fokus, ARIA, Kontrast) OK
- [ ] Semantik korrekt (HTML)
- [ ] Performance optimiert (Lazyload/Kompression)

## Abhängigkeiten / Überschneidungen
- Routing, API-Pagination, Analytics

## Akzeptanzkriterien
- Technische Funktion OK
- Konsistenz zum Designsystem
- A11y & rechtliche Vorgaben erfüllt

## Beispiel / Code
```html
<!-- Minimales, valides HTML-Beispiel -->
<nav class="pagination" aria-label="Seiten">
  <a href="?page=1" aria-label="Vorherige Seite">«</a>
  <a href="?page=1">1</a>
  <span aria-current="page">2</span>
  <a href="?page=3">3</a>
  <a href="?page=3" aria-label="Nächste Seite">»</a>
</nav>
```

Bewertung der Relevanz 2025

⭐⭐⭐⭐ Klassische Pagination bleibt relevant, auch wenn Infinite Scroll zunimmt.
