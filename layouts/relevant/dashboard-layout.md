# Layout: Dashboard Layout

## Beschreibung
Dashboards bündeln Karten, Tabellen und Diagramme in einer übersichtlichen Oberfläche. Sie kommen in Admin-Tools, Analytics-Lösungen oder SaaS-Plattformen zum Einsatz.

## Warum dieses Layout?
- Ermöglicht dichte Darstellung von Kennzahlen.
- Unterstützt modulare Widgets mit unterschiedlichen Größen.
- Benötigt durchdachtes Responsive-Verhalten und Priorisierung.

## Anforderungen & Besonderheiten
- **Responsiveness:** Grid-Areas passen sich an verfügbare Fläche an und erlauben Reordering.
- **Accessibility:** Tabellen, Charts und Widgets benötigen ARIA-Unterstützung und verständliche Labels.
- **SEO:** Bei öffentlichen Dashboards strukturierte Daten und semantische Überschriften verwenden.
- **Design-Guidelines:** Konsistente Spacing- und Farbskalen, klare Kartentitel und Statusindikatoren.

## Umsetzung – Technische Leitplanken
- **Mobile First:** Widgets stapeln und priorisieren, kritische Kennzahlen zuerst.
- **Accessibility:** Keyboard-Navigation für Widgets sicherstellen und Live-Regionen sparsam einsetzen.
- **SEO:** SSR oder statische Ausspielung für indexierbare Inhalte berücksichtigen.
- **Best Practices:** Grid-Areas definieren, Charts mit Textäquivalenten versehen, Skeleton-Loading für Datenabfragen

## Checkliste
- [ ] Widgets bleiben auch mobil lesbar.
- [ ] Fokuspfade für interaktive Module getestet.
- [ ] Charts haben beschreibende Alternativen.
- [ ] Performance-Monitoring implementiert.

## Abhängigkeiten / Überschneidungen
- Charting-Library
- Grid-System

## Akzeptanzkriterien
- Layout unterstützt individuelles Rearrangement ohne Layoutbruch.
- Screenreader können Kennzahlen interpretieren.
- Loading-States vermitteln klaren Status.

## Beispiel / Code
```html
<section class="grid lg:grid-cols-3 gap-4">…</section>
```

Bewertung der Relevanz 2025

⭐⭐⭐⭐☆ Bewährte Grundlage für datengetriebene Anwendungen.
