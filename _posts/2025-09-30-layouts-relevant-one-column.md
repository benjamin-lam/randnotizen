---
title: "One Column: Randnotiz"
date: 2025-09-30
tags: [UI, Komponente, Webentwicklung]
excerpt: "Warum One Column unsere Layouts-Notizen inspiriert."
layout: post
categories: [layouts]
slug: layouts-relevant-one-column
original_path: layouts/relevant/one-column.md
---

## Einleitung
Es fühlt sich an wie ein Fund in einer verstaubten Prototyp-Schublade: **One Column** passte heute perfekt in unsere Layouts-Gedanken, und plötzlich roch der Raum nach Whiteboard-Markern und frisch gebrühtem Kaffee.

## Technischer Kern
Technisch betrachtet verlangt One Column nach klaren Leitplanken. Ich habe die ursprüngliche Beschreibung unten angeheftet und mit Kommentaren versehen, damit der Transfer in das neue Blog sichtbar bleibt.

### Originalnotizen
# Layout: One Column

## Beschreibung
Ein einspaltiges Layout lenkt den Blick auf den Hauptinhalt und reduziert Ablenkungen. Typischerweise wird es für Artikel, Dokumentationen oder fokussierte Landingpages eingesetzt.

## Warum dieses Layout?
- Maximiert Lesbarkeit und Flow für längere Texte.
- Einfach zu pflegen und mit modularen Komponenten zu erweitern.
- Bietet wenig Fläche für sekundäre Navigation oder Promotions.

## Anforderungen & Besonderheiten
- **Responsiveness:** Flexible max-width zwischen 68–76ch und adaptive Seitenränder auf allen Breakpoints.
- **Accessibility:** Saubere Überschriftenhierarchie, ausreichend Zeilenabstand und lesbare Schriftgrößen.
- **SEO:** Semantische Struktur mit <header>, <main>, <footer> und klarer h1–h3-Reihenfolge.
- **Design-Guidelines:** Großzügige Weißräume, konsistente Typografie-Skala und ruhige Farbpalette.

## Umsetzung – Technische Leitplanken
- **Mobile First:** Beginnt als vollbreite Spalte mit progressiver Begrenzung über max-width.
- **Accessibility:** Nutzt Landmark-Rollen und Skip-Links für schnelle Navigation.
- **SEO:** Verwendet strukturierte Überschriften und relevante Meta-Daten.
- **Best Practices:** max-width clamp(), line-height ≥ 1.5, font-size über clamp() skalieren

## Checkliste
- [ ] Maximale Inhaltsbreite und Seitenabstände definiert.
- [ ] Heading-Skala konsistent angewendet.
- [ ] Kontrastwerte für Text und Links geprüft.
- [ ] Core Web Vitals im grünen Bereich.

## Abhängigkeiten / Überschneidungen
- Globaler Header/Footer
- Typografie-Token und Lesbarkeitsrichtlinien

## Akzeptanzkriterien
- Inhalte bleiben auf allen Breakpoints ohne horizontales Scrollen lesbar.
- H1–H3-Struktur validiert und screenreaderfreundlich.
- Layout reagiert flüssig auf Schriftgrößenänderungen.

## Beispiel / Code
```html
<main class="container">
  <article class="prose">
    <h1>Titel</h1>
    <p>Absatz…</p>
  </article>
</main>
```

Bewertung der Relevanz 2025

⭐⭐⭐⭐⭐ Zeitloses Standard-Layout für leselastige Seiten.

## Anekdoten & Nerd-Zitate
Michael Crichton hätte wahrscheinlich eine komplette Katastrophensimulation um One Column gestrickt, nur um zu zeigen, wie viele Dinge gleichzeitig schiefgehen können. Douglas Coupland würde dagegen eine Slack-Konversation voller Insider-Gags daraus machen. Und irgendwo zwinkert eine alte RFC dazu, weil die Nerd-Fakten selten stillstehen.

## Best Practices
- A11y: One Column tastatur- und screenreader-freundlich gestalten.
- Performance: One Column nur laden, wenn der Kontext es wirklich braucht.
- Wartbarkeit: Entscheidungen zu One Column direkt neben dem Code dokumentieren.

## Fazit
One Column bleibt ein schönes Beispiel dafür, wie Layouts-Elemente Geschichten erzählen können, wenn man sie ernst nimmt und trotzdem mit Humor betrachtet.
