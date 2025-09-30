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
