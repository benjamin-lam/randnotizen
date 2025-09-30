---
title: "Storefinder: Randnotiz"
date: 2025-09-30
tags: [UI, Komponente, Webentwicklung]
excerpt: "Warum Storefinder unsere Frontend-Notizen inspiriert."
layout: post
categories: [frontend]
slug: frontend-misc-storefinder
original_path: frontend/misc/storefinder.md
---

## Einleitung
Es fühlt sich an wie ein Fund in einer verstaubten Prototyp-Schublade: **Storefinder** passte heute perfekt in unsere Frontend-Gedanken, und plötzlich roch der Raum nach Whiteboard-Markern und frisch gebrühtem Kaffee.

## Technischer Kern
Technisch betrachtet verlangt Storefinder nach klaren Leitplanken. Ich habe die ursprüngliche Beschreibung unten angeheftet und mit Kommentaren versehen, damit der Transfer in das neue Blog sichtbar bleibt.

### Originalnotizen
# Storefinder / Filial-Locator

## Kundenanforderung  
Als Kund:in möchte ich sehen, wo sich physische Filialen befinden und welche Filiale in meiner Nähe ist.

## Warum ist das so?  
Verbindung zwischen Online und Offline stärkt Vertrauen und ermöglicht Click-and-Collect oder Filialbesuche.

## Anforderungen & Besonderheiten  
- Map-Darstellung (z. B. Google Maps, OpenStreetMap)  
- Standorte mit Adresse, Öffnungszeiten, Kontakt  
- Suchfilter (PLZ, Radius)  
- DSGVO: keine Standortdaten speichern ohne Zustimmung  

## Umsetzung – Technische Leitplanken  
- **Mobile First:** Kartenansicht mobil optimiert  
- **Accessibility:** Karten mit Alternativtext, Tastaturkompatibilität  
- **SEO:** Standortseiten individualisiert und indexierbar  
- **Best Practices:**  
 • Clustering bei vielen Points  
 • Lazy load Karten  
 • Fallback-Ansicht ohne Karte  

## Checkliste  
- [ ] Alle Filialdaten korrekt  
- [ ] Filter & Suchfunktion  
- [ ] Karten-Integration funktioniert  
- [ ] Mobile & Desktop Layout  

## Abhängigkeiten / Überschneidungen  
- Standortdaten / Datenbank  
- Karten-API  
- CMS / Admin-Backend  

## Akzeptanzkriterien  
- Filiale in Nähe korrekt angezeigt  
- Karte lädt & zoomt  
- Kartenfehlerbehandlung  

---

## Bewertung der Relevanz 2025  
⭐⭐⭐☆☆  
Relevanter für Omnichannel-Shops mit Filialen; für reine Online-Händler oft optional.

## Anekdoten & Nerd-Zitate
Michael Crichton hätte wahrscheinlich eine komplette Katastrophensimulation um Storefinder gestrickt, nur um zu zeigen, wie viele Dinge gleichzeitig schiefgehen können. Douglas Coupland würde dagegen eine Slack-Konversation voller Insider-Gags daraus machen. Und irgendwo zwinkert eine alte RFC dazu, weil die Nerd-Fakten selten stillstehen.

## Best Practices
- A11y: Storefinder tastatur- und screenreader-freundlich gestalten.
- Performance: Storefinder nur laden, wenn der Kontext es wirklich braucht.
- Wartbarkeit: Entscheidungen zu Storefinder direkt neben dem Code dokumentieren.

## Fazit
Storefinder bleibt ein schönes Beispiel dafür, wie Frontend-Elemente Geschichten erzählen können, wenn man sie ernst nimmt und trotzdem mit Humor betrachtet.
