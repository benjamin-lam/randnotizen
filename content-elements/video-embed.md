# Content-Element: Video Embed

## Beschreibung
Einbettung von Videos mit Poster, Controls und optionaler Lazyload-Lösung.

## Warum dieses Element?
- Produktdemos oder Tutorials direkt im Content zeigen.
- Kundenreferenzen oder Interviews einbetten.
- Trade-off: Streaming kann Performance belasten und Datenschutzpflichten auslösen.

## Anforderungen & Besonderheiten
- **Responsiveness:** Aspect-Ratio-Container, adaptive Playergröße.
- **Accessibility:** Untertitel, Transkript und Tastaturbedienbarkeit sicherstellen.
- **SEO:** Schema.org VideoObject, sprechende Titles und Thumbnails.
- **Design-Guidelines:** Posterbild definieren, Player-Farben ans Designsystem anpassen.
- **Rechtliches:** Einbettung externer Plattformen nur mit DSGVO-konformer Einwilligung und Hinweis auf Datenübertragung.

## Umsetzung – Technische Leitplanken
- **Mobile First:** Automatisch muted starten, adaptive Bitrate, Bandbreite berücksichtigen.
- **Accessibility:** `controls` aktivieren, Untertiteldateien (`track`) anbieten, Fokusmanagement prüfen.
- **SEO:** Lazyload über Consent-Gate lösen, strukturierte Daten bereitstellen.
- **Best Practices:**
  - Posterbilder optimiert bereitstellen (WebP).
  - Fallback-Link zum Download oder externen Player anbieten.
  - Consent-Management für YouTube/Vimeo integrieren.

## Checkliste
- [ ] Darstellung auf allen Breakpoints geprüft
- [ ] Barrierefreiheit (Fokus, ARIA, Kontrast) OK
- [ ] Semantik korrekt (HTML)
- [ ] Performance optimiert (Lazyload/Kompression)

## Abhängigkeiten / Überschneidungen
- Consent-Tool, CDN/Player, Transkript

## Akzeptanzkriterien
- Technische Funktion OK
- Konsistenz zum Designsystem
- A11y & rechtliche Vorgaben erfüllt

## Beispiel / Code
[content-elements-examples/video-embed.html](../content-elements-examples/video-embed.html)

```html
<!-- Minimales, valides HTML-Beispiel -->
<figure class="video">
  <video controls preload="none" poster="video-poster.webp">
    <source src="demo.mp4" type="video/mp4">
    <track kind="captions" src="demo-de.vtt" srclang="de" label="Deutsch">
    Ihr Browser unterstützt das Video-Element nicht.
  </video>
  <figcaption>Kurze Produktdemo.</figcaption>
</figure>
```

Bewertung der Relevanz 2025

⭐⭐⭐⭐ Videoinhalte gewinnen weiter an Relevanz, müssen aber datenschutzkonform bereitgestellt werden.
