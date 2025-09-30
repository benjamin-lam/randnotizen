---
title: "Image With Caption: Randnotiz"
date: 2025-09-30
tags: [UI, Komponente, Webentwicklung]
excerpt: "Warum Image With Caption unsere Content Elements-Notizen inspiriert."
layout: post
categories: [content-elements]
slug: content-elements-image-with-caption
original_path: content-elements/image-with-caption.md
---

## Einleitung
Es fühlt sich an wie ein Fund in einer verstaubten Prototyp-Schublade: **Image With Caption** passte heute perfekt in unsere Content Elements-Gedanken, und plötzlich roch der Raum nach Whiteboard-Markern und frisch gebrühtem Kaffee.

## Technischer Kern
Technisch betrachtet verlangt Image With Caption nach klaren Leitplanken. Ich habe die ursprüngliche Beschreibung unten angeheftet und mit Kommentaren versehen, damit der Transfer in das neue Blog sichtbar bleibt.

### Originalnotizen
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
  <img src="../assets/agents-and-robots.png" alt="Agentin und Roboter in einer futuristischen Stadt bei Nacht" loading="lazy">
  <figcaption>Agentin und Roboter beobachten die Stadtlichter.</figcaption>
</figure>
```

Bewertung der Relevanz 2025

⭐⭐⭐⭐ Bilder mit Kontext bleiben wichtig für Storytelling und Compliance.

## Anekdoten & Nerd-Zitate
Michael Crichton hätte wahrscheinlich eine komplette Katastrophensimulation um Image With Caption gestrickt, nur um zu zeigen, wie viele Dinge gleichzeitig schiefgehen können. Douglas Coupland würde dagegen eine Slack-Konversation voller Insider-Gags daraus machen. Und irgendwo zwinkert eine alte RFC dazu, weil die Nerd-Fakten selten stillstehen.

## Best Practices
- A11y: Image With Caption tastatur- und screenreader-freundlich gestalten.
- Performance: Image With Caption nur laden, wenn der Kontext es wirklich braucht.
- Wartbarkeit: Entscheidungen zu Image With Caption direkt neben dem Code dokumentieren.

## Fazit
Image With Caption bleibt ein schönes Beispiel dafür, wie Content Elements-Elemente Geschichten erzählen können, wenn man sie ernst nimmt und trotzdem mit Humor betrachtet.
