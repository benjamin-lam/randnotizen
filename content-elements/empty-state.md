# Content-Element: Empty State

## Beschreibung
Darstellung, wenn keine Daten oder Ergebnisse vorliegen.

## Warum dieses Element?
- Suche ohne Treffer informativ gestalten.
- Neue Nutzer in Dashboards an Funktionen heranführen.
- Trade-off: Unpassende Illustrationen oder Texte können Nutzer verwirren.

## Anforderungen & Besonderheiten
- **Responsiveness:** Illustrationen und Text skalieren, Buttons darunter anordnen.
- **Accessibility:** Alternativtexte für Illustrationen, klare Anweisungen auch in Text.
- **SEO:** Keine direkte Relevanz.
- **Design-Guidelines:** Illustration, Headline, Body-Text, CTA optional, konsistente Farben.
- **Rechtliches:** Keine speziellen Anforderungen.

## Umsetzung – Technische Leitplanken
- **Mobile First:** Kurze Texte, klare Handlungsoptionen, Buttons full-width.
- **Accessibility:** Keine rein ikonografischen Aussagen; Text beschreibt Situation.
- **SEO:** Nicht relevant.
- **Best Practices:**
  - Konkrete nächste Schritte anbieten.
  - Optional Hilfelinks einblenden.
  - Tonfall empathisch wählen.

## Checkliste
- [ ] Darstellung auf allen Breakpoints geprüft
- [ ] Barrierefreiheit (Fokus, ARIA, Kontrast) OK
- [ ] Semantik korrekt (HTML)
- [ ] Performance optimiert (Lazyload/Kompression)

## Abhängigkeiten / Überschneidungen
- Illustrationen, CTA-Komponenten

## Akzeptanzkriterien
- Technische Funktion OK
- Konsistenz zum Designsystem
- A11y & rechtliche Vorgaben erfüllt

## Beispiel / Code
```html
<!-- Minimales, valides HTML-Beispiel -->
<section class="empty-state">
  <img src="empty.svg" alt="Kein Ergebnis gefunden" loading="lazy">
  <h2>Keine Ergebnisse</h2>
  <p>Passen Sie Ihre Filter an oder starten Sie eine neue Suche.</p>
  <button type="button">Filter zurücksetzen</button>
</section>
```

Bewertung der Relevanz 2025

⭐⭐⭐⭐ Gute Empty States steigern Engagement und helfen bei der Orientierung.
