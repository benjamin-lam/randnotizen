# Content-Element: Table of Contents

## Beschreibung
Strukturierte Liste von Ankern, die durch längere Inhalte navigiert.

## Warum dieses Element?
- Lange Blog- oder Doku-Artikel navigierbar machen.
- FAQ- oder Richtlinientexte schnell erschließen.
- Trade-off: Pflegeaufwand, wenn Überschriften dynamisch generiert oder häufig geändert werden.

## Anforderungen & Besonderheiten
- **Responsiveness:** Sticky-Verhalten auf Desktop, ausklappbar auf Mobile.
- **Accessibility:** ARIA-Labeling für Navigation, Fokusreihenfolge beachten, Skip-Link anbieten.
- **SEO:** Sprungmarken unterstützen Sitelinks und Rich Snippets.
- **Design-Guidelines:** Klarer Abstand zum Inhalt, aktive Zustände markieren, dezente Typografie.
- **Rechtliches:** Keine speziellen Anforderungen.

## Umsetzung – Technische Leitplanken
- **Mobile First:** Als Akkordeon oder Dropdown starten und auf größeren Screens erweitern.
- **Accessibility:** `nav` mit `aria-label` nutzen, Fokuszustände gut sichtbar machen.
- **SEO:** Anker-IDs sprechend benennen, keine doppelten IDs.
- **Best Practices:**
  - Automatisierte Generierung aus der H-Struktur.
  - Aktuelle Sektion via Intersection Observer hervorheben.
  - Scroll-Offset für Fixed Header berücksichtigen.

## Checkliste
- [ ] Darstellung auf allen Breakpoints geprüft
- [ ] Barrierefreiheit (Fokus, ARIA, Kontrast) OK
- [ ] Semantik korrekt (HTML)
- [ ] Performance optimiert (Lazyload/Kompression)

## Abhängigkeiten / Überschneidungen
- Anchor-Links, Sticky-Header, Scrollspy

## Akzeptanzkriterien
- Technische Funktion OK
- Konsistenz zum Designsystem
- A11y & rechtliche Vorgaben erfüllt

## Beispiel / Code
```html
<!-- Minimales, valides HTML-Beispiel -->
<nav class="toc" aria-label="Inhaltsverzeichnis">
  <ol>
    <li><a href="#section-1">Einleitung</a></li>
    <li><a href="#section-2">Details</a></li>
  </ol>
</nav>
```

Bewertung der Relevanz 2025

⭐⭐⭐⭐ Längere Inhalte bleiben verbreitet, daher ist eine gute Orientierung weiter wichtig.
