# Layout: Card Layout

## Beschreibung
Karten bündeln Bild, Titel, Teasertext und CTA in wiederverwendbaren Modulen. Sie eignen sich für Artikelübersichten, Feature-Highlights oder Produktteaser.

## Warum dieses Layout?
- Skaliert modular über verschiedene Content-Typen.
- Unterstützt klare Scanbarkeit durch visuelle Blöcke.
- Kann bei zu vielen Karten überladen wirken.

## Anforderungen & Besonderheiten
- **Responsiveness:** Karten passen sich in Grid- oder Flexstrukturen an und behalten konsistente Höhen.
- **Accessibility:** Fokusrahmen sichtbar, Klickflächen ausreichend groß und Alternativtexte gepflegt.
- **SEO:** Primärer CTA als Link, sprechende Überschriften und strukturierte Daten optional.
- **Design-Guidelines:** Einheitliche Bildverhältnisse, konsistente Typografie und Abstände.

## Umsetzung – Technische Leitplanken
- **Mobile First:** Beginnt einspaltig und erweitert sich auf mehrere Spalten.
- **Accessibility:** Arbeitet mit aria-labels oder Überschriftenelementen für Kartentitel.
- **SEO:** Linkstruktur so anlegen, dass Karten direkt indexiert werden.
- **Best Practices:** Lazy Loading für Bilder, Hover- und Fokus-States angleichen, Karteninhalte klar priorisieren

## Checkliste
- [ ] Tab-Reihenfolge der Karten ist logisch.
- [ ] Teasertexte bleiben kurz und prägnant.
- [ ] Bilder besitzen Alternativtexte.
- [ ] Performance- und Accessibility-Metriken dokumentiert.

## Abhängigkeiten / Überschneidungen
- Card-Komponentenbibliothek
- Bild-CDN oder Asset-Pipeline

## Akzeptanzkriterien
- Kartenhöhen skalieren ohne Layoutsprünge.
- CTA ist sowohl per Maus als auch Tastatur bedienbar.
- Lazy Loading reduziert initiale Ladezeit spürbar.

## Beispiel / Code
```html
<article class="card">
  <img alt="" src="" />
  <h3>…</h3>
  <p>…</p>
</article>
```

Bewertung der Relevanz 2025

⭐⭐⭐⭐⭐ Universeller Baustein für vielfältige Content-Module.
