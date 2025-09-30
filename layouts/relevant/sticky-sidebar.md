# Layout: Sticky Sidebar

## Beschreibung
Eine Seitenleiste bleibt beim Scrollen sichtbar, während der Hauptinhalt weiterläuft. Sie eignet sich für Inhaltsverzeichnisse, Call-to-Actions oder sekundäre Navigation.

## Warum dieses Layout?
- Ermöglicht schnellen Zugriff auf Sprungziele oder CTAs.
- Verbessert Orientierung bei langen Inhalten.
- Kann auf kleinen Screens wertvollen Platz blockieren.

## Anforderungen & Besonderheiten
- **Responsiveness:** Sticky-Funktion nur auf großen Breakpoints aktiv, mobil alternative Platzierung.
- **Accessibility:** Fokusreihenfolge bewahren, Sticky-Element darf Inhalt nicht überdecken.
- **SEO:** Sidebar-Inhalte bleiben ergänzend und lenken nicht vom Hauptcontent ab.
- **Design-Guidelines:** Ausreichend Abstand zwischen Sidebar und Content, klare Abgrenzung.

## Umsetzung – Technische Leitplanken
- **Mobile First:** Sidebar zunächst unter Content platzieren, Sticky erst ab Desktop aktivieren.
- **Accessibility:** Skip-Link zu Sidebar anbieten und Fokusindikatoren sichtbar halten.
- **SEO:** Wichtige Links priorisieren und Redundanzen vermeiden.
- **Best Practices:** position: sticky mit top-Offset, Scrollbereich begrenzen, Sticky auf Touch testen

## Checkliste
- [ ] Sticky-Offset verhindert Überdeckung durch Header.
- [ ] Sidebar lässt sich mit Tastatur erreichen.
- [ ] Mobil existiert eine sinnvolle Alternative.
- [ ] Accessibility- und Performance-Prüfung erfolgt.

## Abhängigkeiten / Überschneidungen
- Table of Contents oder CTA-Module
- Layout-Utilities

## Akzeptanzkriterien
- Sidebar bleibt auf Desktop sichtbar ohne zu flackern.
- Mobil wird Sidebar sinnvoll eingereiht oder ausgeblendet.
- Screenreader erkennen Sidebar als ergänzenden Bereich.

## Beispiel / Code
```html
<aside class="sticky top-16">
  <nav>…</nav>
</aside>
```

Bewertung der Relevanz 2025

⭐⭐⭐⭐☆ Hilfreich für lange Artikel oder Dokumentationen.
