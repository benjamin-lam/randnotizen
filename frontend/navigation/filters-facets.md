# Filter & Facettennavigation

## Kundenanforderung  
Als Nutzer:in möchte ich auf Kategorieseiten Produkte durch Filter (z. B. Preis, Marke, Eigenschaften) einschränken, um schneller relevante Produkte zu finden.

## Warum ist das so?  
Ohne Filter scrollt man durch viele irrelevante Produkte. Filter verbessern Effizienz und Conversion-Pfad.

## Anforderungen & Besonderheiten  
- Logik bei mehrfacher Auswahl (AND / OR)  
- Filter-Counts (Anzahl möglicher Produkte)  
- SEO: keine zu viele Filterkombinationen indexieren  
- Performance: Filterabanfragen schnell, Partial-Rendering  

## Umsetzung – Technische Leitplanken  
- **Mobile First:** Filter als Side Drawer / Off-Canvas  
- **Accessibility:** ARIA, Fokus, klare Beschriftungen  
- **SEO:** canonical tags, Maskierung von Facetten-URLs  
- **Best Practices:**  
 • Serverseitige Filterkomputation  
 • Clientseitige Inkremente (AJAX)  
 • Ergebniszählung (Counts)  
 • Pagination-Kohärenz  

## Checkliste  
- [ ] Alle wesentlichen Filtertypen integriert  
- [ ] Kombinationen möglich  
- [ ] Performance bei hoher Last  
- [ ] SEO-Filterstrategie definiert  

## Abhängigkeiten / Überschneidungen  
- Such-API / Backend  
- Kategorie-Struktur  
- Pagination / Sortierung  

## Akzeptanzkriterien  
- Filter schneiden richtig  
- Kombinationen korrekt  
- keine toten Filter (leerer Rückgabewert)  
- SEO-konforme URL-Struktur  

---

## Bewertung der Relevanz 2025  
⭐⭐⭐⭐⭐  
Essentiell in mittelgroßen bis großen Shops – besonders bei umfangreichem Sortiment.  

