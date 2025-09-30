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
Als ich heute Morgen die Kaffeemaschine anwarf, vibrierte das Handy wie ein Pager aus den Neunzigern. Im Editor blinkte Accordion und ich hörte innerlich die Titelmusik von ‚Akte X‘. Irgendwo zwischen dem Duft von frisch gemahlenen Bohnen und dem leisen Summen des Lüfters entschied ich: Diese Notiz wird eine Liebeserklärung an Accordion im Rahmen unserer Frontend Layout-Expedition.

## Technischer Kern
Jede Roadmap hat ihren heimlichen Bossfight, und bei uns hieß der im letzten Sprint Accordion. Die Doku unten ist die nüchterne Wahrheit, aber die eigentliche Arbeit passierte zwischen Koffeinflash und Pixel-Poesie. Ich habe die Komponente auf einem ausgeleierten iPhone 8 getestet, während ein Kollege Accessibility-Checks über VoiceOver machte. Mobile First bedeutet hier, das Layout zusammenzufalten, bis es auch mit einer Hand bedienbar bleibt. Accessibility heißt, dass niemand fragen muss: „Wo bin ich hier?“ Genau dann ploppte eine Slack-Nachricht auf, die mich daran erinnerte, dass wir alle Prototypen unserer eigenen Ideen sind – und im Kopf jubelte das innere Regieteam, als wir den letzten Bug fixen konnten.

### Originalnotizen
Bevor wir uns im Meme-Verhau verlieren, bleiben die originalen Notizen unbeschnitten erhalten:
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
- Im Retro-Meeting tippte jemand: „Accordion war mein Bosslevel.“ – Ich antwortete: „Nur weil du den Accessibility-Check nach Mitternacht gemacht hast.“
- In meinem inneren Katastrophenskript gibt es immer eine Szene, in der Accordion ausfällt und der Shop nervös wird. In der Realität helfen uns Logs und Gelassenheit.
- Beim Debuggen flüstert mir eher das Bauchgefühl zu: „Wir leben zwischen Bugfixes, also mach sie hübsch.“ Das gilt besonders, wenn der Mobile-Test im Bus stattfindet.
- O-Ton eines Kunden: „Seit Accordion sauber läuft, fühlt sich unser Interface an wie eine gute Playlist.“ Besseres Lob gibt es nicht.

## Best Practices
- **Accessibility lebt von Ritualen:** Prüfe Accordion mit Tastatur und Screenreader, bevor du überhaupt an Pixel-Politur denkst. Deine künftige Selbstachtung wird es dir danken.
- **Mobile First aus Überzeugung:** Beginne mit dem kleinsten Viewport und frage dich ernsthaft, ob du das Element auch im U-Bahn-Gedränge bedienen könntest.
- **Performance mit Hausverstand:** Lade nur, was wirklich gebraucht wird, sonst fühlt sich Accordion an wie ein Buffering-Screen aus der Modem-Ära.
- **Dokumentation neben dem Code:** Schreib dir dazu, warum Entscheidungen gefallen sind; sonst fragst du dich in drei Monaten selbst, was du damit meintest.
- **Team-Sync:** Stell sicher, dass Design, Content und Dev dieselben Erwartungen haben – sonst erzählt jeder eine andere Story über Accordion.

## Fazit
Accordion ist am Ende wie eine Reihe kleiner Laternen im Tunnel: unscheinbar, aber ohne sie stolpern wir. Ich nehme aus diesem Durchgang mit, dass Mobile First und Accessibility keine Kapitelüberschriften sind, sondern Bauchentscheidungen für Menschen. Beim nächsten Mal baue ich noch früher Tests in den Workflow ein – und trinke meinen Kaffee vermutlich etwas langsamer.
