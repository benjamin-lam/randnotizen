---
title: "Compare Products: Randnotiz"
date: 2025-09-30
tags: [UI, Komponente, Webentwicklung]
excerpt: "Warum Compare Products unsere Frontend-Notizen inspiriert."
layout: post
categories: [frontend]
slug: frontend-product-compare-products
original_path: frontend/product/compare-products.md
---

## Einleitung
Zwischen Straßenbahn, Einkaufskorb und kurzen Pausen auf der Parkbank tippte ich die ersten Sätze ins Smartphone. Compare Products stand noch warm aus dem letzten Deployment im Raum, und klar war: Heute erzählen wir diese Komponente so, wie altundwillig.de über große und kleine Webdramen schreibt – mitten im Alltag unseres Frontend Product-Systems.

## Technischer Kern
Compare Products klingt harmlos, doch in Wahrheit ist es das Klebeband zwischen Layout und Vertrauen. Damals, als wir eine spontane Nachtmigration fahren mussten, zeigte sich, wie sensibel die Details sind: Ein falsch gesetzter Breakpoint, und das mobile Layout fühlte sich an wie Nokia Snake auf einem faltbaren Display. Seitdem teste ich Mobile First auf dem ältesten Gerät im Büro. Accessibility ist keine Checkbox, sondern der Moment, in dem mir eine Screenreader-Nutzerin dankte, weil sie den Flow ohne Frust durchlaufen konnte. Wir sagen intern gern: Der wirkliche Wahnsinn im Code beginnt erst nach Mitternacht – und genau da merkten wir, wie Compare Products mit sauberen `aria`-Labels plötzlich Orientierung stiftete. Statt Zitaten gab es Fäuste in der Luft und einen stillen High-Five übers Debug-Log.

### Originalnotizen
Unterhalb dieser Zeile wohnt das Rohmaterial – nach wie vor mein Truthahnthermometer für saubere Implementierung:
# Produktvergleich (Compare)

## Kundenanforderung  
Als Nutzer:in möchte ich mehrere Produkte nebeneinander vergleichen (Eigenschaften, Preis etc.), um eine fundierte Entscheidung zu treffen.

## Warum ist das so?  
Vergleich minimiert Aufwand, erhöht Vertrauen und vermeidet Rückfragen.

## Anforderungen & Besonderheiten  
- Vergleichbare Merkmale definieren  
- Maximalzahl von Produkten beschränken (z. B. 3–4)  
- Layout auf kleinen Geräten – meist Scroll oder Tabs  
- Datenschutz: nur öffentliche Produktdaten  

## Umsetzung – Technische Leitplanken  
- **Mobile First:** Vergleich als nebeneinander scrollbares Raster oder Tabs  
- **Accessibility:** Tabellenstruktur mit `thead`/`tbody`, ARIA-Labels  
- **SEO:** Vergleichsseiten ggf. nicht indexieren  
- **Best Practices:**  
 • Sync mit Auswahl  
 • Vorkonfigurierte Template-Vergleiche  
 • UX: Hervorhebung der Unterschiede  

## Checkliste  
- [ ] Vergleichsfunktion aktiviert  
- [ ] Detailmerkmale abgebildet  
- [ ] Übersichtliche Darstellung  
- [ ] Mobile-kompatibel  

## Abhängigkeiten / Überschneidungen  
- Produktdaten / API  
- UI-Komponenten  
- Filter / Eigenschaften  

## Akzeptanzkriterien  
- Vergleich funktioniert korrekt  
- Layout responsiv  
- Auswahl & Entfernen funktioniert  

---

## Bewertung der Relevanz 2025  
⭐⭐⭐☆☆  
Nützlich in großen Shops mit vielen ähnlichen Produkten, aber kein Muss in kleinen Shops.

## Anekdoten & Nerd-Zitate
- In meinen Notizen steht noch der Satz: „Compare Products riecht nach Filterkaffee und Ticket-Alarm.“ Das war der Abend vor dem Launch.
- Wir haben uns selbst beobachtet, wie wir mit Taschenlampen (a.k.a. Gerätepark) durch die QA-Nacht stapfen.
- Niemand von außen textet für uns, aber unsere Slack-Emojis halten uns wach, wenn wir wieder Mobile-Bugs jagen.
- Eine Kollegin sagte: „Accessibility fühlt sich an wie barfuß laufen – du merkst jeden Stein.“ Seitdem prüfe ich Compare Products ohne Maus.

## Best Practices
- **Altgeräte-Test:** Wenn Compare Products auf dem alten iPhone aus der Agentur-Schublade gut läuft, kannst du halbwegs ruhig schlafen.
- **Semantik rockt:** HTML-Struktur ernst nehmen, ARIA nur ergänzen. Alles andere ist wie ein Special-Effect ohne Plot.
- **Content-Strategie:** Besprich früh, welche Texte, Bilder oder Daten hier landen. Überraschungen mag höchstens der Cliffhanger im Serienfinale.
- **Fallbacks vorbereiten:** Offline, Low-Bandwidth, reduzierte Animation – Mobile First bedeutet, mit wenig auszukommen.
- **QA-Checklisten:** Hack dir eine Checkliste ins Repo, damit niemand vergisst, warum Compare Products existiert.

## Fazit
Compare Products bleibt ein stiller Held, der uns daran erinnert, warum wir Interfaces mit Herzblut bauen. Ich nehme mir vor, künftig noch radikaler auf echte Nutzungsszenarien zu hören – besonders, wenn das Monitoring ruhig ist. Accessibility, Mobile First, Humor: Diese drei Dinge halten den Laden zusammen.
