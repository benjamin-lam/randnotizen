# Layout: Sidebar Navigation

## Beschreibung
Eine permanent sichtbare Sidebar-Navigation stammt aus Desktop-Zeiten und wird heute häufig von responsiven Drawern ersetzt.

## Warum dieses Layout?
- Bietet konstant sichtbare Navigationspunkte.
- Eignet sich für sehr breite Desktop-Layouts.
- Verbraucht mobil wertvollen Platz und wirkt veraltet.

## Anforderungen & Besonderheiten
- **Responsiveness:** Mobile Alternativen wie Off-Canvas oder Overlay bereitstellen.
- **Accessibility:** Navigation als <nav> kennzeichnen, Fokusmanagement für Drawer-Alternative.
- **SEO:** Links bleiben im DOM, Priorisierung auf Hauptinhalte achten.
- **Design-Guidelines:** Sichtbare aktive Zustände, klare Gruppierung von Links.

## Umsetzung – Technische Leitplanken
- **Mobile First:** Primär einen Drawer oder Overlay planen und Sidebar nur als Desktop-Variante pflegen.
- **Accessibility:** Tastaturbedienung sicherstellen, Skip-Link ergänzen.
- **SEO:** Duplicate Navigation vermeiden.
- **Best Practices:** Mobil Off-Canvas nutzen, Aktive Pfade markieren, Navigation vereinfachen

## Checkliste
- [ ] Off-Canvas-Alternative vorhanden.
- [ ] Fokusmanagement geprüft.
- [ ] Sidebar überdeckt keinen Content.
- [ ] A11y- und Performance-Check dokumentiert.

## Abhängigkeiten / Überschneidungen
- Drawer-/Overlay-Komponente
- Legacy-Navigationsstruktur

## Akzeptanzkriterien
- Mobil wird Sidebar ersetzt oder deaktiviert.
- Screenreader erreichen Navigation ohne Umwege.
- Stakeholder planen Migration zu moderneren Patterns.

## Beispiel / Code
```html
<aside class="sidebar-nav">
  <nav>
    <ul>
      <li><a href="#">Link</a></li>
    </ul>
  </nav>
</aside>
```

> ⚠️ Deprecated: Nicht mehr empfohlen für Mobile-First-Designs (nur zu Dokumentationszwecken).

Bewertung der Relevanz 2025

⭐⭐☆☆☆ Nur für Legacy-Interfaces dokumentiert.
