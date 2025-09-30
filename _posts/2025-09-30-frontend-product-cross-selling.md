---
title: "Cross Selling: Randnotiz"
date: 2025-09-30
tags: [UI, Komponente, Webentwicklung]
excerpt: "Warum Cross Selling unsere Frontend-Notizen inspiriert."
layout: post
categories: [frontend]
slug: frontend-product-cross-selling
original_path: frontend/product/cross-selling.md
---

## Einleitung
Zwischen Straßenbahn, Einkaufskorb und kurzen Pausen auf der Parkbank tippte ich die ersten Sätze ins Smartphone. Cross Selling stand noch warm aus dem letzten Deployment im Raum, und klar war: Heute erzählen wir diese Komponente so, wie altundwillig.de über große und kleine Webdramen schreibt – mitten im Alltag unseres Frontend Product-Systems.

## Technischer Kern
Cross Selling ist einer dieser Bausteine, die niemand beachtet, bis sie fehlen. Wir haben das schmerzhaft gelernt, als ein Kunde das Feature ohne ARIA ausgeliefert hat und ein Feedback-Call zur Selbsthilfegruppe wurde. Seitdem legen wir das Mobile-Layout zuerst fest, tasten uns mit echten Fingern durch Buttons und Links und feiern jeden Moment, in dem der Screenreader flüssig vorliest. Ich halte mich an die Spezifikationen, aber ich erzähle sie wie Lagerfeuergeschichten: mit klaren HTML-Strukturen, sauberen States und einer Prise Humor. Und während ich daran denke, dass wir alle an halb fertigen Interfaces arbeiten, mahnt mich eine innere Stimme, jede Abhängigkeit dreimal zu prüfen.

### Originalnotizen
Ich lasse hier den historischen Steckbrief unangetastet; er ist mein Sicherheitsnetz, wenn das Storytelling überkocht:
# Cross-Selling / Upselling

## Kundenanforderung  
Als Kunde:in möchte ich passende Zusatzprodukte oder höherwertige Varianten zu meinem aktuellen Produkt sehen, damit ich ggf. mehr kaufe oder bessere Varianten entdecke.

## Warum ist das so?  
Upselling / Cross-Selling erhöht Umsatz pro Kunde. Es lenkt auf relevante Angebote, erweitert den Warenkorb sinnvoll.

## Anforderungen & Besonderheiten  
- Empfehlung mit sinnvoller Logik (Kombi, Ergänzung, Zubehör)  
- Darstellung auf PDP oder im Checkout  
- Datenschutz: Empfehlung basierend auf anonymen Mustern, nicht personenbezogene Daten ohne Einwilligung  
- Einfaches Management im Backend  

## Umsetzung – Technische Leitplanken  
- **Mobile First:** Empfehlung unterhalb Produkttab oder „weitere Produkte“ scrollbar  
- **Accessibility:** ARIA-Labels, klare Linkstruktur  
- **SEO:** Empfehlungstitel als Link, kein Cloaking  
- **Best Practices:**  
 • Empfehlung basierend auf Algorithmen (kaufhistorisch, collaborative filtering)  
 • Caching von Empfehlungen  
 • Fallback bei fehlendem Vorschlag  
 • Metriken (Klickraten)  

## Checkliste  
- [ ] Empfehlungslogik definiert  
- [ ] Anzeigen an sinnvollen Stellen  
- [ ] Empfehlungen korrekt verlinkt  
- [ ] Performance getestet  

## Abhängigkeiten / Überschneidungen  
- Product-API / Daten  
- Analytics / Tracking  
- Backend / Empfehlungsservice  

## Akzeptanzkriterien  
- Empfehlungen passen thematisch  
- Links führen zur korrekten Seite  
- Keine Performance-Einbrüche  
- Anzeigen nicht störend  

---

## Bewertung der Relevanz 2025  
⭐⭐⭐⭐☆  
Wichtig, aber weniger kritisch als Produktdetailseite – vor allem in mittleren Shops sinnvoll.

## Anekdoten & Nerd-Zitate
- Ein Chatverlauf von letzter Woche: „Kannst du Cross Selling mal schnell deaktivieren?“ – „Nur wenn du mir einen neuen Kaffee bringst.“ Ergebnis: Kaffee kam, Cross Selling blieb.
- Merksatz: Technologie wird genau dann knifflig, wenn sie unsichtbar wirkt. Genau deshalb lassen wir Cross Selling nicht aus der Doku verschwinden.
- Während der Build lief, las ich alte Projekt-Notizen und sah uns alle als Varianten derselben Crew, die versucht, Cross Selling pixelweise in den Griff zu bekommen.
- In einer altundwillig.de-Sprachnachricht erzählte ich, wie ein Screenreader-User fragte: „Wo bin ich eigentlich?“ – dieser Satz hallt nach wie ein Drum-Solo.

## Best Practices
- **Design Tokens nutzen:** Lass Cross Selling aus dem Designsystem atmen, nicht aus spontanen HEX-Codes.
- **Keyboard-Liebe:** Jede Interaktion muss per Tab erreichbar sein – ein Modal ohne Escape ist ein Support-Ticket in spe.
- **Performance messen:** Lighthouse, WebPageTest, was immer du hast – Hauptsache du kennst deine Zahlen.
- **Copy & Microcopy:** Stimme dich mit Content ab, damit die Sprache genauso flüssig ist wie das Interface.
- **Post-Launch-Retros:** Plane von Anfang an ein, die Komponente nach den ersten echten Nutzerkontakten anzupassen.

## Fazit
Wenn ich den Tag Revue passieren lasse, sehe ich Cross Selling wie eine verlässliche Nebenfigur, die dem Plot erst Sinn gibt. Wir haben gelernt, dass Resilienz aus Routine entsteht: frühe Tests, offene Kommunikation, echte Devices. Beim nächsten Sprint will ich die Kopplung zu Datenquellen sauberer aufsetzen und weiter beweisen, dass Barrierefreiheit kein Extra ist, sondern Haltung.
