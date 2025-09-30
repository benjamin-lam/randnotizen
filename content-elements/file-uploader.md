# Content-Element: File Uploader

## Beschreibung
Komponente zum Hochladen von Dateien inklusive Fortschritt und Validierung.

## Warum dieses Element?
- Bewerbungs- oder Support-Uploads ermöglichen.
- Medienverwaltung in CMS oder Kundenportalen.
- Trade-off: Große Dateien erfordern Chunking, Sicherheit und Storage-Kosten.

## Anforderungen & Besonderheiten
- **Responsiveness:** Drag-and-Drop-Bereich skalierbar, Fortschrittsanzeigen gut lesbar.
- **Accessibility:** Klare Statusmeldungen, Tastaturbedienung, Screenreader-freundliche Feedbacks.
- **SEO:** Keine direkte Relevanz.
- **Design-Guidelines:** Drop-Zonen, Buttons, Fortschrittsbalken konsistent gestalten.
- **Rechtliches:** Datenschutz und sichere Übertragung (TLS), Dateitypen-Policy, ggf. AV-Verträge.

## Umsetzung – Technische Leitplanken
- **Mobile First:** Dateiauswahl über native Picker, klare Hinweise zur Maximalgröße.
- **Accessibility:** Statusupdates via `aria-live`, Fehler klar beschreiben.
- **SEO:** Nicht relevant.
- **Best Practices:**
  - Serverseitige Validierung ergänzen.
  - Uploads pausieren/fortsetzen ermöglichen.
  - Virenscan oder Sicherheitschecks einplanen.

## Checkliste
- [ ] Darstellung auf allen Breakpoints geprüft
- [ ] Barrierefreiheit (Fokus, ARIA, Kontrast) OK
- [ ] Semantik korrekt (HTML)
- [ ] Performance optimiert (Lazyload/Kompression)

## Abhängigkeiten / Überschneidungen
- Storage-Service, Validation, Progress-API

## Akzeptanzkriterien
- Technische Funktion OK
- Konsistenz zum Designsystem
- A11y & rechtliche Vorgaben erfüllt

## Beispiel / Code
```html
<!-- Minimales, valides HTML-Beispiel -->
<form class="uploader">
  <label for="file" class="uploader__dropzone">Datei hier ablegen oder klicken</label>
  <input id="file" name="file" type="file" hidden>
  <progress value="0" max="100" aria-live="polite"></progress>
</form>
```

Bewertung der Relevanz 2025

⭐⭐⭐⭐ Datei-Uploads sind häufig und erfordern hohe UX- und Sicherheitsstandards.
