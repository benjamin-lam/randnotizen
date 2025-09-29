# Produkt-Grid / Kachelansicht

## Kundenanforderung  
Als Besucher:in möchte ich mehrere Produkte gleichzeitig in Form von Kacheln sehen, um schnell mein Interesse zu steuern und ggf. direkt in Produktdetailseiten zu springen.

## Warum ist das so?  
Grid-Darstellung ist effizient, visuell ansprechend und ermöglicht schnellen Überblick.

## Anforderungen & Besonderheiten  
- Einheitliche Kachelgrößen oder variabel (Masonry)  
- Responsive Anzahl der Spalten  
- Bildformatsoptimierung  
- Lazy Loading (Infinite Scroll oder Paginierung)  

## Umsetzung – Technische Leitplanken  
- **Mobile First:** 1–2 Spalten auf kleinen Geräten  
- **Accessibility:** Fokus-States, Tab-Reihenfolge, ARIA-Labels  
- **SEO:** Produktlinks als echte `<a>`-Tags  
- **Best Practices:**  
 • Bildoptimierung / lazy load  
 • CSS Grid oder flexbox  
 • Skeleton-Placeholder beim Laden  
 • Überschrift & Preis direkt in Kachel  

## Checkliste  
- [ ] Responsive Spaltenanzahl implementiert  
- [ ] Bilder mit Alt-Text  
- [ ] Links in Kacheln korrekt  
- [ ] Performance-Tests  

## Abhängigkeiten / Überschneidungen  
- Produkt-API  
- Paginierung / Infinite Scroll  
- Filter & Sortierung  

## Akzeptanzkriterien  
- Kacheln korrekt angezeigt über Breakpoints  
- Klick auf Kachel führt zur Produktseite  
- Kein Layout-Verschieben (CLS minimal)  
- Schnelle Ladezeit  

---

## Bewertung der Relevanz 2025  
⭐⭐⭐⭐⭐  
Sehr hoch – Produkt-Grid ist Basis vieler Shop-Seiten.  

