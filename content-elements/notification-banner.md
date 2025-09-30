# Content-Element: Notification Banner

## Beschreibung
Seitenweite Hinweise oder Promotions am oberen Rand.

## Warum dieses Element?
- Zeitlich begrenzte Aktionen oder Rabatte kommunizieren.
- Systemmeldungen wie Wartungsfenster ankündigen.
- Trade-off: Dauerhafte Banner können Nutzer nerven und Banner-Blindheit erzeugen.

## Anforderungen & Besonderheiten
- **Responsiveness:** Volle Breite, Text umbrechen, Close-Button gut erreichbar.
- **Accessibility:** `role="region"` mit Label, Fokus auf Dismiss-Button möglich, ausreichender Kontrast.
- **SEO:** Kein direkter Einfluss, jedoch sollte Banner den Content nicht verdecken.
- **Design-Guidelines:** Farbige Hintergründe, klare Typografie, optional Icon und CTA.
- **Rechtliches:** Preisaktionen mit Bedingungen verlinken, Pflichtinformationen anzeigen.

## Umsetzung – Technische Leitplanken
- **Mobile First:** Höhe minimieren, Dismiss-Button groß genug.
- **Accessibility:** Banner per Tastatur schließbar, `aria-live` für zeitkritische Infos.
- **SEO:** Keine Cloaking-Praktiken, Banner nicht Inhalt überdecken.
- **Best Practices:**
  - Nur eine aktive Botschaft gleichzeitig anzeigen.
  - Dauer und Wiederholung begrenzen.
  - Dismiss-State speichern (Cookie/LocalStorage).

## Checkliste
- [ ] Darstellung auf allen Breakpoints geprüft
- [ ] Barrierefreiheit (Fokus, ARIA, Kontrast) OK
- [ ] Semantik korrekt (HTML)
- [ ] Performance optimiert (Lazyload/Kompression)

## Abhängigkeiten / Überschneidungen
- Analytics, Feature Flags, Consent (bei Tracking)

## Akzeptanzkriterien
- Technische Funktion OK
- Konsistenz zum Designsystem
- A11y & rechtliche Vorgaben erfüllt

## Beispiel / Code
[content-elements-examples/notification-banner.html](../content-elements-examples/notification-banner.html)

```html
<!-- Minimales, valides HTML-Beispiel -->
<div class="notification-banner" role="region" aria-label="Hinweis">
  <p>Gratis Versand bis Sonntag!</p>
  <button type="button" class="notification-banner__close" aria-label="Banner schließen">×</button>
</div>
```

Bewertung der Relevanz 2025

⭐⭐⭐⭐ Banner bleiben ein zentrales Mittel für dringliche Kommunikation.
