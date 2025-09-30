---
title: "Share Buttons: Randnotiz"
date: 2025-09-30
tags: [UI, Komponente, Webentwicklung]
excerpt: "Warum Share Buttons unsere Content Elements-Notizen inspiriert."
layout: post
categories: [content-elements]
slug: content-elements-share-buttons
original_path: content-elements/share-buttons.md
---

## Einleitung
Es fühlt sich an wie ein Fund in einer verstaubten Prototyp-Schublade: **Share Buttons** passte heute perfekt in unsere Content Elements-Gedanken, und plötzlich roch der Raum nach Whiteboard-Markern und frisch gebrühtem Kaffee.

## Technischer Kern
Technisch betrachtet verlangt Share Buttons nach klaren Leitplanken. Ich habe die ursprüngliche Beschreibung unten angeheftet und mit Kommentaren versehen, damit der Transfer in das neue Blog sichtbar bleibt.

### Originalnotizen
# Content-Element: Share Buttons

## Beschreibung
Buttons zum Teilen von Inhalten in sozialen Netzwerken oder per Link.

## Warum dieses Element?
- Blogbeiträge oder Produkte schnell teilen lassen.
- Eventseiten viral verbreiten.
- Trade-off: Zu viele Netzwerke verlangsamen die Seite und verwirren Nutzer.

## Anforderungen & Besonderheiten
- **Responsiveness:** Icons in flexiblen Layouts, Touch-Ziele ausreichend groß.
- **Accessibility:** Buttons beschriften (`aria-label`), Fokus sichtbar, Tastaturbedienung.
- **SEO:** Indirekter Effekt durch erhöhte Sichtbarkeit und Backlinks.
- **Design-Guidelines:** Markenfarben der Netzwerke oder neutrale Icons, Hover-/Focus-States.
- **Rechtliches:** Social Plugins datenschutzkonform integrieren (2-Klick-Lösung).

## Umsetzung – Technische Leitplanken
- **Mobile First:** Horizontale Scroll-Leiste oder Dropdown für zusätzliche Optionen.
- **Accessibility:** Teilen-Dialog per Tastatur bedienbar, Clipboard-Option anbieten.
- **SEO:** UTM-Parameter konsistent setzen, Sharing-Meta-Tags (OG, Twitter Cards) pflegen.
- **Best Practices:**
  - Nur relevante Netzwerke anzeigen.
  - Copy-Link-Funktion anbieten.
  - Lade Social-Skripte erst nach Interaktion.

## Checkliste
- [ ] Darstellung auf allen Breakpoints geprüft
- [ ] Barrierefreiheit (Fokus, ARIA, Kontrast) OK
- [ ] Semantik korrekt (HTML)
- [ ] Performance optimiert (Lazyload/Kompression)

## Abhängigkeiten / Überschneidungen
- Social APIs, Consent-Tool, Analytics

## Akzeptanzkriterien
- Technische Funktion OK
- Konsistenz zum Designsystem
- A11y & rechtliche Vorgaben erfüllt

## Beispiel / Code
[content-elements-examples/share-buttons.html](../content-elements-examples/share-buttons.html)

```html
<!-- Minimales, valides HTML-Beispiel -->
<div class="share">
  <button type="button" aria-label="Bei LinkedIn teilen">LinkedIn</button>
  <button type="button" aria-label="Link kopieren">Link kopieren</button>
</div>
```

Bewertung der Relevanz 2025

⭐⭐⭐⭐ Teilen-Funktionen bleiben wichtig, müssen aber datenschutzfreundlich umgesetzt werden.

## Anekdoten & Nerd-Zitate
Michael Crichton hätte wahrscheinlich eine komplette Katastrophensimulation um Share Buttons gestrickt, nur um zu zeigen, wie viele Dinge gleichzeitig schiefgehen können. Douglas Coupland würde dagegen eine Slack-Konversation voller Insider-Gags daraus machen. Und irgendwo zwinkert eine alte RFC dazu, weil die Nerd-Fakten selten stillstehen.

## Best Practices
- A11y: Share Buttons tastatur- und screenreader-freundlich gestalten.
- Performance: Share Buttons nur laden, wenn der Kontext es wirklich braucht.
- Wartbarkeit: Entscheidungen zu Share Buttons direkt neben dem Code dokumentieren.

## Fazit
Share Buttons bleibt ein schönes Beispiel dafür, wie Content Elements-Elemente Geschichten erzählen können, wenn man sie ernst nimmt und trotzdem mit Humor betrachtet.
