# Mini-Cart / Off-Canvas Warenkorb

## Kundenanforderung  
Als Nutzer:in möchte ich jederzeit über eine kleine Übersichtsbox (Mini-Cart) sehen, was aktuell im Warenkorb ist, ohne Seite zu verlassen.

## Warum ist das so?  
Reduziert Friktion, Nutzer sehen schnell Änderungen und können Inhalte prüfen, bevor sie weiter navigieren.

## Anforderungen & Besonderheiten  
- Live-Aktualisierung bei Artikeländerung  
- Anzeige von Preis, Mini-Bild, Menge  
- Mögliches Entfernen/Ändern direkt im Mini-Cart  
- Keine Ablenkung (Overlay mit Schließmöglichkeit)  

## Umsetzung – Technische Leitplanken  
- **Mobile First:** Off-Canvas Slide-In / Drawer  
- **Accessibility:** Fokusmanagement beim Öffnen/Schließen, ARIA-Labels  
- **SEO:** Nicht indexierbar  
- **Best Practices:**  
 • Animationen sparsam einsetzen  
 • Minimale Verzögerung bei Aktualisierung  
 • Skeleton Loading  

## Checkliste  
- [ ] Mini-Cart öffnet & schließt korrekt  
- [ ] Inhalt aktuell  
- [ ] Aktionen (Entfernen, Menge) möglich  
- [ ] Performance akzeptabel  

## Abhängigkeiten / Überschneidungen  
- Warenkorb-API  
- Produktseite  
- Checkout  

## Akzeptanzkriterien  
- Live-Update funktioniert  
- Interaktion im Mini-Cart möglich  
- Keine Layoutprobleme  

---

## Bewertung der Relevanz 2025  
⭐⭐⭐⭐⭐  
Sehr hoch – Nutzer erwarten direktes Feedback ohne Seitenwechsel.  

