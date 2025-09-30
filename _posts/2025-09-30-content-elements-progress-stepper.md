---
title: "Progress Stepper: Randnotiz"
date: 2025-09-30
tags: [UI, Komponente, Webentwicklung]
excerpt: "Warum Progress Stepper unsere Content Elements-Notizen inspiriert."
layout: post
categories: [content-elements]
slug: content-elements-progress-stepper
original_path: content-elements/progress-stepper.md
---

## Einleitung
Es fühlt sich an wie ein Fund in einer verstaubten Prototyp-Schublade: **Progress Stepper** passte heute perfekt in unsere Content Elements-Gedanken, und plötzlich roch der Raum nach Whiteboard-Markern und frisch gebrühtem Kaffee.

## Technischer Kern
Technisch betrachtet verlangt Progress Stepper nach klaren Leitplanken. Ich habe die ursprüngliche Beschreibung unten angeheftet und mit Kommentaren versehen, damit der Transfer in das neue Blog sichtbar bleibt.

### Originalnotizen
# Content-Element: Progress Stepper

## Beschreibung
Visualisierung des Fortschritts in mehreren Schritten oder Phasen.

## Warum dieses Element?
- Status in Checkouts oder Formularen anzeigen.
- Projekt- oder Onboarding-Fortschritt visualisieren.
- Trade-off: Falsche oder irreführende Schritte steigern Frust.

## Anforderungen & Besonderheiten
- **Responsiveness:** Horizontal auf Desktop, vertikal oder kompakt auf Mobile.
- **Accessibility:** `aria-current` für aktiven Schritt, klare Beschriftungen.
- **SEO:** Keine Relevanz.
- **Design-Guidelines:** Abstände, Nummern, Icons; aktive und abgeschlossene States klar differenzieren.
- **Rechtliches:** Keine speziellen Anforderungen.

## Umsetzung – Technische Leitplanken
- **Mobile First:** Text kürzen, Symbole mit Tooltips kombinieren.
- **Accessibility:** Stepper in `<nav>` mit `aria-label` einbetten.
- **SEO:** Nicht relevant.
- **Best Practices:**
  - Schritte anklickbar machen, wenn sinnvoll.
  - Fortschritt synchron mit Wizard-State halten.
  - Klar kommunizieren, wie viele Schritte folgen.

## Checkliste
- [ ] Darstellung auf allen Breakpoints geprüft
- [ ] Barrierefreiheit (Fokus, ARIA, Kontrast) OK
- [ ] Semantik korrekt (HTML)
- [ ] Performance optimiert (Lazyload/Kompression)

## Abhängigkeiten / Überschneidungen
- Multi-Step-Wizard, Designsystem

## Akzeptanzkriterien
- Technische Funktion OK
- Konsistenz zum Designsystem
- A11y & rechtliche Vorgaben erfüllt

## Beispiel / Code
[content-elements-examples/progress-stepper.html](../content-elements-examples/progress-stepper.html)

```html
<!-- Minimales, valides HTML-Beispiel -->
<ol class="stepper">
  <li class="stepper__item stepper__item--done">1. Konto</li>
  <li class="stepper__item stepper__item--current" aria-current="step">2. Adresse</li>
  <li class="stepper__item">3. Abschluss</li>
</ol>
```

Bewertung der Relevanz 2025

⭐⭐⭐⭐ Fortschrittsanzeigen bleiben wichtig für Transparenz in Prozessen.

## Anekdoten & Nerd-Zitate
Michael Crichton hätte wahrscheinlich eine komplette Katastrophensimulation um Progress Stepper gestrickt, nur um zu zeigen, wie viele Dinge gleichzeitig schiefgehen können. Douglas Coupland würde dagegen eine Slack-Konversation voller Insider-Gags daraus machen. Und irgendwo zwinkert eine alte RFC dazu, weil die Nerd-Fakten selten stillstehen.

## Best Practices
- A11y: Progress Stepper tastatur- und screenreader-freundlich gestalten.
- Performance: Progress Stepper nur laden, wenn der Kontext es wirklich braucht.
- Wartbarkeit: Entscheidungen zu Progress Stepper direkt neben dem Code dokumentieren.

## Fazit
Progress Stepper bleibt ein schönes Beispiel dafür, wie Content Elements-Elemente Geschichten erzählen können, wenn man sie ernst nimmt und trotzdem mit Humor betrachtet.
