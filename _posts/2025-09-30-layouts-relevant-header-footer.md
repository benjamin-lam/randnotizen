---
title: "Header Footer: Randnotiz"
date: 2025-09-30
tags: [UI, Komponente, Webentwicklung]
excerpt: "Warum Header Footer unsere Layouts-Notizen inspiriert."
layout: post
categories: [layouts]
slug: layouts-relevant-header-footer
original_path: layouts/relevant/header-footer.md
---

## Einleitung
Zwischen Straßenbahn, Supermarktkasse und Handy-Display schrieb ich die ersten Zeilen auf dem Smartphone, während in Bremen der Duft von frisch gemahlenem Kaffee durch die Luft zog. Header Footer blinkte mir entgegen wie ein Mixtape aus einer vergessenen Schublade, und klar war: Heute bekommt Header Footer die große Bühne in unserem Layouts (Relevant)-Tagebuch.

## Technischer Kern
Technisch gesehen sitzt Header Footer genau an der Schnittstelle zwischen Ordnung und Emotion. Ich erinnere mich noch, wie wir im letzten Quartal eine Variante shippten, die auf dem Testgerät butterweich wirkte, auf einem alten Android aber ruckelte wie ein VHS-Band. Seitdem ist Mobile First mein Morgenritual; ich starte immer mit dem kleinsten Screen. Accessibility hält mich ehrlich: Ohne klare Fokuszustände oder Transkripte wird aus Eleganz sofort Chaos, und genau dann ruft jemand aus dem Support an. Die Originalnotizen unten dienen mir als Checkliste, doch meine heimliche Regel lautet: Wir alle tüfteln in unseren Kellern an der Zukunft. In diesem Keller sorge ich dafür, dass Header Footer stabil bleibt, selbst wenn ein Sturm aus Edge Cases tobt.

### Originalnotizen
Unterhalb dieser Zeile wohnt das Rohmaterial – nach wie vor mein Truthahnthermometer für saubere Implementierung:
# Layout: Header & Footer Framework

## Beschreibung
Das Layout bildet die minimale Seitenstruktur aus Kopf- und Fußbereich, die andere Layouts erweitern. Es dient als Ausgangspunkt für Anwendungen, die ihre Inhalte dynamisch in <main> einfügen.

## Warum dieses Layout?
- Schafft ein konsistentes Grundgerüst für wiederkehrende Seiten.
- Erleichtert die Wiederverwendung von Navigations- und Footer-Komponenten.
- Allein nicht ausreichend, da der Hauptinhalt separat gestaltet werden muss.

## Anforderungen & Besonderheiten
- **Responsiveness:** Header- und Footer-Inhalte passen sich flexiblen Breiten an und bleiben lesbar.
- **Accessibility:** Landmark-Rollen nutzen, Skip-Link vorsehen und klare Fokusführung etablieren.
- **SEO:** Semantische Auszeichnung von Navigation, Logo und Pflichtlinks.
- **Design-Guidelines:** Ausreichende Padding-Werte, konsistente Typografie und klare Trennung zwischen Bereichen.

## Umsetzung – Technische Leitplanken
- **Mobile First:** Navigationsinhalte reduzieren und bei Bedarf als Burger-Menü bereitstellen.
- **Accessibility:** Skip-Link implementieren und Fokusindikatoren sichtbar halten.
- **SEO:** Footer für Kontakt- und Organisationsdaten nutzen und korrekt markieren.
- **Best Practices:** Sticky-Header nur bei Bedarf, Footer-Links gruppieren, Navigation logisch ordnen

## Checkliste
- [ ] Skip-Link führt zuverlässig zum Hauptinhalt.
- [ ] Navigation bleibt auch auf kleinen Screens bedienbar.
- [ ] Footer enthält alle Pflichtinformationen (Impressum, Datenschutz).
- [ ] Lighthouse-A11y-Check ohne kritische Fehler.

## Abhängigkeiten / Überschneidungen
- Globale Navigationskomponenten
- Footer-Link-Module

## Akzeptanzkriterien
- Header kollabiert responsiv ohne Layoutsprünge.
- Footer bleibt bei langen Seiten sichtbar und strukturiert.
- Screenreader erkennen die Landmarken korrekt.

## Beispiel / Code
```html
<header>…</header>
<main>Inhalt</main>
<footer>…</footer>
```

Bewertung der Relevanz 2025

⭐⭐⭐⭐☆ Solide Basis für Seiten mit dynamisch eingespeistem Content.

## Anekdoten & Nerd-Zitate
- Ein Chatverlauf von letzter Woche: „Kannst du Header Footer mal schnell deaktivieren?“ – „Nur wenn du mir einen neuen Kaffee bringst.“ Ergebnis: Kaffee kam, Header Footer blieb.
- Merksatz: Technologie wird genau dann knifflig, wenn sie unsichtbar wirkt. Genau deshalb lassen wir Header Footer nicht aus der Doku verschwinden.
- Während der Build lief, las ich alte Projekt-Notizen und sah uns alle als Varianten derselben Crew, die versucht, Header Footer pixelweise in den Griff zu bekommen.
- In einer altundwillig.de-Sprachnachricht erzählte ich, wie ein Screenreader-User fragte: „Wo bin ich eigentlich?“ – dieser Satz hallt nach wie ein Drum-Solo.

## Best Practices
- **Altgeräte-Test:** Wenn Header Footer auf dem alten iPhone aus der Agentur-Schublade gut läuft, kannst du halbwegs ruhig schlafen.
- **Semantik rockt:** HTML-Struktur ernst nehmen, ARIA nur ergänzen. Alles andere ist wie ein Special-Effect ohne Plot.
- **Content-Strategie:** Besprich früh, welche Texte, Bilder oder Daten hier landen. Überraschungen mag höchstens der Cliffhanger im Serienfinale.
- **Fallbacks vorbereiten:** Offline, Low-Bandwidth, reduzierte Animation – Mobile First bedeutet, mit wenig auszukommen.
- **QA-Checklisten:** Hack dir eine Checkliste ins Repo, damit niemand vergisst, warum Header Footer existiert.

## Fazit
Wenn ich den Tag Revue passieren lasse, sehe ich Header Footer wie eine verlässliche Nebenfigur, die dem Plot erst Sinn gibt. Wir haben gelernt, dass Resilienz aus Routine entsteht: frühe Tests, offene Kommunikation, echte Devices. Beim nächsten Sprint will ich die Kopplung zu Datenquellen sauberer aufsetzen und weiter beweisen, dass Barrierefreiheit kein Extra ist, sondern Haltung.
