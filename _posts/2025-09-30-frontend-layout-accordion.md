---
title: "Accordion: Randnotiz"
date: 2025-09-30
tags: [UI, Komponente, Webentwicklung]
excerpt: "Warum Accordion unsere Frontend-Notizen inspiriert."
layout: post
categories: [frontend]
slug: frontend-layout-accordion
original_path: frontend/layout/accordion.md
---

## Einleitung
Es fühlt sich an wie ein Fund in einer verstaubten Prototyp-Schublade: **Accordion** passte heute perfekt in unsere Frontend-Gedanken, und plötzlich roch der Raum nach Whiteboard-Markern und frisch gebrühtem Kaffee.

## Technischer Kern
Technisch betrachtet verlangt Accordion nach klaren Leitplanken. Ich habe die ursprüngliche Beschreibung unten angeheftet und mit Kommentaren versehen, damit der Transfer in das neue Blog sichtbar bleibt.

### Originalnotizen
# Akkordeon (Collapsible Panels)

## Kundenanforderung  
Als Nutzer:in möchte ich Inhalte (z. B. Produktdetails, FAQs) in aufklappbaren Panels sehen, um die Seite übersichtlich zu halten und nur bei Bedarf Details anzuzeigen.

## Warum ist das so?  
Akkordeons sparen Platz, verbessern Übersichtlichkeit und vermeiden überfrachtete Layouts, besonders auf mobilen Geräten.

## Anforderungen & Besonderheiten  
- Animation / Transition verzichten auf zu große Bewegungen  
- Inhalte vollständig aus dem DOM – nicht nur via JS versteckt  
- Barrierefreiheit: ARIA, Fokussteuerung  
- SEO: Inhalte bleiben im DOM, idealerweise auch indexierbar  

## Umsetzung – Technische Leitplanken  
- **Mobile First:** Panels mit Touch-Tap, große Klickflächen  
- **Accessibility:** `aria-expanded`, `aria-controls`, Tastatursteuerung (Enter / Space)  
- **SEO:** Inhalte im DOM vorhanden, nicht nur via JS  
- **Best Practices:**  
 • Minimale Repaint-Kosten  
 • Zustand persistieren (z. B. per Hash)  
 • Offen ggf. Markierung  

## Checkliste  
- [ ] Panels korrekt öffnen/schließen  
- [ ] ARIA-Attribute korrekt  
- [ ] Animation sanft & performant  
- [ ] Inhalte immer zugreifbar  

## Abhängigkeiten / Überschneidungen  
- Produktdetailseite  
- FAQ-Seite  
- UI-Komponenten  

## Akzeptanzkriterien  
- Panels funktionieren mit Maus, Touch, Tastatur  
- Inhalte sichtbar & versteckt korrekt  
- Barrierefreie Navigation  

---

## Bewertung der Relevanz 2025  
⭐⭐⭐⭐☆  
Sehr häufig eingesetzt – besonders bei mobilen Versionen von Detailseiten oder FAQs.

## Anekdoten & Nerd-Zitate
Michael Crichton hätte wahrscheinlich eine komplette Katastrophensimulation um Accordion gestrickt, nur um zu zeigen, wie viele Dinge gleichzeitig schiefgehen können. Douglas Coupland würde dagegen eine Slack-Konversation voller Insider-Gags daraus machen. Und irgendwo zwinkert eine alte RFC dazu, weil die Nerd-Fakten selten stillstehen.

## Best Practices
- A11y: Accordion tastatur- und screenreader-freundlich gestalten.
- Performance: Accordion nur laden, wenn der Kontext es wirklich braucht.
- Wartbarkeit: Entscheidungen zu Accordion direkt neben dem Code dokumentieren.

## Fazit
Accordion bleibt ein schönes Beispiel dafür, wie Frontend-Elemente Geschichten erzählen können, wenn man sie ernst nimmt und trotzdem mit Humor betrachtet.
