# Layout: Two Column – Equal Width

## Beschreibung
Zwei gleich breite Spalten stellen Inhalt und begleitende Medien ausgewogen dar. Geeignet für Feature-Übersichten, Vergleiche oder Bild-Text-Kombinationen.

## Warum dieses Layout?
- Sorgt für visuelles Gleichgewicht zwischen Text und Medien.
- Lässt sich modular mit Komponenten befüllen.
- Kann bei langen Texten fragmentiert wirken und die Leseführung stören.

## Anforderungen & Besonderheiten
- **Responsiveness:** Spalten stapeln auf kleinen Screens und richten sich an Containergrößen aus.
- **Accessibility:** DOM-Reihenfolge folgt der gewünschten Lesereihenfolge, unabhängig vom visuellen Layout.
- **SEO:** Überschriften und Absätze klar strukturieren, damit beide Spalten verständlich bleiben.
- **Design-Guidelines:** Gleichmäßige Spaltenabstände, ausreichend Luft für Medieninhalte.

## Umsetzung – Technische Leitplanken
- **Mobile First:** Beginnt als einspaltiges Layout und erweitert sich ab definiertem Breakpoint auf zwei Spalten.
- **Accessibility:** Verzichtet auf rein optische Reihenfolge-Manipulation zugunsten logischer Lesbarkeit.
- **SEO:** Sichert konsistente h2/h3-Struktur auch bei geteilten Inhalten.
- **Best Practices:** Container Queries nutzen, Bildgrößen responsiv skalieren, Spaltenhöhe flexibel halten

## Checkliste
- [ ] Leselänge der Textspalte geprüft.
- [ ] Fokusreihenfolge entspricht inhaltlicher Priorität.
- [ ] Medien sind responsiv und performant eingebunden.
- [ ] Accessibility- und Performance-Metriken dokumentiert.

## Abhängigkeiten / Überschneidungen
- Medienkomponenten
- Grid-System

## Akzeptanzkriterien
- Auf mobilen Geräten werden Spalten ohne Layout-Brüche gestapelt.
- Content bleibt auch bei reduzierter Breite verständlich.
- Screenreader geben die Inhalte in korrekter Reihenfolge wieder.

## Beispiel / Code
```html
<section class="grid md:grid-cols-2 gap-6">
  <div>Spalte A</div>
  <div>Spalte B</div>
</section>
```

Bewertung der Relevanz 2025

⭐⭐⭐⭐☆ Ausgewogenes Layout für kombinierte Text- und Medienblöcke.
