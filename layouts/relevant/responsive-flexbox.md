# Layout: Responsive Flexbox

## Beschreibung
Ein flexbasiertes Grundlayout nutzt Flexbox für Zeilen- und Spaltenanordnungen. Geeignet für einfache Dashboards, Formularlayouts oder Utility-Bereiche.

## Warum dieses Layout?
- Schnell einzurichten und vielseitig für kleinere Module.
- Erlaubt flexible Umsortierung und Ausrichtung ohne komplexes Grid.
- Bei komplexen Layouts stößt Flexbox an Grenzen gegenüber CSS Grid.

## Anforderungen & Besonderheiten
- **Responsiveness:** Flex-Container nutzen wrap, gap und order, um Breakpoints abzudecken.
- **Accessibility:** DOM-Reihenfolge bleibt logisch, auch wenn die visuelle Reihenfolge angepasst wird.
- **SEO:** Semantische Container (<section>, <article>) innerhalb der Flexstruktur verwenden.
- **Design-Guidelines:** Konsistente Gaps, Padding und Alignment-Regeln definieren.

## Umsetzung – Technische Leitplanken
- **Mobile First:** Flexrichtung zunächst Spalte, erweitert sich zu Reihen erst bei größeren Viewports.
- **Accessibility:** Visuelle Order-Änderungen nur einsetzen, wenn Fokusreihenfolge erhalten bleibt.
- **SEO:** Inhalte klar strukturieren, da Flexbox keine semantische Bedeutung liefert.
- **Best Practices:** flex-wrap aktivieren, Gap statt margin nutzen, Container Queries für Ausrichtung erwägen

## Checkliste
- [ ] Flex-Items brechen sauber um.
- [ ] Order-Manipulation beeinflusst Fokus nicht.
- [ ] Spacing entspricht Design-System.
- [ ] Performance- und Accessibility-Check erledigt.

## Abhängigkeiten / Überschneidungen
- Utility-Klassen oder Design-Tokens
- Layout-Komponenten

## Akzeptanzkriterien
- Layout verhält sich auf allen Breakpoints erwartungsgemäß.
- Screenreader erleben logische Reihenfolge.
- Flex-Gaps entsprechen definierten Abständen.

## Beispiel / Code
```html
<section class="flex flex-col md:flex-row gap-4 flex-wrap">
  <div class="flex-1">Block A</div>
  <div class="flex-1">Block B</div>
</section>
```

Bewertung der Relevanz 2025

⭐⭐⭐⭐⭐ Basispattern für viele responsive Komponenten.
