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
Zwischen Straßenbahn, Supermarktkasse und Handy-Display schrieb ich die ersten Zeilen auf dem Smartphone, während in Bremen der Duft von frisch gemahlenem Kaffee durch die Luft zog. Accessibility blinkte mir entgegen wie ein Mixtape aus einer vergessenen Schublade, und klar war: Heute bekommt Accessibility die große Bühne in unserem Frontend Misc-Tagebuch.

## Technischer Kern
Jede Roadmap hat ihren heimlichen Bossfight, und bei uns hieß der im letzten Sprint Accessibility. Die Doku unten ist die nüchterne Wahrheit, aber die eigentliche Arbeit passierte zwischen Koffeinflash und Pixel-Poesie. Ich habe die Komponente auf einem ausgeleierten iPhone 8 getestet, während ein Kollege Accessibility-Checks über VoiceOver machte. Mobile First bedeutet hier, das Layout zusammenzufalten, bis es auch mit einer Hand bedienbar bleibt. Accessibility heißt, dass niemand fragen muss: „Wo bin ich hier?“ Genau dann ploppte eine Slack-Nachricht auf, die mich daran erinnerte, dass wir alle Prototypen unserer eigenen Ideen sind – und im Kopf jubelte das innere Regieteam, als wir den letzten Bug fixen konnten.

### Originalnotizen
Unterhalb dieser Zeile wohnt das Rohmaterial – nach wie vor mein Truthahnthermometer für saubere Implementierung:
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
- Ein Chatverlauf von letzter Woche: „Kannst du Accessibility mal schnell deaktivieren?“ – „Nur wenn du mir einen neuen Kaffee bringst.“ Ergebnis: Kaffee kam, Accessibility blieb.
- Merksatz: Technologie wird genau dann knifflig, wenn sie unsichtbar wirkt. Genau deshalb lassen wir Accessibility nicht aus der Doku verschwinden.
- Während der Build lief, las ich alte Projekt-Notizen und sah uns alle als Varianten derselben Crew, die versucht, Accessibility pixelweise in den Griff zu bekommen.
- In einer altundwillig.de-Sprachnachricht erzählte ich, wie ein Screenreader-User fragte: „Wo bin ich eigentlich?“ – dieser Satz hallt nach wie ein Drum-Solo.

## Best Practices
- **A11y first:** Gib Accessibility klare Rollen, Zustände und `aria`-Labels. Wer jemals ein Feedback von Screenreader-Profi bekommen hat, weiß, warum.
- **Responsive by default:** Gestalte Breakpoints so, dass das Element nicht wie ein Möbelstück in einer viel zu kleinen Wohnung wirkt.
- **State-Management:** Dokumentiere, wie Hover, Focus, Error und Success klingen und aussehen; Mobile-Geräte haben keine Hover-Liebe.
- **Content Hooks:** Halte die Schnittstellen zu Datenquellen sauber, sonst verheddert sich Accessibility schneller als ein Kassettenband.
- **Monitoring:** Tracke Interaktionen, damit du erkennst, wann Nutzer stranden – und reagiere schneller, als ein Katastrophenfilm es darstellen würde.

## Fazit
Zum Schluss fühlt sich Accessibility an wie ein gut geölter Plattenspieler: nicht prahlerisch, aber unverzichtbar. Wir haben wieder gelernt, dass Disziplin bei Breakpoints und `aria`-Attributen genau der Unterschied zwischen Frust und Flow ist. Beim nächsten Rollout gönne ich mir mehr Zeit für User-Feedback, bevor der nächste Sturm aus Edge Cases anklopft.
