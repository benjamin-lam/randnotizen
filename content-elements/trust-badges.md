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
```html
<!-- Minimales, valides HTML-Beispiel -->
<ul class="trust-badges">
  <li><img src="tuev.svg" alt="TÜV zertifiziert"></li>
  <li><img src="ssl.svg" alt="SSL verschlüsselt"></li>
</ul>
```

Bewertung der Relevanz 2025

⭐⭐⭐⭐ Vertrauenssiegel beeinflussen weiterhin Conversion und Glaubwürdigkeit.
