# Akkordeon (Collapsible Panels)

## Kundenanforderung  
Als Nutzer:in möchte ich Inhalte (z. B. Produktdetails, FAQs) in aufklappbaren Panels sehen, um die Seite übersichtlich zu halten und nur bei Bedarf Details anzuzeigen.

## Warum ist das so?  
Akkordeons sparen Platz, verbessern Übersichtlichkeit und vermeiden überfrachtete Layouts, besonders auf mobilen Geräten.

## Anforderungen & Besonderheiten  
- Animation / Transition verzichten auf zu große Bewegungen  
- Inhalte vollständig aus dem DOM – nicht nur via JS versteckt  
- Barrierefreiheit: ARIA, Fokussteuerung  
- SEO: Inhalte bleiben im DOM, idealerweise auch indexierbar  

## Umsetzung – Technische Leitplanken  
- **Mobile First:** Panels mit Touch-Tap, große Klickflächen  
- **Accessibility:** `aria-expanded`, `aria-controls`, Tastatursteuerung (Enter / Space)  
- **SEO:** Inhalte im DOM vorhanden, nicht nur via JS  
- **Best Practices:**  
 • Minimale Repaint-Kosten  
 • Zustand persistieren (z. B. per Hash)  
 • Offen ggf. Markierung  

## Checkliste  
- [ ] Panels korrekt öffnen/schließen  
- [ ] ARIA-Attribute korrekt  
- [ ] Animation sanft & performant  
- [ ] Inhalte immer zugreifbar  

## Abhängigkeiten / Überschneidungen  
- Produktdetailseite  
- FAQ-Seite  
- UI-Komponenten  

## Akzeptanzkriterien  
- Panels funktionieren mit Maus, Touch, Tastatur  
- Inhalte sichtbar & versteckt korrekt  
- Barrierefreie Navigation  

---

## Bewertung der Relevanz 2025  
⭐⭐⭐⭐☆  
Sehr häufig eingesetzt – besonders bei mobilen Versionen von Detailseiten oder FAQs.  

