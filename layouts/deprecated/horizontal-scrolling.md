# Layout: Horizontal Scrolling Layout

## Beschreibung
Ein Layout mit horizontalem Scrollen als primäre Navigationsachse wirkt unnatürlich und ist auf mobilen Geräten schwer steuerbar.

## Warum dieses Layout?
- Kann besondere Storytelling-Experiences liefern.
- Setzt visuelle Highlights in Szene.
- Verursacht UX-Probleme bei Scroll-Gesten und Orientierung.

## Anforderungen & Besonderheiten
- **Responsiveness:** Klare Scroll-Hinweise, horizontale Scrollbereiche mit Touch-Unterstützung.
- **Accessibility:** Alternativen für Tastatur und Screenreader bereitstellen, wheel-Events bedacht einsetzen.
- **SEO:** Wichtige Inhalte auch vertikal zugänglich machen.
- **Design-Guidelines:** Deutliche Pfeile, Pagination oder Snap-Punkte, um Orientierung zu sichern.

## Umsetzung – Technische Leitplanken
- **Mobile First:** Standard-Layouts bevorzugen und horizontale Scrollstrecken nur optional einbinden.
- **Accessibility:** Scroll-Mapping auf Trackpad/Wheel nur vorsichtig nutzen.
- **SEO:** Vertikale Alternativansicht oder Jump-Links bereitstellen.
- **Best Practices:** Scroll-Hints anzeigen, Snapping optional, Fallback auf vertikale Liste

## Checkliste
- [ ] Scroll-Hinweise sind sichtbar.
- [ ] Tastaturbedienung möglich.
- [ ] Vertikale Alternative vorhanden.
- [ ] A11y- und Performance-Check dokumentiert.

## Abhängigkeiten / Überschneidungen
- Scroll- und Animation-Utilities
- Fallback-Layouts

## Akzeptanzkriterien
- Nutzer verstehen Interaktion ohne Tutorial.
- Screenreader erhalten linearen Alternativzugang.
- Stakeholder akzeptieren Einsatz nur in Spezialfällen.

## Beispiel / Code
```html
<section class="horizontal-scroll" aria-label="Galerie">
  <div class="scroll-track">…</div>
</section>
```

> ⚠️ Deprecated: Nicht mehr empfohlen für Mobile-First-Designs (nur zu Dokumentationszwecken).

Bewertung der Relevanz 2025

⭐⭐☆☆☆ Nur für spezielle Storytelling-Experimente erhalten.
