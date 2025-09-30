Layout: Fixed Footer

Beschreibung

Layout mit dauerhaft fixiertem Footer am unteren Bildschirmrand.

Warum dieses Layout?

Früher beliebt für Navigationsleisten, blockiert aber heute wertvollen Platz.

Anforderungen & Besonderheiten

Footer mit position: fixed.

Responsiveness

Auf kleinen Screens verdeckt Inhalte.

Accessibility

Keyboard-Fokus kann verdeckt werden.

SEO

Wenig Einfluss, aber schlechter UX-Eindruck.

Design-Guidelines

Wirkt schnell gedrängt.

Rechtliche / technische Randbedingungen (falls relevant)

Kann Cookie-Banner kollidieren lassen.

Umsetzung – Technische Leitplanken

Mobile First

Software-Tastaturen schneiden Elemente ab.

Accessibility

WCAG rät zu vermeidbaren Overlays.

SEO

Negative UX wirkt indirekt.

Best Practices

Stattdessen kontextuelle Toolbars.

Checkliste

[ ] zentrale Punkte prüfen

[ ] mobile Darstellung

[ ] Performance

[ ] Accessibility

Abhängigkeiten / Überschneidungen

Legacy Navigation.

Akzeptanzkriterien

Nicht mehr für neue Projekte freigegeben.

Beispiel / Code

```html
<footer class="footer-fixed">Footer</footer>
<main>Content</main>
```

Bewertung der Relevanz 2025

⭐⭐☆☆☆

⚠️ Deprecated – nicht mehr empfohlen für Mobile-First-Designs, nur noch zu Dokumentationszwecken.
