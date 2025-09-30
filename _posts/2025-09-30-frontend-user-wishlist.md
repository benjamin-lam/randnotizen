---
title: "Wishlist: Randnotiz"
date: 2025-09-30
tags: [UI, Komponente, Webentwicklung]
excerpt: "Warum Wishlist unsere Frontend-Notizen inspiriert."
layout: post
categories: [frontend]
slug: frontend-user-wishlist
original_path: frontend/user/wishlist.md
---

## Einleitung
Zwischen Straßenbahn, Einkaufskorb und kurzen Pausen auf der Parkbank tippte ich die ersten Sätze ins Smartphone. Wishlist stand noch warm aus dem letzten Deployment im Raum, und klar war: Heute erzählen wir diese Komponente so, wie altundwillig.de über große und kleine Webdramen schreibt – mitten im Alltag unseres Frontend User Experience-Systems.

## Technischer Kern
Technisch gesehen sitzt Wishlist genau an der Schnittstelle zwischen Ordnung und Emotion. Ich erinnere mich noch, wie wir im letzten Quartal eine Variante shippten, die auf dem Testgerät butterweich wirkte, auf einem alten Android aber ruckelte wie ein VHS-Band. Seitdem ist Mobile First mein Morgenritual; ich starte immer mit dem kleinsten Screen. Accessibility hält mich ehrlich: Ohne klare Fokuszustände oder Transkripte wird aus Eleganz sofort Chaos, und genau dann ruft jemand aus dem Support an. Die Originalnotizen unten dienen mir als Checkliste, doch meine heimliche Regel lautet: Wir alle tüfteln in unseren Kellern an der Zukunft. In diesem Keller sorge ich dafür, dass Wishlist stabil bleibt, selbst wenn ein Sturm aus Edge Cases tobt.

### Originalnotizen
Ich lasse hier den historischen Steckbrief unangetastet; er ist mein Sicherheitsnetz, wenn das Storytelling überkocht:
# Wunschliste / Merkliste

## Kundenanforderung  
Als registrierte:r Nutzer:in möchte ich Produkte auf eine Wunschliste setzen, um sie später zu überblicken oder zu teilen.

## Warum ist das so?  
Nutzer nutzen Wishlist zur Planung, zum Vergleich, zur Erinnerung – und oftmals wird später daraus ein Kauf. Es erhöht Engagement.

## Anforderungen & Besonderheiten  
- Bestände mitberücksichtigen  
- Nutzerbindung & Synchronisation (z. B. zwischen Geräten)  
- Teilen-Funktionen (optional)  
- Datenschutz bei Teil-Links  

## Umsetzung – Technische Leitplanken  
- **Mobile First:** Button „Zur Wunschliste“ prominent erreichbar  
- **Accessibility:** ARIA-Labels, Zustände (aktiv/inaktiv)  
- **SEO:** Kein indexierter Link (Wunschlistenseiten privat)  
- **Best Practices:**  
 • Real-time Feedback („hinzugefügt“)  
 • Synchronisation mit Nutzerkonto  
 • Fallback für Gäste (Session-basiert)  

## Checkliste  
- [ ] Produkte zur Wunschliste hinzufügen / entfernen  
- [ ] Wunschliste persistiert zwischen Sitzungen  
- [ ] Synchronisation über Geräte  
- [ ] Teilen-Option (falls geplant)  

## Abhängigkeiten / Überschneidungen  
- Nutzerkonto / Auth  
- Produktdaten / API  
- Session / Cache  

## Akzeptanzkriterien  
- Wunschliste editierbar  
- Sichtbarkeit & Status korrekt  
- Performance unter hoher Last  

---

## Bewertung der Relevanz 2025  
⭐⭐⭐⭐☆  
Mittel bis hoch – in vielen Shops bereits erwartet. Für kleinere Shops optional.

## Anekdoten & Nerd-Zitate
- In meinen Notizen steht noch der Satz: „Wishlist riecht nach Filterkaffee und Ticket-Alarm.“ Das war der Abend vor dem Launch.
- Wir haben uns selbst beobachtet, wie wir mit Taschenlampen (a.k.a. Gerätepark) durch die QA-Nacht stapfen.
- Niemand von außen textet für uns, aber unsere Slack-Emojis halten uns wach, wenn wir wieder Mobile-Bugs jagen.
- Eine Kollegin sagte: „Accessibility fühlt sich an wie barfuß laufen – du merkst jeden Stein.“ Seitdem prüfe ich Wishlist ohne Maus.

## Best Practices
- **Design Tokens nutzen:** Lass Wishlist aus dem Designsystem atmen, nicht aus spontanen HEX-Codes.
- **Keyboard-Liebe:** Jede Interaktion muss per Tab erreichbar sein – ein Modal ohne Escape ist ein Support-Ticket in spe.
- **Performance messen:** Lighthouse, WebPageTest, was immer du hast – Hauptsache du kennst deine Zahlen.
- **Copy & Microcopy:** Stimme dich mit Content ab, damit die Sprache genauso flüssig ist wie das Interface.
- **Post-Launch-Retros:** Plane von Anfang an ein, die Komponente nach den ersten echten Nutzerkontakten anzupassen.

## Fazit
Zum Schluss fühlt sich Wishlist an wie ein gut geölter Plattenspieler: nicht prahlerisch, aber unverzichtbar. Wir haben wieder gelernt, dass Disziplin bei Breakpoints und `aria`-Attributen genau der Unterschied zwischen Frust und Flow ist. Beim nächsten Rollout gönne ich mir mehr Zeit für User-Feedback, bevor der nächste Sturm aus Edge Cases anklopft.
