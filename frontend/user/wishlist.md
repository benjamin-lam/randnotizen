# Wunschliste / Merkliste

## Kundenanforderung  
Als registrierte:r Nutzer:in möchte ich Produkte auf eine Wunschliste setzen, um sie später zu überblicken oder zu teilen.

## Warum ist das so?  
Nutzer nutzen Wishlist zur Planung, zum Vergleich, zur Erinnerung – und oftmals wird später daraus ein Kauf. Es erhöht Engagement.

## Anforderungen & Besonderheiten  
- Bestände mitberücksichtigen  
- Nutzerbindung & Synchronisation (z. B. zwischen Geräten)  
- Teilen-Funktionen (optional)  
- Datenschutz bei Teil-Links  

## Umsetzung – Technische Leitplanken  
- **Mobile First:** Button „Zur Wunschliste“ prominent erreichbar  
- **Accessibility:** ARIA-Labels, Zustände (aktiv/inaktiv)  
- **SEO:** Kein indexierter Link (Wunschlistenseiten privat)  
- **Best Practices:**  
 • Real-time Feedback („hinzugefügt“)  
 • Synchronisation mit Nutzerkonto  
 • Fallback für Gäste (Session-basiert)  

## Checkliste  
- [ ] Produkte zur Wunschliste hinzufügen / entfernen  
- [ ] Wunschliste persistiert zwischen Sitzungen  
- [ ] Synchronisation über Geräte  
- [ ] Teilen-Option (falls geplant)  

## Abhängigkeiten / Überschneidungen  
- Nutzerkonto / Auth  
- Produktdaten / API  
- Session / Cache  

## Akzeptanzkriterien  
- Wunschliste editierbar  
- Sichtbarkeit & Status korrekt  
- Performance unter hoher Last  

---

## Bewertung der Relevanz 2025  
⭐⭐⭐⭐☆  
Mittel bis hoch – in vielen Shops bereits erwartet. Für kleinere Shops optional.  

