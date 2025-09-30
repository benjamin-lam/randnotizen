# Content-Element: Newsletter Opt-in

## Beschreibung
Formular zum Anmelden für einen Newsletter mit Double-Opt-In.

## Warum dieses Element?
- Newsletter-Anmeldungen auf Landingpages erhöhen.
- Content-Angebote oder Downloads mit E-Mail-Opt-In koppeln.
- Trade-off: Zu aggressive Platzierung kann Nutzer abschrecken und Bounce-Rate erhöhen.

## Anforderungen & Besonderheiten
- **Responsiveness:** Einspaltig, klar strukturierte Abstände, Button gut erreichbar.
- **Accessibility:** Labels, Fehlermeldungen, Fokusmanagement für Bestätigung.
- **SEO:** Nicht indexrelevant, aber kann Conversion beeinflussen.
- **Design-Guidelines:** Vertrauensaufbau durch Social Proof, DSGVO-Hinweis, konsistente Buttons.
- **Rechtliches:** Double-Opt-In verpflichtend, Datenschutzhinweis und Widerrufsrecht klar kommunizieren.

## Umsetzung – Technische Leitplanken
- **Mobile First:** Kurz gehaltene Texte, AutoComplete für E-Mail, schneller Abschluss.
- **Accessibility:** Bestätigungen via `aria-live`, klare Checkbox für Einwilligung.
- **SEO:** Nicht relevant.
- **Best Practices:**
  - Transparenz über Versandfrequenz schaffen.
  - Captcha barrierefrei gestalten.
  - Bestätigungsseite mit Tracking-Opt-In dokumentieren.

## Checkliste
- [ ] Darstellung auf allen Breakpoints geprüft
- [ ] Barrierefreiheit (Fokus, ARIA, Kontrast) OK
- [ ] Semantik korrekt (HTML)
- [ ] Performance optimiert (Lazyload/Kompression)

## Abhängigkeiten / Überschneidungen
- E-Mail-Service, Consent-Management, CRM

## Akzeptanzkriterien
- Technische Funktion OK
- Konsistenz zum Designsystem
- A11y & rechtliche Vorgaben erfüllt

## Beispiel / Code
[content-elements-examples/newsletter-optin.html](../content-elements-examples/newsletter-optin.html)

```html
<!-- Minimales, valides HTML-Beispiel -->
<form class="newsletter">
  <label for="newsletter-email">E-Mail</label>
  <input id="newsletter-email" name="email" type="email" required>
  <label><input type="checkbox" required> Ich stimme dem Erhalt des Newsletters zu.</label>
  <button type="submit">Anmelden</button>
</form>
```

Bewertung der Relevanz 2025

⭐⭐⭐⭐ Newsletter sind weiterhin wichtig, müssen aber rechtlich sauber umgesetzt werden.
