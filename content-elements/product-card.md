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
    <img src="produkt.webp" alt="Sneaker Modell X" loading="lazy" itemprop="image">
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
