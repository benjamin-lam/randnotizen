---
title: "Product Card: Randnotiz"
date: 2025-09-30
tags: [UI, Komponente, Webentwicklung]
excerpt: "Warum Product Card unsere Content Elements-Notizen inspiriert."
layout: post
categories: [content-elements]
slug: content-elements-product-card
original_path: content-elements/product-card.md
---

## Einleitung
Es fühlt sich an wie ein Fund in einer verstaubten Prototyp-Schublade: **Product Card** passte heute perfekt in unsere Content Elements-Gedanken, und plötzlich roch der Raum nach Whiteboard-Markern und frisch gebrühtem Kaffee.

## Technischer Kern
Technisch betrachtet verlangt Product Card nach klaren Leitplanken. Ich habe die ursprüngliche Beschreibung unten angeheftet und mit Kommentaren versehen, damit der Transfer in das neue Blog sichtbar bleibt.

### Originalnotizen
# Content-Element: Product Card

## Beschreibung
Produktkachel mit Bild, Preis, Bewertung und CTA.

## Warum dieses Element?
- Produktlisten in Shops darstellen.
- Empfehlungen oder Upselling-Module einbinden.
- Trade-off: Zu viele Informationen können die Vergleichbarkeit erschweren.

## Anforderungen & Besonderheiten
- **Responsiveness:** Card-Layout responsive stacken, Bildverhältnis beibehalten.
- **Accessibility:** Komplette Karte als Link, aber Fokus auf einzelne Aktionen erlauben.
- **SEO:** Strukturierte Daten (`Product`) und Rich Snippets.
- **Design-Guidelines:** Bildgrößen, Typografie, Badge-Positionen, Hover-Styling.
- **Rechtliches:** Preisangabenverordnung beachten, inkl. MwSt. und Versandhinweis.

## Umsetzung – Technische Leitplanken
- **Mobile First:** Wichtige Infos priorisieren, CTA prominent.
- **Accessibility:** Alt-Texte für Produktbilder, Preis als Text, klare Fokus-States.
- **SEO:** `itemprop`-Attribute oder JSON-LD einsetzen.
- **Best Practices:**
  - Lazyload für Bilder.
  - Varianten/Verfügbarkeiten klar kennzeichnen.
  - CTA mit eindeutiger Aktion beschriften.

## Checkliste
- [ ] Darstellung auf allen Breakpoints geprüft
- [ ] Barrierefreiheit (Fokus, ARIA, Kontrast) OK
- [ ] Semantik korrekt (HTML)
- [ ] Performance optimiert (Lazyload/Kompression)

## Abhängigkeiten / Überschneidungen
- Bewertungen, Preis-API, Tracking

## Akzeptanzkriterien
- Technische Funktion OK
- Konsistenz zum Designsystem
- A11y & rechtliche Vorgaben erfüllt

## Beispiel / Code
[content-elements-examples/product-card.html](../content-elements-examples/product-card.html)

```html
<!-- Minimales, valides HTML-Beispiel -->
<article class="product-card" itemscope itemtype="https://schema.org/Product">
  <a href="/produkt" class="product-card__link">
    <img src="../assets/agents-and-robots.png" alt="Agentin und Roboter in einer futuristischen Stadt bei Nacht" loading="lazy" itemprop="image">
    <h3 itemprop="name">Sneaker X</h3>
    <p class="product-card__price" itemprop="offers" itemscope itemtype="https://schema.org/Offer">
      <span itemprop="price">89,90</span> €
    </p>
  </a>
  <button type="button">In den Warenkorb</button>
</article>
```

Bewertung der Relevanz 2025

⭐⭐⭐⭐⭐ Produktkacheln sind zentral für E-Commerce und Conversion-relevant.

## Anekdoten & Nerd-Zitate
Michael Crichton hätte wahrscheinlich eine komplette Katastrophensimulation um Product Card gestrickt, nur um zu zeigen, wie viele Dinge gleichzeitig schiefgehen können. Douglas Coupland würde dagegen eine Slack-Konversation voller Insider-Gags daraus machen. Und irgendwo zwinkert eine alte RFC dazu, weil die Nerd-Fakten selten stillstehen.

## Best Practices
- A11y: Product Card tastatur- und screenreader-freundlich gestalten.
- Performance: Product Card nur laden, wenn der Kontext es wirklich braucht.
- Wartbarkeit: Entscheidungen zu Product Card direkt neben dem Code dokumentieren.

## Fazit
Product Card bleibt ein schönes Beispiel dafür, wie Content Elements-Elemente Geschichten erzählen können, wenn man sie ernst nimmt und trotzdem mit Humor betrachtet.
