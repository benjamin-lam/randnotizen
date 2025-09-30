---
title: "Tabbed Interface: Randnotiz"
date: 2025-09-30
tags: [UI, Komponente, Webentwicklung]
excerpt: "Warum Tabbed Interface unsere Layouts-Notizen inspiriert."
layout: post
categories: [layouts]
slug: layouts-relevant-tabbed-interface
original_path: layouts/relevant/tabbed-interface.md
---

## Einleitung
Als ich heute Morgen die Kaffeemaschine anwarf, vibrierte das Handy wie ein Pager aus den Neunzigern. Im Editor blinkte Tabbed Interface und ich hörte innerlich die Titelmusik von ‚Akte X‘. Irgendwo zwischen dem Duft von frisch gemahlenen Bohnen und dem leisen Summen des Lüfters entschied ich: Diese Notiz wird eine Liebeserklärung an Tabbed Interface im Rahmen unserer Layouts (Relevant)-Expedition.

## Technischer Kern
Tabbed Interface ist einer dieser Bausteine, die niemand beachtet, bis sie fehlen. Wir haben das schmerzhaft gelernt, als ein Kunde das Feature ohne ARIA ausgeliefert hat und ein Feedback-Call zur Selbsthilfegruppe wurde. Seitdem legen wir das Mobile-Layout zuerst fest, tasten uns mit echten Fingern durch Buttons und Links und feiern jeden Moment, in dem der Screenreader flüssig vorliest. Ich halte mich an die Spezifikationen, aber ich erzähle sie wie Lagerfeuergeschichten: mit klaren HTML-Strukturen, sauberen States und einer Prise Humor. Und während ich daran denke, dass wir alle an halb fertigen Interfaces arbeiten, mahnt mich eine innere Stimme, jede Abhängigkeit dreimal zu prüfen.

### Originalnotizen
Und weil Fakten auch bei aller Nostalgie zählen, folgt hier das unveränderte Archiv, das unsere Entscheidungen stützt:
# Layout: Tabbed Interface

## Beschreibung
Inhalte werden in Reitern organisiert und lassen sich per Tabs wechseln. Ideal für vergleichbare Inhalte, Produktdetails oder komprimierte Informationsbereiche.

## Warum dieses Layout?
- Strukturiert komplexe Inhalte übersichtlich.
- Reduziert Scrollwege und zeigt relevante Informationen kontextuell.
- Versteckt Inhalte hinter Interaktion, daher gute Kommunikation nötig.

## Anforderungen & Besonderheiten
- **Responsiveness:** Tabs sind horizontal oder in Dropdowns/Accordions überführbar.
- **Accessibility:** WAI-ARIA Tabs-Pattern mit role=tablist, tab und aria-controls nutzen.
- **SEO:** Wichtige Inhalte bleiben crawlbar und werden nicht verzögert nachgeladen.
- **Design-Guidelines:** Aktiver Tab klar markiert, konsistente Abstände und Hover/Fokus-Zustände.

## Umsetzung – Technische Leitplanken
- **Mobile First:** Tabs stapeln oder in ein horizontales Scroll-Menü wechseln.
- **Accessibility:** Keyboard-Steuerung mit Pfeiltasten, Home/End und Fokus-Management implementieren.
- **SEO:** Tab-Inhalte im DOM belassen, optional lazy load sekundärer Ressourcen.
- **Best Practices:** ARIA-Attribute korrekt setzen, Fokus sichtbar halten, State in URL optional spiegeln

## Checkliste
- [ ] Tab-Reihenfolge ist logisch und beschriftet.
- [ ] Fokus springt beim Wechsel zum aktiven Panel.
- [ ] Mobile Darstellung bleibt bedienbar.
- [ ] Accessibility- und Performance-Tests abgeschlossen.

## Abhängigkeiten / Überschneidungen
- Tabs-Komponente
- State-Management oder Router

## Akzeptanzkriterien
- Tabs erfüllen WAI-ARIA-Authoring-Practices.
- Aktives Panel wird beim Wechsel sofort sichtbar.
- Screenreader kündigen Tab-Status korrekt an.

## Beispiel / Code
```html
<div class="tabs" role="tablist">
  <button role="tab" aria-controls="panel-1" aria-selected="true">Tab 1</button>
  <button role="tab" aria-controls="panel-2">Tab 2</button>
</div>
<section id="panel-1" role="tabpanel">Inhalt 1</section>
<section id="panel-2" role="tabpanel" hidden>Inhalt 2</section>
```

Bewertung der Relevanz 2025

⭐⭐⭐⭐⭐ Beliebtes Muster zur Verdichtung thematisch verwandter Inhalte.

## Anekdoten & Nerd-Zitate
- In meinen Notizen steht noch der Satz: „Tabbed Interface riecht nach Filterkaffee und Ticket-Alarm.“ Das war der Abend vor dem Launch.
- Wir haben uns selbst beobachtet, wie wir mit Taschenlampen (a.k.a. Gerätepark) durch die QA-Nacht stapfen.
- Niemand von außen textet für uns, aber unsere Slack-Emojis halten uns wach, wenn wir wieder Mobile-Bugs jagen.
- Eine Kollegin sagte: „Accessibility fühlt sich an wie barfuß laufen – du merkst jeden Stein.“ Seitdem prüfe ich Tabbed Interface ohne Maus.

## Best Practices
- **Altgeräte-Test:** Wenn Tabbed Interface auf dem alten iPhone aus der Agentur-Schublade gut läuft, kannst du halbwegs ruhig schlafen.
- **Semantik rockt:** HTML-Struktur ernst nehmen, ARIA nur ergänzen. Alles andere ist wie ein Special-Effect ohne Plot.
- **Content-Strategie:** Besprich früh, welche Texte, Bilder oder Daten hier landen. Überraschungen mag höchstens der Cliffhanger im Serienfinale.
- **Fallbacks vorbereiten:** Offline, Low-Bandwidth, reduzierte Animation – Mobile First bedeutet, mit wenig auszukommen.
- **QA-Checklisten:** Hack dir eine Checkliste ins Repo, damit niemand vergisst, warum Tabbed Interface existiert.

## Fazit
Wenn ich den Tag Revue passieren lasse, sehe ich Tabbed Interface wie eine verlässliche Nebenfigur, die dem Plot erst Sinn gibt. Wir haben gelernt, dass Resilienz aus Routine entsteht: frühe Tests, offene Kommunikation, echte Devices. Beim nächsten Sprint will ich die Kopplung zu Datenquellen sauberer aufsetzen und weiter beweisen, dass Barrierefreiheit kein Extra ist, sondern Haltung.
