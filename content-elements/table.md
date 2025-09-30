# Content-Element: Table

## Beschreibung
Tabellarische Darstellung von Daten mit Headern, Spalten und optionaler Sortierung.

## Warum dieses Element?
- Vergleichstabellen für Spezifikationen oder Features.
- Reporting- oder Statistik-Daten innerhalb von Artikeln darstellen.
- Trade-off: Viele Spalten auf kleinen Screens erschweren Lesbarkeit, erfordern alternative Layouts.

## Anforderungen & Besonderheiten
- **Responsiveness:** Scrollbare Container oder Kartenlayout für mobile Endgeräte bereitstellen.
- **Accessibility:** Korrekte `<th>`-Zuordnungen, `scope`/`headers` einsetzen, ausreichend Kontrast.
- **SEO:** Saubere Tabellenstruktur unterstützt Featured Snippets.
- **Design-Guidelines:** Konsistente Zellabstände, zebra stripes optional, klare Sortier-Icons.
- **Rechtliches:** Keine speziellen Anforderungen.

## Umsetzung – Technische Leitplanken
- **Mobile First:** Wichtige Spalten priorisieren, horizontales Scrollen klar kennzeichnen.
- **Accessibility:** Sortier-Buttons mit `aria-sort` pflegen, Tabellenzusammenfassung (`caption`) nutzen.
- **SEO:** Relevante Keywords in Header-Zellen platzieren, keine leeren Zellen.
- **Best Practices:**
  - Tabellen mit `<caption>` einführen.
  - Responsives Verhalten testen (Stacking, Scroll).
  - Sortierung und Filterung server- oder clientseitig konsistent halten.

## Checkliste
- [ ] Darstellung auf allen Breakpoints geprüft
- [ ] Barrierefreiheit (Fokus, ARIA, Kontrast) OK
- [ ] Semantik korrekt (HTML)
- [ ] Performance optimiert (Lazyload/Kompression)

## Abhängigkeiten / Überschneidungen
- Filter, Sortier-Controls, Datenquellen

## Akzeptanzkriterien
- Technische Funktion OK
- Konsistenz zum Designsystem
- A11y & rechtliche Vorgaben erfüllt

## Beispiel / Code
[content-elements-examples/table.html](../content-elements-examples/table.html)

```html
<!-- Minimales, valides HTML-Beispiel -->
<table class="data-table">
  <caption>Leistungsdaten</caption>
  <thead>
    <tr><th scope="col">Feature</th><th scope="col">Wert</th></tr>
  </thead>
  <tbody>
    <tr><th scope="row">Latenz</th><td>120 ms</td></tr>
  </tbody>
</table>
```

Bewertung der Relevanz 2025

⭐⭐⭐⭐ Datenvisualisierung bleibt kritisch, responsive Tabellen sind unverzichtbar.
