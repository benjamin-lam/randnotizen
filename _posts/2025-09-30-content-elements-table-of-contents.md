---
title: "Table Of Contents: Randnotiz"
date: 2025-09-30
tags: [UI, Komponente, Webentwicklung]
excerpt: "Warum Table Of Contents unsere Content Elements-Notizen inspiriert."
layout: post
categories: [content-elements]
slug: content-elements-table-of-contents
original_path: content-elements/table-of-contents.md
---

## Einleitung
Es fühlt sich an wie ein Fund in einer verstaubten Prototyp-Schublade: **Table Of Contents** passte heute perfekt in unsere Content Elements-Gedanken, und plötzlich roch der Raum nach Whiteboard-Markern und frisch gebrühtem Kaffee.

## Technischer Kern
Technisch betrachtet verlangt Table Of Contents nach klaren Leitplanken. Ich habe die ursprüngliche Beschreibung unten angeheftet und mit Kommentaren versehen, damit der Transfer in das neue Blog sichtbar bleibt.

### Originalnotizen
# Content-Element: Table of Contents

## Beschreibung
Strukturierte Liste von Ankern, die durch längere Inhalte navigiert.

## Warum dieses Element?
- Lange Blog- oder Doku-Artikel navigierbar machen.
- FAQ- oder Richtlinientexte schnell erschließen.
- Trade-off: Pflegeaufwand, wenn Überschriften dynamisch generiert oder häufig geändert werden.

## Anforderungen & Besonderheiten
- **Responsiveness:** Sticky-Verhalten auf Desktop, ausklappbar auf Mobile.
- **Accessibility:** ARIA-Labeling für Navigation, Fokusreihenfolge beachten, Skip-Link anbieten.
- **SEO:** Sprungmarken unterstützen Sitelinks und Rich Snippets.
- **Design-Guidelines:** Klarer Abstand zum Inhalt, aktive Zustände markieren, dezente Typografie.
- **Rechtliches:** Keine speziellen Anforderungen.

## Umsetzung – Technische Leitplanken
- **Mobile First:** Als Akkordeon oder Dropdown starten und auf größeren Screens erweitern.
- **Accessibility:** `nav` mit `aria-label` nutzen, Fokuszustände gut sichtbar machen.
- **SEO:** Anker-IDs sprechend benennen, keine doppelten IDs.
- **Best Practices:**
  - Automatisierte Generierung aus der H-Struktur.
  - Aktuelle Sektion via Intersection Observer hervorheben.
  - Scroll-Offset für Fixed Header berücksichtigen.

## Checkliste
- [ ] Darstellung auf allen Breakpoints geprüft
- [ ] Barrierefreiheit (Fokus, ARIA, Kontrast) OK
- [ ] Semantik korrekt (HTML)
- [ ] Performance optimiert (Lazyload/Kompression)

## Abhängigkeiten / Überschneidungen
- Anchor-Links, Sticky-Header, Scrollspy

## Akzeptanzkriterien
- Technische Funktion OK
- Konsistenz zum Designsystem
- A11y & rechtliche Vorgaben erfüllt

## Beispiel / Code
[content-elements-examples/table-of-contents.html](../content-elements-examples/table-of-contents.html)

```html
<!-- Minimales, valides HTML-Beispiel -->
<nav class="toc" aria-label="Inhaltsverzeichnis">
  <ol>
    <li><a href="#section-1">Einleitung</a></li>
    <li><a href="#section-2">Details</a></li>
  </ol>
</nav>
```

Bewertung der Relevanz 2025

⭐⭐⭐⭐ Längere Inhalte bleiben verbreitet, daher ist eine gute Orientierung weiter wichtig.

## Anekdoten & Nerd-Zitate
Michael Crichton hätte wahrscheinlich eine komplette Katastrophensimulation um Table Of Contents gestrickt, nur um zu zeigen, wie viele Dinge gleichzeitig schiefgehen können. Douglas Coupland würde dagegen eine Slack-Konversation voller Insider-Gags daraus machen. Und irgendwo zwinkert eine alte RFC dazu, weil die Nerd-Fakten selten stillstehen.

## Best Practices
- A11y: Table Of Contents tastatur- und screenreader-freundlich gestalten.
- Performance: Table Of Contents nur laden, wenn der Kontext es wirklich braucht.
- Wartbarkeit: Entscheidungen zu Table Of Contents direkt neben dem Code dokumentieren.

## Fazit
Table Of Contents bleibt ein schönes Beispiel dafür, wie Content Elements-Elemente Geschichten erzählen können, wenn man sie ernst nimmt und trotzdem mit Humor betrachtet.
