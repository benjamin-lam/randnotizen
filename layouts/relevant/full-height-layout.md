# Layout: Full Height Layout

## Beschreibung
Das Layout streckt Container auf die volle Höhe des Viewports, um Inhalte mittig zu platzieren. Typisch für Login-Seiten, Splash-Screens oder Deckblätter.

## Warum dieses Layout?
- Erzeugt eine konzentrierte Bühne für einzelne Inhalte.
- Hilft, kurze Inhalte visuell zu zentrieren.
- Muss Browserleisten und kleine Displays berücksichtigen.

## Anforderungen & Besonderheiten
- **Responsiveness:** min-height: 100dvh mit sicherem Fallback für iOS/Android, Padding für kleinere Screens.
- **Accessibility:** Zentrierte Inhalte müssen bei Zoom und größeren Schriftgrößen funktionieren.
- **SEO:** Wichtige Botschaften im sichtbaren Bereich platzieren.
- **Design-Guidelines:** Kontrastreiche Hintergründe, klare Typografie und ausreichend Weißraum.

## Umsetzung – Technische Leitplanken
- **Mobile First:** Flexible Höhen nutzen und erst ab größeren Breakpoints strikte Full-Height-Anmutung einsetzen.
- **Accessibility:** Focus-Traps vermeiden und Skip-Links bereitstellen, falls weiterer Content folgt.
- **SEO:** Meta-Daten auf Kernbotschaften abstimmen.
- **Best Practices:** 100dvh statt 100vh, Content vertikal via flexbox zentrieren, Fallback bei Tastaturfokus testen

## Checkliste
- [ ] Viewport-Variationen getestet (iOS Safari, Android Chrome).
- [ ] Zentrierter Inhalt bleibt bei Zoom erreichbar.
- [ ] Kontrast und Lesbarkeit geprüft.
- [ ] A11y- und Performance-Check durchgeführt.

## Abhängigkeiten / Überschneidungen
- Hero- oder Auth-Komponenten
- Design-Tokens für Abstände

## Akzeptanzkriterien
- Layout bleibt ohne Scroll-Fallen nutzbar.
- Screenreader erreichen weitere Inhalte nach dem Full-Height-Block.
- Darstellung kollabiert nicht auf kleinen Displays.

## Beispiel / Code
```html
<section class="min-h-[100dvh] flex items-center justify-center p-8">
  <div>Inhalt</div>
</section>
```

Bewertung der Relevanz 2025

⭐⭐⭐⭐☆ Ideal für fokussierte Einstiegs- oder Login-Screens.
