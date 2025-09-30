# Content-Element: Typography

## Beschreibung
Basis-Elemente für Textstruktur wie Überschriften, Absätze, Listen und Zitate, die Inhalte lesbar und hierarchisch gliedern.

## Warum dieses Element?
- Landingpages und Blogposts klar strukturieren.
- Dokumentationen und Wissensdatenbanken gliedern.
- Trade-off: Zu viele Formatvarianten erschweren Konsistenz und Pflege.

## Anforderungen & Besonderheiten
- **Responsiveness:** Schriftgrößen und Zeilenabstände fluid skalieren, Lesbarkeit auf allen Viewports sicherstellen.
- **Accessibility:** Semantische Heading-Hierarchie, ausreichender Kontrast, Fokusreihenfolge für Sprungmarken.
- **SEO:** Korrekte H-Struktur, strukturierte Inhalte, Schema für Zitate optional.
- **Design-Guidelines:** Definierte Typografie-Skala, konsistente Margins und Zeilenhöhen, Zustände für Links.
- **Rechtliches:** Keine speziellen Anforderungen.

## Umsetzung – Technische Leitplanken
- **Mobile First:** Basisgrößen für kleine Screens festlegen und nach oben progressiv vergrößern.
- **Accessibility:** Screenreader-freundliche Hierarchie, Skip-Links für lange Inhalte.
- **SEO:** Nur ein H1 pro Seite, Überschriften nicht für reines Styling missbrauchen.
- **Best Practices:**
  - Systemschrift-Fallbacks definieren.
  - Zeilenlänge auf 60–80 Zeichen begrenzen.
  - Listen mit `ul`/`ol` semantisch korrekt einsetzen.

## Checkliste
- [ ] Darstellung auf allen Breakpoints geprüft
- [ ] Barrierefreiheit (Fokus, ARIA, Kontrast) OK
- [ ] Semantik korrekt (HTML)
- [ ] Performance optimiert (Lazyload/Kompression)

## Abhängigkeiten / Überschneidungen
- Layout-Raster, Komponentenbibliothek

## Akzeptanzkriterien
- Technische Funktion OK
- Konsistenz zum Designsystem
- A11y & rechtliche Vorgaben erfüllt

## Beispiel / Code
[content-elements-examples/typography.html](../content-elements-examples/typography.html)

```html
<!-- Minimales, valides HTML-Beispiel -->
<article>
  <h1>Überschrift H1</h1>
  <p>Absatztext mit <strong>Betonung</strong> und <a href="#">Link</a>.</p>
  <h2>Liste</h2>
  <ul>
    <li>Listenpunkt</li>
  </ul>
  <blockquote>Zitat mit Quellenangabe.</blockquote>
</article>
```

Bewertung der Relevanz 2025

⭐⭐⭐⭐⭐ Typografie bleibt Grundlage für jede Content-Seite und beeinflusst Lesbarkeit sowie SEO direkt.
