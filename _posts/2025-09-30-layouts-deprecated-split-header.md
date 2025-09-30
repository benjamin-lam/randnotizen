---
title: "Split Header: Randnotiz"
date: 2025-09-30
tags: [UI, Komponente, Webentwicklung]
excerpt: "Warum Split Header unsere Layouts-Notizen inspiriert."
layout: post
categories: [layouts]
slug: layouts-deprecated-split-header
original_path: layouts/deprecated/split-header.md
---

## Einleitung
Noch bevor Slack das erste Ping losließ, balancierte ich zwischen Straßenbahn und improvisiertem Stehtisch und schrieb die ersten Stichworte ins Smartphone. Auf dem Screen wartete Split Header; kein Thriller, sondern das nächste Kapitel für Layouts (Deprecated).

## Technischer Kern
Split Header ist einer dieser Bausteine, die niemand beachtet, bis sie fehlen. Wir haben das schmerzhaft gelernt, als ein Kunde das Feature ohne ARIA ausgeliefert hat und ein Feedback-Call zur Selbsthilfegruppe wurde. Seitdem legen wir das Mobile-Layout zuerst fest, tasten uns mit echten Fingern durch Buttons und Links und feiern jeden Moment, in dem der Screenreader flüssig vorliest. Ich halte mich an die Spezifikationen, aber ich erzähle sie wie Lagerfeuergeschichten: mit klaren HTML-Strukturen, sauberen States und einer Prise Humor. Und während ich daran denke, dass wir alle an halb fertigen Interfaces arbeiten, mahnt mich eine innere Stimme, jede Abhängigkeit dreimal zu prüfen.

### Originalnotizen
Ich lasse hier den historischen Steckbrief unangetastet; er ist mein Sicherheitsnetz, wenn das Storytelling überkocht:
# Layout: Split Header

## Beschreibung
Ein geteiltes Header-Layout mit gegensätzlichen Ausrichtungen bricht auf kleinen Screens leicht und erschwert mobile Navigation.

## Warum dieses Layout?
- Kann komplexe Markenbotschaften transportieren.
- Erlaubt simultane Darstellung von Navigation und Aktionen.
- Skaliert auf mobilen Geräten schlecht und erhöht Implementierungsaufwand.

## Anforderungen & Besonderheiten
- **Responsiveness:** Header sollte auf mobile Breakpoints vereinfacht werden.
- **Accessibility:** Fokusreihenfolge sicherstellen, da Elemente weit auseinander liegen.
- **SEO:** Kein direkter Vorteil, Risiko von unklaren Hierarchien.
- **Design-Guidelines:** Branding und Aktionen priorisieren, redundante Inhalte streichen.

## Umsetzung – Technische Leitplanken
- **Mobile First:** Auf einfachere Header-Varianten umstellen und Split-Design nur dokumentieren.
- **Accessibility:** Skip-Link und klare Landmarken bieten.
- **SEO:** Wichtige Links logisch gruppieren.
- **Best Practices:** Frühe Reduktion auf einspaltige Navigation, Aktionen priorisieren, Übergangsanimationen vermeiden

## Checkliste
- [ ] Fallback-Header vorhanden.
- [ ] Navigation funktioniert auf Touch-Geräten.
- [ ] Fokus-Indikatoren sichtbar.
- [ ] A11y- und Performance-Prüfung dokumentiert.

## Abhängigkeiten / Überschneidungen
- Legacy-Header-Komponenten
- Branding-Richtlinien

## Akzeptanzkriterien
- Mobile Ersatzlayout implementiert.
- Screenreader navigieren Header ohne Verwirrung.
- Stakeholder planen Umstellung auf modernes Pattern.

## Beispiel / Code
```html
<header class="split-header">
  <div class="left">Logo</div>
  <div class="right">Aktionen</div>
</header>
```

> ⚠️ Deprecated: Nicht mehr empfohlen für Mobile-First-Designs (nur zu Dokumentationszwecken).

Bewertung der Relevanz 2025

⭐⭐☆☆☆ Nur noch aus historischen Gründen vermerkt.

## Anekdoten & Nerd-Zitate
- Ein Chatverlauf von letzter Woche: „Kannst du Split Header mal schnell deaktivieren?“ – „Nur wenn du mir einen neuen Kaffee bringst.“ Ergebnis: Kaffee kam, Split Header blieb.
- Merksatz: Technologie wird genau dann knifflig, wenn sie unsichtbar wirkt. Genau deshalb lassen wir Split Header nicht aus der Doku verschwinden.
- Während der Build lief, las ich alte Projekt-Notizen und sah uns alle als Varianten derselben Crew, die versucht, Split Header pixelweise in den Griff zu bekommen.
- In einer altundwillig.de-Sprachnachricht erzählte ich, wie ein Screenreader-User fragte: „Wo bin ich eigentlich?“ – dieser Satz hallt nach wie ein Drum-Solo.

## Best Practices
- **Design Tokens nutzen:** Lass Split Header aus dem Designsystem atmen, nicht aus spontanen HEX-Codes.
- **Keyboard-Liebe:** Jede Interaktion muss per Tab erreichbar sein – ein Modal ohne Escape ist ein Support-Ticket in spe.
- **Performance messen:** Lighthouse, WebPageTest, was immer du hast – Hauptsache du kennst deine Zahlen.
- **Copy & Microcopy:** Stimme dich mit Content ab, damit die Sprache genauso flüssig ist wie das Interface.
- **Post-Launch-Retros:** Plane von Anfang an ein, die Komponente nach den ersten echten Nutzerkontakten anzupassen.

## Fazit
Split Header ist am Ende wie eine Reihe kleiner Laternen im Tunnel: unscheinbar, aber ohne sie stolpern wir. Ich nehme aus diesem Durchgang mit, dass Mobile First und Accessibility keine Kapitelüberschriften sind, sondern Bauchentscheidungen für Menschen. Beim nächsten Mal baue ich noch früher Tests in den Workflow ein – und trinke meinen Kaffee vermutlich etwas langsamer.
