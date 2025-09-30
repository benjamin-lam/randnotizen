---
title: "Horizontal Scrolling: Randnotiz"
date: 2025-09-30
tags: [UI, Komponente, Webentwicklung]
excerpt: "Warum Horizontal Scrolling unsere Layouts-Notizen inspiriert."
layout: post
categories: [layouts]
slug: layouts-deprecated-horizontal-scrolling
original_path: layouts/deprecated/horizontal-scrolling.md
---

## Einleitung
Es fühlt sich an wie ein Fund in einer verstaubten Prototyp-Schublade: **Horizontal Scrolling** passte heute perfekt in unsere Layouts-Gedanken, und plötzlich roch der Raum nach Whiteboard-Markern und frisch gebrühtem Kaffee.

## Technischer Kern
Technisch betrachtet verlangt Horizontal Scrolling nach klaren Leitplanken. Ich habe die ursprüngliche Beschreibung unten angeheftet und mit Kommentaren versehen, damit der Transfer in das neue Blog sichtbar bleibt.

### Originalnotizen
# Layout: Horizontal Scrolling Layout

## Beschreibung
Ein Layout mit horizontalem Scrollen als primäre Navigationsachse wirkt unnatürlich und ist auf mobilen Geräten schwer steuerbar.

## Warum dieses Layout?
- Kann besondere Storytelling-Experiences liefern.
- Setzt visuelle Highlights in Szene.
- Verursacht UX-Probleme bei Scroll-Gesten und Orientierung.

## Anforderungen & Besonderheiten
- **Responsiveness:** Klare Scroll-Hinweise, horizontale Scrollbereiche mit Touch-Unterstützung.
- **Accessibility:** Alternativen für Tastatur und Screenreader bereitstellen, wheel-Events bedacht einsetzen.
- **SEO:** Wichtige Inhalte auch vertikal zugänglich machen.
- **Design-Guidelines:** Deutliche Pfeile, Pagination oder Snap-Punkte, um Orientierung zu sichern.

## Umsetzung – Technische Leitplanken
- **Mobile First:** Standard-Layouts bevorzugen und horizontale Scrollstrecken nur optional einbinden.
- **Accessibility:** Scroll-Mapping auf Trackpad/Wheel nur vorsichtig nutzen.
- **SEO:** Vertikale Alternativansicht oder Jump-Links bereitstellen.
- **Best Practices:** Scroll-Hints anzeigen, Snapping optional, Fallback auf vertikale Liste

## Checkliste
- [ ] Scroll-Hinweise sind sichtbar.
- [ ] Tastaturbedienung möglich.
- [ ] Vertikale Alternative vorhanden.
- [ ] A11y- und Performance-Check dokumentiert.

## Abhängigkeiten / Überschneidungen
- Scroll- und Animation-Utilities
- Fallback-Layouts

## Akzeptanzkriterien
- Nutzer verstehen Interaktion ohne Tutorial.
- Screenreader erhalten linearen Alternativzugang.
- Stakeholder akzeptieren Einsatz nur in Spezialfällen.

## Beispiel / Code
```html
<section class="horizontal-scroll" aria-label="Galerie">
  <div class="scroll-track">…</div>
</section>
```

> ⚠️ Deprecated: Nicht mehr empfohlen für Mobile-First-Designs (nur zu Dokumentationszwecken).

Bewertung der Relevanz 2025

⭐⭐☆☆☆ Nur für spezielle Storytelling-Experimente erhalten.

## Anekdoten & Nerd-Zitate
Michael Crichton hätte wahrscheinlich eine komplette Katastrophensimulation um Horizontal Scrolling gestrickt, nur um zu zeigen, wie viele Dinge gleichzeitig schiefgehen können. Douglas Coupland würde dagegen eine Slack-Konversation voller Insider-Gags daraus machen. Und irgendwo zwinkert eine alte RFC dazu, weil die Nerd-Fakten selten stillstehen.

## Best Practices
- A11y: Horizontal Scrolling tastatur- und screenreader-freundlich gestalten.
- Performance: Horizontal Scrolling nur laden, wenn der Kontext es wirklich braucht.
- Wartbarkeit: Entscheidungen zu Horizontal Scrolling direkt neben dem Code dokumentieren.

## Fazit
Horizontal Scrolling bleibt ein schönes Beispiel dafür, wie Layouts-Elemente Geschichten erzählen können, wenn man sie ernst nimmt und trotzdem mit Humor betrachtet.
