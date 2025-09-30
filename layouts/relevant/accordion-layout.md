Layout: Accordion Layout

Beschreibung

Akkordeon zum Ausklappen mehrerer Informationsblöcke.

Warum dieses Layout?

Hilfreich für FAQs oder Support-Seiten. Stärke: platzsparend; Schwäche: Inhalte können verborgen bleiben.

Anforderungen & Besonderheiten

Mehrere aufklappbare Panels mit Zustandsspeicherung.

Responsiveness

Funktioniert nativ auf allen Viewports.

Accessibility

Buttons mit aria-expanded und aria-controls.

SEO

Serverseitig rendern, damit Crawler Inhalte sehen.

Design-Guidelines

Klare Trennlinien und Animationen dezent.

Rechtliche / technische Randbedingungen (falls relevant)

Wichtige rechtliche Informationen immer sichtbar halten.

Umsetzung – Technische Leitplanken

Mobile First

Touchfreundliche Trigger mit ausreichend Höhe.

Accessibility

Fokusindikatoren und Tastatursteuerung.

SEO

Strukturierte Daten für FAQ möglich.

Best Practices

Nur ein Panel gleichzeitig offen optional.

Checkliste

[ ] zentrale Punkte prüfen

[ ] mobile Darstellung

[ ] Performance

[ ] Accessibility

Abhängigkeiten / Überschneidungen

Accordion-Komponente, Icon-System.

Akzeptanzkriterien

Fertig, wenn Panels Animationen flüssig und ARIA geprüft sind.

Beispiel / Code

```html
<section class="accordion">
  <button aria-expanded="false">Frage</button>
  <div hidden>Antwort</div>
</section>
```

Bewertung der Relevanz 2025

⭐⭐⭐⭐☆
