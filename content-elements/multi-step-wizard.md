# Content-Element: Multi-Step Wizard

## Beschreibung
Mehrschrittige Benutzerführung für komplexe Prozesse.

## Warum dieses Element?
- Onboarding oder Registrierung in Etappen aufteilen.
- Konfiguratoren und Formulare mit vielen Feldern strukturieren.
- Trade-off: Höherer Implementierungsaufwand und potenzielle Abbrüche zwischen Schritten.

## Anforderungen & Besonderheiten
- **Responsiveness:** Schritte vertikal stacken, Fortschritt klar anzeigen.
- **Accessibility:** Fokus zwischen Schritten managen, `aria-current` für aktiven Schritt.
- **SEO:** Kein direkter Einfluss.
- **Design-Guidelines:** Klare Navigation, Buttons (Weiter/Zürück), Zwischenspeicherung.
- **Rechtliches:** Zwischenspeicherung personenbezogener Daten rechtlich absichern.

## Umsetzung – Technische Leitplanken
- **Mobile First:** Jeden Schritt auf das Wesentliche reduzieren, Auto-Save integrieren.
- **Accessibility:** Schrittwechsel ankündigen (`aria-live`), Escape aus Fokusfallen vermeiden.
- **SEO:** Nicht relevant.
- **Best Practices:**
  - Fortschritt speichern und wiederaufnehmen ermöglichen.
  - Zusammenfassung vor Abschluss anzeigen.
  - Validierung pro Schritt durchführen.

## Checkliste
- [ ] Darstellung auf allen Breakpoints geprüft
- [ ] Barrierefreiheit (Fokus, ARIA, Kontrast) OK
- [ ] Semantik korrekt (HTML)
- [ ] Performance optimiert (Lazyload/Kompression)

## Abhängigkeiten / Überschneidungen
- Progress-Steps, Form-Validation, State-Management

## Akzeptanzkriterien
- Technische Funktion OK
- Konsistenz zum Designsystem
- A11y & rechtliche Vorgaben erfüllt

## Beispiel / Code
[content-elements-examples/multi-step-wizard.html](../content-elements-examples/multi-step-wizard.html)

```html
<!-- Minimales, valides HTML-Beispiel -->
<form class="wizard">
  <section aria-labelledby="step1">
    <h2 id="step1">Schritt 1: Konto</h2>
    <label>Name<input name="name"></label>
    <button type="button">Weiter</button>
  </section>
</form>
```

Bewertung der Relevanz 2025

⭐⭐⭐⭐ Mehrschrittprozesse bleiben nötig, wenn komplexe Eingaben zu strukturieren sind.
