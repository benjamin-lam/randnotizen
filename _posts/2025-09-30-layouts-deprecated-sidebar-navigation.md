---
title: "Sidebar Navigation: Randnotiz"
date: 2025-09-30
tags: [UI, Komponente, Webentwicklung]
excerpt: "Warum Sidebar Navigation unsere Layouts-Notizen inspiriert."
layout: post
categories: [layouts]
slug: layouts-deprecated-sidebar-navigation
original_path: layouts/deprecated/sidebar-navigation.md
---

## Einleitung
Es fühlt sich an wie ein Fund in einer verstaubten Prototyp-Schublade: **Sidebar Navigation** passte heute perfekt in unsere Layouts-Gedanken, und plötzlich roch der Raum nach Whiteboard-Markern und frisch gebrühtem Kaffee.

## Technischer Kern
Technisch betrachtet verlangt Sidebar Navigation nach klaren Leitplanken. Ich habe die ursprüngliche Beschreibung unten angeheftet und mit Kommentaren versehen, damit der Transfer in das neue Blog sichtbar bleibt.

### Originalnotizen
# Layout: Sidebar Navigation

## Beschreibung
Eine permanent sichtbare Sidebar-Navigation stammt aus Desktop-Zeiten und wird heute häufig von responsiven Drawern ersetzt.

## Warum dieses Layout?
- Bietet konstant sichtbare Navigationspunkte.
- Eignet sich für sehr breite Desktop-Layouts.
- Verbraucht mobil wertvollen Platz und wirkt veraltet.

## Anforderungen & Besonderheiten
- **Responsiveness:** Mobile Alternativen wie Off-Canvas oder Overlay bereitstellen.
- **Accessibility:** Navigation als <nav> kennzeichnen, Fokusmanagement für Drawer-Alternative.
- **SEO:** Links bleiben im DOM, Priorisierung auf Hauptinhalte achten.
- **Design-Guidelines:** Sichtbare aktive Zustände, klare Gruppierung von Links.

## Umsetzung – Technische Leitplanken
- **Mobile First:** Primär einen Drawer oder Overlay planen und Sidebar nur als Desktop-Variante pflegen.
- **Accessibility:** Tastaturbedienung sicherstellen, Skip-Link ergänzen.
- **SEO:** Duplicate Navigation vermeiden.
- **Best Practices:** Mobil Off-Canvas nutzen, Aktive Pfade markieren, Navigation vereinfachen

## Checkliste
- [ ] Off-Canvas-Alternative vorhanden.
- [ ] Fokusmanagement geprüft.
- [ ] Sidebar überdeckt keinen Content.
- [ ] A11y- und Performance-Check dokumentiert.

## Abhängigkeiten / Überschneidungen
- Drawer-/Overlay-Komponente
- Legacy-Navigationsstruktur

## Akzeptanzkriterien
- Mobil wird Sidebar ersetzt oder deaktiviert.
- Screenreader erreichen Navigation ohne Umwege.
- Stakeholder planen Migration zu moderneren Patterns.

## Beispiel / Code
```html
<aside class="sidebar-nav">
  <nav>
    <ul>
      <li><a href="#">Link</a></li>
    </ul>
  </nav>
</aside>
```

> ⚠️ Deprecated: Nicht mehr empfohlen für Mobile-First-Designs (nur zu Dokumentationszwecken).

Bewertung der Relevanz 2025

⭐⭐☆☆☆ Nur für Legacy-Interfaces dokumentiert.

## Anekdoten & Nerd-Zitate
Michael Crichton hätte wahrscheinlich eine komplette Katastrophensimulation um Sidebar Navigation gestrickt, nur um zu zeigen, wie viele Dinge gleichzeitig schiefgehen können. Douglas Coupland würde dagegen eine Slack-Konversation voller Insider-Gags daraus machen. Und irgendwo zwinkert eine alte RFC dazu, weil die Nerd-Fakten selten stillstehen.

## Best Practices
- A11y: Sidebar Navigation tastatur- und screenreader-freundlich gestalten.
- Performance: Sidebar Navigation nur laden, wenn der Kontext es wirklich braucht.
- Wartbarkeit: Entscheidungen zu Sidebar Navigation direkt neben dem Code dokumentieren.

## Fazit
Sidebar Navigation bleibt ein schönes Beispiel dafür, wie Layouts-Elemente Geschichten erzählen können, wenn man sie ernst nimmt und trotzdem mit Humor betrachtet.
