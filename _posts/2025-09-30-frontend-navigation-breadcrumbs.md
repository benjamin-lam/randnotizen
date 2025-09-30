---
title: "Breadcrumbs: Randnotiz"
date: 2025-09-30
tags: [UI, Komponente, Webentwicklung]
excerpt: "Warum Breadcrumbs unsere Frontend-Notizen inspiriert."
layout: post
categories: [frontend]
slug: frontend-navigation-breadcrumbs
original_path: frontend/navigation/breadcrumbs.md
---

## Einleitung
Es fühlt sich an wie ein Fund in einer verstaubten Prototyp-Schublade: **Breadcrumbs** passte heute perfekt in unsere Frontend-Gedanken, und plötzlich roch der Raum nach Whiteboard-Markern und frisch gebrühtem Kaffee.

## Technischer Kern
Technisch betrachtet verlangt Breadcrumbs nach klaren Leitplanken. Ich habe die ursprüngliche Beschreibung unten angeheftet und mit Kommentaren versehen, damit der Transfer in das neue Blog sichtbar bleibt.

### Originalnotizen
# Breadcrumb-Navigation

## Kundenanforderung  
Als Nutzer:in möchte ich eine Pfadnavigation („Home > Kategorie > Subkategorie“) sehen, damit ich weiß, wo ich mich befinde und zurück navigieren kann.

## Warum ist das so?  
Breadcrumbs verbessern Orientierung, Navigationsgeschwindigkeit und reduzieren „Lost in navigation“.  

## Anforderungen & Besonderheiten  
- Dynamisch generiert entsprechend Kategorie-Hierarchie  
- Klickbare Pfade  
- Rücksicht auf SEO (Breadcrumbs von Suchmaschinen nutzbar)  

## Umsetzung – Technische Leitplanken  
- **Mobile First:** ggf. gekürzte Breadcrumbs oder „… > Unterkategorie“  
- **Accessibility:** ARIA „breadcrumb“ Landmark  
- **SEO:** strukturierte Daten (BreadcrumbList)  
- **Best Practices:**  
 • Konsistentes Format  
 • Trennung mit Separator  
 • Keine redundanten Segmentnamen  

## Checkliste  
- [ ] Pfad korrekt aufgebaut  
- [ ] Alle Segmente klickbar  
- [ ] Strukturierte Daten  
- [ ] Mobile Anzeigelogik  

## Abhängigkeiten / Überschneidungen  
- Kategoriestruktur  
- SEO / Schema  
- Navigationssystem  

## Akzeptanzkriterien  
- Breadcrumbs funktionieren durchgängig  
- Strukturielle SEO-Daten korrekt  
- Anzeige passt für mobile Geräte  

---

## Bewertung der Relevanz 2025  
⭐⭐⭐☆☆  
Wichtig für Usability & SEO – aber nicht „sichtbar sexy“.

## Anekdoten & Nerd-Zitate
Michael Crichton hätte wahrscheinlich eine komplette Katastrophensimulation um Breadcrumbs gestrickt, nur um zu zeigen, wie viele Dinge gleichzeitig schiefgehen können. Douglas Coupland würde dagegen eine Slack-Konversation voller Insider-Gags daraus machen. Und irgendwo zwinkert eine alte RFC dazu, weil die Nerd-Fakten selten stillstehen.

## Best Practices
- A11y: Breadcrumbs tastatur- und screenreader-freundlich gestalten.
- Performance: Breadcrumbs nur laden, wenn der Kontext es wirklich braucht.
- Wartbarkeit: Entscheidungen zu Breadcrumbs direkt neben dem Code dokumentieren.

## Fazit
Breadcrumbs bleibt ein schönes Beispiel dafür, wie Frontend-Elemente Geschichten erzählen können, wenn man sie ernst nimmt und trotzdem mit Humor betrachtet.
