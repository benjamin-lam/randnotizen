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
Es fühlt sich an wie ein Fund in einer verstaubten Prototyp-Schublade: **Split Screen** passte heute perfekt in unsere Layouts-Gedanken, und plötzlich roch der Raum nach Whiteboard-Markern und frisch gebrühtem Kaffee.

## Technischer Kern
Technisch betrachtet verlangt Split Screen nach klaren Leitplanken. Ich habe die ursprüngliche Beschreibung unten angeheftet und mit Kommentaren versehen, damit der Transfer in das neue Blog sichtbar bleibt.

### Originalnotizen
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
Michael Crichton hätte wahrscheinlich eine komplette Katastrophensimulation um Split Screen gestrickt, nur um zu zeigen, wie viele Dinge gleichzeitig schiefgehen können. Douglas Coupland würde dagegen eine Slack-Konversation voller Insider-Gags daraus machen. Und irgendwo zwinkert eine alte RFC dazu, weil die Nerd-Fakten selten stillstehen.

## Best Practices
- A11y: Split Screen tastatur- und screenreader-freundlich gestalten.
- Performance: Split Screen nur laden, wenn der Kontext es wirklich braucht.
- Wartbarkeit: Entscheidungen zu Split Screen direkt neben dem Code dokumentieren.

## Fazit
Split Screen bleibt ein schönes Beispiel dafür, wie Layouts-Elemente Geschichten erzählen können, wenn man sie ernst nimmt und trotzdem mit Humor betrachtet.
