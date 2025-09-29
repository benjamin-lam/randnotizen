# Produktdetailseite (PDP)

## Kundenanforderung  
Als Nutzer:in möchte ich auf einer Produktdetailseite alle relevanten Informationen (Bilder, Beschreibung, Preis, Varianten, Bewertungen etc.) sehen, um eine Kaufentscheidung treffen zu können.

## Warum ist das so?  
Die PDP ist der zentrale Conversion-Punkt. Eine gute PDP liefert Vertrauen und Klarheit, reduziert Abbrüche.

## Anforderungen & Besonderheiten  
- Varianten (Farben, Größen, Bundles)  
- Lagerbestand / Verfügbarkeit  
- Preis & Staffelpreise  
- Bewertung & Rezensionen  
- Cross-Selling / Upselling  
- Rich Snippets / strukturierte Daten für SEO  
- Datenschutz: keine personenbezogenen Elemente ohne Zustimmung  

## Umsetzung – Technische Leitplanken  
- **Mobile First:** responsives Layout, Accordion für Details bei kleinen Geräten  
- **Accessibility:** strukturierte Überschriften, Fokussteuerung, ARIA für Varianten  
- **SEO:** JSON-LD für Produktdaten, Canonical, Meta-Daten  
- **Best Practices:**  
 • Pre-Rendering / SSR  
 • Code-Splitting bei interaktiven Modulen  
 • Deferred Loading von Sektionen (Bewertungen, Cross-Selling)  

## Checkliste  
- [ ] Bilder & Galerie korrekt  
- [ ] Varianten-Auswahl funktionsfähig  
- [ ] Preisanzeige & Verfügbarkeit  
- [ ] Bewertungsabschnitt  
- [ ] Rich Snippets eingebunden  
- [ ] CTA (In den Warenkorb) präsent  

## Abhängigkeiten / Überschneidungen  
- Produkt-API Backend  
- Reviews-Service  
- Cross-Selling / Empfehlungssystem  
- Lager-/Inventarsystem  

## Akzeptanzkriterien  
- Alle Varianten auswählbar  
- Bilder galeriefähig  
- Richtige Metadaten im HTML  
- Kein Performance-Engpass  

---

## Bewertung der Relevanz 2025  
⭐⭐⭐⭐⭐  
Extrem wichtig – Kern jeder E-Commerce-Plattform.  

