# Layout: Gallery Layout

## Beschreibung
Eine Galerie präsentiert Bild- oder Medienkollektionen mit optionaler Lightbox. Sie eignet sich für Pressebereiche, Produktansichten oder Moodboards.

## Warum dieses Layout?
- Setzt visuelle Inhalte in den Mittelpunkt.
- Unterstützt verschiedene Medienformate inklusive Video.
- Kann bei schlechter Optimierung zu Performance-Problemen führen.

## Anforderungen & Besonderheiten
- **Responsiveness:** Skaliert zwischen einzelnen Spalten und Mehrspalt-Ansichten, unterstützt Swipe-Gesten.
- **Accessibility:** Lightbox steuerbar per Tastatur, klare Alt-Texte und Beschreibungen.
- **SEO:** Bilddaten mit beschreibenden Dateinamen, Alt-Texten und optional JSON-LD.
- **Design-Guidelines:** Konsistente Abstände, Thumbnail-Ratio und Hover-Zustände.

## Umsetzung – Technische Leitplanken
- **Mobile First:** Beginnt mit einspaltiger Darstellung und ermöglicht horizontales Scrollen nur kontextuell.
- **Accessibility:** Lightbox nutzt Dialog-Pattern mit Fokus-Trap und ESC-Schließen.
- **SEO:** Strukturierte Daten (ImageGallery) bei öffentlichen Sammlungen ergänzen.
- **Best Practices:** Lazy Loading, Srcset für responsive Bilder, Keyboard Shortcuts dokumentieren

## Checkliste
- [ ] Lazy Loading für alle Medien aktiviert.
- [ ] Lightbox ist vollständig tastaturbedienbar.
- [ ] Alt-Texte beschreiben Inhalt präzise.
- [ ] Performance- und Accessibility-Checks bestanden.

## Abhängigkeiten / Überschneidungen
- Lightbox-Komponente
- Medien-Asset-Management

## Akzeptanzkriterien
- Galerie bleibt auch bei vielen Assets performant.
- Lightbox respektiert Fokusreihenfolge und ESC.
- Swipe- oder Pfeilnavigation funktioniert zuverlässig.

## Beispiel / Code
```html
<section class="gallery grid sm:grid-cols-2 lg:grid-cols-3 gap-4">
  <a class="gallery-item" href="#" aria-label="Bild öffnen">…</a>
</section>
```

Bewertung der Relevanz 2025

⭐⭐⭐⭐⭐ Schlüssel-Layout für visuelle Asset-Sammlungen.
