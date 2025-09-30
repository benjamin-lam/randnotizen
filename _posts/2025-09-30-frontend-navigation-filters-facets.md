---
title: "Filters Facets: Randnotiz"
date: 2025-09-30
tags: [UI, Komponente, Webentwicklung]
excerpt: "Warum Filters Facets unsere Frontend-Notizen inspiriert."
layout: post
categories: [frontend]
slug: frontend-navigation-filters-facets
original_path: frontend/navigation/filters-facets.md
---

## Einleitung
Es fühlt sich an wie ein Fund in einer verstaubten Prototyp-Schublade: **Filters Facets** passte heute perfekt in unsere Frontend-Gedanken, und plötzlich roch der Raum nach Whiteboard-Markern und frisch gebrühtem Kaffee.

## Technischer Kern
Technisch betrachtet verlangt Filters Facets nach klaren Leitplanken. Ich habe die ursprüngliche Beschreibung unten angeheftet und mit Kommentaren versehen, damit der Transfer in das neue Blog sichtbar bleibt.

### Originalnotizen
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

## Anekdoten & Nerd-Zitate
Michael Crichton hätte wahrscheinlich eine komplette Katastrophensimulation um Filters Facets gestrickt, nur um zu zeigen, wie viele Dinge gleichzeitig schiefgehen können. Douglas Coupland würde dagegen eine Slack-Konversation voller Insider-Gags daraus machen. Und irgendwo zwinkert eine alte RFC dazu, weil die Nerd-Fakten selten stillstehen.

## Best Practices
- A11y: Filters Facets tastatur- und screenreader-freundlich gestalten.
- Performance: Filters Facets nur laden, wenn der Kontext es wirklich braucht.
- Wartbarkeit: Entscheidungen zu Filters Facets direkt neben dem Code dokumentieren.

## Fazit
Filters Facets bleibt ein schönes Beispiel dafür, wie Frontend-Elemente Geschichten erzählen können, wenn man sie ernst nimmt und trotzdem mit Humor betrachtet.
