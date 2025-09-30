---
title: "Recently Viewed: Randnotiz"
date: 2025-09-30
tags: [UI, Komponente, Webentwicklung]
excerpt: "Warum Recently Viewed unsere Frontend-Notizen inspiriert."
layout: post
categories: [frontend]
slug: frontend-product-recently-viewed
original_path: frontend/product/recently-viewed.md
---

## Einleitung
Es fühlt sich an wie ein Fund in einer verstaubten Prototyp-Schublade: **Recently Viewed** passte heute perfekt in unsere Frontend-Gedanken, und plötzlich roch der Raum nach Whiteboard-Markern und frisch gebrühtem Kaffee.

## Technischer Kern
Technisch betrachtet verlangt Recently Viewed nach klaren Leitplanken. Ich habe die ursprüngliche Beschreibung unten angeheftet und mit Kommentaren versehen, damit der Transfer in das neue Blog sichtbar bleibt.

### Originalnotizen
# Zuletzt angesehene Produkte

## Kundenanforderung  
Als Nutzer:in möchte ich eine Liste der zuletzt angesehenen Produkte sehen, um schnell zurückzukehren zu einem Artikel, den ich interessant fand.

## Warum ist das so?  
Fördert Wiederentdeckung, erhöht Engagement und erleichtert Navigation zwischen Produkten.

## Anforderungen & Besonderheiten  
- Session- oder Nutzer-basiert speichern  
- Begrenzte Anzahl (z. B. 4–6 Items)  
- Datenschutz: keine personenbezogenen Daten ohne Zustimmung  

## Umsetzung – Technische Leitplanken  
- **Mobile First:** horizontale Scrollliste oder Carousel  
- **Accessibility:** ARIA wandern, Fokussteuerung  
- **SEO:** keine indexierten Links (nur interne Navigation)  
- **Best Practices:**  
 • Cache-basiert, nicht zu viele Anfragen  
 • Fallback bei leeren Historien  
 • Synchronisation über Geräte  

## Checkliste  
- [ ] Funktion aktiv  
- [ ] Anzeige korrekt  
- [ ] Updates bei neuen Ansichten  
- [ ] Performance geprüft  

## Akzeptanzkriterien  
- Liste aktualisiert korrekt  
- Klick auf Element führt zum Produkt  
- Layout passt auf allen Geräten  

---

## Bewertung der Relevanz 2025  
⭐⭐⭐⭐☆  
Sehr nützlich für UX, häufig erwartet.

## Anekdoten & Nerd-Zitate
Michael Crichton hätte wahrscheinlich eine komplette Katastrophensimulation um Recently Viewed gestrickt, nur um zu zeigen, wie viele Dinge gleichzeitig schiefgehen können. Douglas Coupland würde dagegen eine Slack-Konversation voller Insider-Gags daraus machen. Und irgendwo zwinkert eine alte RFC dazu, weil die Nerd-Fakten selten stillstehen.

## Best Practices
- A11y: Recently Viewed tastatur- und screenreader-freundlich gestalten.
- Performance: Recently Viewed nur laden, wenn der Kontext es wirklich braucht.
- Wartbarkeit: Entscheidungen zu Recently Viewed direkt neben dem Code dokumentieren.

## Fazit
Recently Viewed bleibt ein schönes Beispiel dafür, wie Frontend-Elemente Geschichten erzählen können, wenn man sie ernst nimmt und trotzdem mit Humor betrachtet.
