Layout: Sidebar Dropdown Menu

Beschreibung

Sidebar mit verschachtelten Dropdown-Navigationspunkten.

Warum dieses Layout?

Für komplexe Anwendungen mit vielen Sektionen. Stärke: hierarchische Navigation; Schwäche: kann überfordern.

Anforderungen & Besonderheiten

Zusammenklappbare Navigationsgruppen, aktive Zustände.

Responsiveness

Sidebar auf Mobil als Offcanvas.

Accessibility

ARIA-Attribute für expand/collapse.

SEO

Für Apps sekundär, dennoch semantische Listen.

Design-Guidelines

Aktiven Bereich deutlich hervorheben.

Rechtliche / technische Randbedingungen (falls relevant)

Pflichtlinks verfügbar halten.

Umsetzung – Technische Leitplanken

Mobile First

Offcanvas mit Focus-Trap.

Accessibility

Tastatursteuerung für Dropdowns.

SEO

Sitemap mit gleichen Links.

Best Practices

ARIA Authoring Practices für Treeviews.

Checkliste

[ ] zentrale Punkte prüfen

[ ] mobile Darstellung

[ ] Performance

[ ] Accessibility

Abhängigkeiten / Überschneidungen

Navigation, Iconography, Routing.

Akzeptanzkriterien

Fertig, wenn alle Menüpunkte erreichbar und Zustand gespeichert sind.

Beispiel / Code

```html
<nav class="sidebar">
  <button aria-expanded="false">Sektion</button>
  <ul hidden>
    <li><a href="#">Unterpunkt</a></li>
  </ul>
</nav>
```

Bewertung der Relevanz 2025

⭐⭐⭐⭐☆
