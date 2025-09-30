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
Als ich heute Morgen die Kaffeemaschine anwarf, vibrierte das Handy wie ein Pager aus den Neunzigern. Im Editor blinkte Multi Step Wizard und ich hörte innerlich die Titelmusik von ‚Akte X‘. Irgendwo zwischen dem Duft von frisch gemahlenen Bohnen und dem leisen Summen des Lüfters entschied ich: Diese Notiz wird eine Liebeserklärung an Multi Step Wizard im Rahmen unserer Content Elements-Expedition.

## Technischer Kern
Multi Step Wizard ist einer dieser Bausteine, die niemand beachtet, bis sie fehlen. Wir haben das schmerzhaft gelernt, als ein Kunde das Feature ohne ARIA ausgeliefert hat und ein Feedback-Call zur Selbsthilfegruppe wurde. Seitdem legen wir das Mobile-Layout zuerst fest, tasten uns mit echten Fingern durch Buttons und Links und feiern jeden Moment, in dem der Screenreader flüssig vorliest. Ich halte mich an die Spezifikationen, aber ich erzähle sie wie Lagerfeuergeschichten: mit klaren HTML-Strukturen, sauberen States und einer Prise Humor. Und während ich daran denke, dass wir alle an halb fertigen Interfaces arbeiten, mahnt mich eine innere Stimme, jede Abhängigkeit dreimal zu prüfen.

### Originalnotizen
Ich lasse hier den historischen Steckbrief unangetastet; er ist mein Sicherheitsnetz, wenn das Storytelling überkocht:
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
- Ein Chatverlauf von letzter Woche: „Kannst du Multi Step Wizard mal schnell deaktivieren?“ – „Nur wenn du mir einen neuen Kaffee bringst.“ Ergebnis: Kaffee kam, Multi Step Wizard blieb.
- Merksatz: Technologie wird genau dann knifflig, wenn sie unsichtbar wirkt. Genau deshalb lassen wir Multi Step Wizard nicht aus der Doku verschwinden.
- Während der Build lief, las ich alte Projekt-Notizen und sah uns alle als Varianten derselben Crew, die versucht, Multi Step Wizard pixelweise in den Griff zu bekommen.
- In einer altundwillig.de-Sprachnachricht erzählte ich, wie ein Screenreader-User fragte: „Wo bin ich eigentlich?“ – dieser Satz hallt nach wie ein Drum-Solo.

## Best Practices
- **Altgeräte-Test:** Wenn Multi Step Wizard auf dem alten iPhone aus der Agentur-Schublade gut läuft, kannst du halbwegs ruhig schlafen.
- **Semantik rockt:** HTML-Struktur ernst nehmen, ARIA nur ergänzen. Alles andere ist wie ein Special-Effect ohne Plot.
- **Content-Strategie:** Besprich früh, welche Texte, Bilder oder Daten hier landen. Überraschungen mag höchstens der Cliffhanger im Serienfinale.
- **Fallbacks vorbereiten:** Offline, Low-Bandwidth, reduzierte Animation – Mobile First bedeutet, mit wenig auszukommen.
- **QA-Checklisten:** Hack dir eine Checkliste ins Repo, damit niemand vergisst, warum Multi Step Wizard existiert.

## Fazit
Multi Step Wizard bleibt ein stiller Held, der uns daran erinnert, warum wir Interfaces mit Herzblut bauen. Ich nehme mir vor, künftig noch radikaler auf echte Nutzungsszenarien zu hören – besonders, wenn das Monitoring ruhig ist. Accessibility, Mobile First, Humor: Diese drei Dinge halten den Laden zusammen.
