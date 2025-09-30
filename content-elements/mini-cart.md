# Content-Element: Mini Cart

## Beschreibung
Warenkorb-Vorschau als Off-Canvas oder Dropdown.

## Warum dieses Element?
- Schnellen Zugriff auf Warenkorb-Inhalte bieten.
- Upselling im Warenkorb-Kontext ermöglichen.
- Trade-off: Zu komplexe Interaktionen im Mini-Cart können zu Fehlern führen.

## Anforderungen & Besonderheiten
- **Responsiveness:** Off-Canvas auf Mobile, Dropdown auf Desktop, Scrollbereich für lange Listen.
- **Accessibility:** `aria-modal` bei Overlays, Tastaturbedienbarkeit, Screenreader-Labels.
- **SEO:** Nicht indexrelevant.
- **Design-Guidelines:** Klares Layout, Produktbilder klein, Gesamtpreis deutlich, Checkout-CTA.
- **Rechtliches:** Preisangaben (MwSt., Versand) verpflichtend anzeigen.

## Umsetzung – Technische Leitplanken
- **Mobile First:** Schnell sichtbar, einfache Änderungen (Menge, Entfernen).
- **Accessibility:** Änderungen per `aria-live` ankündigen, Fokus beim Öffnen setzen.
- **SEO:** Nicht relevant.
- **Best Practices:**
  - Persistenten Warenkorbstatus synchronisieren.
  - Checkout-Link deutlich hervorheben.
  - Produkte entfernen/ändern ohne Seitenwechsel.

## Checkliste
- [ ] Darstellung auf allen Breakpoints geprüft
- [ ] Barrierefreiheit (Fokus, ARIA, Kontrast) OK
- [ ] Semantik korrekt (HTML)
- [ ] Performance optimiert (Lazyload/Kompression)

## Abhängigkeiten / Überschneidungen
- Cart-API, Modal-System, Analytics

## Akzeptanzkriterien
- Technische Funktion OK
- Konsistenz zum Designsystem
- A11y & rechtliche Vorgaben erfüllt

## Beispiel / Code
[content-elements-examples/mini-cart.html](../content-elements-examples/mini-cart.html)

```html
<!-- Minimales, valides HTML-Beispiel -->
<button type="button" aria-haspopup="dialog" aria-expanded="false">Warenkorb</button>
<aside class="mini-cart" role="dialog" aria-modal="true" hidden>
  <h2>Warenkorb</h2>
  <ul>
    <li>Produkt A ×1</li>
  </ul>
  <p>Summe: 89 €</p>
  <a href="/checkout">Zum Checkout</a>
</aside>
```

Bewertung der Relevanz 2025

⭐⭐⭐⭐ Mini-Carts bleiben für Conversion und Übersicht essenziell.
