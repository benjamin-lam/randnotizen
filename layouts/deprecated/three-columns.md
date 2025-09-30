# Layout: Three Columns

## Beschreibung
Drei gleichbreite Spalten waren früher verbreitet, wirken heute aber überladen und sind mobil schwer nutzbar.

## Warum dieses Layout?
- Bietet viel Platz für Navigation, Inhalt und Zusatzmodule.
- Kann historische Portale abbilden.
- Auf mobilen Geräten entsteht häufig Scroll- und Priorisierungschaos.

## Anforderungen & Besonderheiten
- **Responsiveness:** Spalten müssen auf mobilen Geräten komplett gestapelt werden.
- **Accessibility:** Inhaltliche Priorisierung klar kommunizieren, Reihenfolge logisch halten.
- **SEO:** Wichtige Inhalte im DOM nach vorn ziehen, damit sie nicht von Sidebars verdrängt werden.
- **Design-Guidelines:** Große Weißräume zur Entzerrung nutzen, klare Typo-Hierarchie.

## Umsetzung – Technische Leitplanken
- **Mobile First:** Lieber ein- bis zweispaltige Alternativen wählen und Sidebars als Off-Canvas abbilden.
- **Accessibility:** DOM-Struktur nicht für rein visuelle Zwecke verbiegen.
- **SEO:** Hauptinhalt deutlich kennzeichnen.
- **Best Practices:** Spalten priorisieren, Off-Canvas prüfen, Reduzierte Inhalte bereitstellen

## Checkliste
- [ ] Keine horizontale Scrollbar entsteht.
- [ ] Reihenfolge der Spalten logisch.
- [ ] Sidebars enthalten nur unbedingt nötige Inhalte.
- [ ] A11y- und Performance-Check dokumentiert.

## Abhängigkeiten / Überschneidungen
- Historische Portallayouts
- Legacy-Navigationsmodule

## Akzeptanzkriterien
- Mobile Stack funktioniert ohne Layoutbruch.
- Screenreader erkennen Hauptinhalt zuerst.
- Stakeholder akzeptieren Ersatz- oder Migrationsplan.

## Beispiel / Code
```html
<section class="grid md:grid-cols-3 gap-4">
  <div>Spalte 1</div>
  <div>Spalte 2</div>
  <div>Spalte 3</div>
</section>
```

> ⚠️ Deprecated: Nicht mehr empfohlen für Mobile-First-Designs (nur zu Dokumentationszwecken).

Bewertung der Relevanz 2025

⭐⭐☆☆☆ Nur noch zur Pflege historischer Portale dokumentiert.
