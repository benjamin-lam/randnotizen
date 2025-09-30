---
title: "Fixed Footer: Randnotiz"
date: 2025-09-30
tags: [UI, Komponente, Webentwicklung]
excerpt: "Warum Fixed Footer unsere Layouts-Notizen inspiriert."
layout: post
categories: [layouts]
slug: layouts-deprecated-fixed-footer
original_path: layouts/deprecated/fixed-footer.md
---

## Einleitung
Es fühlt sich an wie ein Fund in einer verstaubten Prototyp-Schublade: **Fixed Footer** passte heute perfekt in unsere Layouts-Gedanken, und plötzlich roch der Raum nach Whiteboard-Markern und frisch gebrühtem Kaffee.

## Technischer Kern
Technisch betrachtet verlangt Fixed Footer nach klaren Leitplanken. Ich habe die ursprüngliche Beschreibung unten angeheftet und mit Kommentaren versehen, damit der Transfer in das neue Blog sichtbar bleibt.

### Originalnotizen
# Layout: Fixed Footer

## Beschreibung
Ein dauerhaft fixierter Footer verdeckt auf mobilen Geräten häufig Inhalte oder Steuerungen und wird daher nicht mehr empfohlen.

## Warum dieses Layout?
- Kann für spezielle App-Bars genutzt werden.
- Bietet permanente Sichtbarkeit für Aktionen.
- Verhindert sichtbaren Content und verursacht Bedienprobleme.

## Anforderungen & Besonderheiten
- **Responsiveness:** Nur in Ausnahmen aktivieren, ausreichend Abstand zum Content einplanen.
- **Accessibility:** Fokus und Screenreader dürfen nicht blockiert werden, Inhalte müssen erreichbar bleiben.
- **SEO:** Kein direkter Mehrwert, eher Risiko für schlechte UX.
- **Design-Guidelines:** Wenn unvermeidlich, transparente Hintergründe und ausreichende Höhen nutzen.

## Umsetzung – Technische Leitplanken
- **Mobile First:** Fixed Footer deaktivieren und stattdessen Sticky- oder Inline-Alternativen wählen.
- **Accessibility:** Skip-Link oder Close-Button bereitstellen, wenn Footer unvermeidlich.
- **SEO:** Keine übermäßigen Links im Footer platzieren.
- **Best Practices:** Nur kontextuell einsetzen, Touch-Ziele groß halten, CLS vermeiden

## Checkliste
- [ ] Footer kann bei Bedarf ausgeblendet werden.
- [ ] Inhalte bleiben vollständig sichtbar.
- [ ] Tastaturfokus nicht blockiert.
- [ ] A11y- und Performance-Check dokumentiert.

## Abhängigkeiten / Überschneidungen
- Legacy-App-Bars
- CTA-Module

## Akzeptanzkriterien
- Alternatives Pattern liegt vor.
- Screenreader können Inhalte hinter dem Footer erreichen.
- Stakeholder stimmen dem Rückbau zu.

## Beispiel / Code
```html
<footer class="fixed bottom-0 inset-x-0">
  <nav>…</nav>
</footer>
```

> ⚠️ Deprecated: Nicht mehr empfohlen für Mobile-First-Designs (nur zu Dokumentationszwecken).

Bewertung der Relevanz 2025

⭐⭐☆☆☆ Nur für Spezialfälle mit großer Vorsicht nutzen.

## Anekdoten & Nerd-Zitate
Michael Crichton hätte wahrscheinlich eine komplette Katastrophensimulation um Fixed Footer gestrickt, nur um zu zeigen, wie viele Dinge gleichzeitig schiefgehen können. Douglas Coupland würde dagegen eine Slack-Konversation voller Insider-Gags daraus machen. Und irgendwo zwinkert eine alte RFC dazu, weil die Nerd-Fakten selten stillstehen.

## Best Practices
- A11y: Fixed Footer tastatur- und screenreader-freundlich gestalten.
- Performance: Fixed Footer nur laden, wenn der Kontext es wirklich braucht.
- Wartbarkeit: Entscheidungen zu Fixed Footer direkt neben dem Code dokumentieren.

## Fazit
Fixed Footer bleibt ein schönes Beispiel dafür, wie Layouts-Elemente Geschichten erzählen können, wenn man sie ernst nimmt und trotzdem mit Humor betrachtet.
