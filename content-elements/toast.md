# Content-Element: Toast

## Beschreibung
Kurzlebige Benachrichtigungen, die temporär eingeblendet werden.

## Warum dieses Element?
- Feedback nach Formularaktionen geben.
- Hintergrundprozesse wie Speichern oder Sync bestätigen.
- Trade-off: Können von Screenreadern überhört werden, wenn nicht korrekt implementiert.

## Anforderungen & Besonderheiten
- **Responsiveness:** Position adaptiv, ausreichend Abstand vom Rand, Stapel auf Mobile vermeiden.
- **Accessibility:** `role="status"` oder `role="alert"`, sichtbare und hörbare Dauer.
- **SEO:** Kein Einfluss.
- **Design-Guidelines:** Farbvarianten, dezente Animation, Close-Icon optional.
- **Rechtliches:** Keine speziellen Anforderungen.

## Umsetzung – Technische Leitplanken
- **Mobile First:** Zentrierte oder untere Platzierung, Buttons groß genug.
- **Accessibility:** Lesezeit ausreichend (mind. 5 Sekunden), Fokus nicht unerwartet verschieben.
- **SEO:** Nicht relevant, da dynamisch.
- **Best Practices:**
  - Toast-Queue begrenzen.
  - Manuelles Schließen ermöglichen.
  - Animationen reduziert und bevorzugt per CSS implementieren.

## Checkliste
- [ ] Darstellung auf allen Breakpoints geprüft
- [ ] Barrierefreiheit (Fokus, ARIA, Kontrast) OK
- [ ] Semantik korrekt (HTML)
- [ ] Performance optimiert (Lazyload/Kompression)

## Abhängigkeiten / Überschneidungen
- Notification-System, Event-Bus

## Akzeptanzkriterien
- Technische Funktion OK
- Konsistenz zum Designsystem
- A11y & rechtliche Vorgaben erfüllt

## Beispiel / Code
[content-elements-examples/toast.html](../content-elements-examples/toast.html)

```html
<!-- Minimales, valides HTML-Beispiel -->
<div class="toast toast--success" role="status" aria-live="polite">Erfolg gespeichert.</div>
```

Bewertung der Relevanz 2025

⭐⭐⭐⭐ Kurze Benachrichtigungen bleiben wichtig für Feedback in Webanwendungen.
