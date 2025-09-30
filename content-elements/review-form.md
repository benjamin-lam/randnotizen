# Content-Element: Review Form

## Beschreibung
Formular zum Abgeben von Bewertungen mit Rating und Textfeld.

## Warum dieses Element?
- Produkt- oder Service-Bewertungen einholen.
- Feedback auf Kurs- oder Eventseiten sammeln.
- Trade-off: Aufwendig in Moderation und Spam-Schutz.

## Anforderungen & Besonderheiten
- **Responsiveness:** Formularelemente stacken, Sterne groß genug.
- **Accessibility:** Rating per Tastatur bedienbar, Labels, Fehlermeldungen.
- **SEO:** Generierter Content steigert Sichtbarkeit, Schema.org `Review`.
- **Design-Guidelines:** Sternewahl, Textarea, Upload für Bilder optional, Hinweis auf Richtlinien.
- **Rechtliches:** Transparenzpflichten, DSGVO (personenbezogene Daten) und Nutzungsbedingungen.

## Umsetzung – Technische Leitplanken
- **Mobile First:** Einfache Eingabe, AutoComplete für Name/E-Mail.
- **Accessibility:** Rating-Widget mit `role="radiogroup"`, Fehlerfeedback via `aria-live`.
- **SEO:** Reviews moderieren, Duplicate Content vermeiden.
- **Best Practices:**
  - Spam-Filter (Honeypot, Captcha) einsetzen.
  - Richtlinien und Moderationshinweise anzeigen.
  - Bestätigungsmail zur Verifikation senden.

## Checkliste
- [ ] Darstellung auf allen Breakpoints geprüft
- [ ] Barrierefreiheit (Fokus, ARIA, Kontrast) OK
- [ ] Semantik korrekt (HTML)
- [ ] Performance optimiert (Lazyload/Kompression)

## Abhängigkeiten / Überschneidungen
- Auth, Moderation, Storage

## Akzeptanzkriterien
- Technische Funktion OK
- Konsistenz zum Designsystem
- A11y & rechtliche Vorgaben erfüllt

## Beispiel / Code
[content-elements-examples/review-form.html](../content-elements-examples/review-form.html)

```html
<!-- Minimales, valides HTML-Beispiel -->
<form class="review-form">
  <fieldset role="radiogroup" aria-labelledby="rating-label">
    <legend id="rating-label">Bewertung</legend>
    <label><input type="radio" name="rating" value="5"> ★★★★★</label>
  </fieldset>
  <label for="review-text">Ihre Erfahrung</label>
  <textarea id="review-text" name="review"></textarea>
  <button type="submit">Absenden</button>
</form>
```

Bewertung der Relevanz 2025

⭐⭐⭐⭐ Nutzerfeedback bleibt wertvoll, erfordert jedoch gute Moderation.
