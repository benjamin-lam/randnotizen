# Layout: E-Commerce Product Grid

## Beschreibung
Produktkacheln mit Bild, Preis, Bewertung und CTA bilden den Kern vieler Shop-Übersichten. Das Layout ermöglicht Sortierung, Filterung und Batch-Aktionen.

## Warum dieses Layout?
- Präsentiert viele Produkte strukturiert und vergleichbar.
- Unterstützt Facetten- und Filterlogik für schnelle Auswahl.
- Braucht sorgfältiges Management von Datenqualität und Performance.

## Anforderungen & Besonderheiten
- **Responsiveness:** Grid reagiert auf Breakpoints und unterstützt unterschiedliche Kartenbreiten.
- **Accessibility:** Komplette Karte als Link oder Button mit sichtbarem Fokus und ARIA-Labels.
- **SEO:** Jede Karte verlinkt auf kanonische Produktseiten mit strukturierten Daten.
- **Design-Guidelines:** Konsistente Bildverhältnisse, Preisformatierung und Label-Hierarchie.

## Umsetzung – Technische Leitplanken
- **Mobile First:** Startet einspaltig, priorisiert Produktbild und Preis.
- **Accessibility:** Beschriftet Aktionen wie Merkliste oder Warenkorb klar und fokussierbar.
- **SEO:** Vermeidet Duplicate Content durch Filterparameter und setzt rel="canonical".
- **Best Practices:** Lazy Loading + LQIP für Bilder, Sichtbare Rabatt-Badges, Skeleton-Loading bei Filtersuche

## Checkliste
- [ ] Bildgrößen und Ratio sind vereinheitlicht.
- [ ] Preisangaben entsprechen regulatorischen Vorgaben.
- [ ] Filter/Sortierung funktionieren mit Tastatur.
- [ ] Performance- und Tracking-Messung vorhanden.

## Abhängigkeiten / Überschneidungen
- Produktdaten-API
- Filter- und Sortiermodule

## Akzeptanzkriterien
- Produktgrid bleibt bei Filterwechsel performant.
- Screenreader können Karteninhalt vollständig erfassen.
- CWV bleiben trotz vieler Bilder im Zielbereich.

## Beispiel / Code
```html
<section class="grid sm:grid-cols-2 lg:grid-cols-3 gap-4">
  <article class="product-card">…</article>
</section>
```

Bewertung der Relevanz 2025

⭐⭐⭐⭐⭐ Zentral für digitale Handelsflächen.
