# Content-Element: Dropdown Select

## Beschreibung
Auswahlliste als Native-Select oder erweiterte Combobox.

## Warum dieses Element?
- Filter- oder Sortieroptionen bereitstellen.
- Formulareingaben mit vorgegebenen Werten strukturieren.
- Trade-off: Custom Selects können A11y-Probleme verursachen, wenn native Funktionen ersetzt werden.

## Anforderungen & Besonderheiten
- **Responsiveness:** Volle Breite auf kleinen Screens, Listenhöhe begrenzen.
- **Accessibility:** `label`-Zuordnung, `aria-expanded`, Tastaturnavigation.
- **SEO:** Kein direkter Einfluss.
- **Design-Guidelines:** Pfeil-Icon, States (hover/focus/disabled), konsistente Höhe.
- **Rechtliches:** Keine speziellen Anforderungen.

## Umsetzung – Technische Leitplanken
- **Mobile First:** Native Select bevorzugen, da optimierte Mobile UI vorhanden.
- **Accessibility:** Combobox-Rollen nur verwenden, wenn Funktionalität vollständig unterstützt.
- **SEO:** Nicht relevant.
- **Best Practices:**
  - Optionen logisch gruppieren (`optgroup`).
  - Leeren Default-State klar kennzeichnen.
  - Maximale Optionsanzahl begrenzen oder Suche anbieten.

## Checkliste
- [ ] Darstellung auf allen Breakpoints geprüft
- [ ] Barrierefreiheit (Fokus, ARIA, Kontrast) OK
- [ ] Semantik korrekt (HTML)
- [ ] Performance optimiert (Lazyload/Kompression)

## Abhängigkeiten / Überschneidungen
- Form-Controller, Such-API (optional)

## Akzeptanzkriterien
- Technische Funktion OK
- Konsistenz zum Designsystem
- A11y & rechtliche Vorgaben erfüllt

## Beispiel / Code
[content-elements-examples/dropdown-select.html](../content-elements-examples/dropdown-select.html)

```html
<!-- Minimales, valides HTML-Beispiel -->
<label for="country">Land</label>
<select id="country" name="country">
  <option value="">Bitte wählen</option>
  <option value="de">Deutschland</option>
</select>
```

Bewertung der Relevanz 2025

⭐⭐⭐⭐ Dropdowns bleiben häufig, doch Usability hängt von sauberer Umsetzung ab.
