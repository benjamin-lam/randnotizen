# Layout: SPA Shell Layout

## Beschreibung
Eine Single-Page-Application-Shell mit persistentem Header, Navigation und dynamischem Content-Bereich. Ideal für Web-Apps mit Client-Routing.

## Warum dieses Layout?
- Bietet app-ähnliches Nutzererlebnis mit schnellen Übergängen.
- Ermöglicht Code-Splitting und dynamische Komponentenauslieferung.
- Erfordert besondere Sorgfalt bei SEO und Initial-Ladezeit.

## Anforderungen & Besonderheiten
- **Responsiveness:** Shell-Elemente passen sich an mobile und Desktop-Viewports an, Navigation adaptiv.
- **Accessibility:** Routenwechsel ankündigen, Fokusmanagement und Skip-Links implementieren.
- **SEO:** SSR/SSG oder Prerendering nutzen, Meta-Handling pro Route.
- **Design-Guidelines:** Konsistente Shell-Komponenten, Spacing und Zustände für Ladeindikatoren.

## Umsetzung – Technische Leitplanken
- **Mobile First:** Navigation und Panels zuerst für Touch optimieren, Desktop mit erweiterten Flächen.
- **Accessibility:** Fokus nach Navigationswechsel auf Hauptbereich setzen, Live-Region optional.
- **SEO:** Sitemap und strukturierte Daten serverseitig bereitstellen.
- **Best Practices:** Code-Splitting per Route, Skeleton- oder Spinner-States, Service Worker für Assets

## Checkliste
- [ ] Routing funktioniert mit Browser-Historie und Deep Links.
- [ ] Fokus springt nach Route zum Hauptinhalt.
- [ ] Loading-States kommunizieren Status klar.
- [ ] Performance- und Accessibility-Audits durchgeführt.

## Abhängigkeiten / Überschneidungen
- Client-Router
- State- und Data-Layer

## Akzeptanzkriterien
- Shell bleibt persistent, Content tauscht ohne Full Reload.
- Screenreader werden über Routenwechsel informiert.
- CWV-Ziele trotz Client-Routing erreichbar.

## Beispiel / Code
```html
<div class="app-shell">
  <header>Navigation</header>
  <main id="app">Route-Content</main>
</div>
```

Bewertung der Relevanz 2025

⭐⭐⭐⭐⭐ Grundlage moderner Web-Applikationen.
