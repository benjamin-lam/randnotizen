---
title: "Date Picker: Randnotiz"
date: 2025-09-30
tags: [UI, Komponente, Webentwicklung]
excerpt: "Warum Date Picker unsere Content Elements-Notizen inspiriert."
layout: post
categories: [content-elements]
slug: content-elements-date-picker
original_path: content-elements/date-picker.md
---

## Einleitung
Es fühlt sich an wie ein Fund in einer verstaubten Prototyp-Schublade: **Date Picker** passte heute perfekt in unsere Content Elements-Gedanken, und plötzlich roch der Raum nach Whiteboard-Markern und frisch gebrühtem Kaffee.

## Technischer Kern
Technisch betrachtet verlangt Date Picker nach klaren Leitplanken. Ich habe die ursprüngliche Beschreibung unten angeheftet und mit Kommentaren versehen, damit der Transfer in das neue Blog sichtbar bleibt.

### Originalnotizen
# Content-Element: Date Picker

## Beschreibung
Komponente zur Auswahl einzelner Daten oder Zeitspannen.

## Warum dieses Element?
- Buchungen oder Terminplanungen ermöglichen.
- Filter nach Zeitraum in Reports oder Dashboards anbieten.
- Trade-off: Komplexe Kalenderlogik kann Fehler hervorrufen und ist schwer barrierefrei umzusetzen.

## Anforderungen & Besonderheiten
- **Responsiveness:** Kalender auf Mobile als Vollbild oder Listenansicht.
- **Accessibility:** Tastaturbedienung (Pfeiltasten), Screenreader-Beschriftungen, Ansagen der Auswahl.
- **SEO:** Keine direkte Relevanz.
- **Design-Guidelines:** Hervorhebung von aktiven, ausgewählten und deaktivierten Tagen, klare Navigation.
- **Rechtliches:** Bei Buchungen gesetzliche Aufbewahrung von Daten beachten.

## Umsetzung – Technische Leitplanken
- **Mobile First:** Native Picker nutzen, wenn verfügbar, oder optimierte Touch-Gesten.
- **Accessibility:** `aria-live` für Monatswechsel, `aria-selected` für Tage pflegen.
- **SEO:** Nicht relevant.
- **Best Practices:**
  - Min-/Max-Daten definieren.
  - Datumsformat klar kommunizieren.
  - Range-Auswahl mit Drag oder zwei Feldern ermöglichen.

## Checkliste
- [ ] Darstellung auf allen Breakpoints geprüft
- [ ] Barrierefreiheit (Fokus, ARIA, Kontrast) OK
- [ ] Semantik korrekt (HTML)
- [ ] Performance optimiert (Lazyload/Kompression)

## Abhängigkeiten / Überschneidungen
- Lokalisierung, Zeitbibliothek

## Akzeptanzkriterien
- Technische Funktion OK
- Konsistenz zum Designsystem
- A11y & rechtliche Vorgaben erfüllt

## Beispiel / Code
[content-elements-examples/date-picker.html](../content-elements-examples/date-picker.html)

```html
<!-- Minimales, valides HTML-Beispiel -->
<label for="date">Datum</label>
<input id="date" name="date" type="date">
```

Bewertung der Relevanz 2025

⭐⭐⭐⭐ Datumsauswahl bleibt komplex, aber unverzichtbar für Transaktionen.

## Anekdoten & Nerd-Zitate
Michael Crichton hätte wahrscheinlich eine komplette Katastrophensimulation um Date Picker gestrickt, nur um zu zeigen, wie viele Dinge gleichzeitig schiefgehen können. Douglas Coupland würde dagegen eine Slack-Konversation voller Insider-Gags daraus machen. Und irgendwo zwinkert eine alte RFC dazu, weil die Nerd-Fakten selten stillstehen.

## Best Practices
- A11y: Date Picker tastatur- und screenreader-freundlich gestalten.
- Performance: Date Picker nur laden, wenn der Kontext es wirklich braucht.
- Wartbarkeit: Entscheidungen zu Date Picker direkt neben dem Code dokumentieren.

## Fazit
Date Picker bleibt ein schönes Beispiel dafür, wie Content Elements-Elemente Geschichten erzählen können, wenn man sie ernst nimmt und trotzdem mit Humor betrachtet.
