# Content-Element: Review Stars

## Beschreibung
Darstellung von Bewertungen mit Sterne-Rating.

## Warum dieses Element?
- Produktbewertungen in Listen oder Detailseiten anzeigen.
- Testimonials und Social Proof hervorheben.
- Trade-off: Durchschnittswerte können Erwartungen verzerren, wenn zu wenige Bewertungen vorliegen.

## Anforderungen & Besonderheiten
- **Responsiveness:** Sternegröße anpassen, Text daneben umbrechen lassen.
- **Accessibility:** `aria-label` für Bewertung, numerische Werte ausgeben.
- **SEO:** Schema.org `AggregateRating` für Rich Snippets.
- **Design-Guidelines:** Farbige Sterne, klarer Kontrast, optional Text (4,5/5).
- **Rechtliches:** Echtheit der Bewertungen sicherstellen (UWG).

## Umsetzung – Technische Leitplanken
- **Mobile First:** Komprimierte Darstellung, Sterne neben Text.
- **Accessibility:** Bewertung zusätzlich in Textform ausgeben.
- **SEO:** JSON-LD mit Review-Daten pflegen.
- **Best Practices:**
  - Anzahl der Bewertungen anzeigen.
  - Filter oder Sortierung nach Bewertung ermöglichen.
  - Manipulation vermeiden und Kennzeichnungspflicht beachten.

## Checkliste
- [ ] Darstellung auf allen Breakpoints geprüft
- [ ] Barrierefreiheit (Fokus, ARIA, Kontrast) OK
- [ ] Semantik korrekt (HTML)
- [ ] Performance optimiert (Lazyload/Kompression)

## Abhängigkeiten / Überschneidungen
- Bewertungs-API, Produktdaten, Schema-Markup

## Akzeptanzkriterien
- Technische Funktion OK
- Konsistenz zum Designsystem
- A11y & rechtliche Vorgaben erfüllt

## Beispiel / Code
```html
<!-- Minimales, valides HTML-Beispiel -->
<div class="rating" aria-label="4,5 von 5 Sternen">
  <span aria-hidden="true">★★★★☆</span>
  <span class="rating__value">4,5/5 (120 Bewertungen)</span>
</div>
```

Bewertung der Relevanz 2025

⭐⭐⭐⭐ Bewertungen bleiben kaufentscheidend und stärken Vertrauen.
