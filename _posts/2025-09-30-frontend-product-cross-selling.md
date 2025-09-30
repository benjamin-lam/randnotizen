---
title: "Cross Selling: Randnotiz"
date: 2025-09-30
tags: [UI, Komponente, Webentwicklung]
excerpt: "Warum Cross Selling unsere Frontend-Notizen inspiriert."
layout: post
categories: [frontend]
slug: frontend-product-cross-selling
original_path: frontend/product/cross-selling.md
---

## Einleitung
Es fühlt sich an wie ein Fund in einer verstaubten Prototyp-Schublade: **Cross Selling** passte heute perfekt in unsere Frontend-Gedanken, und plötzlich roch der Raum nach Whiteboard-Markern und frisch gebrühtem Kaffee.

## Technischer Kern
Technisch betrachtet verlangt Cross Selling nach klaren Leitplanken. Ich habe die ursprüngliche Beschreibung unten angeheftet und mit Kommentaren versehen, damit der Transfer in das neue Blog sichtbar bleibt.

### Originalnotizen
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

## Anekdoten & Nerd-Zitate
Michael Crichton hätte wahrscheinlich eine komplette Katastrophensimulation um Cross Selling gestrickt, nur um zu zeigen, wie viele Dinge gleichzeitig schiefgehen können. Douglas Coupland würde dagegen eine Slack-Konversation voller Insider-Gags daraus machen. Und irgendwo zwinkert eine alte RFC dazu, weil die Nerd-Fakten selten stillstehen.

## Best Practices
- A11y: Cross Selling tastatur- und screenreader-freundlich gestalten.
- Performance: Cross Selling nur laden, wenn der Kontext es wirklich braucht.
- Wartbarkeit: Entscheidungen zu Cross Selling direkt neben dem Code dokumentieren.

## Fazit
Cross Selling bleibt ein schönes Beispiel dafür, wie Frontend-Elemente Geschichten erzählen können, wenn man sie ernst nimmt und trotzdem mit Humor betrachtet.
