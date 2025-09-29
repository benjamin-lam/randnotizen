# Cross-Selling / Upselling

## Kundenanforderung  
Als Kunde:in möchte ich passende Zusatzprodukte oder höherwertige Varianten zu meinem aktuellen Produkt sehen, damit ich ggf. mehr kaufe oder bessere Varianten entdecke.

## Warum ist das so?  
Upselling / Cross-Selling erhöht Umsatz pro Kunde. Es lenkt auf relevante Angebote, erweitert den Warenkorb sinnvoll.

## Anforderungen & Besonderheiten  
- Empfehlung mit sinnvoller Logik (Kombi, Ergänzung, Zubehör)  
- Darstellung auf PDP oder im Checkout  
- Datenschutz: Empfehlung basierend auf anonymen Mustern, nicht personenbezogene Daten ohne Einwilligung  
- Einfaches Management im Backend  

## Umsetzung – Technische Leitplanken  
- **Mobile First:** Empfehlung unterhalb Produkttab oder „weitere Produkte“ scrollbar  
- **Accessibility:** ARIA-Labels, klare Linkstruktur  
- **SEO:** Empfehlungstitel als Link, kein Cloaking  
- **Best Practices:**  
 • Empfehlung basierend auf Algorithmen (kaufhistorisch, collaborative filtering)  
 • Caching von Empfehlungen  
 • Fallback bei fehlendem Vorschlag  
 • Metriken (Klickraten)  

## Checkliste  
- [ ] Empfehlungslogik definiert  
- [ ] Anzeigen an sinnvollen Stellen  
- [ ] Empfehlungen korrekt verlinkt  
- [ ] Performance getestet  

## Abhängigkeiten / Überschneidungen  
- Product-API / Daten  
- Analytics / Tracking  
- Backend / Empfehlungsservice  

## Akzeptanzkriterien  
- Empfehlungen passen thematisch  
- Links führen zur korrekten Seite  
- Keine Performance-Einbrüche  
- Anzeigen nicht störend  

---

## Bewertung der Relevanz 2025  
⭐⭐⭐⭐☆  
Wichtig, aber weniger kritisch als Produktdetailseite – vor allem in mittleren Shops sinnvoll.  

