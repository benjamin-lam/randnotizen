---
title: "Search: Randnotiz"
date: 2025-09-30
tags: [UI, Komponente, Webentwicklung]
excerpt: "Warum Search unsere Content Elements-Notizen inspiriert."
layout: post
categories: [content-elements]
slug: content-elements-search
original_path: content-elements/search.md
---

## Einleitung
Zwischen Straßenbahn, Einkaufskorb und kurzen Pausen auf der Parkbank tippte ich die ersten Sätze ins Smartphone. Search stand noch warm aus dem letzten Deployment im Raum, und klar war: Heute erzählen wir diese Komponente so, wie altundwillig.de über große und kleine Webdramen schreibt – mitten im Alltag unseres Content Elements-Systems.

## Technischer Kern
Search ist einer dieser Bausteine, die niemand beachtet, bis sie fehlen. Wir haben das schmerzhaft gelernt, als ein Kunde das Feature ohne ARIA ausgeliefert hat und ein Feedback-Call zur Selbsthilfegruppe wurde. Seitdem legen wir das Mobile-Layout zuerst fest, tasten uns mit echten Fingern durch Buttons und Links und feiern jeden Moment, in dem der Screenreader flüssig vorliest. Ich halte mich an die Spezifikationen, aber ich erzähle sie wie Lagerfeuergeschichten: mit klaren HTML-Strukturen, sauberen States und einer Prise Humor. Und während ich daran denke, dass wir alle an halb fertigen Interfaces arbeiten, mahnt mich eine innere Stimme, jede Abhängigkeit dreimal zu prüfen.

### Originalnotizen
Bevor wir uns im Meme-Verhau verlieren, bleiben die originalen Notizen unbeschnitten erhalten:
# Content-Element: Search

## Beschreibung
Suchfeld mit optionaler Autosuggest-Funktion.

## Warum dieses Element?
- Produktsuche in Shops oder Verzeichnissen.
- Suche in Knowledge-Bases oder Blogs.
- Trade-off: Schlechte Ergebnisse oder langsame Suggests schaden Vertrauen.

## Anforderungen & Besonderheiten
- **Responsiveness:** Eingabefeld volle Breite, Suggest-Panel adaptiv.
- **Accessibility:** `aria-expanded`, `aria-controls`, Tastaturnavigation im Suggest.
- **SEO:** Interne Suche kann für Site-Search-Snippets genutzt werden.
- **Design-Guidelines:** Lupe-Icon, deutlicher Fokus, Loading-Indicator für Suggests.
- **Rechtliches:** Suchlogs datenschutzkonform speichern und anonymisieren.

## Umsetzung – Technische Leitplanken
- **Mobile First:** Fullscreen-Suche mit On-Screen-Keyboard, History-Vorschläge.
- **Accessibility:** Ergebnisse in `role=listbox`, Items mit `role=option` versehen.
- **SEO:** Suchseiten indexieren oder bewusst ausschließen (noindex).
- **Best Practices:**
  - Fehlertoleranz (Fuzzy Search) anbieten.
  - Analytics zur Suchnutzung integrieren.
  - Leere Ergebnisse mit Hilfestellungen versehen.

## Checkliste
- [ ] Darstellung auf allen Breakpoints geprüft
- [ ] Barrierefreiheit (Fokus, ARIA, Kontrast) OK
- [ ] Semantik korrekt (HTML)
- [ ] Performance optimiert (Lazyload/Kompression)

## Abhängigkeiten / Überschneidungen
- Search-API, Analytics, Autosuggest-Service

## Akzeptanzkriterien
- Technische Funktion OK
- Konsistenz zum Designsystem
- A11y & rechtliche Vorgaben erfüllt

## Beispiel / Code
[content-elements-examples/search.html](../content-elements-examples/search.html)

```html
<!-- Minimales, valides HTML-Beispiel -->
<form role="search">
  <label for="search" class="sr-only">Suche</label>
  <input id="search" name="q" type="search" placeholder="Suche">
  <button type="submit">Suchen</button>
</form>
```

Bewertung der Relevanz 2025

⭐⭐⭐⭐⭐ Suche bleibt zentral für Nutzerzufriedenheit und Conversions.

## Anekdoten & Nerd-Zitate
- Ein Chatverlauf von letzter Woche: „Kannst du Search mal schnell deaktivieren?“ – „Nur wenn du mir einen neuen Kaffee bringst.“ Ergebnis: Kaffee kam, Search blieb.
- Merksatz: Technologie wird genau dann knifflig, wenn sie unsichtbar wirkt. Genau deshalb lassen wir Search nicht aus der Doku verschwinden.
- Während der Build lief, las ich alte Projekt-Notizen und sah uns alle als Varianten derselben Crew, die versucht, Search pixelweise in den Griff zu bekommen.
- In einer altundwillig.de-Sprachnachricht erzählte ich, wie ein Screenreader-User fragte: „Wo bin ich eigentlich?“ – dieser Satz hallt nach wie ein Drum-Solo.

## Best Practices
- **Accessibility lebt von Ritualen:** Prüfe Search mit Tastatur und Screenreader, bevor du überhaupt an Pixel-Politur denkst. Deine künftige Selbstachtung wird es dir danken.
- **Mobile First aus Überzeugung:** Beginne mit dem kleinsten Viewport und frage dich ernsthaft, ob du das Element auch im U-Bahn-Gedränge bedienen könntest.
- **Performance mit Hausverstand:** Lade nur, was wirklich gebraucht wird, sonst fühlt sich Search an wie ein Buffering-Screen aus der Modem-Ära.
- **Dokumentation neben dem Code:** Schreib dir dazu, warum Entscheidungen gefallen sind; sonst fragst du dich in drei Monaten selbst, was du damit meintest.
- **Team-Sync:** Stell sicher, dass Design, Content und Dev dieselben Erwartungen haben – sonst erzählt jeder eine andere Story über Search.

## Fazit
Zum Schluss fühlt sich Search an wie ein gut geölter Plattenspieler: nicht prahlerisch, aber unverzichtbar. Wir haben wieder gelernt, dass Disziplin bei Breakpoints und `aria`-Attributen genau der Unterschied zwischen Frust und Flow ist. Beim nächsten Rollout gönne ich mir mehr Zeit für User-Feedback, bevor der nächste Sturm aus Edge Cases anklopft.
