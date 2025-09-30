# Content-Element: Tooltip

## Beschreibung
Kurze Hilfetexte, die bei Hover oder Fokus zusätzliche Informationen geben.

## Warum dieses Element?
- Formularfelder mit Kontextinformationen versehen.
- Tabellenwerte oder Icons erläutern, ohne Layout zu überladen.
- Trade-off: Nicht auf Touch-Geräten verfügbar, daher alternative Darstellung nötig.

## Anforderungen & Besonderheiten
- **Responsiveness:** Positionierung relativ zum Trigger, auf Mobile ggf. als Inline-Hinweis.
- **Accessibility:** `aria-describedby` verwenden, Fokus-Management beachten.
- **SEO:** Kein direkter Einfluss, Inhalte sollten auch ohne Tooltip verfügbar sein.
- **Design-Guidelines:** Klarer Kontrast, dezente Animation, Pfeile optional.
- **Rechtliches:** Keine speziellen Anforderungen.

## Umsetzung – Technische Leitplanken
- **Mobile First:** Tooltip als Click-to-toggle oder Inline-Expand umsetzen.
- **Accessibility:** Tooltip bei Fokus sichtbar halten, Escape zum Schließen ermöglichen.
- **SEO:** Tooltip-Inhalte nicht exklusiv halten, immer auch im Fließtext erwähnen.
- **Best Practices:**
  - Trigger als Button oder Link deklarieren.
  - Tooltip mit `role="tooltip"` und IDs verknüpfen.
  - Autohide mit Verzögerung, um Flickern zu vermeiden.

## Checkliste
- [ ] Darstellung auf allen Breakpoints geprüft
- [ ] Barrierefreiheit (Fokus, ARIA, Kontrast) OK
- [ ] Semantik korrekt (HTML)
- [ ] Performance optimiert (Lazyload/Kompression)

## Abhängigkeiten / Überschneidungen
- Popover-System, Focus-Management

## Akzeptanzkriterien
- Technische Funktion OK
- Konsistenz zum Designsystem
- A11y & rechtliche Vorgaben erfüllt

## Beispiel / Code
```html
<!-- Minimales, valides HTML-Beispiel -->
<button type="button" aria-describedby="tip-id">?
</button>
<span id="tip-id" role="tooltip">Erklärt das Feld</span>
```

Bewertung der Relevanz 2025

⭐⭐⭐⭐ Tooltips bleiben relevant, solange Touch-Alternativen berücksichtigt werden.
