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
Zwischen Straßenbahn, Supermarktkasse und Handy-Display schrieb ich die ersten Zeilen auf dem Smartphone, während in Bremen der Duft von frisch gemahlenem Kaffee durch die Luft zog. Tooltip blinkte mir entgegen wie ein Mixtape aus einer vergessenen Schublade, und klar war: Heute bekommt Tooltip die große Bühne in unserem Content Elements-Tagebuch.

## Technischer Kern
Tooltip ist einer dieser Bausteine, die niemand beachtet, bis sie fehlen. Wir haben das schmerzhaft gelernt, als ein Kunde das Feature ohne ARIA ausgeliefert hat und ein Feedback-Call zur Selbsthilfegruppe wurde. Seitdem legen wir das Mobile-Layout zuerst fest, tasten uns mit echten Fingern durch Buttons und Links und feiern jeden Moment, in dem der Screenreader flüssig vorliest. Ich halte mich an die Spezifikationen, aber ich erzähle sie wie Lagerfeuergeschichten: mit klaren HTML-Strukturen, sauberen States und einer Prise Humor. Und während ich daran denke, dass wir alle an halb fertigen Interfaces arbeiten, mahnt mich eine innere Stimme, jede Abhängigkeit dreimal zu prüfen.

### Originalnotizen
Ich lasse hier den historischen Steckbrief unangetastet; er ist mein Sicherheitsnetz, wenn das Storytelling überkocht:
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
- Wir haben einmal eine interne Nostalgie-Matrix gebaut, um Tooltip gegen Erinnerungsglitzer zu testen. Ergebnis: 42 Prozent erinnern an MP3-Player aus 2003.
- Mein Lieblings-Feedback kam aus dem Support: „Endlich muss ich niemandem mehr erklären, wo Tooltip versteckt ist.“
- Wenn das Monitoring blinkt, fühlt es sich kurz wie im Katastrophenfilm an – diesmal blieb der Alarm still.
- Altundwillig.de hätte es so zusammengefasst: „Mach es benutzbar oder lass es bleiben.“

## Best Practices
- **Design Tokens nutzen:** Lass Tooltip aus dem Designsystem atmen, nicht aus spontanen HEX-Codes.
- **Keyboard-Liebe:** Jede Interaktion muss per Tab erreichbar sein – ein Modal ohne Escape ist ein Support-Ticket in spe.
- **Performance messen:** Lighthouse, WebPageTest, was immer du hast – Hauptsache du kennst deine Zahlen.
- **Copy & Microcopy:** Stimme dich mit Content ab, damit die Sprache genauso flüssig ist wie das Interface.
- **Post-Launch-Retros:** Plane von Anfang an ein, die Komponente nach den ersten echten Nutzerkontakten anzupassen.

## Fazit
Tooltip ist am Ende wie eine Reihe kleiner Laternen im Tunnel: unscheinbar, aber ohne sie stolpern wir. Ich nehme aus diesem Durchgang mit, dass Mobile First und Accessibility keine Kapitelüberschriften sind, sondern Bauchentscheidungen für Menschen. Beim nächsten Mal baue ich noch früher Tests in den Workflow ein – und trinke meinen Kaffee vermutlich etwas langsamer.
