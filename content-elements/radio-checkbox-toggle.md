# Content-Element: Radio / Checkbox / Toggle

## Beschreibung
Steuerelemente für Einzel- oder Mehrfachauswahl inklusive Switches.

## Warum dieses Element?
- Einstellungen oder Präferenzen erfassen.
- Filteroptionen in Listen oder Formularen anbieten.
- Trade-off: Custom Styles ohne native Elemente können Barrieren erzeugen.

## Anforderungen & Besonderheiten
- **Responsiveness:** Gruppen vertikal auf Mobile, horizontal auf Desktop.
- **Accessibility:** Labels klickbar, Status per Screenreader lesbar, Tastaturnavigation.
- **SEO:** Keine direkte Wirkung.
- **Design-Guidelines:** Klar sichtbare Zustände, Gruppierung, Abstände.
- **Rechtliches:** Bei Einwilligungen Nachweisbarkeit sicherstellen.

## Umsetzung – Technische Leitplanken
- **Mobile First:** Touch-Ziele mind. 44 px, Gruppierungen logisch.
- **Accessibility:** Fieldset/Legend für Gruppen, `aria-checked` bei Custom Controls pflegen.
- **SEO:** Nicht relevant.
- **Best Practices:**
  - Native Inputs verwenden und visuell stylen.
  - States (hover/focus/disabled) testen.
  - Toggles nur für sofort wirksame Aktionen nutzen.

## Checkliste
- [ ] Darstellung auf allen Breakpoints geprüft
- [ ] Barrierefreiheit (Fokus, ARIA, Kontrast) OK
- [ ] Semantik korrekt (HTML)
- [ ] Performance optimiert (Lazyload/Kompression)

## Abhängigkeiten / Überschneidungen
- Form-Validation, State-Management

## Akzeptanzkriterien
- Technische Funktion OK
- Konsistenz zum Designsystem
- A11y & rechtliche Vorgaben erfüllt

## Beispiel / Code
[content-elements-examples/radio-checkbox-toggle.html](../content-elements-examples/radio-checkbox-toggle.html)

```html
<!-- Minimales, valides HTML-Beispiel -->
<fieldset>
  <legend>Newsletter Frequenz</legend>
  <label><input type="radio" name="freq" value="weekly"> Wöchentlich</label>
  <label><input type="radio" name="freq" value="monthly"> Monatlich</label>
</fieldset>
```

Bewertung der Relevanz 2025

⭐⭐⭐⭐ Auswahlkontrollen bleiben Standard und benötigen sorgfältige Gestaltung.
