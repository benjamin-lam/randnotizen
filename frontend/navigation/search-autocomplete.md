# Suchfunktion mit Autocomplete

## Kundenanforderung  
Als Nutzer:in möchte ich bei Eingabe im Suchfeld Vorschläge (Produkte, Kategorien, Schlagwörter) sehen, um schneller zum Ziel zu kommen.

## Warum ist das so?  
Suchfunktion ist zentrale Navigation. Vorschläge reduzieren Tippfehler, führen schneller zum Ziel und verbessern Conversion.  

## Anforderungen & Besonderheiten  
- Typo-Toleranz / fuzzy matching  
- Anzeige von Produktvorschlägen + Kategorien + Aktionen  
- Caching und Performance unter Last  
- Datenschutz: keine ungewollte Speicherung personenbezogener Suchdaten.

## Umsetzung – Technische Leitplanken  
- **Mobile First:** Vorschlagsliste unter dem Suchfeld passend zum Viewport.  
- **Accessibility:** ARIA-Combobox, Listen mit Rollen, Fokusmanagement.  
- **SEO:** keine Indexierung von Autocomplete-URLs, nur Hauptseiten.  
- **Best Practices:**  
 • Debounce / Throttle der Eingaben  
 • Minimaler Request-Länge (z. B. 2 Zeichen)  
 • Caching auf Client und Server  
 • Synonymliste & Stoppwörter  

## Checkliste  
- [ ] Vorschläge erscheinen ab x Zeichen  
- [ ] Auswahl via Tastatur möglich  
- [ ] Performance unter Last getestet  
- [ ] Datenschutz eingehalten  

## Abhängigkeiten / Überschneidungen  
- Produktdaten-API / Backend-Suche  
- Taxonomie / Kategorien  
- Cache-Layer  

## Akzeptanzkriterien  
- Vorschlagsliste korrekt gefüllt  
- Auswahl via Enter oder Klick möglich  
- Latency unter Zielwert (z. B. 100 ms)  
- Keine Fehler bei Edge Cases  

---

## Bewertung der Relevanz 2025  
⭐⭐⭐⭐⭐  
Sehr hoch – Nutzergewöhntheit, Conversion-Wirkung, Performance entscheidend.  

