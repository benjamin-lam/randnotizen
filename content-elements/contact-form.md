# Content-Element: Contact Form

## Beschreibung
Formular zur Kontaktaufnahme mit Validierung und Spam-Schutz.

## Warum dieses Element?
- Support-Anfragen sammeln.
- Sales-Leads auf Landingpages generieren.
- Trade-off: Zu viele Felder senken Conversion und erhöhen Absprungrate.

## Anforderungen & Besonderheiten
- **Responsiveness:** Einspaltiges Layout auf Mobile, mehrspaltig auf Desktop möglich.
- **Accessibility:** Labels, Fehlerfeedback, Fokus-Reihenfolge, Captcha-barrierefrei.
- **SEO:** Kontaktseiten für lokale Suche optimieren (`LocalBusiness`-Markup).
- **Design-Guidelines:** Klare Hierarchie, Call-to-Action, Fehlermeldungen konsistent.
- **Rechtliches:** Datenschutzhinweis und Einwilligung gem. DSGVO, Double-Opt-In optional.

## Umsetzung – Technische Leitplanken
- **Mobile First:** Kurze Felder, AutoComplete nutzen, Soft-Keyboard steuern.
- **Accessibility:** Serverseitige Fehler wiedergeben, `aria-live` für Bestätigungen.
- **SEO:** `rel="noopener"` bei externen Links, strukturierte Daten für Kontakt hinzufügen.
- **Best Practices:**
  - Spam-Schutz (Honeypot, Rate-Limiting).
  - Erfolgsmeldung klar anzeigen.
  - Pflichtfelder auf ein Minimum reduzieren.

## Checkliste
- [ ] Darstellung auf allen Breakpoints geprüft
- [ ] Barrierefreiheit (Fokus, ARIA, Kontrast) OK
- [ ] Semantik korrekt (HTML)
- [ ] Performance optimiert (Lazyload/Kompression)

## Abhängigkeiten / Überschneidungen
- Form-Backend, Spam-Schutz, CRM

## Akzeptanzkriterien
- Technische Funktion OK
- Konsistenz zum Designsystem
- A11y & rechtliche Vorgaben erfüllt

## Beispiel / Code
[content-elements-examples/contact-form.html](../content-elements-examples/contact-form.html)

```html
<!-- Minimales, valides HTML-Beispiel -->
<form class="contact-form">
  <label for="name">Name</label>
  <input id="name" name="name" required>
  <label for="message">Nachricht</label>
  <textarea id="message" name="message"></textarea>
  <button type="submit">Senden</button>
</form>
```

Bewertung der Relevanz 2025

⭐⭐⭐⭐ Kontaktformulare bleiben primärer Kanal für Leads und Support.
