---
title: "Breadcrumbs: Randnotiz"
date: 2025-09-30
tags: [UI, Komponente, Webentwicklung]
excerpt: "Warum Breadcrumbs unsere Content Elements-Notizen inspiriert."
layout: post
categories: [content-elements]
slug: content-elements-breadcrumbs
original_path: content-elements/breadcrumbs.md
---

## Einleitung
Es fühlt sich an wie ein Fund in einer verstaubten Prototyp-Schublade: **Breadcrumbs** passte heute perfekt in unsere Content Elements-Gedanken, und plötzlich roch der Raum nach Whiteboard-Markern und frisch gebrühtem Kaffee.

## Technischer Kern
Technisch betrachtet verlangt Breadcrumbs nach klaren Leitplanken. Ich habe die ursprüngliche Beschreibung unten angeheftet und mit Kommentaren versehen, damit der Transfer in das neue Blog sichtbar bleibt.

### Originalnotizen
# Content-Element: Breadcrumbs

## Beschreibung
Hierarchische Navigation zur Orientierung im Seitensystem.

## Warum dieses Element?
- Nutzer auf tiefen Kategoriestrukturen unterstützen.
- SEO-verbesserte Navigation mit strukturierter Daten-Auszeichnung bieten.
- Trade-off: Bei flacher Struktur wenig Mehrwert und zusätzlicher Pflegeaufwand.

## Anforderungen & Besonderheiten
- **Responsiveness:** Horizontale Liste, auf Mobile kürzen oder scrollen lassen.
- **Accessibility:** `nav` mit `aria-label`, Trennzeichen nur dekorativ.
- **SEO:** `BreadcrumbList`-Markup für Rich Snippets.
- **Design-Guidelines:** Dezente Typografie, ausreichende Abstände, Chevron-Icons optional.
- **Rechtliches:** Keine speziellen Anforderungen.

## Umsetzung – Technische Leitplanken
- **Mobile First:** Nur letzte zwei Ebenen zeigen, Rest einklappbar.
- **Accessibility:** Aktuelle Seite mit `aria-current=page` kennzeichnen.
- **SEO:** Links auf wichtige Kategorie-Seiten setzen, Duplicate vermeiden.
- **Best Practices:**
  - Automatisch aus URL/Navigation generieren.
  - Home-Link immer anbieten.
  - Trennzeichen als CSS-Pseudo-Element rendern.

## Checkliste
- [ ] Darstellung auf allen Breakpoints geprüft
- [ ] Barrierefreiheit (Fokus, ARIA, Kontrast) OK
- [ ] Semantik korrekt (HTML)
- [ ] Performance optimiert (Lazyload/Kompression)

## Abhängigkeiten / Überschneidungen
- Hauptnavigation, Routing

## Akzeptanzkriterien
- Technische Funktion OK
- Konsistenz zum Designsystem
- A11y & rechtliche Vorgaben erfüllt

## Beispiel / Code
[content-elements-examples/breadcrumbs.html](../content-elements-examples/breadcrumbs.html)

```html
<!-- Minimales, valides HTML-Beispiel -->
<nav aria-label="Breadcrumb">
  <ol class="breadcrumbs">
    <li><a href="/">Start</a></li>
    <li><a href="/shop">Shop</a></li>
    <li aria-current="page">Sneaker</li>
  </ol>
</nav>
```

Bewertung der Relevanz 2025

⭐⭐⭐⭐ Breadcrumbs bleiben wichtig für Orientierung und SEO.

## Anekdoten & Nerd-Zitate
Michael Crichton hätte wahrscheinlich eine komplette Katastrophensimulation um Breadcrumbs gestrickt, nur um zu zeigen, wie viele Dinge gleichzeitig schiefgehen können. Douglas Coupland würde dagegen eine Slack-Konversation voller Insider-Gags daraus machen. Und irgendwo zwinkert eine alte RFC dazu, weil die Nerd-Fakten selten stillstehen.

## Best Practices
- A11y: Breadcrumbs tastatur- und screenreader-freundlich gestalten.
- Performance: Breadcrumbs nur laden, wenn der Kontext es wirklich braucht.
- Wartbarkeit: Entscheidungen zu Breadcrumbs direkt neben dem Code dokumentieren.

## Fazit
Breadcrumbs bleibt ein schönes Beispiel dafür, wie Content Elements-Elemente Geschichten erzählen können, wenn man sie ernst nimmt und trotzdem mit Humor betrachtet.
