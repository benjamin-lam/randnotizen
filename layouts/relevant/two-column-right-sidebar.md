# Layout: Two Column – Right Sidebar

## Beschreibung
Das Layout spiegelt die linke Sidebar-Variante und platziert zusätzliche Informationen rechts vom Content. Ideal für Produktseiten, Blogartikel mit Meta-Infos oder Supportbereiche.

## Warum dieses Layout?
- Bietet Platz für kontextuelle Hinweise oder CTAs neben dem Inhalt.
- Unterstützt vertraute Leseführung mit Hauptfokus auf der linken Spalte.
- Mobil müssen beide Spalten in sinnvoller Reihenfolge gestapelt werden.

## Anforderungen & Besonderheiten
- **Responsiveness:** Grid- oder Flex-Setup mit klaren Breakpoints für den Spaltenwechsel.
- **Accessibility:** DOM-Reihenfolge belässt den Hauptinhalt zuerst; Sidebar erhält <aside>-Landmarke.
- **SEO:** Sicherstellen, dass Search-Bots den Main-Content als primär erkennen.
- **Design-Guidelines:** Konsistente Spaltenbreiten und ausreichende Abstände zwischen Content und Sidebar.

## Umsetzung – Technische Leitplanken
- **Mobile First:** Stackt Content und Sidebar vertikal, Content bleibt zuerst.
- **Accessibility:** Tab-Reihenfolge überprüfen, insbesondere bei interaktiven Widgets in der Sidebar.
- **SEO:** Semantische Struktur mit klarer Kennzeichnung von Haupt- und Nebeninhalten.
- **Best Practices:** Spaltenbreiten per clamp(), Responsive Gaps für bessere Lesbarkeit, Sidebar-Inhalte priorisieren

## Checkliste
- [ ] Tab-Reihenfolge und Fokuszustände getestet.
- [ ] Visuelle Priorisierung zwischen Content und Sidebar abgestimmt.
- [ ] Mobile Stack wirkt nicht überladen.
- [ ] Performance- und Accessibility-Prüfung bestanden.

## Abhängigkeiten / Überschneidungen
- Promo- oder Widget-Module
- Globale Navigationsstruktur

## Akzeptanzkriterien
- Desktop-Spalten bleiben bei unterschiedlicher Höhe optisch ausbalanciert.
- Mobil wird der Hauptinhalt vor der Sidebar dargestellt.
- Screenreader erkennen die Sidebar als ergänzenden Bereich.

## Beispiel / Code
```html
<main class="grid grid-cols-12 gap-4">
  <article class="col-span-12 md:col-span-8">Inhalt</article>
  <aside class="col-span-12 md:col-span-4">Sidebar</aside>
</main>
```

Bewertung der Relevanz 2025

⭐⭐⭐⭐☆ Bewährtes Muster für produktnahe Inhalte mit Zusatzinfos.
