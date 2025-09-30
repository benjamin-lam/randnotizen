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
Zwischen Straßenbahn, Einkaufskorb und kurzen Pausen auf der Parkbank tippte ich die ersten Sätze ins Smartphone. Recently Viewed stand noch warm aus dem letzten Deployment im Raum, und klar war: Heute erzählen wir diese Komponente so, wie altundwillig.de über große und kleine Webdramen schreibt – mitten im Alltag unseres Frontend Product-Systems.

## Technischer Kern
Jede Roadmap hat ihren heimlichen Bossfight, und bei uns hieß der im letzten Sprint Recently Viewed. Die Doku unten ist die nüchterne Wahrheit, aber die eigentliche Arbeit passierte zwischen Koffeinflash und Pixel-Poesie. Ich habe die Komponente auf einem ausgeleierten iPhone 8 getestet, während ein Kollege Accessibility-Checks über VoiceOver machte. Mobile First bedeutet hier, das Layout zusammenzufalten, bis es auch mit einer Hand bedienbar bleibt. Accessibility heißt, dass niemand fragen muss: „Wo bin ich hier?“ Genau dann ploppte eine Slack-Nachricht auf, die mich daran erinnerte, dass wir alle Prototypen unserer eigenen Ideen sind – und im Kopf jubelte das innere Regieteam, als wir den letzten Bug fixen konnten.

### Originalnotizen
Unterhalb dieser Zeile wohnt das Rohmaterial – nach wie vor mein Truthahnthermometer für saubere Implementierung:
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
- Wir haben einmal eine interne Nostalgie-Matrix gebaut, um Recently Viewed gegen Erinnerungsglitzer zu testen. Ergebnis: 42 Prozent erinnern an MP3-Player aus 2003.
- Mein Lieblings-Feedback kam aus dem Support: „Endlich muss ich niemandem mehr erklären, wo Recently Viewed versteckt ist.“
- Wenn das Monitoring blinkt, fühlt es sich kurz wie im Katastrophenfilm an – diesmal blieb der Alarm still.
- Altundwillig.de hätte es so zusammengefasst: „Mach es benutzbar oder lass es bleiben.“

## Best Practices
- **A11y first:** Gib Recently Viewed klare Rollen, Zustände und `aria`-Labels. Wer jemals ein Feedback von Screenreader-Profi bekommen hat, weiß, warum.
- **Responsive by default:** Gestalte Breakpoints so, dass das Element nicht wie ein Möbelstück in einer viel zu kleinen Wohnung wirkt.
- **State-Management:** Dokumentiere, wie Hover, Focus, Error und Success klingen und aussehen; Mobile-Geräte haben keine Hover-Liebe.
- **Content Hooks:** Halte die Schnittstellen zu Datenquellen sauber, sonst verheddert sich Recently Viewed schneller als ein Kassettenband.
- **Monitoring:** Tracke Interaktionen, damit du erkennst, wann Nutzer stranden – und reagiere schneller, als ein Katastrophenfilm es darstellen würde.

## Fazit
Recently Viewed ist am Ende wie eine Reihe kleiner Laternen im Tunnel: unscheinbar, aber ohne sie stolpern wir. Ich nehme aus diesem Durchgang mit, dass Mobile First und Accessibility keine Kapitelüberschriften sind, sondern Bauchentscheidungen für Menschen. Beim nächsten Mal baue ich noch früher Tests in den Workflow ein – und trinke meinen Kaffee vermutlich etwas langsamer.
