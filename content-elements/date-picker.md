# Content-Element: Date Picker

## Beschreibung
Komponente zur Auswahl einzelner Daten oder Zeitspannen.

## Warum dieses Element?
- Buchungen oder Terminplanungen ermöglichen.
- Filter nach Zeitraum in Reports oder Dashboards anbieten.
- Trade-off: Komplexe Kalenderlogik kann Fehler hervorrufen und ist schwer barrierefrei umzusetzen.

## Anforderungen & Besonderheiten
- **Responsiveness:** Kalender auf Mobile als Vollbild oder Listenansicht.
- **Accessibility:** Tastaturbedienung (Pfeiltasten), Screenreader-Beschriftungen, Ansagen der Auswahl.
- **SEO:** Keine direkte Relevanz.
- **Design-Guidelines:** Hervorhebung von aktiven, ausgewählten und deaktivierten Tagen, klare Navigation.
- **Rechtliches:** Bei Buchungen gesetzliche Aufbewahrung von Daten beachten.

## Umsetzung – Technische Leitplanken
- **Mobile First:** Native Picker nutzen, wenn verfügbar, oder optimierte Touch-Gesten.
- **Accessibility:** `aria-live` für Monatswechsel, `aria-selected` für Tage pflegen.
- **SEO:** Nicht relevant.
- **Best Practices:**
  - Min-/Max-Daten definieren.
  - Datumsformat klar kommunizieren.
  - Range-Auswahl mit Drag oder zwei Feldern ermöglichen.

## Checkliste
- [ ] Darstellung auf allen Breakpoints geprüft
- [ ] Barrierefreiheit (Fokus, ARIA, Kontrast) OK
- [ ] Semantik korrekt (HTML)
- [ ] Performance optimiert (Lazyload/Kompression)

## Abhängigkeiten / Überschneidungen
- Lokalisierung, Zeitbibliothek

## Akzeptanzkriterien
- Technische Funktion OK
- Konsistenz zum Designsystem
- A11y & rechtliche Vorgaben erfüllt

## Beispiel / Code
```html
<!-- Minimales, valides HTML-Beispiel -->
<label for="date">Datum</label>
<input id="date" name="date" type="date">
```

Bewertung der Relevanz 2025

⭐⭐⭐⭐ Datumsauswahl bleibt komplex, aber unverzichtbar für Transaktionen.
