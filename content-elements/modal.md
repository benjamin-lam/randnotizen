# Content-Element: Modal

## Beschreibung
Dialog-Overlay, das den restlichen Inhalt überlagert und fokussierte Interaktion verlangt.

## Warum dieses Element?
- Bestätigungsdialoge oder wichtige Hinweise anzeigen.
- Formulare oder Medien ohne Seitenwechsel bereitstellen.
- Trade-off: Unterbrechung des Nutzerflusses, daher sparsam einsetzen.

## Anforderungen & Besonderheiten
- **Responsiveness:** Auf kleinen Screens fullscreen, auf Desktop zentriert mit max-width.
- **Accessibility:** Focus-Trap, `aria-modal`, Escape-Handling, beschreibende Titel.
- **SEO:** Kein direkter Einfluss, Inhalte sollten auch anderweitig zugänglich sein.
- **Design-Guidelines:** Overlay-Opacity, Schatten, Close-Icon, klare Buttons.
- **Rechtliches:** Bei rechtlich relevanten Hinweisen (z. B. AGB) Dokumentation der Zustimmung sichern.

## Umsetzung – Technische Leitplanken
- **Mobile First:** Fullwidth-Layout, große Touch-Ziele, Scrollverhalten prüfen.
- **Accessibility:** Fokus beim Öffnen auf Heading setzen, beim Schließen zum Trigger zurückführen.
- **SEO:** Modal-Inhalte indexierbar im DOM halten oder serverseitig rendern.
- **Best Practices:**
  - Schließen per ESC, Button und Overlay-Klick ermöglichen.
  - Hintergrund scrollbar sperren.
  - Eindeutige Beschriftung (Heading) verwenden.

## Checkliste
- [ ] Darstellung auf allen Breakpoints geprüft
- [ ] Barrierefreiheit (Fokus, ARIA, Kontrast) OK
- [ ] Semantik korrekt (HTML)
- [ ] Performance optimiert (Lazyload/Kompression)

## Abhängigkeiten / Überschneidungen
- Overlay-System, Focus-Trap, Scroll-Lock

## Akzeptanzkriterien
- Technische Funktion OK
- Konsistenz zum Designsystem
- A11y & rechtliche Vorgaben erfüllt

## Beispiel / Code
```html
<!-- Minimales, valides HTML-Beispiel -->
<button type="button" data-open="modal">Modal öffnen</button>
<div id="modal" class="modal" role="dialog" aria-modal="true" aria-labelledby="modal-title" hidden>
  <div class="modal__content">
    <h2 id="modal-title">Hinweis</h2>
    <p>Bitte bestätigen Sie die Aktion.</p>
    <button type="button" data-close>Schließen</button>
  </div>
</div>
```

Bewertung der Relevanz 2025

⭐⭐⭐⭐ Modale Dialoge bleiben Standard, wenn sie zugänglich und sparsam eingesetzt werden.
