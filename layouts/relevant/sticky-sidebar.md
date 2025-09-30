Layout: Sticky Sidebar

Beschreibung

Layout mit fixierter Sidebar, die beim Scrollen sichtbar bleibt.

Warum dieses Layout?

Ideal für Inhaltsverzeichnisse oder Kontextinfos. Stärke: schnelle Navigation; Schwäche: Platzverbrauch auf kleinen Screens.

Anforderungen & Besonderheiten

Sticky-Position mit Offset, fallback für Mobil.

Responsiveness

Sidebar mobil einklappen oder oben platzieren.

Accessibility

Skip-Links und Tastaturzugänglichkeit.

SEO

Sidebar-Inhalte nicht duplizieren.

Design-Guidelines

Leichte Abhebung und klare Typografie.

Rechtliche / technische Randbedingungen (falls relevant)

Pflichtlinks, wenn Sidebar rechtlich relevant.

Umsetzung – Technische Leitplanken

Mobile First

Sticky deaktivieren, wenn Viewport zu klein.

Accessibility

Focus-Verlust verhindern.

SEO

Content priorisieren.

Best Practices

Intersection Observer für aktive Abschnitte.

Checkliste

[ ] zentrale Punkte prüfen

[ ] mobile Darstellung

[ ] Performance

[ ] Accessibility

Abhängigkeiten / Überschneidungen

TOC-Komponente, Scrollspy.

Akzeptanzkriterien

Fertig, wenn Sticky-Verhalten smooth ist und keine Überlagerungen entstehen.

Beispiel / Code

```html
<div class="layout layout--sticky-sidebar">
  <aside class="sidebar">Inhaltsverzeichnis</aside>
  <main>Artikel</main>
</div>
```

Bewertung der Relevanz 2025

⭐⭐⭐⭐☆
