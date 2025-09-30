---
title: "Tooltip: Randnotiz"
date: 2025-09-30
tags: [UI, Komponente, Webentwicklung]
excerpt: "Warum Tooltip unsere Content Elements-Notizen inspiriert."
layout: post
categories: [content-elements]
slug: content-elements-tooltip
original_path: content-elements/tooltip.md
---

## Einleitung
Es fühlt sich an wie ein Fund in einer verstaubten Prototyp-Schublade: **Tooltip** passte heute perfekt in unsere Content Elements-Gedanken, und plötzlich roch der Raum nach Whiteboard-Markern und frisch gebrühtem Kaffee.

## Technischer Kern
Technisch betrachtet verlangt Tooltip nach klaren Leitplanken. Ich habe die ursprüngliche Beschreibung unten angeheftet und mit Kommentaren versehen, damit der Transfer in das neue Blog sichtbar bleibt.

### Originalnotizen
# Content-Element: Tooltip

## Beschreibung
Kurze Hilfetexte, die bei Hover oder Fokus zusätzliche Informationen geben.

## Warum dieses Element?
- Formularfelder mit Kontextinformationen versehen.
- Tabellenwerte oder Icons erläutern, ohne Layout zu überladen.
- Trade-off: Nicht auf Touch-Geräten verfügbar, daher alternative Darstellung nötig.

## Anforderungen & Besonderheiten
- **Responsiveness:** Positionierung relativ zum Trigger, auf Mobile ggf. als Inline-Hinweis.
- **Accessibility:** `aria-describedby` verwenden, Fokus-Management beachten.
- **SEO:** Kein direkter Einfluss, Inhalte sollten auch ohne Tooltip verfügbar sein.
- **Design-Guidelines:** Klarer Kontrast, dezente Animation, Pfeile optional.
- **Rechtliches:** Keine speziellen Anforderungen.

## Umsetzung – Technische Leitplanken
- **Mobile First:** Tooltip als Click-to-toggle oder Inline-Expand umsetzen.
- **Accessibility:** Tooltip bei Fokus sichtbar halten, Escape zum Schließen ermöglichen.
- **SEO:** Tooltip-Inhalte nicht exklusiv halten, immer auch im Fließtext erwähnen.
- **Best Practices:**
  - Trigger als Button oder Link deklarieren.
  - Tooltip mit `role="tooltip"` und IDs verknüpfen.
  - Autohide mit Verzögerung, um Flickern zu vermeiden.

## Checkliste
- [ ] Darstellung auf allen Breakpoints geprüft
- [ ] Barrierefreiheit (Fokus, ARIA, Kontrast) OK
- [ ] Semantik korrekt (HTML)
- [ ] Performance optimiert (Lazyload/Kompression)

## Abhängigkeiten / Überschneidungen
- Popover-System, Focus-Management

## Akzeptanzkriterien
- Technische Funktion OK
- Konsistenz zum Designsystem
- A11y & rechtliche Vorgaben erfüllt

## Beispiel / Code
[content-elements-examples/tooltip.html](../content-elements-examples/tooltip.html)

```html
<!-- Minimales, valides HTML-Beispiel -->
<button type="button" aria-describedby="tip-id">?
</button>
<span id="tip-id" role="tooltip">Erklärt das Feld</span>
```

Bewertung der Relevanz 2025

⭐⭐⭐⭐ Tooltips bleiben relevant, solange Touch-Alternativen berücksichtigt werden.

## Anekdoten & Nerd-Zitate
Michael Crichton hätte wahrscheinlich eine komplette Katastrophensimulation um Tooltip gestrickt, nur um zu zeigen, wie viele Dinge gleichzeitig schiefgehen können. Douglas Coupland würde dagegen eine Slack-Konversation voller Insider-Gags daraus machen. Und irgendwo zwinkert eine alte RFC dazu, weil die Nerd-Fakten selten stillstehen.

## Best Practices
- A11y: Tooltip tastatur- und screenreader-freundlich gestalten.
- Performance: Tooltip nur laden, wenn der Kontext es wirklich braucht.
- Wartbarkeit: Entscheidungen zu Tooltip direkt neben dem Code dokumentieren.

## Fazit
Tooltip bleibt ein schönes Beispiel dafür, wie Content Elements-Elemente Geschichten erzählen können, wenn man sie ernst nimmt und trotzdem mit Humor betrachtet.
