---
title: "Three Columns: Randnotiz"
date: 2025-09-30
tags: [UI, Komponente, Webentwicklung]
excerpt: "Warum Three Columns unsere Layouts-Notizen inspiriert."
layout: post
categories: [layouts]
slug: layouts-deprecated-three-columns
original_path: layouts/deprecated/three-columns.md
---

## Einleitung
Es fühlt sich an wie ein Fund in einer verstaubten Prototyp-Schublade: **Three Columns** passte heute perfekt in unsere Layouts-Gedanken, und plötzlich roch der Raum nach Whiteboard-Markern und frisch gebrühtem Kaffee.

## Technischer Kern
Technisch betrachtet verlangt Three Columns nach klaren Leitplanken. Ich habe die ursprüngliche Beschreibung unten angeheftet und mit Kommentaren versehen, damit der Transfer in das neue Blog sichtbar bleibt.

### Originalnotizen
# Layout: Three Columns

## Beschreibung
Drei gleichbreite Spalten waren früher verbreitet, wirken heute aber überladen und sind mobil schwer nutzbar.

## Warum dieses Layout?
- Bietet viel Platz für Navigation, Inhalt und Zusatzmodule.
- Kann historische Portale abbilden.
- Auf mobilen Geräten entsteht häufig Scroll- und Priorisierungschaos.

## Anforderungen & Besonderheiten
- **Responsiveness:** Spalten müssen auf mobilen Geräten komplett gestapelt werden.
- **Accessibility:** Inhaltliche Priorisierung klar kommunizieren, Reihenfolge logisch halten.
- **SEO:** Wichtige Inhalte im DOM nach vorn ziehen, damit sie nicht von Sidebars verdrängt werden.
- **Design-Guidelines:** Große Weißräume zur Entzerrung nutzen, klare Typo-Hierarchie.

## Umsetzung – Technische Leitplanken
- **Mobile First:** Lieber ein- bis zweispaltige Alternativen wählen und Sidebars als Off-Canvas abbilden.
- **Accessibility:** DOM-Struktur nicht für rein visuelle Zwecke verbiegen.
- **SEO:** Hauptinhalt deutlich kennzeichnen.
- **Best Practices:** Spalten priorisieren, Off-Canvas prüfen, Reduzierte Inhalte bereitstellen

## Checkliste
- [ ] Keine horizontale Scrollbar entsteht.
- [ ] Reihenfolge der Spalten logisch.
- [ ] Sidebars enthalten nur unbedingt nötige Inhalte.
- [ ] A11y- und Performance-Check dokumentiert.

## Abhängigkeiten / Überschneidungen
- Historische Portallayouts
- Legacy-Navigationsmodule

## Akzeptanzkriterien
- Mobile Stack funktioniert ohne Layoutbruch.
- Screenreader erkennen Hauptinhalt zuerst.
- Stakeholder akzeptieren Ersatz- oder Migrationsplan.

## Beispiel / Code
```html
<section class="grid md:grid-cols-3 gap-4">
  <div>Spalte 1</div>
  <div>Spalte 2</div>
  <div>Spalte 3</div>
</section>
```

> ⚠️ Deprecated: Nicht mehr empfohlen für Mobile-First-Designs (nur zu Dokumentationszwecken).

Bewertung der Relevanz 2025

⭐⭐☆☆☆ Nur noch zur Pflege historischer Portale dokumentiert.

## Anekdoten & Nerd-Zitate
Michael Crichton hätte wahrscheinlich eine komplette Katastrophensimulation um Three Columns gestrickt, nur um zu zeigen, wie viele Dinge gleichzeitig schiefgehen können. Douglas Coupland würde dagegen eine Slack-Konversation voller Insider-Gags daraus machen. Und irgendwo zwinkert eine alte RFC dazu, weil die Nerd-Fakten selten stillstehen.

## Best Practices
- A11y: Three Columns tastatur- und screenreader-freundlich gestalten.
- Performance: Three Columns nur laden, wenn der Kontext es wirklich braucht.
- Wartbarkeit: Entscheidungen zu Three Columns direkt neben dem Code dokumentieren.

## Fazit
Three Columns bleibt ein schönes Beispiel dafür, wie Layouts-Elemente Geschichten erzählen können, wenn man sie ernst nimmt und trotzdem mit Humor betrachtet.
