Layout: Nested Columns

Beschreibung

Mehrfach verschachtelte Spalten-Layouts.

Warum dieses Layout?

Früher für komplexe Tabellen-Layouts genutzt, heute schwer wartbar.

Anforderungen & Besonderheiten

Mehrere verschachtelte Container.

Responsiveness

Breakpoints explodieren, Wartung teuer.

Accessibility

Lesereihenfolge chaotisch.

SEO

Wichtige Inhalte verlieren Gewicht.

Design-Guidelines

Überladen, mangelnde Klarheit.

Rechtliche / technische Randbedingungen (falls relevant)

Keine besonderen Anforderungen.

Umsetzung – Technische Leitplanken

Mobile First

Auf Mobil kaum nutzbar.

Accessibility

Screenreader-Kontext unklar.

SEO

Crawler bewerten Chaos negativ.

Best Practices

Modulare Komponenten statt Nesting.

Checkliste

[ ] zentrale Punkte prüfen

[ ] mobile Darstellung

[ ] Performance

[ ] Accessibility

Abhängigkeiten / Überschneidungen

Alte Table-basierten Systeme.

Akzeptanzkriterien

Wird nicht mehr weiterentwickelt.

Beispiel / Code

```html
<div class="nested">
  <div class="column">
    <div class="column">Inhalt</div>
  </div>
</div>
```

Bewertung der Relevanz 2025

⭐⭐☆☆☆

⚠️ Deprecated – nicht mehr empfohlen für Mobile-First-Designs, nur noch zu Dokumentationszwecken.
