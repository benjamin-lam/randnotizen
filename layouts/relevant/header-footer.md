# Layout: Header & Footer Framework

## Beschreibung
Das Layout bildet die minimale Seitenstruktur aus Kopf- und Fußbereich, die andere Layouts erweitern. Es dient als Ausgangspunkt für Anwendungen, die ihre Inhalte dynamisch in <main> einfügen.

## Warum dieses Layout?
- Schafft ein konsistentes Grundgerüst für wiederkehrende Seiten.
- Erleichtert die Wiederverwendung von Navigations- und Footer-Komponenten.
- Allein nicht ausreichend, da der Hauptinhalt separat gestaltet werden muss.

## Anforderungen & Besonderheiten
- **Responsiveness:** Header- und Footer-Inhalte passen sich flexiblen Breiten an und bleiben lesbar.
- **Accessibility:** Landmark-Rollen nutzen, Skip-Link vorsehen und klare Fokusführung etablieren.
- **SEO:** Semantische Auszeichnung von Navigation, Logo und Pflichtlinks.
- **Design-Guidelines:** Ausreichende Padding-Werte, konsistente Typografie und klare Trennung zwischen Bereichen.

## Umsetzung – Technische Leitplanken
- **Mobile First:** Navigationsinhalte reduzieren und bei Bedarf als Burger-Menü bereitstellen.
- **Accessibility:** Skip-Link implementieren und Fokusindikatoren sichtbar halten.
- **SEO:** Footer für Kontakt- und Organisationsdaten nutzen und korrekt markieren.
- **Best Practices:** Sticky-Header nur bei Bedarf, Footer-Links gruppieren, Navigation logisch ordnen

## Checkliste
- [ ] Skip-Link führt zuverlässig zum Hauptinhalt.
- [ ] Navigation bleibt auch auf kleinen Screens bedienbar.
- [ ] Footer enthält alle Pflichtinformationen (Impressum, Datenschutz).
- [ ] Lighthouse-A11y-Check ohne kritische Fehler.

## Abhängigkeiten / Überschneidungen
- Globale Navigationskomponenten
- Footer-Link-Module

## Akzeptanzkriterien
- Header kollabiert responsiv ohne Layoutsprünge.
- Footer bleibt bei langen Seiten sichtbar und strukturiert.
- Screenreader erkennen die Landmarken korrekt.

## Beispiel / Code
```html
<header>…</header>
<main>Inhalt</main>
<footer>…</footer>
```

Bewertung der Relevanz 2025

⭐⭐⭐⭐☆ Solide Basis für Seiten mit dynamisch eingespeistem Content.
