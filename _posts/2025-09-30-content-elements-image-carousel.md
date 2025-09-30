---
title: "Image Carousel: Randnotiz"
date: 2025-09-30
tags: [UI, Komponente, Webentwicklung]
excerpt: "Warum Image Carousel unsere Content Elements-Notizen inspiriert."
layout: post
categories: [content-elements]
slug: content-elements-image-carousel
original_path: content-elements/image-carousel.md
---

## Einleitung
Es fühlt sich an wie ein Fund in einer verstaubten Prototyp-Schublade: **Image Carousel** passte heute perfekt in unsere Content Elements-Gedanken, und plötzlich roch der Raum nach Whiteboard-Markern und frisch gebrühtem Kaffee.

## Technischer Kern
Technisch betrachtet verlangt Image Carousel nach klaren Leitplanken. Ich habe die ursprüngliche Beschreibung unten angeheftet und mit Kommentaren versehen, damit der Transfer in das neue Blog sichtbar bleibt.

### Originalnotizen
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
    <li class="carousel__slide"><img src="../assets/agents-and-robots.png" alt="Agentin und Roboter in einer futuristischen Stadt bei Nacht" loading="lazy"></li>
  </ul>
  <button class="carousel__next" aria-label="Nächstes Bild">›</button>
</div>
```

Bewertung der Relevanz 2025

⭐⭐⭐⭐ Karussells bleiben gängig, müssen jedoch nutzerzentriert optimiert werden.

## Anekdoten & Nerd-Zitate
Michael Crichton hätte wahrscheinlich eine komplette Katastrophensimulation um Image Carousel gestrickt, nur um zu zeigen, wie viele Dinge gleichzeitig schiefgehen können. Douglas Coupland würde dagegen eine Slack-Konversation voller Insider-Gags daraus machen. Und irgendwo zwinkert eine alte RFC dazu, weil die Nerd-Fakten selten stillstehen.

## Best Practices
- A11y: Image Carousel tastatur- und screenreader-freundlich gestalten.
- Performance: Image Carousel nur laden, wenn der Kontext es wirklich braucht.
- Wartbarkeit: Entscheidungen zu Image Carousel direkt neben dem Code dokumentieren.

## Fazit
Image Carousel bleibt ein schönes Beispiel dafür, wie Content Elements-Elemente Geschichten erzählen können, wenn man sie ernst nimmt und trotzdem mit Humor betrachtet.
