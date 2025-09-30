# Content-Element: Code Snippets

## Beschreibung
Darstellung von Codebeispielen als Inline- oder Block-Elemente inkl. Kopierfunktion.

## Warum dieses Element?
- Developer-Dokumentationen und API-Referenzen präsentieren.
- How-to-Artikel mit konkreten Codeausschnitten anreichern.
- Trade-off: Syntax-Highlighting kann Performance und Barrierefreiheit beeinträchtigen, wenn schlecht umgesetzt.

## Anforderungen & Besonderheiten
- **Responsiveness:** Codeblöcke horizontal scrollbar machen, Inline-Code mit Wrap-Strategien versehen.
- **Accessibility:** ARIA-Labels für Kopier-Buttons, Screenreader-kompatible Spracheinstellung, ausreichender Kontrast.
- **SEO:** Strukturierte Daten für Code (`<pre><code>`) korrekt einsetzen, optionale `<figure>`-Einbettung.
- **Design-Guidelines:** Monospace-Fonts, dezente Hintergrundflächen, klare Abstände und Hover-/Focus-States für Aktionen.
- **Rechtliches:** Keine speziellen Anforderungen.

## Umsetzung – Technische Leitplanken
- **Mobile First:** Kurze Codezeilen bevorzugen, ansonsten Scrollcontainer mit sichtbarer Scrollbarkeit.
- **Accessibility:** `aria-live`-Feedback für erfolgreiche Kopieraktionen, Fokusreihenfolge beibehalten.
- **SEO:** Konsistente Sprachangabe per `lang`-Attribut, nicht renderrelevanten Code vermeiden.
- **Best Practices:**
  - Syntax-Highlighting serverseitig oder per leichtgewichtiges Skript.
  - Kopier-Button erst nach dem Code rendern, um Tab-Reihenfolge logisch zu halten.
  - Codeblöcke in `<figure>` mit `<figcaption>` erläutern.

## Checkliste
- [ ] Darstellung auf allen Breakpoints geprüft
- [ ] Barrierefreiheit (Fokus, ARIA, Kontrast) OK
- [ ] Semantik korrekt (HTML)
- [ ] Performance optimiert (Lazyload/Kompression)

## Abhängigkeiten / Überschneidungen
- Buttons, Clipboard-API, Syntax-Highlighting-Utility

## Akzeptanzkriterien
- Technische Funktion OK
- Konsistenz zum Designsystem
- A11y & rechtliche Vorgaben erfüllt

## Beispiel / Code
[content-elements-examples/code-snippets.html](../content-elements-examples/code-snippets.html)

```html
<!-- Minimales, valides HTML-Beispiel -->
<figure class="code-snippet">
  <figcaption>cURL-Beispiel</figcaption>
  <pre><code>curl https://api.example.com/v1</code></pre>
  <button type="button" aria-label="Code kopieren">Copy</button>
</figure>
```

Bewertung der Relevanz 2025

⭐⭐⭐⭐⭐ Codebeispiele bleiben essenziell für Developer-Content und Wissensvermittlung.
