# Content-Element: Progress Stepper

## Beschreibung
Visualisierung des Fortschritts in mehreren Schritten oder Phasen.

## Warum dieses Element?
- Status in Checkouts oder Formularen anzeigen.
- Projekt- oder Onboarding-Fortschritt visualisieren.
- Trade-off: Falsche oder irreführende Schritte steigern Frust.

## Anforderungen & Besonderheiten
- **Responsiveness:** Horizontal auf Desktop, vertikal oder kompakt auf Mobile.
- **Accessibility:** `aria-current` für aktiven Schritt, klare Beschriftungen.
- **SEO:** Keine Relevanz.
- **Design-Guidelines:** Abstände, Nummern, Icons; aktive und abgeschlossene States klar differenzieren.
- **Rechtliches:** Keine speziellen Anforderungen.

## Umsetzung – Technische Leitplanken
- **Mobile First:** Text kürzen, Symbole mit Tooltips kombinieren.
- **Accessibility:** Stepper in `<nav>` mit `aria-label` einbetten.
- **SEO:** Nicht relevant.
- **Best Practices:**
  - Schritte anklickbar machen, wenn sinnvoll.
  - Fortschritt synchron mit Wizard-State halten.
  - Klar kommunizieren, wie viele Schritte folgen.

## Checkliste
- [ ] Darstellung auf allen Breakpoints geprüft
- [ ] Barrierefreiheit (Fokus, ARIA, Kontrast) OK
- [ ] Semantik korrekt (HTML)
- [ ] Performance optimiert (Lazyload/Kompression)

## Abhängigkeiten / Überschneidungen
- Multi-Step-Wizard, Designsystem

## Akzeptanzkriterien
- Technische Funktion OK
- Konsistenz zum Designsystem
- A11y & rechtliche Vorgaben erfüllt

## Beispiel / Code
[content-elements-examples/progress-stepper.html](../content-elements-examples/progress-stepper.html)

```html
<!-- Minimales, valides HTML-Beispiel -->
<ol class="stepper">
  <li class="stepper__item stepper__item--done">1. Konto</li>
  <li class="stepper__item stepper__item--current" aria-current="step">2. Adresse</li>
  <li class="stepper__item">3. Abschluss</li>
</ol>
```

Bewertung der Relevanz 2025

⭐⭐⭐⭐ Fortschrittsanzeigen bleiben wichtig für Transparenz in Prozessen.
