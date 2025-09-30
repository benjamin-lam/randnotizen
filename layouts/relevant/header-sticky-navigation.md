# Layout: Header mit Sticky Navigation

## Beschreibung
Die Navigation bleibt beim Scrollen sichtbar und erleichtert schnellen Zugriff auf wichtige Bereiche. Geeignet für lange Seiten, Wissensdatenbanken oder Anwendungen mit häufigen Kontextwechseln.

## Warum dieses Layout?
- Verbessert Orientierung und Zugänglichkeit bei langen Seiten.
- Reduziert Interaktionskosten, weil Hauptnavigation immer erreichbar ist.
- Verbraucht vertikalen Raum, insbesondere auf mobilen Geräten.

## Anforderungen & Besonderheiten
- **Responsiveness:** Sticky-Verhalten an Breakpoints anpassen, damit auf kleinen Screens genug Inhalt sichtbar bleibt.
- **Accessibility:** Sichtbare Fokuszustände und sinnvolle Tab-Reihenfolge, keine Überblendung von Inhalten.
- **SEO:** Navigation bleibt semantisch als <nav> ausgezeichnet, ohne redundante Links.
- **Design-Guidelines:** Z-Index und Schatten definieren, um Überlagerungen zu vermeiden.

## Umsetzung – Technische Leitplanken
- **Mobile First:** Navigation verschlanken oder als kompakte Bar darstellen.
- **Accessibility:** Sticky-Header darf keine Inhalte überdecken; Skip-Link nach dem Header anbieten.
- **SEO:** Relevante Links priorisieren und doppelte Navigation vermeiden.
- **Best Practices:** CLS durch feste Höhen verhindern, Scroll-Hide/Show vorsichtig einsetzen, Sticky-Offset testen

## Checkliste
- [ ] Sticky-Header überdeckt keine Inhalte oder Fokusindikatoren.
- [ ] Tastatur- und Screenreader-Bedienung geprüft.
- [ ] Scroll-Verhalten auf Touch-Geräten getestet.
- [ ] Performance- und Accessibility-Audit durchgeführt.

## Abhängigkeiten / Überschneidungen
- Navigationskomponenten
- Scroll-Behaviour-Skripte

## Akzeptanzkriterien
- Header bleibt in allen Breakpoints funktional sticky.
- Skip-Link führt zum Beginn des Hauptinhalts.
- Navigation reagiert flüssig auf Scroll-Interaktionen.

## Beispiel / Code
```html
<header class="sticky top-0">…</header>
```

Bewertung der Relevanz 2025

⭐⭐⭐⭐⭐ Essentiell für informationsreiche oder lange Seiten.
