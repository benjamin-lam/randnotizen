# Layout: Two Column – Left Sidebar

## Beschreibung
Dieses Layout kombiniert eine linke Sidebar für Navigation oder Filter mit einem rechten Inhaltsbereich. Es eignet sich für Shops, Wissensdatenbanken oder umfangreiche Kategorie-Seiten.

## Warum dieses Layout?
- Ermöglicht eine prominente Platzierung sekundärer Navigation.
- Unterstützt schnelle Kontextwechsel zwischen Kategorien oder Filtern.
- Erfordert auf mobilen Geräten ein sinnvolles Umsortieren der Spalten.

## Anforderungen & Besonderheiten
- **Responsiveness:** CSS Grid oder Flex mit klar definierter Spaltenaufteilung und Umschaltung der Reihenfolge.
- **Accessibility:** Sidebar als <aside> mit aria-labelledby und Fokusmanagement auszeichnen.
- **SEO:** Sicherstellen, dass der Hauptinhalt im DOM vor der Sidebar kommt.
- **Design-Guidelines:** Konsistente Spaltenabstände und visuelle Abgrenzung zwischen Navigation und Content.

## Umsetzung – Technische Leitplanken
- **Mobile First:** Startet als gestapelte Ansicht, in der der Content vor der Sidebar steht.
- **Accessibility:** Steuert die DOM-Reihenfolge per CSS order, nicht über inhaltliche Umstellungen.
- **SEO:** Kennzeichnet Navigation mit strukturierten Listen und sprechenden Linktexten.
- **Best Practices:** CSS order sparsam einsetzen, aria-labelledby für Sidebar-Titel, Off-Canvas-Alternative evaluieren

## Checkliste
- [ ] Spaltenreihenfolge auf mobilen Breakpoints geprüft.
- [ ] Off-Canvas-Lösung für enge Viewports bewertet.
- [ ] Fokusreihenfolge und Skip-Link getestet.
- [ ] Performance- und Accessibility-Audit durchgeführt.

## Abhängigkeiten / Überschneidungen
- Filter- oder Navigationsmodule
- Layout-Grid-Token

## Akzeptanzkriterien
- Auf mobilen Geräten erscheint der Hauptinhalt vor der Sidebar.
- Desktop-Version hält stabile Spaltenbreiten bei unterschiedlichen Content-Längen.
- Tastaturnavigation erreicht Sidebar-Elemente in logischer Reihenfolge.

## Beispiel / Code
```html
<main class="grid grid-cols-12 gap-4">
  <article class="col-span-12 md:col-span-8 order-1">Inhalt</article>
  <aside class="col-span-12 md:col-span-4 order-0 md:order-2">Sidebar</aside>
</main>
```

Bewertung der Relevanz 2025

⭐⭐⭐⭐⭐ Häufiger Standard in Shops und wissenslastigen Seiten.
