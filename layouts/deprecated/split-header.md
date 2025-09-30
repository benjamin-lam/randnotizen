# Layout: Split Header

## Beschreibung
Ein geteiltes Header-Layout mit gegensätzlichen Ausrichtungen bricht auf kleinen Screens leicht und erschwert mobile Navigation.

## Warum dieses Layout?
- Kann komplexe Markenbotschaften transportieren.
- Erlaubt simultane Darstellung von Navigation und Aktionen.
- Skaliert auf mobilen Geräten schlecht und erhöht Implementierungsaufwand.

## Anforderungen & Besonderheiten
- **Responsiveness:** Header sollte auf mobile Breakpoints vereinfacht werden.
- **Accessibility:** Fokusreihenfolge sicherstellen, da Elemente weit auseinander liegen.
- **SEO:** Kein direkter Vorteil, Risiko von unklaren Hierarchien.
- **Design-Guidelines:** Branding und Aktionen priorisieren, redundante Inhalte streichen.

## Umsetzung – Technische Leitplanken
- **Mobile First:** Auf einfachere Header-Varianten umstellen und Split-Design nur dokumentieren.
- **Accessibility:** Skip-Link und klare Landmarken bieten.
- **SEO:** Wichtige Links logisch gruppieren.
- **Best Practices:** Frühe Reduktion auf einspaltige Navigation, Aktionen priorisieren, Übergangsanimationen vermeiden

## Checkliste
- [ ] Fallback-Header vorhanden.
- [ ] Navigation funktioniert auf Touch-Geräten.
- [ ] Fokus-Indikatoren sichtbar.
- [ ] A11y- und Performance-Prüfung dokumentiert.

## Abhängigkeiten / Überschneidungen
- Legacy-Header-Komponenten
- Branding-Richtlinien

## Akzeptanzkriterien
- Mobile Ersatzlayout implementiert.
- Screenreader navigieren Header ohne Verwirrung.
- Stakeholder planen Umstellung auf modernes Pattern.

## Beispiel / Code
```html
<header class="split-header">
  <div class="left">Logo</div>
  <div class="right">Aktionen</div>
</header>
```

> ⚠️ Deprecated: Nicht mehr empfohlen für Mobile-First-Designs (nur zu Dokumentationszwecken).

Bewertung der Relevanz 2025

⭐⭐☆☆☆ Nur noch aus historischen Gründen vermerkt.
