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
Noch bevor Slack das erste Ping losließ, balancierte ich zwischen Straßenbahn und improvisiertem Stehtisch und schrieb die ersten Stichworte ins Smartphone. Auf dem Screen wartete Filters Facets; kein Thriller, sondern das nächste Kapitel für F.ontend Navigation.

## Technischer Kern
Technisch gesehen sitzt Filters Facets genau an der Schnittstelle zwischen Ordnung und Emotion. Ich erinnere mich noch, wie wir im letzten Quartal eine Variante shippten, die auf dem Testgerät butterweich wirkte, auf einem alten Android aber ruckelte wie ein VHS-Band. Seitdem ist Mobile First mein Morgenritual; ich starte immer mit dem kleinsten Screen. Accessibility hält mich ehrlich: Ohne klare Fokuszustände oder Transkripte wird aus Eleganz sofort Chaos, und genau dann ruft jemand aus dem Support an. Die Originalnotizen unten dienen mir als Checkliste, doch meine heimliche Regel lautet: Wir alle tüfteln in unseren Kellern an der Zukunft. In diesem Keller sorge ich dafür, dass Filters Facets stabil bleibt, selbst wenn ein Sturm aus Edge Cases tobt.

### Originalnotizen
Unterhalb dieser Zeile wohnt das Rohmaterial – nach wie vor mein Truthahnthermometer für saubere Implementierung:
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
- In meinen Notizen steht noch der Satz: „Filters Facets riecht nach Filterkaffee und Ticket-Alarm.“ Das war der Abend vor dem Launch.
- Wir haben uns selbst beobachtet, wie wir mit Taschenlampen (a.k.a. Gerätepark) durch die QA-Nacht stapfen.
- Niemand von außen textet für uns, aber unsere Slack-Emojis halten uns wach, wenn wir wieder Mobile-Bugs jagen.
- Eine Kollegin sagte: „Accessibility fühlt sich an wie barfuß laufen – du merkst jeden Stein.“ Seitdem prüfe ich Filters Facets ohne Maus.

## Best Practices
- **Altgeräte-Test:** Wenn Filters Facets auf dem alten iPhone aus der Agentur-Schublade gut läuft, kannst du halbwegs ruhig schlafen.
- **Semantik rockt:** HTML-Struktur ernst nehmen, ARIA nur ergänzen. Alles andere ist wie ein Special-Effect ohne Plot.
- **Content-Strategie:** Besprich früh, welche Texte, Bilder oder Daten hier landen. Überraschungen mag höchstens der Cliffhanger im Serienfinale.
- **Fallbacks vorbereiten:** Offline, Low-Bandwidth, reduzierte Animation – Mobile First bedeutet, mit wenig auszukommen.
- **QA-Checklisten:** Hack dir eine Checkliste ins Repo, damit niemand vergisst, warum Filters Facets existiert.

## Fazit
Filters Facets ist am Ende wie eine Reihe kleiner Laternen im Tunnel: unscheinbar, aber ohne sie stolpern wir. Ich nehme aus diesem Durchgang mit, dass Mobile First und Accessibility keine Kapitelüberschriften sind, sondern Bauchentscheidungen für Menschen. Beim nächsten Mal baue ich noch früher Tests in den Workflow ein – und trinke meinen Kaffee vermutlich etwas langsamer.
