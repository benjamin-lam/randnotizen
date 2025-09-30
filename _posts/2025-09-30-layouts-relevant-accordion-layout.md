---
title: "Accordion Layout: Randnotiz"
date: 2025-09-30
tags: [UI, Komponente, Webentwicklung]
excerpt: "Warum Accordion Layout unsere Layouts-Notizen inspiriert."
layout: post
categories: [layouts]
slug: layouts-relevant-accordion-layout
original_path: layouts/relevant/accordion-layout.md
---

## Einleitung
Es fühlt sich an wie ein Fund in einer verstaubten Prototyp-Schublade: **Accordion Layout** passte heute perfekt in unsere Layouts-Gedanken, und plötzlich roch der Raum nach Whiteboard-Markern und frisch gebrühtem Kaffee.

## Technischer Kern
Technisch betrachtet verlangt Accordion Layout nach klaren Leitplanken. Ich habe die ursprüngliche Beschreibung unten angeheftet und mit Kommentaren versehen, damit der Transfer in das neue Blog sichtbar bleibt.

### Originalnotizen
# Layout: Accordion Layout

## Beschreibung
Ausklappbare Bereiche bündeln FAQs, Detailinfos oder Spezifikationen und halten Seiten kompakt.

## Warum dieses Layout?
- Hilft bei der Strukturierung langer Informationslisten.
- Reduziert kognitive Last durch progressive Offenlegung.
- Kann wichtige Inhalte vor Nutzern und Suchmaschinen verbergen.

## Anforderungen & Besonderheiten
- **Responsiveness:** Accordion-Elemente passen sich in Breite und Typografie an.
- **Accessibility:** WAI-ARIA Disclosure Pattern mit button, aria-expanded und aria-controls nutzen.
- **SEO:** Wesentliche Inhalte sollten im initial geöffneten Zustand verfügbar sein.
- **Design-Guidelines:** Klare Trennlinien, ausreichend Padding und deutliche Icons für Zustände.

## Umsetzung – Technische Leitplanken
- **Mobile First:** Accordion ist Standard, Desktop kann parallele Spalten ergänzen.
- **Accessibility:** Focus-Stati und Tastatursteuerung (Enter/Space) berücksichtigen.
- **SEO:** Accordion-Inhalte im DOM belassen und nicht per JS nachladen.
- **Best Practices:** Weiche Animationen einsetzen, Nur ein Panel optional offen halten, Status programmatisch speichern

## Checkliste
- [ ] Accordion lässt sich mit Tastatur komplett bedienen.
- [ ] Icons und Labels kommunizieren den Zustand klar.
- [ ] Wichtige Inhalte sind initial sichtbar oder angekündigt.
- [ ] A11y- und Performance-Audit abgeschlossen.

## Abhängigkeiten / Überschneidungen
- Disclosure-Komponente
- Content-Module

## Akzeptanzkriterien
- ARIA-Attribute entsprechen dem Disclosure-Pattern.
- Panels lassen sich ohne Layoutsprünge öffnen und schließen.
- Screenreader geben Statusänderungen korrekt wieder.

## Beispiel / Code
```html
<section class="accordion">
  <button aria-expanded="false" aria-controls="faq-1">Frage</button>
  <div id="faq-1" hidden>Antwort…</div>
</section>
```

Bewertung der Relevanz 2025

⭐⭐⭐⭐⭐ Standardmuster für FAQs und Detailinformationen.

## Anekdoten & Nerd-Zitate
Michael Crichton hätte wahrscheinlich eine komplette Katastrophensimulation um Accordion Layout gestrickt, nur um zu zeigen, wie viele Dinge gleichzeitig schiefgehen können. Douglas Coupland würde dagegen eine Slack-Konversation voller Insider-Gags daraus machen. Und irgendwo zwinkert eine alte RFC dazu, weil die Nerd-Fakten selten stillstehen.

## Best Practices
- A11y: Accordion Layout tastatur- und screenreader-freundlich gestalten.
- Performance: Accordion Layout nur laden, wenn der Kontext es wirklich braucht.
- Wartbarkeit: Entscheidungen zu Accordion Layout direkt neben dem Code dokumentieren.

## Fazit
Accordion Layout bleibt ein schönes Beispiel dafür, wie Layouts-Elemente Geschichten erzählen können, wenn man sie ernst nimmt und trotzdem mit Humor betrachtet.
