# Content-Element: Loading Spinner

## Beschreibung
Animierter Indikator für laufende Prozesse.

## Warum dieses Element?
- Kurze Ladezeiten bei Formularen oder API-Calls anzeigen.
- Asynchrone Aktionen wie Datenabrufe visualisieren.
- Trade-off: Reine Spinner ohne Kontext frustrieren, wenn Ladezeiten länger dauern.

## Anforderungen & Besonderheiten
- **Responsiveness:** Größe skaliert mit Container, Kontrast zum Hintergrund.
- **Accessibility:** `role="status"` und beschreibender Text, `aria-live=polite`.
- **SEO:** Keine Relevanz.
- **Design-Guidelines:** Konsistente Animation, Designsystem-konforme Farben.
- **Rechtliches:** Keine speziellen Anforderungen.

## Umsetzung – Technische Leitplanken
- **Mobile First:** Spinner nicht zu groß, damit Inhalte sichtbar bleiben.
- **Accessibility:** Zusätzlichen Text wie „Lädt…“ bereitstellen.
- **SEO:** Nicht relevant.
- **Best Practices:**
  - Maximale Ladezeit definieren und Fehlerzustand zeigen.
  - Spinner erst nach 500 ms anzeigen, um Flackern zu vermeiden.
  - Mit Skeletons kombinieren, wenn längere Wartezeiten zu erwarten sind.

## Checkliste
- [ ] Darstellung auf allen Breakpoints geprüft
- [ ] Barrierefreiheit (Fokus, ARIA, Kontrast) OK
- [ ] Semantik korrekt (HTML)
- [ ] Performance optimiert (Lazyload/Kompression)

## Abhängigkeiten / Überschneidungen
- Animationslibrary, State-Management

## Akzeptanzkriterien
- Technische Funktion OK
- Konsistenz zum Designsystem
- A11y & rechtliche Vorgaben erfüllt

## Beispiel / Code
```html
<!-- Minimales, valides HTML-Beispiel -->
<div class="spinner" role="status" aria-live="polite">
  <span class="sr-only">Lädt…</span>
</div>
```

Bewertung der Relevanz 2025

⭐⭐⭐⭐ Ladeindikatoren bleiben Standard, sollten aber immer mit Kontext kombiniert werden.
