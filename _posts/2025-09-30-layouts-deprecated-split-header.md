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
Es fühlt sich an wie ein Fund in einer verstaubten Prototyp-Schublade: **Split Header** passte heute perfekt in unsere Layouts-Gedanken, und plötzlich roch der Raum nach Whiteboard-Markern und frisch gebrühtem Kaffee.

## Technischer Kern
Technisch betrachtet verlangt Split Header nach klaren Leitplanken. Ich habe die ursprüngliche Beschreibung unten angeheftet und mit Kommentaren versehen, damit der Transfer in das neue Blog sichtbar bleibt.

### Originalnotizen
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
Michael Crichton hätte wahrscheinlich eine komplette Katastrophensimulation um Split Header gestrickt, nur um zu zeigen, wie viele Dinge gleichzeitig schiefgehen können. Douglas Coupland würde dagegen eine Slack-Konversation voller Insider-Gags daraus machen. Und irgendwo zwinkert eine alte RFC dazu, weil die Nerd-Fakten selten stillstehen.

## Best Practices
- A11y: Split Header tastatur- und screenreader-freundlich gestalten.
- Performance: Split Header nur laden, wenn der Kontext es wirklich braucht.
- Wartbarkeit: Entscheidungen zu Split Header direkt neben dem Code dokumentieren.

## Fazit
Split Header bleibt ein schönes Beispiel dafür, wie Layouts-Elemente Geschichten erzählen können, wenn man sie ernst nimmt und trotzdem mit Humor betrachtet.
