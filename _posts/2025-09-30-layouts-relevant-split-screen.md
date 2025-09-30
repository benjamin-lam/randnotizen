---
title: "Split Screen: Randnotiz"
date: 2025-09-30
tags: [UI, Komponente, Webentwicklung]
excerpt: "Warum Split Screen unsere Layouts-Notizen inspiriert."
layout: post
categories: [layouts]
slug: layouts-relevant-split-screen
original_path: layouts/relevant/split-screen.md
---

## Einleitung
Als ich heute Morgen die Kaffeemaschine anwarf, vibrierte das Handy wie ein Pager aus den Neunzigern. Im Editor blinkte Split Screen und ich hörte innerlich die Titelmusik von ‚Akte X‘. Irgendwo zwischen dem Duft von frisch gemahlenen Bohnen und dem leisen Summen des Lüfters entschied ich: Diese Notiz wird eine Liebeserklärung an Split Screen im Rahmen unserer Layouts (Relevant)-Expedition.

## Technischer Kern
Technisch gesehen sitzt Split Screen genau an der Schnittstelle zwischen Ordnung und Emotion. Ich erinnere mich noch, wie wir im letzten Quartal eine Variante shippten, die auf dem Testgerät butterweich wirkte, auf einem alten Android aber ruckelte wie ein VHS-Band. Seitdem ist Mobile First mein Morgenritual; ich starte immer mit dem kleinsten Screen. Accessibility hält mich ehrlich: Ohne klare Fokuszustände oder Transkripte wird aus Eleganz sofort Chaos, und genau dann ruft jemand aus dem Support an. Die Originalnotizen unten dienen mir als Checkliste, doch meine heimliche Regel lautet: Wir alle tüfteln in unseren Kellern an der Zukunft. In diesem Keller sorge ich dafür, dass Split Screen stabil bleibt, selbst wenn ein Sturm aus Edge Cases tobt.

### Originalnotizen
Und weil Fakten auch bei aller Nostalgie zählen, folgt hier das unveränderte Archiv, das unsere Entscheidungen stützt:
# Layout: Split Screen

## Beschreibung
Zwei Bereiche teilen sich die Breite, häufig Text und Bild oder ein Formular neben einer Vorschau. Ideal für Produktvorstellungen, Kampagnen oder Vergleichsdarstellungen.

## Warum dieses Layout?
- Erzeugt einen starken visuellen Kontrast zwischen Inhalt und Medien.
- Eignet sich für Storytelling mit parallelen Informationssträngen.
- Erfordert auf kleinen Screens sauberes Stapeln, damit nichts verloren geht.

## Anforderungen & Besonderheiten
- **Responsiveness:** Bricht auf mobilen Geräten in eine vertikale Reihenfolge um.
- **Accessibility:** DOM-Reihenfolge folgt der gewünschten Leselogik, Bilder mit aussagekräftigen Alternativtexten.
- **SEO:** Klare Überschriftenstruktur und relevante Meta-Texte für beide Bereiche.
- **Design-Guidelines:** Ausreichende Abstände, harmonische Typografie und abgestimmte Bildkomposition.

## Umsetzung – Technische Leitplanken
- **Mobile First:** Startet gestapelt und erweitert sich ab mittleren Breakpoints auf zwei Spalten.
- **Accessibility:** Sorgt für erkennbare Fokuszustände und sinnvolle Reihenfolge bei Tastaturbedienung.
- **SEO:** Betont wichtige Botschaften im Textbereich und nutzt beschreibende Alt-Texte.
- **Best Practices:** grid md:grid-cols-2 einsetzen, Bilder responsive laden, Scroll-Hinweise optional ergänzen

## Checkliste
- [ ] Bilder sind in passenden Größen optimiert.
- [ ] Text bleibt auch bei Reduktion der Breite lesbar.
- [ ] Tastaturnavigation folgt der inhaltlichen Reihenfolge.
- [ ] Performance- und Accessibility-Check dokumentiert.

## Abhängigkeiten / Überschneidungen
- Medien- und CTA-Komponenten
- Responsive Grid-Utilities

## Akzeptanzkriterien
- Split-Layout skaliert von mobil bis Desktop ohne Überlappungen.
- Bild und Text erhalten ausreichenden Kontrast.
- Screenreader greifen auf eine logische Reihenfolge zu.

## Beispiel / Code
```html
<section class="grid md:grid-cols-2">
  <div>Text</div>
  <div><img src="../../assets/agents-and-robots.png" alt="Agentin und Roboter in einer futuristischen Stadt bei Nacht" /></div>
</section>
```

Bewertung der Relevanz 2025

⭐⭐⭐⭐☆ Starkes Muster für bildstarke Kampagnen und Vergleiche.

## Anekdoten & Nerd-Zitate
- In meinen Notizen steht noch der Satz: „Split Screen riecht nach Filterkaffee und Ticket-Alarm.“ Das war der Abend vor dem Launch.
- Wir haben uns selbst beobachtet, wie wir mit Taschenlampen (a.k.a. Gerätepark) durch die QA-Nacht stapfen.
- Niemand von außen textet für uns, aber unsere Slack-Emojis halten uns wach, wenn wir wieder Mobile-Bugs jagen.
- Eine Kollegin sagte: „Accessibility fühlt sich an wie barfuß laufen – du merkst jeden Stein.“ Seitdem prüfe ich Split Screen ohne Maus.

## Best Practices
- **Design Tokens nutzen:** Lass Split Screen aus dem Designsystem atmen, nicht aus spontanen HEX-Codes.
- **Keyboard-Liebe:** Jede Interaktion muss per Tab erreichbar sein – ein Modal ohne Escape ist ein Support-Ticket in spe.
- **Performance messen:** Lighthouse, WebPageTest, was immer du hast – Hauptsache du kennst deine Zahlen.
- **Copy & Microcopy:** Stimme dich mit Content ab, damit die Sprache genauso flüssig ist wie das Interface.
- **Post-Launch-Retros:** Plane von Anfang an ein, die Komponente nach den ersten echten Nutzerkontakten anzupassen.

## Fazit
Wenn ich den Tag Revue passieren lasse, sehe ich Split Screen wie eine verlässliche Nebenfigur, die dem Plot erst Sinn gibt. Wir haben gelernt, dass Resilienz aus Routine entsteht: frühe Tests, offene Kommunikation, echte Devices. Beim nächsten Sprint will ich die Kopplung zu Datenquellen sauberer aufsetzen und weiter beweisen, dass Barrierefreiheit kein Extra ist, sondern Haltung.
