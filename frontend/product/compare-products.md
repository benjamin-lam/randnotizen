# Produktvergleich (Compare)

## Kundenanforderung  
Als Nutzer:in möchte ich mehrere Produkte nebeneinander vergleichen (Eigenschaften, Preis etc.), um eine fundierte Entscheidung zu treffen.

## Warum ist das so?  
Vergleich minimiert Aufwand, erhöht Vertrauen und vermeidet Rückfragen.

## Anforderungen & Besonderheiten  
- Vergleichbare Merkmale definieren  
- Maximalzahl von Produkten beschränken (z. B. 3–4)  
- Layout auf kleinen Geräten – meist Scroll oder Tabs  
- Datenschutz: nur öffentliche Produktdaten  

## Umsetzung – Technische Leitplanken  
- **Mobile First:** Vergleich als nebeneinander scrollbares Raster oder Tabs  
- **Accessibility:** Tabellenstruktur mit `thead`/`tbody`, ARIA-Labels  
- **SEO:** Vergleichsseiten ggf. nicht indexieren  
- **Best Practices:**  
 • Sync mit Auswahl  
 • Vorkonfigurierte Template-Vergleiche  
 • UX: Hervorhebung der Unterschiede  

## Checkliste  
- [ ] Vergleichsfunktion aktiviert  
- [ ] Detailmerkmale abgebildet  
- [ ] Übersichtliche Darstellung  
- [ ] Mobile-kompatibel  

## Abhängigkeiten / Überschneidungen  
- Produktdaten / API  
- UI-Komponenten  
- Filter / Eigenschaften  

## Akzeptanzkriterien  
- Vergleich funktioniert korrekt  
- Layout responsiv  
- Auswahl & Entfernen funktioniert  

---

## Bewertung der Relevanz 2025  
⭐⭐⭐☆☆  
Nützlich in großen Shops mit vielen ähnlichen Produkten, aber kein Muss in kleinen Shops.  

