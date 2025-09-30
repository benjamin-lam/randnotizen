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
Zwischen Straßenbahn, Supermarktkasse und Handy-Display schrieb ich die ersten Zeilen auf dem Smartphone, während in Bremen der Duft von frisch gemahlenem Kaffee durch die Luft zog. Three Columns blinkte mir entgegen wie ein Mixtape aus einer vergessenen Schublade, und klar war: Heute bekommt Three Columns die große Bühne in unserem Layouts (Deprecated)-Tagebuch.

## Technischer Kern
Technisch gesehen sitzt Three Columns genau an der Schnittstelle zwischen Ordnung und Emotion. Ich erinnere mich noch, wie wir im letzten Quartal eine Variante shippten, die auf dem Testgerät butterweich wirkte, auf einem alten Android aber ruckelte wie ein VHS-Band. Seitdem ist Mobile First mein Morgenritual; ich starte immer mit dem kleinsten Screen. Accessibility hält mich ehrlich: Ohne klare Fokuszustände oder Transkripte wird aus Eleganz sofort Chaos, und genau dann ruft jemand aus dem Support an. Die Originalnotizen unten dienen mir als Checkliste, doch meine heimliche Regel lautet: Wir alle tüfteln in unseren Kellern an der Zukunft. In diesem Keller sorge ich dafür, dass Three Columns stabil bleibt, selbst wenn ein Sturm aus Edge Cases tobt.

### Originalnotizen
Unterhalb dieser Zeile wohnt das Rohmaterial – nach wie vor mein Truthahnthermometer für saubere Implementierung:
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
- Wir haben einmal eine interne Nostalgie-Matrix gebaut, um Three Columns gegen Erinnerungsglitzer zu testen. Ergebnis: 42 Prozent erinnern an MP3-Player aus 2003.
- Mein Lieblings-Feedback kam aus dem Support: „Endlich muss ich niemandem mehr erklären, wo Three Columns versteckt ist.“
- Wenn das Monitoring blinkt, fühlt es sich kurz wie im Katastrophenfilm an – diesmal blieb der Alarm still.
- Altundwillig.de hätte es so zusammengefasst: „Mach es benutzbar oder lass es bleiben.“

## Best Practices
- **Altgeräte-Test:** Wenn Three Columns auf dem alten iPhone aus der Agentur-Schublade gut läuft, kannst du halbwegs ruhig schlafen.
- **Semantik rockt:** HTML-Struktur ernst nehmen, ARIA nur ergänzen. Alles andere ist wie ein Special-Effect ohne Plot.
- **Content-Strategie:** Besprich früh, welche Texte, Bilder oder Daten hier landen. Überraschungen mag höchstens der Cliffhanger im Serienfinale.
- **Fallbacks vorbereiten:** Offline, Low-Bandwidth, reduzierte Animation – Mobile First bedeutet, mit wenig auszukommen.
- **QA-Checklisten:** Hack dir eine Checkliste ins Repo, damit niemand vergisst, warum Three Columns existiert.

## Fazit
Wenn ich den Tag Revue passieren lasse, sehe ich Three Columns wie eine verlässliche Nebenfigur, die dem Plot erst Sinn gibt. Wir haben gelernt, dass Resilienz aus Routine entsteht: frühe Tests, offene Kommunikation, echte Devices. Beim nächsten Sprint will ich die Kopplung zu Datenquellen sauberer aufsetzen und weiter beweisen, dass Barrierefreiheit kein Extra ist, sondern Haltung.
