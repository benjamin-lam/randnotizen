# Storefinder / Filial-Locator

## Kundenanforderung  
Als Kund:in möchte ich sehen, wo sich physische Filialen befinden und welche Filiale in meiner Nähe ist.

## Warum ist das so?  
Verbindung zwischen Online und Offline stärkt Vertrauen und ermöglicht Click-and-Collect oder Filialbesuche.

## Anforderungen & Besonderheiten  
- Map-Darstellung (z. B. Google Maps, OpenStreetMap)  
- Standorte mit Adresse, Öffnungszeiten, Kontakt  
- Suchfilter (PLZ, Radius)  
- DSGVO: keine Standortdaten speichern ohne Zustimmung  

## Umsetzung – Technische Leitplanken  
- **Mobile First:** Kartenansicht mobil optimiert  
- **Accessibility:** Karten mit Alternativtext, Tastaturkompatibilität  
- **SEO:** Standortseiten individualisiert und indexierbar  
- **Best Practices:**  
 • Clustering bei vielen Points  
 • Lazy load Karten  
 • Fallback-Ansicht ohne Karte  

## Checkliste  
- [ ] Alle Filialdaten korrekt  
- [ ] Filter & Suchfunktion  
- [ ] Karten-Integration funktioniert  
- [ ] Mobile & Desktop Layout  

## Abhängigkeiten / Überschneidungen  
- Standortdaten / Datenbank  
- Karten-API  
- CMS / Admin-Backend  

## Akzeptanzkriterien  
- Filiale in Nähe korrekt angezeigt  
- Karte lädt & zoomt  
- Kartenfehlerbehandlung  

---

## Bewertung der Relevanz 2025  
⭐⭐⭐☆☆  
Relevanter für Omnichannel-Shops mit Filialen; für reine Online-Händler oft optional.  

