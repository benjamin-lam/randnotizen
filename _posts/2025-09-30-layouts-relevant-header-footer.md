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
Es fühlt sich an wie ein Fund in einer verstaubten Prototyp-Schublade: **Header Footer** passte heute perfekt in unsere Layouts-Gedanken, und plötzlich roch der Raum nach Whiteboard-Markern und frisch gebrühtem Kaffee.

## Technischer Kern
Technisch betrachtet verlangt Header Footer nach klaren Leitplanken. Ich habe die ursprüngliche Beschreibung unten angeheftet und mit Kommentaren versehen, damit der Transfer in das neue Blog sichtbar bleibt.

### Originalnotizen
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
Michael Crichton hätte wahrscheinlich eine komplette Katastrophensimulation um Header Footer gestrickt, nur um zu zeigen, wie viele Dinge gleichzeitig schiefgehen können. Douglas Coupland würde dagegen eine Slack-Konversation voller Insider-Gags daraus machen. Und irgendwo zwinkert eine alte RFC dazu, weil die Nerd-Fakten selten stillstehen.

## Best Practices
- A11y: Header Footer tastatur- und screenreader-freundlich gestalten.
- Performance: Header Footer nur laden, wenn der Kontext es wirklich braucht.
- Wartbarkeit: Entscheidungen zu Header Footer direkt neben dem Code dokumentieren.

## Fazit
Header Footer bleibt ein schönes Beispiel dafür, wie Layouts-Elemente Geschichten erzählen können, wenn man sie ernst nimmt und trotzdem mit Humor betrachtet.
