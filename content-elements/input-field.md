# Content-Element: Input Field

## Beschreibung
Standardisierte Eingabefelder für Text, E-Mail oder Nummern mit optionalen Masken.

## Warum dieses Element?
- Kontakt- und Registrierungsformulare erstellen.
- Datenpflege in internen Tools ermöglichen.
- Trade-off: Falsche Masken oder Validierungen frustrieren Nutzer.

## Anforderungen & Besonderheiten
- **Responsiveness:** Volle Breite auf Mobile, angepasste Feldbreiten auf Desktop.
- **Accessibility:** Label-Verknüpfung, Fehlermeldungen beschreiben, ausreichende Touch-Ziele.
- **SEO:** Relevanz nur bei Formular-Landingpages (Micro-Conversions).
- **Design-Guidelines:** Konsistente Höhen, Zustände für Fokus/Fehler, lesbare Typografie.
- **Rechtliches:** Datenschutz bei personenbezogenen Daten beachten (z. B. TLS, Speicherung).

## Umsetzung – Technische Leitplanken
- **Mobile First:** Passende Keyboard-Typen (`inputmode`, `type`) definieren.
- **Accessibility:** Fehlerhinweise via `aria-live`, Pflichtfelder kennzeichnen.
- **SEO:** Formulare beschleunigen Conversion-Rate, Schema.org `ContactPoint` optional.
- **Best Practices:**
  - AutoComplete-Attribute setzen.
  - Masken nur bei klaren Formaten nutzen.
  - Client- und Server-Validierung kombinieren.

## Checkliste
- [ ] Darstellung auf allen Breakpoints geprüft
- [ ] Barrierefreiheit (Fokus, ARIA, Kontrast) OK
- [ ] Semantik korrekt (HTML)
- [ ] Performance optimiert (Lazyload/Kompression)

## Abhängigkeiten / Überschneidungen
- Form-Validation, Masking-Library

## Akzeptanzkriterien
- Technische Funktion OK
- Konsistenz zum Designsystem
- A11y & rechtliche Vorgaben erfüllt

## Beispiel / Code
[content-elements-examples/input-field.html](../content-elements-examples/input-field.html)

```html
<!-- Minimales, valides HTML-Beispiel -->
<label for="email">E-Mail</label>
<input id="email" name="email" type="email" required inputmode="email">
```

Bewertung der Relevanz 2025

⭐⭐⭐⭐⭐ Eingabefelder sind Kernbausteine jeder Interaktion und bleiben unverzichtbar.
