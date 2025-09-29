# Breadcrumb-Navigation

## Kundenanforderung  
Als Nutzer:in möchte ich eine Pfadnavigation („Home > Kategorie > Subkategorie“) sehen, damit ich weiß, wo ich mich befinde und zurück navigieren kann.

## Warum ist das so?  
Breadcrumbs verbessern Orientierung, Navigationsgeschwindigkeit und reduzieren „Lost in navigation“.  

## Anforderungen & Besonderheiten  
- Dynamisch generiert entsprechend Kategorie-Hierarchie  
- Klickbare Pfade  
- Rücksicht auf SEO (Breadcrumbs von Suchmaschinen nutzbar)  

## Umsetzung – Technische Leitplanken  
- **Mobile First:** ggf. gekürzte Breadcrumbs oder „… > Unterkategorie“  
- **Accessibility:** ARIA „breadcrumb“ Landmark  
- **SEO:** strukturierte Daten (BreadcrumbList)  
- **Best Practices:**  
 • Konsistentes Format  
 • Trennung mit Separator  
 • Keine redundanten Segmentnamen  

## Checkliste  
- [ ] Pfad korrekt aufgebaut  
- [ ] Alle Segmente klickbar  
- [ ] Strukturierte Daten  
- [ ] Mobile Anzeigelogik  

## Abhängigkeiten / Überschneidungen  
- Kategoriestruktur  
- SEO / Schema  
- Navigationssystem  

## Akzeptanzkriterien  
- Breadcrumbs funktionieren durchgängig  
- Strukturielle SEO-Daten korrekt  
- Anzeige passt für mobile Geräte  

---

## Bewertung der Relevanz 2025  
⭐⭐⭐☆☆  
Wichtig für Usability & SEO – aber nicht „sichtbar sexy“.  

