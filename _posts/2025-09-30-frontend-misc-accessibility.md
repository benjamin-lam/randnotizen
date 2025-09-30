---
title: "Accessibility: Randnotiz"
date: 2025-09-30
tags: [UI, Komponente, Webentwicklung]
excerpt: "Warum Accessibility unsere Frontend-Notizen inspiriert."
layout: post
categories: [frontend]
slug: frontend-misc-accessibility
original_path: frontend/misc/accessibility.md
---

## Einleitung
Es fühlt sich an wie ein Fund in einer verstaubten Prototyp-Schublade: **Accessibility** passte heute perfekt in unsere Frontend-Gedanken, und plötzlich roch der Raum nach Whiteboard-Markern und frisch gebrühtem Kaffee.

## Technischer Kern
Technisch betrachtet verlangt Accessibility nach klaren Leitplanken. Ich habe die ursprüngliche Beschreibung unten angeheftet und mit Kommentaren versehen, damit der Transfer in das neue Blog sichtbar bleibt.

### Originalnotizen
# Accessibility / Barrierefreiheit

## Kundenanforderung  
Als Nutzer:in mit besonderen Anforderungen möchte ich die Website barrierefrei verwenden können (z. B. per Tastatur, Screenreader).

## Warum ist das so?  
Barrierefreiheit ist gesetzlich vorgeschrieben (z. B. EU-Richtlinien) und erweitert den Nutzerkreis. Zudem verbessert sie Grundqualität des Frontends.

## Anforderungen & Besonderheiten  
- WCAG 2.1 / 2.2 (AA) Richtlinien erfüllen  
- Tastaturnavigation, Fokus-Indikatoren  
- Alt-Texte, kontrastreicher Text  
- ARIA-Rollen, Landmarken  

## Umsetzung – Technische Leitplanken  
- **Mobile First:** Fokusflächen ausreichend groß  
- **Accessibility:** Semantische HTML-Elemente, ARIA-Attribute  
- **SEO:** Barrierefreiheit unterstützt SEO indirekt  
- **Best Practices:**  
 • Skip-Links  
 • Überspringbare Navigation  
 • Color-Contrast-Tests automatisiert  
 • Test mit Screenreadern  

## Checkliste  
- [ ] WCAG AA erfüllt  
- [ ] Tastaturnavigation durchgängig  
- [ ] Alt-Texte & Beschriftungen  
- [ ] Fokus- & ARIA-Attribute  

## Abhängigkeiten / Überschneidungen  
- Alle Frontend-Komponenten  
- Templates / HTML-Struktur  
- CSS / Design-System  

## Akzeptanzkriterien  
- Site nutzbar nur mit Tastatur  
- Screenreader-Tests erfolgreich  
- Farbkombinationen konform  

---

## Bewertung der Relevanz 2025  
⭐⭐⭐⭐⭐  
Unverzichtbar – gesetzlich und UX-technisch relevant.

## Anekdoten & Nerd-Zitate
Michael Crichton hätte wahrscheinlich eine komplette Katastrophensimulation um Accessibility gestrickt, nur um zu zeigen, wie viele Dinge gleichzeitig schiefgehen können. Douglas Coupland würde dagegen eine Slack-Konversation voller Insider-Gags daraus machen. Und irgendwo zwinkert eine alte RFC dazu, weil die Nerd-Fakten selten stillstehen.

## Best Practices
- A11y: Accessibility tastatur- und screenreader-freundlich gestalten.
- Performance: Accessibility nur laden, wenn der Kontext es wirklich braucht.
- Wartbarkeit: Entscheidungen zu Accessibility direkt neben dem Code dokumentieren.

## Fazit
Accessibility bleibt ein schönes Beispiel dafür, wie Frontend-Elemente Geschichten erzählen können, wenn man sie ernst nimmt und trotzdem mit Humor betrachtet.
