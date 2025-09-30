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
Zwischen Straßenbahn, Einkaufskorb und kurzen Pausen auf der Parkbank tippte ich die ersten Sätze ins Smartphone. Image Carousel stand noch warm aus dem letzten Deployment im Raum, und klar war: Heute erzählen wir diese Komponente so, wie altundwillig.de über große und kleine Webdramen schreibt – mitten im Alltag unseres Content Elements-Systems.

## Technischer Kern
Image Carousel ist einer dieser Bausteine, die niemand beachtet, bis sie fehlen. Wir haben das schmerzhaft gelernt, als ein Kunde das Feature ohne ARIA ausgeliefert hat und ein Feedback-Call zur Selbsthilfegruppe wurde. Seitdem legen wir das Mobile-Layout zuerst fest, tasten uns mit echten Fingern durch Buttons und Links und feiern jeden Moment, in dem der Screenreader flüssig vorliest. Ich halte mich an die Spezifikationen, aber ich erzähle sie wie Lagerfeuergeschichten: mit klaren HTML-Strukturen, sauberen States und einer Prise Humor. Und während ich daran denke, dass wir alle an halb fertigen Interfaces arbeiten, mahnt mich eine innere Stimme, jede Abhängigkeit dreimal zu prüfen.

### Originalnotizen
Ich lasse hier den historischen Steckbrief unangetastet; er ist mein Sicherheitsnetz, wenn das Storytelling überkocht:
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
- Ein Chatverlauf von letzter Woche: „Kannst du Image Carousel mal schnell deaktivieren?“ – „Nur wenn du mir einen neuen Kaffee bringst.“ Ergebnis: Kaffee kam, Image Carousel blieb.
- Merksatz: Technologie wird genau dann knifflig, wenn sie unsichtbar wirkt. Genau deshalb lassen wir Image Carousel nicht aus der Doku verschwinden.
- Während der Build lief, las ich alte Projekt-Notizen und sah uns alle als Varianten derselben Crew, die versucht, Image Carousel pixelweise in den Griff zu bekommen.
- In einer altundwillig.de-Sprachnachricht erzählte ich, wie ein Screenreader-User fragte: „Wo bin ich eigentlich?“ – dieser Satz hallt nach wie ein Drum-Solo.

## Best Practices
- **Accessibility lebt von Ritualen:** Prüfe Image Carousel mit Tastatur und Screenreader, bevor du überhaupt an Pixel-Politur denkst. Deine künftige Selbstachtung wird es dir danken.
- **Mobile First aus Überzeugung:** Beginne mit dem kleinsten Viewport und frage dich ernsthaft, ob du das Element auch im U-Bahn-Gedränge bedienen könntest.
- **Performance mit Hausverstand:** Lade nur, was wirklich gebraucht wird, sonst fühlt sich Image Carousel an wie ein Buffering-Screen aus der Modem-Ära.
- **Dokumentation neben dem Code:** Schreib dir dazu, warum Entscheidungen gefallen sind; sonst fragst du dich in drei Monaten selbst, was du damit meintest.
- **Team-Sync:** Stell sicher, dass Design, Content und Dev dieselben Erwartungen haben – sonst erzählt jeder eine andere Story über Image Carousel.

## Fazit
Zum Schluss fühlt sich Image Carousel an wie ein gut geölter Plattenspieler: nicht prahlerisch, aber unverzichtbar. Wir haben wieder gelernt, dass Disziplin bei Breakpoints und `aria`-Attributen genau der Unterschied zwischen Frust und Flow ist. Beim nächsten Rollout gönne ich mir mehr Zeit für User-Feedback, bevor der nächste Sturm aus Edge Cases anklopft.
