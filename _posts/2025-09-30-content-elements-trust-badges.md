---
title: "Trust Badges: Randnotiz"
date: 2025-09-30
tags: [UI, Komponente, Webentwicklung]
excerpt: "Warum Trust Badges unsere Content Elements-Notizen inspiriert."
layout: post
categories: [content-elements]
slug: content-elements-trust-badges
original_path: content-elements/trust-badges.md
---

## Einleitung
Es fühlt sich an wie ein Fund in einer verstaubten Prototyp-Schublade: **Trust Badges** passte heute perfekt in unsere Content Elements-Gedanken, und plötzlich roch der Raum nach Whiteboard-Markern und frisch gebrühtem Kaffee.

## Technischer Kern
Technisch betrachtet verlangt Trust Badges nach klaren Leitplanken. Ich habe die ursprüngliche Beschreibung unten angeheftet und mit Kommentaren versehen, damit der Transfer in das neue Blog sichtbar bleibt.

### Originalnotizen
# Content-Element: Trust Badges

## Beschreibung
Sicherheits- und Vertrauenssiegel wie Zahlungsanbieter oder Zertifikate.

## Warum dieses Element?
- Checkout-Seiten mit Gütesiegeln versehen.
- Landingpages mit Referenzen und Zertifizierungen stärken.
- Trade-off: Zu viele Badges wirken unseriös oder ablenkend.

## Anforderungen & Besonderheiten
- **Responsiveness:** Icons skalierbar, Raster flexibel.
- **Accessibility:** Alternativtexte für Logos, dekorative Elemente mit `aria-hidden`.
- **SEO:** Alt-Texte tragen zu Markensichtbarkeit bei.
- **Design-Guidelines:** Konsistente Größe, ausreichender Abstand, monochrome Varianten.
- **Rechtliches:** Nur tatsächlich vorhandene Zertifikate nutzen, Nutzungsrechte prüfen.

## Umsetzung – Technische Leitplanken
- **Mobile First:** Badges gruppieren oder in Slider packen, ohne Scroll zu erzwingen.
- **Accessibility:** Logos, die nur dekorativ sind, per `aria-hidden` ausblenden.
- **SEO:** Dateinamen beschreibend wählen, Lazyload bei vielen Logos.
- **Best Practices:**
  - Maximal fünf relevante Badges gleichzeitig zeigen.
  - Badges bei Bedarf verlinken (z. B. TÜV Zertifikat).
  - Kontrast zum Hintergrund sicherstellen.

## Checkliste
- [ ] Darstellung auf allen Breakpoints geprüft
- [ ] Barrierefreiheit (Fokus, ARIA, Kontrast) OK
- [ ] Semantik korrekt (HTML)
- [ ] Performance optimiert (Lazyload/Kompression)

## Abhängigkeiten / Überschneidungen
- Asset-Management, Legal-Team

## Akzeptanzkriterien
- Technische Funktion OK
- Konsistenz zum Designsystem
- A11y & rechtliche Vorgaben erfüllt

## Beispiel / Code
[content-elements-examples/trust-badges.html](../content-elements-examples/trust-badges.html)

```html
<!-- Minimales, valides HTML-Beispiel -->
<ul class="trust-badges">
  <li><img src="../assets/agents-and-robots.png" alt="Agentin und Roboter in einer futuristischen Stadt bei Nacht"></li>
  <li><img src="../assets/agents-and-robots.png" alt="Agentin und Roboter in einer futuristischen Stadt bei Nacht"></li>
</ul>
```

Bewertung der Relevanz 2025

⭐⭐⭐⭐ Vertrauenssiegel beeinflussen weiterhin Conversion und Glaubwürdigkeit.

## Anekdoten & Nerd-Zitate
Michael Crichton hätte wahrscheinlich eine komplette Katastrophensimulation um Trust Badges gestrickt, nur um zu zeigen, wie viele Dinge gleichzeitig schiefgehen können. Douglas Coupland würde dagegen eine Slack-Konversation voller Insider-Gags daraus machen. Und irgendwo zwinkert eine alte RFC dazu, weil die Nerd-Fakten selten stillstehen.

## Best Practices
- A11y: Trust Badges tastatur- und screenreader-freundlich gestalten.
- Performance: Trust Badges nur laden, wenn der Kontext es wirklich braucht.
- Wartbarkeit: Entscheidungen zu Trust Badges direkt neben dem Code dokumentieren.

## Fazit
Trust Badges bleibt ein schönes Beispiel dafür, wie Content Elements-Elemente Geschichten erzählen können, wenn man sie ernst nimmt und trotzdem mit Humor betrachtet.
