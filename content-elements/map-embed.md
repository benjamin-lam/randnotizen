# Content-Element: Map Embed

## Beschreibung
Interaktive Karte zur Standortanzeige oder Wegbeschreibung.

## Warum dieses Element?
- Standortübersicht auf Kontakt- oder Filialseiten.
- Event-Locations oder Veranstaltungsorte darstellen.
- Trade-off: Externe Maps erhöhen Ladezeit und bergen Datenschutzrisiken.

## Anforderungen & Besonderheiten
- **Responsiveness:** Adaptive Höhe/Breite, Touch-Gesten unterstützen.
- **Accessibility:** Alternativbeschreibung und Adresse als Text, Fokusfalle vermeiden.
- **SEO:** Strukturierte Daten für Organisation/LocalBusiness, statische Karte als Fallback.
- **Design-Guidelines:** Kartenrahmen, Marker-Branding, klare Buttons.
- **Rechtliches:** DSGVO-konforme Einwilligung vor Laden externer Dienste (Google Maps), Datenschutzhinweis bereitstellen.

## Umsetzung – Technische Leitplanken
- **Mobile First:** Statische Karte oder Screenshot bis Interaktion, geringe Datenlast.
- **Accessibility:** Tastaturbedienung prüfen, Zoomkontrollen beschriftet, Adresse zusätzlich in HTML.
- **SEO:** `loading="lazy"` für iframes, strukturierte Adresse in Microdata.
- **Best Practices:**
  - Privacy-Proxy oder Selbsthosting (OSM) bevorzugen.
  - Fallback-Link zu Routenplanung anbieten.
  - Interaktion nur nach Consent aktivieren.

## Checkliste
- [ ] Darstellung auf allen Breakpoints geprüft
- [ ] Barrierefreiheit (Fokus, ARIA, Kontrast) OK
- [ ] Semantik korrekt (HTML)
- [ ] Performance optimiert (Lazyload/Kompression)

## Abhängigkeiten / Überschneidungen
- Consent-Tool, Map-Provider, Standortdaten

## Akzeptanzkriterien
- Technische Funktion OK
- Konsistenz zum Designsystem
- A11y & rechtliche Vorgaben erfüllt

## Beispiel / Code
```html
<!-- Minimales, valides HTML-Beispiel -->
<section class="map">
  <button type="button" data-action="load-map">Karte laden (externer Inhalt)</button>
  <p>Adresse: Beispielstraße 1, 12345 Musterstadt</p>
</section>
```

Bewertung der Relevanz 2025

⭐⭐⭐⭐ Standortinformationen bleiben wichtig, Datenschutzanforderungen steigen jedoch.
