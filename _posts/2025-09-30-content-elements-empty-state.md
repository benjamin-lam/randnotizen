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
Zwischen Straßenbahn, Supermarktkasse und Handy-Display schrieb ich die ersten Zeilen auf dem Smartphone, während in Bremen der Duft von frisch gemahlenem Kaffee durch die Luft zog. Empty State blinkte mir entgegen wie ein Mixtape aus einer vergessenen Schublade, und klar war: Heute bekommt Empty State die große Bühne in unserem Content Elements-Tagebuch.

## Technischer Kern
Empty State ist einer dieser Bausteine, die niemand beachtet, bis sie fehlen. Wir haben das schmerzhaft gelernt, als ein Kunde das Feature ohne ARIA ausgeliefert hat und ein Feedback-Call zur Selbsthilfegruppe wurde. Seitdem legen wir das Mobile-Layout zuerst fest, tasten uns mit echten Fingern durch Buttons und Links und feiern jeden Moment, in dem der Screenreader flüssig vorliest. Ich halte mich an die Spezifikationen, aber ich erzähle sie wie Lagerfeuergeschichten: mit klaren HTML-Strukturen, sauberen States und einer Prise Humor. Und während ich daran denke, dass wir alle an halb fertigen Interfaces arbeiten, mahnt mich eine innere Stimme, jede Abhängigkeit dreimal zu prüfen.

### Originalnotizen
Unterhalb dieser Zeile wohnt das Rohmaterial – nach wie vor mein Truthahnthermometer für saubere Implementierung:
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
- Wir haben einmal eine interne Nostalgie-Matrix gebaut, um Empty State gegen Erinnerungsglitzer zu testen. Ergebnis: 42 Prozent erinnern an MP3-Player aus 2003.
- Mein Lieblings-Feedback kam aus dem Support: „Endlich muss ich niemandem mehr erklären, wo Empty State versteckt ist.“
- Wenn das Monitoring blinkt, fühlt es sich kurz wie im Katastrophenfilm an – diesmal blieb der Alarm still.
- Altundwillig.de hätte es so zusammengefasst: „Mach es benutzbar oder lass es bleiben.“

## Best Practices
- **Design Tokens nutzen:** Lass Empty State aus dem Designsystem atmen, nicht aus spontanen HEX-Codes.
- **Keyboard-Liebe:** Jede Interaktion muss per Tab erreichbar sein – ein Modal ohne Escape ist ein Support-Ticket in spe.
- **Performance messen:** Lighthouse, WebPageTest, was immer du hast – Hauptsache du kennst deine Zahlen.
- **Copy & Microcopy:** Stimme dich mit Content ab, damit die Sprache genauso flüssig ist wie das Interface.
- **Post-Launch-Retros:** Plane von Anfang an ein, die Komponente nach den ersten echten Nutzerkontakten anzupassen.

## Fazit
Zum Schluss fühlt sich Empty State an wie ein gut geölter Plattenspieler: nicht prahlerisch, aber unverzichtbar. Wir haben wieder gelernt, dass Disziplin bei Breakpoints und `aria`-Attributen genau der Unterschied zwischen Frust und Flow ist. Beim nächsten Rollout gönne ich mir mehr Zeit für User-Feedback, bevor der nächste Sturm aus Edge Cases anklopft.
