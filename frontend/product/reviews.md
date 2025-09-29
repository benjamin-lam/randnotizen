# Bewertungen & Rezensionen

## Kundenanforderung  
Als Nutzer:in möchte ich sehen können, wie andere Kunden ein Produkt bewertet haben (Sterne, Text), um Vertrauen und eine informierte Kaufentscheidung zu treffen.

## Warum ist das so?  
Sozialer Beweis („Social Proof“) erhöht Glaubwürdigkeit. Kunden vertrauen oft Erfahrungen anderer. Außerdem verringert eine transparente Bewertungen-Komponente Retouren oder Frustrationen.

## Anforderungen & Besonderheiten  
- Aggregierte Sternewertung + einzelne Rezensionen  
- Filter / Sortierung nach „neueste“, „hilfreichste“  
- Möglichkeit, eigene Bewertung zu hinterlassen  
- Moderation / Verifizierung (z. B. „echter Käufer“)  
- Datenschutz: keine personenbezogenen Daten ohne Einwilligung  

## Umsetzung – Technische Leitplanken  
- **Mobile First:** Rezensionen in Accordion oder Tab-Ansicht auf kleinen Geräten  
- **Accessibility:** Überschriftenstruktur, ARIA-Labels, Fokus beim Wechsel  
- **SEO:** Strukturierte Daten (Schema.org `Review` / `AggregateRating`)  
- **Best Practices:**  
 • Lazy load für viele Bewertungen  
 • Anzeige nur sinnvoller Ausschnitte + „mehr laden“  
 • Verifizierte Käufe kennzeichnen  
 • Stern-Icons skalierbar  

## Checkliste  
- [ ] Durchschnittsbewertung angezeigt  
- [ ] Einzelne Rezensionen verfügbar  
- [ ] Sortieren / Filtern möglich  
- [ ] Nutzer können selbst bewerten  
- [ ] Strukturierte Daten integriert  

## Abhängigkeiten / Überschneidungen  
- Produktdetailseite  
- Nutzerkonto / Login  
- Moderations-Backend / Admin  
- API für Bewertungen  

## Akzeptanzkriterien  
- Bewertungsdaten korrekt aggregiert  
- Neue Bewertung speicherbar  
- Display funktioniert auf allen Geräten  
- Rich Snippets korrekt ausgegeben  

---

## Bewertung der Relevanz 2025  
⭐⭐⭐⭐☆  
Sehr relevant – Standards mittlerweile üblich. Besonders wichtig: Moderation & Qualität sichern.  
