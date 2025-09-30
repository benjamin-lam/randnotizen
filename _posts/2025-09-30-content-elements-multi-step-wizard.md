---
title: "Multi Step Wizard: Randnotiz"
date: 2025-09-30
tags: [UI, Komponente, Webentwicklung]
excerpt: "Warum Multi Step Wizard unsere Content Elements-Notizen inspiriert."
layout: post
categories: [content-elements]
slug: content-elements-multi-step-wizard
original_path: content-elements/multi-step-wizard.md
---

## Einleitung
Es fühlt sich an wie ein Fund in einer verstaubten Prototyp-Schublade: **Multi Step Wizard** passte heute perfekt in unsere Content Elements-Gedanken, und plötzlich roch der Raum nach Whiteboard-Markern und frisch gebrühtem Kaffee.

## Technischer Kern
Technisch betrachtet verlangt Multi Step Wizard nach klaren Leitplanken. Ich habe die ursprüngliche Beschreibung unten angeheftet und mit Kommentaren versehen, damit der Transfer in das neue Blog sichtbar bleibt.

### Originalnotizen
# Content-Element: Multi-Step Wizard

## Beschreibung
Mehrschrittige Benutzerführung für komplexe Prozesse.

## Warum dieses Element?
- Onboarding oder Registrierung in Etappen aufteilen.
- Konfiguratoren und Formulare mit vielen Feldern strukturieren.
- Trade-off: Höherer Implementierungsaufwand und potenzielle Abbrüche zwischen Schritten.

## Anforderungen & Besonderheiten
- **Responsiveness:** Schritte vertikal stacken, Fortschritt klar anzeigen.
- **Accessibility:** Fokus zwischen Schritten managen, `aria-current` für aktiven Schritt.
- **SEO:** Kein direkter Einfluss.
- **Design-Guidelines:** Klare Navigation, Buttons (Weiter/Zürück), Zwischenspeicherung.
- **Rechtliches:** Zwischenspeicherung personenbezogener Daten rechtlich absichern.

## Umsetzung – Technische Leitplanken
- **Mobile First:** Jeden Schritt auf das Wesentliche reduzieren, Auto-Save integrieren.
- **Accessibility:** Schrittwechsel ankündigen (`aria-live`), Escape aus Fokusfallen vermeiden.
- **SEO:** Nicht relevant.
- **Best Practices:**
  - Fortschritt speichern und wiederaufnehmen ermöglichen.
  - Zusammenfassung vor Abschluss anzeigen.
  - Validierung pro Schritt durchführen.

## Checkliste
- [ ] Darstellung auf allen Breakpoints geprüft
- [ ] Barrierefreiheit (Fokus, ARIA, Kontrast) OK
- [ ] Semantik korrekt (HTML)
- [ ] Performance optimiert (Lazyload/Kompression)

## Abhängigkeiten / Überschneidungen
- Progress-Steps, Form-Validation, State-Management

## Akzeptanzkriterien
- Technische Funktion OK
- Konsistenz zum Designsystem
- A11y & rechtliche Vorgaben erfüllt

## Beispiel / Code
[content-elements-examples/multi-step-wizard.html](../content-elements-examples/multi-step-wizard.html)

```html
<!-- Minimales, valides HTML-Beispiel -->
<form class="wizard">
  <section aria-labelledby="step1">
    <h2 id="step1">Schritt 1: Konto</h2>
    <label>Name<input name="name"></label>
    <button type="button">Weiter</button>
  </section>
</form>
```

Bewertung der Relevanz 2025

⭐⭐⭐⭐ Mehrschrittprozesse bleiben nötig, wenn komplexe Eingaben zu strukturieren sind.

## Anekdoten & Nerd-Zitate
Michael Crichton hätte wahrscheinlich eine komplette Katastrophensimulation um Multi Step Wizard gestrickt, nur um zu zeigen, wie viele Dinge gleichzeitig schiefgehen können. Douglas Coupland würde dagegen eine Slack-Konversation voller Insider-Gags daraus machen. Und irgendwo zwinkert eine alte RFC dazu, weil die Nerd-Fakten selten stillstehen.

## Best Practices
- A11y: Multi Step Wizard tastatur- und screenreader-freundlich gestalten.
- Performance: Multi Step Wizard nur laden, wenn der Kontext es wirklich braucht.
- Wartbarkeit: Entscheidungen zu Multi Step Wizard direkt neben dem Code dokumentieren.

## Fazit
Multi Step Wizard bleibt ein schönes Beispiel dafür, wie Content Elements-Elemente Geschichten erzählen können, wenn man sie ernst nimmt und trotzdem mit Humor betrachtet.
