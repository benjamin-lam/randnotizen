# Content-Element: Skeleton Loader

## Beschreibung
Platzhalter-Layouts, die die spätere Struktur andeuten, während Inhalte laden.

## Warum dieses Element?
- Listen oder Karten während Datenabruf darstellen.
- Dashboard-Widgets ohne Layoutverschiebung laden.
- Trade-off: Falsche Skeletons können Erwartungen enttäuschen, wenn Inhalte anders aussehen.

## Anforderungen & Besonderheiten
- **Responsiveness:** Skeleton-Elemente spiegeln spätere Layoutgrößen, fluid skalieren.
- **Accessibility:** `aria-hidden` für Skeletons, tatsächliche Inhalte bei Verfügbarkeit ansagen.
- **SEO:** Kein direkter Einfluss, aber reduziert Cumulative Layout Shift.
- **Design-Guidelines:** Animierte Shimmer-Effekte dezent, Farben aus Neutraltönen.
- **Rechtliches:** Keine speziellen Anforderungen.

## Umsetzung – Technische Leitplanken
- **Mobile First:** Skeletons für kritische Bereiche priorisieren, um wahrgenommene Geschwindigkeit zu erhöhen.
- **Accessibility:** Skeletons entfernen, sobald Content geladen ist, `aria-busy` nutzen.
- **SEO:** Nicht relevant.
- **Best Practices:**
  - Skeletons an reale Content-Höhen anpassen.
  - Nicht zu viele Animationen verwenden (Performance).
  - Mit echten Ladezeiten abstimmen und Timeout setzen.

## Checkliste
- [ ] Darstellung auf allen Breakpoints geprüft
- [ ] Barrierefreiheit (Fokus, ARIA, Kontrast) OK
- [ ] Semantik korrekt (HTML)
- [ ] Performance optimiert (Lazyload/Kompression)

## Abhängigkeiten / Überschneidungen
- Designsystem, State-Management

## Akzeptanzkriterien
- Technische Funktion OK
- Konsistenz zum Designsystem
- A11y & rechtliche Vorgaben erfüllt

## Beispiel / Code
[content-elements-examples/skeleton-loader.html](../content-elements-examples/skeleton-loader.html)

```html
<!-- Minimales, valides HTML-Beispiel -->
<div class="skeleton-card" aria-hidden="true">
  <div class="skeleton skeleton--image"></div>
  <div class="skeleton skeleton--text"></div>
</div>
```

Bewertung der Relevanz 2025

⭐⭐⭐⭐ Skeletons verbessern wahrgenommene Performance und bleiben relevant.
