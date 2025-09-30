# Content-Element: Image with Caption

## Beschreibung
Bilddarstellung mit erläuternder Bildunterschrift.

## Warum dieses Element?
- Produktfotos oder Screenshots mit erklärender Caption einsetzen.
- Blogartikel mit Bildnachweisen oder Quellenangaben versehen.
- Trade-off: Große Bilder beeinflussen Ladezeiten, erfordern Optimierung.

## Anforderungen & Besonderheiten
- **Responsiveness:** Fluides Verhalten, `srcset`/`sizes` nutzen, Captions unterhalb anordnen.
- **Accessibility:** Alternativtexte bereitstellen, Caption als ergänzende Beschreibung, ausreichender Kontrast.
- **SEO:** Alt-Texte und strukturierte Daten (`figure`, `figcaption`) verbessern Bild-Sichtbarkeit.
- **Design-Guidelines:** Bildgrößen definieren, Weißraum um Caption, Typografie harmonisch.
- **Rechtliches:** Bildrechte beachten, Quellenangabe bei Lizenzanforderung integrieren.

## Umsetzung – Technische Leitplanken
- **Mobile First:** Bilder zunächst klein laden, progressive Vergrößerung via `srcset`.
- **Accessibility:** Kontrast für Text auf Caption-Hintergrund sicherstellen, keine rein dekorativen Captions.
- **SEO:** Dateinamen beschreibend, Lazyloading (`loading="lazy"`) einsetzen.
- **Best Practices:**
  - Moderne Formate (WebP/AVIF) mit Fallback anbieten.
  - Responsive Container mit `max-width` begrenzen.
  - Caption optional mit Quellenlink versehen.

## Checkliste
- [ ] Darstellung auf allen Breakpoints geprüft
- [ ] Barrierefreiheit (Fokus, ARIA, Kontrast) OK
- [ ] Semantik korrekt (HTML)
- [ ] Performance optimiert (Lazyload/Kompression)

## Abhängigkeiten / Überschneidungen
- Bild-CDN, Lightbox (optional)

## Akzeptanzkriterien
- Technische Funktion OK
- Konsistenz zum Designsystem
- A11y & rechtliche Vorgaben erfüllt

## Beispiel / Code
[content-elements-examples/image-with-caption.html](../content-elements-examples/image-with-caption.html)

```html
<!-- Minimales, valides HTML-Beispiel -->
<figure class="image">
  <img src="/assets/agents-and-robots.txt" alt="Agentin und Roboter in einer futuristischen Stadt bei Nacht" loading="lazy">
  <figcaption>Agentin und Roboter beobachten die Stadtlichter.</figcaption>
</figure>
```

Bewertung der Relevanz 2025

⭐⭐⭐⭐ Bilder mit Kontext bleiben wichtig für Storytelling und Compliance.
