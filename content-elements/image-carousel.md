# Content-Element: Image Carousel

## Beschreibung
Slider-Komponente für mehrere Bilder mit optionaler Lightbox.

## Warum dieses Element?
- Produktgalerien auf E-Commerce-Seiten.
- Event- oder Referenz-Slideshows auf Landingpages.
- Trade-off: Zu viele Slides reduzieren Aufmerksamkeit, Interaktion oft gering.

## Anforderungen & Besonderheiten
- **Responsiveness:** Touch- und Mausbedienung, Breakpoints für Anzahl sichtbarer Slides.
- **Accessibility:** Fokusreihenfolge, `aria-live` für Slide-Wechsel, Pause-/Play-Controls.
- **SEO:** Bilder mit Alt-Text und Lazyload, Lightbox nicht indexrelevant.
- **Design-Guidelines:** Navigationselemente konsistent, Dot-/Arrow-Styling, Übergänge dezent.
- **Rechtliches:** Bildrechte beachten, Tracking in Lightbox vermeiden.

## Umsetzung – Technische Leitplanken
- **Mobile First:** Einzelne Slides, Swipe-Gesten, geringe Dateigrößen.
- **Accessibility:** Autoplay standardmäßig deaktiviert, klare Fokusindikatoren.
- **SEO:** `loading="lazy"`, strukturierte Daten für Produktbilder möglich.
- **Best Practices:**
  - Slides per Keyboard navigierbar machen.
  - Progressive Enhancement bei deaktiviertem JS.
  - Bildvorab-Laden für nächstes Slide optimieren.

## Checkliste
- [ ] Darstellung auf allen Breakpoints geprüft
- [ ] Barrierefreiheit (Fokus, ARIA, Kontrast) OK
- [ ] Semantik korrekt (HTML)
- [ ] Performance optimiert (Lazyload/Kompression)

## Abhängigkeiten / Überschneidungen
- Slider-Library, Lightbox, Bild-CDN

## Akzeptanzkriterien
- Technische Funktion OK
- Konsistenz zum Designsystem
- A11y & rechtliche Vorgaben erfüllt

## Beispiel / Code
[content-elements-examples/image-carousel.html](../content-elements-examples/image-carousel.html)

```html
<!-- Minimales, valides HTML-Beispiel -->
<div class="carousel" aria-roledescription="Karussell">
  <button class="carousel__prev" aria-label="Vorheriges Bild">‹</button>
  <ul class="carousel__track">
    <li class="carousel__slide"><img src="bild1.webp" alt="Produkt Vorderansicht" loading="lazy"></li>
  </ul>
  <button class="carousel__next" aria-label="Nächstes Bild">›</button>
</div>
```

Bewertung der Relevanz 2025

⭐⭐⭐⭐ Karussells bleiben gängig, müssen jedoch nutzerzentriert optimiert werden.
