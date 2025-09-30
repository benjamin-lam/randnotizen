# Layout: Accordion Layout

## Beschreibung
Ausklappbare Bereiche bündeln FAQs, Detailinfos oder Spezifikationen und halten Seiten kompakt.

## Warum dieses Layout?
- Hilft bei der Strukturierung langer Informationslisten.
- Reduziert kognitive Last durch progressive Offenlegung.
- Kann wichtige Inhalte vor Nutzern und Suchmaschinen verbergen.

## Anforderungen & Besonderheiten
- **Responsiveness:** Accordion-Elemente passen sich in Breite und Typografie an.
- **Accessibility:** WAI-ARIA Disclosure Pattern mit button, aria-expanded und aria-controls nutzen.
- **SEO:** Wesentliche Inhalte sollten im initial geöffneten Zustand verfügbar sein.
- **Design-Guidelines:** Klare Trennlinien, ausreichend Padding und deutliche Icons für Zustände.

## Umsetzung – Technische Leitplanken
- **Mobile First:** Accordion ist Standard, Desktop kann parallele Spalten ergänzen.
- **Accessibility:** Focus-Stati und Tastatursteuerung (Enter/Space) berücksichtigen.
- **SEO:** Accordion-Inhalte im DOM belassen und nicht per JS nachladen.
- **Best Practices:** Weiche Animationen einsetzen, Nur ein Panel optional offen halten, Status programmatisch speichern

## Checkliste
- [ ] Accordion lässt sich mit Tastatur komplett bedienen.
- [ ] Icons und Labels kommunizieren den Zustand klar.
- [ ] Wichtige Inhalte sind initial sichtbar oder angekündigt.
- [ ] A11y- und Performance-Audit abgeschlossen.

## Abhängigkeiten / Überschneidungen
- Disclosure-Komponente
- Content-Module

## Akzeptanzkriterien
- ARIA-Attribute entsprechen dem Disclosure-Pattern.
- Panels lassen sich ohne Layoutsprünge öffnen und schließen.
- Screenreader geben Statusänderungen korrekt wieder.

## Beispiel / Code
```html
<section class="accordion">
  <button aria-expanded="false" aria-controls="faq-1">Frage</button>
  <div id="faq-1" hidden>Antwort…</div>
</section>
```

Bewertung der Relevanz 2025

⭐⭐⭐⭐⭐ Standardmuster für FAQs und Detailinformationen.
