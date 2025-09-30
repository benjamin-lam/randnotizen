---
title: "Filter Facets: Randnotiz"
date: 2025-09-30
tags: [UI, Komponente, Webentwicklung]
excerpt: "Warum Filter Facets unsere Content Elements-Notizen inspiriert."
layout: post
categories: [content-elements]
slug: content-elements-filter-facets
original_path: content-elements/filter-facets.md
---

## Einleitung
Es fühlt sich an wie ein Fund in einer verstaubten Prototyp-Schublade: **Filter Facets** passte heute perfekt in unsere Content Elements-Gedanken, und plötzlich roch der Raum nach Whiteboard-Markern und frisch gebrühtem Kaffee.

## Technischer Kern
Technisch betrachtet verlangt Filter Facets nach klaren Leitplanken. Ich habe die ursprüngliche Beschreibung unten angeheftet und mit Kommentaren versehen, damit der Transfer in das neue Blog sichtbar bleibt.

### Originalnotizen
# Content-Element: Filter Facets

## Beschreibung
Facettierte Filtersteuerung mit Chips, Listen oder Slidern.

## Warum dieses Element?
- Produkt- oder Artikellisten zielgerichtet einschränken.
- Suchergebnisse nach Kategorien, Preisen oder Tags verfeinern.
- Trade-off: Zu viele Filteroptionen überfordern Nutzer und erhöhen Komplexität.

## Anforderungen & Besonderheiten
- **Responsiveness:** Auf Mobile als Akkordeon oder Off-Canvas, auf Desktop nebeneinander.
- **Accessibility:** Checkbox-/Radio-Labels klar benennen, `aria-pressed` für Chips.
- **SEO:** Filter-URLs sauber handhaben, Duplicate Content vermeiden.
- **Design-Guidelines:** Visuelle Hierarchie, aktive Filter hervorheben, Reset-Option.
- **Rechtliches:** Tracking von Filterinteraktionen DSGVO-konform behandeln.

## Umsetzung – Technische Leitplanken
- **Mobile First:** Filter über Button einblenden, Prioritäten setzen.
- **Accessibility:** Statusänderungen per `aria-live` ankündigen, Fokus nach Anwendung sinnvoll setzen.
- **SEO:** Kanonsiche URLs definieren, Parameter whitelisten.
- **Best Practices:**
  - Aktive Filter deutlich anzeigen und entfernen lassen.
  - Filterzustand in URL speichern.
  - Serverseitige und clientseitige Filter synchron halten.

## Checkliste
- [ ] Darstellung auf allen Breakpoints geprüft
- [ ] Barrierefreiheit (Fokus, ARIA, Kontrast) OK
- [ ] Semantik korrekt (HTML)
- [ ] Performance optimiert (Lazyload/Kompression)

## Abhängigkeiten / Überschneidungen
- Such-API, State-Management, Analytics

## Akzeptanzkriterien
- Technische Funktion OK
- Konsistenz zum Designsystem
- A11y & rechtliche Vorgaben erfüllt

## Beispiel / Code
[content-elements-examples/filter-facets.html](../content-elements-examples/filter-facets.html)

```html
<!-- Minimales, valides HTML-Beispiel -->
<section class="filters">
  <button type="button" class="filter-chip" aria-pressed="true">Sofort lieferbar</button>
  <label><input type="checkbox" name="brand" value="acme"> ACME</label>
</section>
```

Bewertung der Relevanz 2025

⭐⭐⭐⭐ Komplexe Kataloge brauchen weiterhin leistungsfähige Filtersteuerungen.

## Anekdoten & Nerd-Zitate
Michael Crichton hätte wahrscheinlich eine komplette Katastrophensimulation um Filter Facets gestrickt, nur um zu zeigen, wie viele Dinge gleichzeitig schiefgehen können. Douglas Coupland würde dagegen eine Slack-Konversation voller Insider-Gags daraus machen. Und irgendwo zwinkert eine alte RFC dazu, weil die Nerd-Fakten selten stillstehen.

## Best Practices
- A11y: Filter Facets tastatur- und screenreader-freundlich gestalten.
- Performance: Filter Facets nur laden, wenn der Kontext es wirklich braucht.
- Wartbarkeit: Entscheidungen zu Filter Facets direkt neben dem Code dokumentieren.

## Fazit
Filter Facets bleibt ein schönes Beispiel dafür, wie Content Elements-Elemente Geschichten erzählen können, wenn man sie ernst nimmt und trotzdem mit Humor betrachtet.
