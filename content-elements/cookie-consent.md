# Content-Element: Cookie Consent

## Beschreibung
Consent-Banner oder Layer zur Einholung der DSGVO-konformen Zustimmung für Cookies.

## Warum dieses Element?
- Tracking- und Marketing-Cookies rechtskonform einholen.
- Einwilligungen für externe Dienste (Maps, Videos) verwalten.
- Trade-off: Schlechte UX führt zu Ablehnung oder rechtlichen Risiken.

## Anforderungen & Besonderheiten
- **Responsiveness:** Fullscreen-Layer auf Mobile, dezenter Banner auf Desktop.
- **Accessibility:** Tastaturbedienbar, Fokus-Trap, klare Beschriftungen, Screenreader-freundlich.
- **SEO:** Consent-Banner darf Inhalte nicht dauerhaft verdecken, sonst Rankingrisiko.
- **Design-Guidelines:** Klares Layout, Buttons für „Akzeptieren“, „Ablehnen“, „Einstellungen“, farblich differenziert.
- **Rechtliches:** DSGVO, TTDSG: Granulare Einwilligung, Dokumentation, Widerrufsmöglichkeit, Datenschutzerklärung verlinken.

## Umsetzung – Technische Leitplanken
- **Mobile First:** Schnelle Auswahl, aber granularer Zugriff über Einstellungen gewährleisten.
- **Accessibility:** Fokus auf ersten Button setzen, `aria-modal` nutzen, Einstellungsdialog beschreiben.
- **SEO:** Banner erst nach Page Load anzeigen, Consent-Status serverseitig speichern.
- **Best Practices:**
  - Voreinstellungen auf technisch notwendige Cookies beschränken.
  - Consent-Logs revisionssicher speichern.
  - Regelmäßige rechtliche Prüfung durchführen.

## Checkliste
- [ ] Darstellung auf allen Breakpoints geprüft
- [ ] Barrierefreiheit (Fokus, ARIA, Kontrast) OK
- [ ] Semantik korrekt (HTML)
- [ ] Performance optimiert (Lazyload/Kompression)

## Abhängigkeiten / Überschneidungen
- Consent-Management-Plattform, Tag-Manager, Legal

## Akzeptanzkriterien
- Technische Funktion OK
- Konsistenz zum Designsystem
- A11y & rechtliche Vorgaben erfüllt

## Beispiel / Code
```html
<!-- Minimales, valides HTML-Beispiel -->
<div class="cookie-consent" role="dialog" aria-modal="true" aria-labelledby="cookie-title">
  <h2 id="cookie-title">Datenschutz-Einstellungen</h2>
  <p>Wir verwenden Cookies, um unsere Website zu verbessern.</p>
  <div class="cookie-consent__actions">
    <button type="button">Alle akzeptieren</button>
    <button type="button">Nur notwendige</button>
    <button type="button">Einstellungen</button>
  </div>
</div>
```

Bewertung der Relevanz 2025

⭐⭐⭐⭐ Cookie-Consent bleibt rechtlich zwingend und entwickelt sich weiter.
