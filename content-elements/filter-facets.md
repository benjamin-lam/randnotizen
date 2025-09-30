# Content-Element: Filter Facets

## Beschreibung
Facettierte Filtersteuerung mit Chips, Listen oder Slidern.

## Warum dieses Element?
- Produkt- oder Artikellisten zielgerichtet einschränken.
- Suchergebnisse nach Kategorien, Preisen oder Tags verfeinern.
- Trade-off: Zu viele Filteroptionen überfordern Nutzer und erhöhen Komplexität.

## Anforderungen & Besonderheiten
- **Responsiveness:** Auf Mobile als Akkordeon oder Off-Canvas, auf Desktop nebeneinander.
- **Accessibility:** Checkbox-/Radio-Labels klar benennen, `aria-pressed` für Chips.
- **SEO:** Filter-URLs sauber handhaben, Duplicate Content vermeiden.
- **Design-Guidelines:** Visuelle Hierarchie, aktive Filter hervorheben, Reset-Option.
- **Rechtliches:** Tracking von Filterinteraktionen DSGVO-konform behandeln.

## Umsetzung – Technische Leitplanken
- **Mobile First:** Filter über Button einblenden, Prioritäten setzen.
- **Accessibility:** Statusänderungen per `aria-live` ankündigen, Fokus nach Anwendung sinnvoll setzen.
- **SEO:** Kanonsiche URLs definieren, Parameter whitelisten.
- **Best Practices:**
  - Aktive Filter deutlich anzeigen und entfernen lassen.
  - Filterzustand in URL speichern.
  - Serverseitige und clientseitige Filter synchron halten.

## Checkliste
- [ ] Darstellung auf allen Breakpoints geprüft
- [ ] Barrierefreiheit (Fokus, ARIA, Kontrast) OK
- [ ] Semantik korrekt (HTML)
- [ ] Performance optimiert (Lazyload/Kompression)

## Abhängigkeiten / Überschneidungen
- Such-API, State-Management, Analytics

## Akzeptanzkriterien
- Technische Funktion OK
- Konsistenz zum Designsystem
- A11y & rechtliche Vorgaben erfüllt

## Beispiel / Code
```html
<!-- Minimales, valides HTML-Beispiel -->
<section class="filters">
  <button type="button" class="filter-chip" aria-pressed="true">Sofort lieferbar</button>
  <label><input type="checkbox" name="brand" value="acme"> ACME</label>
</section>
```

Bewertung der Relevanz 2025

⭐⭐⭐⭐ Komplexe Kataloge brauchen weiterhin leistungsfähige Filtersteuerungen.
