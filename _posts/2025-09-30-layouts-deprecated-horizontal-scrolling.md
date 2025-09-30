---
title: "Horizontal Scrolling: Randnotiz"
date: 2025-09-30
tags: [UI, Komponente, Webentwicklung]
excerpt: "Warum Horizontal Scrolling unsere Layouts-Notizen inspiriert."
layout: post
categories: [layouts]
slug: layouts-deprecated-horizontal-scrolling
original_path: layouts/deprecated/horizontal-scrolling.md
---

## Einleitung
Zwischen Straßenbahn, Supermarktkasse und Handy-Display schrieb ich die ersten Zeilen auf dem Smartphone, während in Bremen der Duft von frisch gemahlenem Kaffee durch die Luft zog. Horizontal Scrolling blinkte mir entgegen wie ein Mixtape aus einer vergessenen Schublade, und klar war: Heute bekommt Horizontal Scrolling die große Bühne in unserem Layouts (Deprecated)-Tagebuch.

## Technischer Kern
Jede Roadmap hat ihren heimlichen Bossfight, und bei uns hieß der im letzten Sprint Horizontal Scrolling. Die Doku unten ist die nüchterne Wahrheit, aber die eigentliche Arbeit passierte zwischen Koffeinflash und Pixel-Poesie. Ich habe die Komponente auf einem ausgeleierten iPhone 8 getestet, während ein Kollege Accessibility-Checks über VoiceOver machte. Mobile First bedeutet hier, das Layout zusammenzufalten, bis es auch mit einer Hand bedienbar bleibt. Accessibility heißt, dass niemand fragen muss: „Wo bin ich hier?“ Genau dann ploppte eine Slack-Nachricht auf, die mich daran erinnerte, dass wir alle Prototypen unserer eigenen Ideen sind – und im Kopf jubelte das innere Regieteam, als wir den letzten Bug fixen konnten.

### Originalnotizen
Ich lasse hier den historischen Steckbrief unangetastet; er ist mein Sicherheitsnetz, wenn das Storytelling überkocht:
# Layout: Horizontal Scrolling Layout

## Beschreibung
Ein Layout mit horizontalem Scrollen als primäre Navigationsachse wirkt unnatürlich und ist auf mobilen Geräten schwer steuerbar.

## Warum dieses Layout?
- Kann besondere Storytelling-Experiences liefern.
- Setzt visuelle Highlights in Szene.
- Verursacht UX-Probleme bei Scroll-Gesten und Orientierung.

## Anforderungen & Besonderheiten
- **Responsiveness:** Klare Scroll-Hinweise, horizontale Scrollbereiche mit Touch-Unterstützung.
- **Accessibility:** Alternativen für Tastatur und Screenreader bereitstellen, wheel-Events bedacht einsetzen.
- **SEO:** Wichtige Inhalte auch vertikal zugänglich machen.
- **Design-Guidelines:** Deutliche Pfeile, Pagination oder Snap-Punkte, um Orientierung zu sichern.

## Umsetzung – Technische Leitplanken
- **Mobile First:** Standard-Layouts bevorzugen und horizontale Scrollstrecken nur optional einbinden.
- **Accessibility:** Scroll-Mapping auf Trackpad/Wheel nur vorsichtig nutzen.
- **SEO:** Vertikale Alternativansicht oder Jump-Links bereitstellen.
- **Best Practices:** Scroll-Hints anzeigen, Snapping optional, Fallback auf vertikale Liste

## Checkliste
- [ ] Scroll-Hinweise sind sichtbar.
- [ ] Tastaturbedienung möglich.
- [ ] Vertikale Alternative vorhanden.
- [ ] A11y- und Performance-Check dokumentiert.

## Abhängigkeiten / Überschneidungen
- Scroll- und Animation-Utilities
- Fallback-Layouts

## Akzeptanzkriterien
- Nutzer verstehen Interaktion ohne Tutorial.
- Screenreader erhalten linearen Alternativzugang.
- Stakeholder akzeptieren Einsatz nur in Spezialfällen.

## Beispiel / Code
```html
<section class="horizontal-scroll" aria-label="Galerie">
  <div class="scroll-track">…</div>
</section>
```

> ⚠️ Deprecated: Nicht mehr empfohlen für Mobile-First-Designs (nur zu Dokumentationszwecken).

Bewertung der Relevanz 2025

⭐⭐☆☆☆ Nur für spezielle Storytelling-Experimente erhalten.

## Anekdoten & Nerd-Zitate
- Wir haben einmal eine interne Nostalgie-Matrix gebaut, um Horizontal Scrolling gegen Erinnerungsglitzer zu testen. Ergebnis: 42 Prozent erinnern an MP3-Player aus 2003.
- Mein Lieblings-Feedback kam aus dem Support: „Endlich muss ich niemandem mehr erklären, wo Horizontal Scrolling versteckt ist.“
- Wenn das Monitoring blinkt, fühlt es sich kurz wie im Katastrophenfilm an – diesmal blieb der Alarm still.
- Altundwillig.de hätte es so zusammengefasst: „Mach es benutzbar oder lass es bleiben.“

## Best Practices
- **Design Tokens nutzen:** Lass Horizontal Scrolling aus dem Designsystem atmen, nicht aus spontanen HEX-Codes.
- **Keyboard-Liebe:** Jede Interaktion muss per Tab erreichbar sein – ein Modal ohne Escape ist ein Support-Ticket in spe.
- **Performance messen:** Lighthouse, WebPageTest, was immer du hast – Hauptsache du kennst deine Zahlen.
- **Copy & Microcopy:** Stimme dich mit Content ab, damit die Sprache genauso flüssig ist wie das Interface.
- **Post-Launch-Retros:** Plane von Anfang an ein, die Komponente nach den ersten echten Nutzerkontakten anzupassen.

## Fazit
Wenn ich den Tag Revue passieren lasse, sehe ich Horizontal Scrolling wie eine verlässliche Nebenfigur, die dem Plot erst Sinn gibt. Wir haben gelernt, dass Resilienz aus Routine entsteht: frühe Tests, offene Kommunikation, echte Devices. Beim nächsten Sprint will ich die Kopplung zu Datenquellen sauberer aufsetzen und weiter beweisen, dass Barrierefreiheit kein Extra ist, sondern Haltung.
