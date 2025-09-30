---
title: "Empty State: Randnotiz"
date: 2025-09-30
tags: [UI, Komponente, Webentwicklung]
excerpt: "Warum Empty State unsere Content Elements-Notizen inspiriert."
layout: post
categories: [content-elements]
slug: content-elements-empty-state
original_path: content-elements/empty-state.md
---

## Einleitung
Es fühlt sich an wie ein Fund in einer verstaubten Prototyp-Schublade: **Empty State** passte heute perfekt in unsere Content Elements-Gedanken, und plötzlich roch der Raum nach Whiteboard-Markern und frisch gebrühtem Kaffee.

## Technischer Kern
Technisch betrachtet verlangt Empty State nach klaren Leitplanken. Ich habe die ursprüngliche Beschreibung unten angeheftet und mit Kommentaren versehen, damit der Transfer in das neue Blog sichtbar bleibt.

### Originalnotizen
# Content-Element: Empty State

## Beschreibung
Darstellung, wenn keine Daten oder Ergebnisse vorliegen.

## Warum dieses Element?
- Suche ohne Treffer informativ gestalten.
- Neue Nutzer in Dashboards an Funktionen heranführen.
- Trade-off: Unpassende Illustrationen oder Texte können Nutzer verwirren.

## Anforderungen & Besonderheiten
- **Responsiveness:** Illustrationen und Text skalieren, Buttons darunter anordnen.
- **Accessibility:** Alternativtexte für Illustrationen, klare Anweisungen auch in Text.
- **SEO:** Keine direkte Relevanz.
- **Design-Guidelines:** Illustration, Headline, Body-Text, CTA optional, konsistente Farben.
- **Rechtliches:** Keine speziellen Anforderungen.

## Umsetzung – Technische Leitplanken
- **Mobile First:** Kurze Texte, klare Handlungsoptionen, Buttons full-width.
- **Accessibility:** Keine rein ikonografischen Aussagen; Text beschreibt Situation.
- **SEO:** Nicht relevant.
- **Best Practices:**
  - Konkrete nächste Schritte anbieten.
  - Optional Hilfelinks einblenden.
  - Tonfall empathisch wählen.

## Checkliste
- [ ] Darstellung auf allen Breakpoints geprüft
- [ ] Barrierefreiheit (Fokus, ARIA, Kontrast) OK
- [ ] Semantik korrekt (HTML)
- [ ] Performance optimiert (Lazyload/Kompression)

## Abhängigkeiten / Überschneidungen
- Illustrationen, CTA-Komponenten

## Akzeptanzkriterien
- Technische Funktion OK
- Konsistenz zum Designsystem
- A11y & rechtliche Vorgaben erfüllt

## Beispiel / Code
[content-elements-examples/empty-state.html](../content-elements-examples/empty-state.html)

```html
<!-- Minimales, valides HTML-Beispiel -->
<section class="empty-state">
  <img src="../assets/agents-and-robots.png" alt="Agentin und Roboter in einer futuristischen Stadt bei Nacht" loading="lazy">
  <h2>Keine Ergebnisse</h2>
  <p>Passen Sie Ihre Filter an oder starten Sie eine neue Suche.</p>
  <button type="button">Filter zurücksetzen</button>
</section>
```

Bewertung der Relevanz 2025

⭐⭐⭐⭐ Gute Empty States steigern Engagement und helfen bei der Orientierung.

## Anekdoten & Nerd-Zitate
Michael Crichton hätte wahrscheinlich eine komplette Katastrophensimulation um Empty State gestrickt, nur um zu zeigen, wie viele Dinge gleichzeitig schiefgehen können. Douglas Coupland würde dagegen eine Slack-Konversation voller Insider-Gags daraus machen. Und irgendwo zwinkert eine alte RFC dazu, weil die Nerd-Fakten selten stillstehen.

## Best Practices
- A11y: Empty State tastatur- und screenreader-freundlich gestalten.
- Performance: Empty State nur laden, wenn der Kontext es wirklich braucht.
- Wartbarkeit: Entscheidungen zu Empty State direkt neben dem Code dokumentieren.

## Fazit
Empty State bleibt ein schönes Beispiel dafür, wie Content Elements-Elemente Geschichten erzählen können, wenn man sie ernst nimmt und trotzdem mit Humor betrachtet.
