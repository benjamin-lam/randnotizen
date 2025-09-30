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
Zwischen Straßenbahn, Supermarktkasse und Handy-Display schrieb ich die ersten Zeilen auf dem Smartphone, während in Bremen der Duft von frisch gemahlenem Kaffee durch die Luft zog. Product Card blinkte mir entgegen wie ein Mixtape aus einer vergessenen Schublade, und klar war: Heute bekommt Product Card die große Bühne in unserem Content Elements-Tagebuch.

## Technischer Kern
Technisch gesehen sitzt Product Card genau an der Schnittstelle zwischen Ordnung und Emotion. Ich erinnere mich noch, wie wir im letzten Quartal eine Variante shippten, die auf dem Testgerät butterweich wirkte, auf einem alten Android aber ruckelte wie ein VHS-Band. Seitdem ist Mobile First mein Morgenritual; ich starte immer mit dem kleinsten Screen. Accessibility hält mich ehrlich: Ohne klare Fokuszustände oder Transkripte wird aus Eleganz sofort Chaos, und genau dann ruft jemand aus dem Support an. Die Originalnotizen unten dienen mir als Checkliste, doch meine heimliche Regel lautet: Wir alle tüfteln in unseren Kellern an der Zukunft. In diesem Keller sorge ich dafür, dass Product Card stabil bleibt, selbst wenn ein Sturm aus Edge Cases tobt.

### Originalnotizen
Unterhalb dieser Zeile wohnt das Rohmaterial – nach wie vor mein Truthahnthermometer für saubere Implementierung:
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
- Im Retro-Meeting tippte jemand: „Product Card war mein Bosslevel.“ – Ich antwortete: „Nur weil du den Accessibility-Check nach Mitternacht gemacht hast.“
- In meinem inneren Katastrophenskript gibt es immer eine Szene, in der Product Card ausfällt und der Shop nervös wird. In der Realität helfen uns Logs und Gelassenheit.
- Beim Debuggen flüstert mir eher das Bauchgefühl zu: „Wir leben zwischen Bugfixes, also mach sie hübsch.“ Das gilt besonders, wenn der Mobile-Test im Bus stattfindet.
- O-Ton eines Kunden: „Seit Product Card sauber läuft, fühlt sich unser Interface an wie eine gute Playlist.“ Besseres Lob gibt es nicht.

## Best Practices
- **Altgeräte-Test:** Wenn Product Card auf dem alten iPhone aus der Agentur-Schublade gut läuft, kannst du halbwegs ruhig schlafen.
- **Semantik rockt:** HTML-Struktur ernst nehmen, ARIA nur ergänzen. Alles andere ist wie ein Special-Effect ohne Plot.
- **Content-Strategie:** Besprich früh, welche Texte, Bilder oder Daten hier landen. Überraschungen mag höchstens der Cliffhanger im Serienfinale.
- **Fallbacks vorbereiten:** Offline, Low-Bandwidth, reduzierte Animation – Mobile First bedeutet, mit wenig auszukommen.
- **QA-Checklisten:** Hack dir eine Checkliste ins Repo, damit niemand vergisst, warum Product Card existiert.

## Fazit
Product Card ist am Ende wie eine Reihe kleiner Laternen im Tunnel: unscheinbar, aber ohne sie stolpern wir. Ich nehme aus diesem Durchgang mit, dass Mobile First und Accessibility keine Kapitelüberschriften sind, sondern Bauchentscheidungen für Menschen. Beim nächsten Mal baue ich noch früher Tests in den Workflow ein – und trinke meinen Kaffee vermutlich etwas langsamer.
