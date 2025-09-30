# Content-Element: Audio Embed

## Beschreibung
Einbettung eines Audio- oder Podcast-Players.

## Warum dieses Element?
- Podcastepisoden im Blog bereitstellen.
- Audio-Zitate oder Interviews ergänzend zum Text anbieten.
- Trade-off: Autoplay oder zu große Dateien beeinträchtigen Nutzererlebnis.

## Anforderungen & Besonderheiten
- **Responsiveness:** Player skalierbar, Bedienelemente ausreichend groß.
- **Accessibility:** Transkripte bereitstellen, Tastaturbedienung sicherstellen.
- **SEO:** Schema.org AudioObject, sprechende Dateinamen.
- **Design-Guidelines:** Player-Farben und States definieren, Fortschrittsanzeige klar.
- **Rechtliches:** Urheberrechte, Lizenzen und ggf. GEMA-Klärung beachten.

## Umsetzung – Technische Leitplanken
- **Mobile First:** Streaming adaptiv, Download-Option optional.
- **Accessibility:** `aria-labels` für Buttons, Lautstärkeregelung per Tastatur erreichbar.
- **SEO:** Transkript als HTML bereitstellen, Metadaten im Head ergänzen.
- **Best Practices:**
  - Ladezeiten durch Kompression (AAC/Opus) optimieren.
  - Player erst nach Interaktion laden (Lazyload).
  - Download-Link und Episodennotizen bereitstellen.

## Checkliste
- [ ] Darstellung auf allen Breakpoints geprüft
- [ ] Barrierefreiheit (Fokus, ARIA, Kontrast) OK
- [ ] Semantik korrekt (HTML)
- [ ] Performance optimiert (Lazyload/Kompression)

## Abhängigkeiten / Überschneidungen
- Media-Player, CDN, Transkript

## Akzeptanzkriterien
- Technische Funktion OK
- Konsistenz zum Designsystem
- A11y & rechtliche Vorgaben erfüllt

## Beispiel / Code
```html
<!-- Minimales, valides HTML-Beispiel -->
<figure class="audio">
  <figcaption>Podcast Folge 12</figcaption>
  <audio controls preload="none">
    <source src="podcast-12.mp3" type="audio/mpeg">
    Ihr Browser unterstützt das Audio-Element nicht.
  </audio>
</figure>
```

Bewertung der Relevanz 2025

⭐⭐⭐⭐ Audio ist für Content-Marketing weiterhin relevant, vor allem für barrierefreie Alternativen.
