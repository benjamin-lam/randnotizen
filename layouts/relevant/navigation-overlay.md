# Layout: Navigation Overlay

## Beschreibung
Eine Vollbild-Navigation blendet sich über den Inhalt und eignet sich für minimalistische Seiten oder mobile Menüs.

## Warum dieses Layout?
- Lenkt volle Aufmerksamkeit auf Navigationsziele.
- Schafft klare, fokussierte Nutzerführung.
- Kann tiefe Hierarchien oder viele Links überfrachten.

## Anforderungen & Besonderheiten
- **Responsiveness:** Overlay deckt gesamte Viewports ab, Übergang von Burger-Icon zu Overlay.
- **Accessibility:** Dialog- oder Drawer-Pattern mit Fokus-Trap, aria-modal und ESC-Schließen.
- **SEO:** Navigation bleibt im DOM vorhanden, auch wenn sie überlagert.
- **Design-Guidelines:** Kontrastreiche Links, animierte Übergänge nur subtil.

## Umsetzung – Technische Leitplanken
- **Mobile First:** Overlay ist Standard, Desktop optional als sekundärer Einstieg.
- **Accessibility:** Fokus beim Öffnen auf erstes Element setzen, beim Schließen zurückführen.
- **SEO:** Wichtige Links bleiben crawlbar, Hidden-Attribute korrekt einsetzen.
- **Best Practices:** aria-modal verwenden, ESC- und Klick-Outside-Handling, Animationen mit prefers-reduced-motion abstimmen

## Checkliste
- [ ] Overlay öffnet und schließt mit Tastatur.
- [ ] Fokus bleibt innerhalb des Overlays gefangen.
- [ ] Links sind klar lesbar und kontrastreich.
- [ ] A11y- und Performance-Tests abgeschlossen.

## Abhängigkeiten / Überschneidungen
- Navigation-/Dialog-Komponente
- State-Management

## Akzeptanzkriterien
- Overlay erfüllt Dialog-Pattern-Anforderungen.
- Screenreader erhalten Ankündigung des Overlays.
- Interaktion funktioniert auch ohne Animationen.

## Beispiel / Code
```html
<nav class="overlay" aria-modal="true" hidden>
  <button class="close" aria-label="Menü schließen">×</button>
  <ul>
    <li><a href="#">Link</a></li>
  </ul>
</nav>
```

Bewertung der Relevanz 2025

⭐⭐⭐⭐☆ Starkes Pattern für fokussierte mobile Navigation.
