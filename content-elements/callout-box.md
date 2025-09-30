# Content-Element: Callout Box

## Beschreibung
Hervorgehobene Boxen für Hinweise, Warnungen oder Erfolgsnachrichten innerhalb von Inhalten.

## Warum dieses Element?
- Wichtige Hinweise in Dokumentationen oder Anleitungen hervorheben.
- Statusmeldungen in Knowledge-Base-Artikeln kommunizieren.
- Trade-off: Übermäßiger Einsatz verringert Aufmerksamkeit und führt zu Informationsrauschen.

## Anforderungen & Besonderheiten
- **Responsiveness:** Breite und Padding an Viewport anpassen, Icons skalierbar halten.
- **Accessibility:** Korrekte Rollen (`status`, `alert`) je nach Kontext, ausreichender Kontrast und Fokus für Links.
- **SEO:** Klarer Kontext im Fließtext, optionale `<aside>`-Semantik.
- **Design-Guidelines:** Farbcodierte Varianten (Info, Warnung, Erfolg), konsistente Typografie und Iconografie.
- **Rechtliches:** Keine speziellen Anforderungen.

## Umsetzung – Technische Leitplanken
- **Mobile First:** Vertikale Layouts bevorzugen, Icons oberhalb des Textes platzieren, wenn Platz fehlt.
- **Accessibility:** Rollen nur bei dynamischen Updates setzen, sonst semantisch neutral halten.
- **SEO:** Boxen nicht für kritische Überschriften missbrauchen, semantisch im Textfluss belassen.
- **Best Practices:**
  - Varianten in Designsystem definieren.
  - Icons als dekorativ markieren (`aria-hidden`).
  - Nicht mehr als zwei Callouts pro Bildschirmhöhe verwenden.

## Checkliste
- [ ] Darstellung auf allen Breakpoints geprüft
- [ ] Barrierefreiheit (Fokus, ARIA, Kontrast) OK
- [ ] Semantik korrekt (HTML)
- [ ] Performance optimiert (Lazyload/Kompression)

## Abhängigkeiten / Überschneidungen
- Iconset, Alert-Komponenten

## Akzeptanzkriterien
- Technische Funktion OK
- Konsistenz zum Designsystem
- A11y & rechtliche Vorgaben erfüllt

## Beispiel / Code
[content-elements-examples/callout-box.html](../content-elements-examples/callout-box.html)

```html
<!-- Minimales, valides HTML-Beispiel -->
<aside class="callout callout--info">
  <h3 class="callout__title">Hinweis</h3>
  <p>Bitte sichern Sie Ihre Daten regelmäßig.</p>
</aside>
```

Bewertung der Relevanz 2025

⭐⭐⭐⭐ Callouts unterstützen Lesbarkeit, sollten aber gezielt eingesetzt werden.
