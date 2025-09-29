# Sortieroptionen

## Kundenanforderung  
Als Nutzer:in möchte ich Produkte sortieren nach Preis, Relevanz, Beliebtheit, Neuheiten etc., um meine Auswahl besser steuern zu können.

## Warum ist das so?  
Sortierung ist Usability-Standard: Nutzer erwarten Kontrolle über Reihenfolge. Ohne Sortierung kann Relevanz leiden.

## Anforderungen & Besonderheiten  
- Sorte der Optionen: Preis auf/ab, Name, Neuheit, Bewertung  
- Kombination mit Filter & Paginierung  
- SEO: Vermeidung von Duplicate Content  
- Performance: Sortierung effizient backendseitig  

## Umsetzung – Technische Leitplanken  
- **Mobile First:** einfache Dropdowns oder Buttons  
- **Accessibility:** Label, ARIA, Fokus-Elemente  
- **SEO:** canonical oder parameterbereinigte URLs  
- **Best Practices:**  
 • Standard-Sortierung definieren  
 • Parameter konsistent (z. B. `?sort=price_asc`)  
 • Vermeidung überflüssiger Kombinationen  

## Checkliste  
- [ ] Alle relevanten Sortieroptionen vorhanden  
- [ ] Sortierung funktioniert mit Filter/Pagination  
- [ ] SEO-Parameterstrategie vorhanden  
- [ ] Performance unter Last  

## Abhängigkeiten / Überschneidungen  
- Filter / Facetten  
- Pagination  
- Backend-Sortier-API  

## Akzeptanzkriterien  
- Sortierung korrekt und stabil  
- URLs repräsentieren Sortierung  
- Keine unerwarteten Nebeneffekte  

---

## Bewertung der Relevanz 2025  
⭐⭐⭐⭐☆  
Hoch – Standard in fast jedem Shop, aber kein Killer-Feature in kleinen Shops.  

