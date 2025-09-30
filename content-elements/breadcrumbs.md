# Content-Element: Breadcrumbs

## Beschreibung
Hierarchische Navigation zur Orientierung im Seitensystem.

## Warum dieses Element?
- Nutzer auf tiefen Kategoriestrukturen unterstützen.
- SEO-verbesserte Navigation mit strukturierter Daten-Auszeichnung bieten.
- Trade-off: Bei flacher Struktur wenig Mehrwert und zusätzlicher Pflegeaufwand.

## Anforderungen & Besonderheiten
- **Responsiveness:** Horizontale Liste, auf Mobile kürzen oder scrollen lassen.
- **Accessibility:** `nav` mit `aria-label`, Trennzeichen nur dekorativ.
- **SEO:** `BreadcrumbList`-Markup für Rich Snippets.
- **Design-Guidelines:** Dezente Typografie, ausreichende Abstände, Chevron-Icons optional.
- **Rechtliches:** Keine speziellen Anforderungen.

## Umsetzung – Technische Leitplanken
- **Mobile First:** Nur letzte zwei Ebenen zeigen, Rest einklappbar.
- **Accessibility:** Aktuelle Seite mit `aria-current=page` kennzeichnen.
- **SEO:** Links auf wichtige Kategorie-Seiten setzen, Duplicate vermeiden.
- **Best Practices:**
  - Automatisch aus URL/Navigation generieren.
  - Home-Link immer anbieten.
  - Trennzeichen als CSS-Pseudo-Element rendern.

## Checkliste
- [ ] Darstellung auf allen Breakpoints geprüft
- [ ] Barrierefreiheit (Fokus, ARIA, Kontrast) OK
- [ ] Semantik korrekt (HTML)
- [ ] Performance optimiert (Lazyload/Kompression)

## Abhängigkeiten / Überschneidungen
- Hauptnavigation, Routing

## Akzeptanzkriterien
- Technische Funktion OK
- Konsistenz zum Designsystem
- A11y & rechtliche Vorgaben erfüllt

## Beispiel / Code
[content-elements-examples/breadcrumbs.html](../content-elements-examples/breadcrumbs.html)

```html
<!-- Minimales, valides HTML-Beispiel -->
<nav aria-label="Breadcrumb">
  <ol class="breadcrumbs">
    <li><a href="/">Start</a></li>
    <li><a href="/shop">Shop</a></li>
    <li aria-current="page">Sneaker</li>
  </ol>
</nav>
```

Bewertung der Relevanz 2025

⭐⭐⭐⭐ Breadcrumbs bleiben wichtig für Orientierung und SEO.
