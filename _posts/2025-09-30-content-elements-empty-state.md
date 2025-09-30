---
title: "Wenn der Screen leer bleibt: Empty-State-Feldnotizen"
date: 2025-09-30
layout: post
categories:
  - content-elements
tags:
  - Content Element
  - UX Writing
  - Service Design
excerpt: "Wie ein gut erzählter Empty State Suchmasken rettet, Dashboards erklärt und mich trotz Kaffeeentzug lachen lässt."
slug: content-elements-empty-state
original_path: content-elements/empty-state.md
---

## Szene: Support-Call zwischen zwei Straßenbahnhaltestellen
Ich stand im Regen, AirPods im Ohr, und hörte zu, wie ein Kunde erklärte, dass neue Nutzer in seinem Dashboard verloren gingen. Während die Bahn Verspätung hatte, skizzierte ich auf dem Handy-Screen einen neuen Empty State – Headline, Text, Button, fertig? Nicht ganz. Wir lachten kurz über die Wetterlage, dann versprach ich, dass niemand mehr ratlos auf eine blanke Fläche starren muss.

## Feldnotizen aus dem Bau
Empty States sind unsere freundlichen Platzhalter, wenn eine Suche keine Ergebnisse liefert oder ein frischer Account noch keine Daten hat. Wir kombinieren Headline, Bodytext und optionalen CTA, abgestimmt auf das Illustration-Set aus dem Designsystem. Zu schrille Visuals lenken ab, also bleiben wir bei klaren Linien und Farben. Hilfelinks stehen bereit, damit Support nicht zum Flaschenhals wird, und der Ton bleibt empathisch – schließlich sind Nutzer ohnehin schon in einer Null-Daten-Situation.

## Mobile-First-Fahrplan
Auf kleinen Screens stapeln wir Elemente vertikal, Buttons laufen full-width, und Texte bleiben knackig, damit niemand scrollen muss, um die Aktion zu finden. Illustrationen werden responsive skaliert oder bei sehr schmalen Viewports ausgeblendet, damit die Botschaft nicht untergeht. Erst ab Tablet-Größe gönnen wir uns mehr Weißraum oder zusätzliche Tipps.

## Accessibility & Fürsorge
Auch wenn kein Bild angezeigt wird, liefern wir Screenreader-freundliche Texte, die die Situation beschreiben und eine klare Handlungsoption anbieten. Fokusreihenfolge startet beim erklärenden Absatz, gefolgt vom primären Button, damit niemand durch dekorative Elemente tabben muss. Tooltips oder Inline-Hilfe stehen in Textform bereit – keine ikonografischen Rätsel. Für internationale Teams übersetzen wir die Botschaften früh, weil Humor im Deutschen selten genauso im Französischen funktioniert.

## Technik, Validierung & Betrieb
Empty States hängen am gleichen Rendering-Pfad wie die Datenlisten: Wir prüfen Serverantworten und zeigen nur dann den leeren Zustand, wenn wirklich keine Items vorliegen. Feature-Flags erlauben uns, CTA-Experimente zu fahren, ohne alle Nutzer zu überraschen. Performance behalten wir im Blick, indem Illustrationen lazy geladen werden und Monitoring mitloggt, wie oft Nutzer direkt in Hilfelinks abbiegen.

## Takeaways
- Empty States erklären Suche und Dashboards, bevor Frust entsteht – klare Texte plus optionale Hilfelinks sind Pflicht.
- Mobile-First bedeutet kurze Botschaften, Full-Width-Buttons und nur so viel Illustration, wie der Screen verträgt.
- Barrierefreiheit funktioniert, wenn Fokus, Sprache und Hilfen ohne dekorative Umwege auskommen.
- Datenpfad, Feature-Flags und Monitoring halten den Zustand ehrlich und geben Support-Team und Produkt klare Signale.
