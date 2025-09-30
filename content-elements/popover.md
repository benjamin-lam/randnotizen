# Content-Element: Popover

## Beschreibung
Kontextbezogene Overlays mit weiterführenden Inhalten oder Aktionen.

## Warum dieses Element?
- Detailinformationen in Tabellen oder Dashboards anzeigen.
- Kleine Formulare oder Aktionen ohne Seitenwechsel anbieten.
- Trade-off: Zu komplexe Inhalte in kleinen Overlays beeinträchtigen Usability.

## Anforderungen & Besonderheiten
- **Responsiveness:** Auf Mobile bildschirmfüllend oder als Bottom Sheet darstellen.
- **Accessibility:** Fokusmanagement, `aria-modal` bei exklusiven Popovern, Escape zum Schließen.
- **SEO:** Dynamische Inhalte nicht indexrelevant, daher im DOM verfügbar halten.
- **Design-Guidelines:** Schatten, Abstände, Pfeile anpassen, klare Close-Icons.
- **Rechtliches:** Keine speziellen Anforderungen.

## Umsetzung – Technische Leitplanken
- **Mobile First:** Popover als Vollbild-Overlay oder expandierbaren Bereich planen.
- **Accessibility:** Fokus auf erstes interaktives Element setzen, Rücksprung zum Trigger ermöglichen.
- **SEO:** Inhalte serverseitig rendern, falls für SEO wichtig.
- **Best Practices:**
  - Offene Popover schließen, wenn außerhalb geklickt wird.
  - Transitions kurz halten (<200 ms).
  - Popover-Größe begrenzen und Scroll innerhalb erlauben.

## Checkliste
- [ ] Darstellung auf allen Breakpoints geprüft
- [ ] Barrierefreiheit (Fokus, ARIA, Kontrast) OK
- [ ] Semantik korrekt (HTML)
- [ ] Performance optimiert (Lazyload/Kompression)

## Abhängigkeiten / Überschneidungen
- Dialog-System, Overlay-Layer, Focus-Trap

## Akzeptanzkriterien
- Technische Funktion OK
- Konsistenz zum Designsystem
- A11y & rechtliche Vorgaben erfüllt

## Beispiel / Code
[content-elements-examples/popover.html](../content-elements-examples/popover.html)

```html
<!-- Minimales, valides HTML-Beispiel -->
<button type="button" aria-haspopup="dialog" aria-expanded="false">Details</button>
<div class="popover" role="dialog" hidden>
  <h3>Mehr Infos</h3>
  <p>Zusätzliche Details.</p>
  <button type="button" class="popover__close">Schließen</button>
</div>
```

Bewertung der Relevanz 2025

⭐⭐⭐⭐ Popover bleiben vielseitig, benötigen aber klare Regeln für Mobile und A11y.
