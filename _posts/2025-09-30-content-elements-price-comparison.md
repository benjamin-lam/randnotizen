---
title: "Price Comparison: Randnotiz"
date: 2025-09-30
tags: [UI, Komponente, Webentwicklung]
excerpt: "Warum Price Comparison unsere Content Elements-Notizen inspiriert."
layout: post
categories: [content-elements]
slug: content-elements-price-comparison
original_path: content-elements/price-comparison.md
---

## Einleitung
Es fühlt sich an wie ein Fund in einer verstaubten Prototyp-Schublade: **Price Comparison** passte heute perfekt in unsere Content Elements-Gedanken, und plötzlich roch der Raum nach Whiteboard-Markern und frisch gebrühtem Kaffee.

## Technischer Kern
Technisch betrachtet verlangt Price Comparison nach klaren Leitplanken. Ich habe die ursprüngliche Beschreibung unten angeheftet und mit Kommentaren versehen, damit der Transfer in das neue Blog sichtbar bleibt.

### Originalnotizen
# Content-Element: Price Comparison

## Beschreibung
Kompakte Vergleichstabelle für Tarife oder Pakete.

## Warum dieses Element?
- SaaS-Preise oder Abos übersichtlich darstellen.
- Feature-Vergleich verschiedener Varianten zeigen.
- Trade-off: Komplexe Tabellen können auf Mobile schwer lesbar sein.

## Anforderungen & Besonderheiten
- **Responsiveness:** Kartenlayout für Mobile, Tabelle auf Desktop.
- **Accessibility:** Tabellenbeschriftungen, `aria-describedby` für Besonderheiten.
- **SEO:** Preisangaben mit `Product`/`Offer` Markup.
- **Design-Guidelines:** Highlight des empfohlenen Plans, klare Buttons, Farben abgestimmt.
- **Rechtliches:** Preisangaben, Laufzeit, MwSt., Kündigungsfristen transparent kommunizieren.

## Umsetzung – Technische Leitplanken
- **Mobile First:** Swipebare Karten oder Akkordeon für Details.
- **Accessibility:** Fokus zwischen Plan-Karten steuerbar, Preisänderungen ansagen.
- **SEO:** Rich Snippets für Preise, keine versteckten Kosten.
- **Best Practices:**
  - Wichtigste Unterschiede klar hervorheben.
  - Call-to-Action pro Plan konsistent.
  - Zahlungsintervalle wählbar machen.

## Checkliste
- [ ] Darstellung auf allen Breakpoints geprüft
- [ ] Barrierefreiheit (Fokus, ARIA, Kontrast) OK
- [ ] Semantik korrekt (HTML)
- [ ] Performance optimiert (Lazyload/Kompression)

## Abhängigkeiten / Überschneidungen
- Produktdaten, Analytics, CTA-Komponenten

## Akzeptanzkriterien
- Technische Funktion OK
- Konsistenz zum Designsystem
- A11y & rechtliche Vorgaben erfüllt

## Beispiel / Code
[content-elements-examples/price-comparison.html](../content-elements-examples/price-comparison.html)

```html
<!-- Minimales, valides HTML-Beispiel -->
<section class="pricing">
  <article class="pricing__plan pricing__plan--highlight">
    <h3>Pro</h3>
    <p class="pricing__price">29 € / Monat</p>
    <ul>
      <li>Unbegrenzte Projekte</li>
    </ul>
    <button type="button">Jetzt starten</button>
  </article>
</section>
```

Bewertung der Relevanz 2025

⭐⭐⭐⭐ Preisvergleiche bleiben kaufentscheidend, müssen jedoch mobilfreundlich sein.

## Anekdoten & Nerd-Zitate
Michael Crichton hätte wahrscheinlich eine komplette Katastrophensimulation um Price Comparison gestrickt, nur um zu zeigen, wie viele Dinge gleichzeitig schiefgehen können. Douglas Coupland würde dagegen eine Slack-Konversation voller Insider-Gags daraus machen. Und irgendwo zwinkert eine alte RFC dazu, weil die Nerd-Fakten selten stillstehen.

## Best Practices
- A11y: Price Comparison tastatur- und screenreader-freundlich gestalten.
- Performance: Price Comparison nur laden, wenn der Kontext es wirklich braucht.
- Wartbarkeit: Entscheidungen zu Price Comparison direkt neben dem Code dokumentieren.

## Fazit
Price Comparison bleibt ein schönes Beispiel dafür, wie Content Elements-Elemente Geschichten erzählen können, wenn man sie ernst nimmt und trotzdem mit Humor betrachtet.
