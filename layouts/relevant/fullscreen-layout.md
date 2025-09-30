# Layout: Fullscreen Layout

## Beschreibung
Sektionen nutzen die komplette Viewport-Höhe, um Inhalte immersiv zu inszenieren. Geeignet für Storytelling, Produkt-Highlights oder Scroll-Snapping-Erfahrungen.

## Warum dieses Layout?
- Erzeugt starke visuelle Präsenz und Fokus.
- Unterstützt Schritt-für-Schritt-Inszenierungen.
- Kann die Wahrnehmung des "Folds" beeinträchtigen und Nutzer zum Scrollen motivieren müssen.

## Anforderungen & Besonderheiten
- **Responsiveness:** min-height: 100dvh mit Fallbacks für mobile Browserleisten, Scroll-Hinweis ergänzen.
- **Accessibility:** Keine Scroll-Fallen erzeugen, Tastatur- und Screenreader-Steuerung sicherstellen.
- **SEO:** Wichtige Inhalte nicht ausschließlich in späteren Panels verstecken.
- **Design-Guidelines:** Klare Kontraste, großzügige Typografie und visuelle Balance zwischen Panels.

## Umsetzung – Technische Leitplanken
- **Mobile First:** Startet mit flexiblen Höhen und erweitert sich zu Fullscreen erst ab größeren Breakpoints.
- **Accessibility:** Scroll-Hinweise und Skip-Links bereitstellen, Animationspräferenzen respektieren.
- **SEO:** Meta-Beschreibungen auf Kernbotschaften der ersten Sektion abstimmen.
- **Best Practices:** 100dvh statt 100vh verwenden, Scroll-Snap nur optional aktivieren, Interaktionen klar kennzeichnen

## Checkliste
- [ ] Scroll-Hinweis vorhanden und erkennbar.
- [ ] Inhalt bleibt bei deaktivierten Animationen verständlich.
- [ ] Kontrast- und Lesbarkeitswerte geprüft.
- [ ] Performance- und Accessibility-Test durchgeführt.

## Abhängigkeiten / Überschneidungen
- Hero- oder Storytelling-Komponenten
- Scroll- und Animationsutilities

## Akzeptanzkriterien
- Panels passen sich an unterschiedliche Viewport-Höhen an.
- Screenreader können Sektionen sequentiell durchlaufen.
- Keine unerwünschten Scroll-Fallen bei Tastatur- oder Touchbedienung.

## Beispiel / Code
```html
<section class="min-h-[100dvh] flex items-center justify-center">
  <div>Inhalt</div>
</section>
```

Bewertung der Relevanz 2025

⭐⭐⭐⭐☆ Wirkt stark, erfordert aber sorgfältige Nutzerführung.
