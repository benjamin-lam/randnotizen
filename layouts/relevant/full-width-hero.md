# Layout: Full Width Hero

## Beschreibung
Der Hero-Bereich nutzt die gesamte Seitenbreite für starke Botschaften, Visuals und Calls-to-Action. Eingesetzt auf Landingpages, Produktseiten oder Kampagnenstarts.

## Warum dieses Layout?
- Sichert maximale Aufmerksamkeit direkt beim Einstieg.
- Bietet viel Raum für Bildsprache und zentrale Call-to-Actions.
- Kann bei schlechter Optimierung LCP und Fokus beeinträchtigen.

## Anforderungen & Besonderheiten
- **Responsiveness:** Fluides Skalieren von Bildern, Texten und CTA-Elementen.
- **Accessibility:** Kontraste zwischen Text und Hintergrund sowie aussagekräftige Alt-Texte gewährleisten.
- **SEO:** Hero enthält die Hauptüberschrift und relevante Keywords.
- **Design-Guidelines:** Klare Hierarchie, großzügiges Spacing und ggf. Overlays zur Textlesbarkeit.

## Umsetzung – Technische Leitplanken
- **Mobile First:** Hero-Text und CTA priorisieren, Hintergrundbild adaptiv laden.
- **Accessibility:** Sichtbare Fokuszustände und tastaturfreundliche CTAs sicherstellen.
- **SEO:** H1 im Hero platzieren und strukturierte Daten bei Kampagnen ergänzen.
- **Best Practices:** <picture> für responsive Images, LCP-Optimierung durch Preload, CTA oberhalb des Folds positionieren

## Checkliste
- [ ] CTA ist sofort sichtbar und fokussierbar.
- [ ] Hintergrundbilder sind komprimiert und responsive.
- [ ] Hero erfüllt Kontrastanforderungen.
- [ ] Lighthouse-LCP und A11y-Checks bestanden.

## Abhängigkeiten / Überschneidungen
- CTA-Komponenten
- Bildoptimierungs-Stack

## Akzeptanzkriterien
- Hero lädt performant mit optimiertem LCP.
- Texte bleiben auf allen Breakpoints gut lesbar.
- CTA ist mit Tastatur und Screenreader erreichbar.

## Beispiel / Code
```html
<section class="hero">
  <h1>Headline</h1>
  <a class="btn" href="#">CTA</a>
</section>
```

Bewertung der Relevanz 2025

⭐⭐⭐⭐⭐ Kernbaustein für aufmerksamkeitsstarke Landingpages.
