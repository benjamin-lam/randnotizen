# Layout: Nested Columns

## Beschreibung
Mehrfach verschachtelte Spalten erzeugen komplexe Strukturen, die schwer zu pflegen und zu optimieren sind.

## Warum dieses Layout?
- Ermöglicht theoretisch sehr flexible Layouts.
- Kann alte Enterprise-Portale widerspiegeln.
- Führt zu hoher Komplexität, Wartungsaufwand und Performance-Problemen.

## Anforderungen & Besonderheiten
- **Responsiveness:** Verschachtelung auflösen und durch flachere Grids ersetzen.
- **Accessibility:** Lesereihenfolge testen, da verschachtelte Container häufig für Verwirrung sorgen.
- **SEO:** Semantische Struktur leidet, daher Content möglichst flach halten.
- **Design-Guidelines:** Grid Areas statt mehrfacher nested Columns bevorzugen.

## Umsetzung – Technische Leitplanken
- **Mobile First:** Auf flache Layouts migrieren und Nested Columns nur dokumentieren.
- **Accessibility:** Struktur mit Überschriften und Landmarken stabilisieren.
- **SEO:** Hauptinhalt im DOM priorisieren.
- **Best Practices:** Migration zu modernen Layouts planen, Komplexität reduzieren, Performance messen

## Checkliste
- [ ] Verschachtelungstiefe dokumentiert.
- [ ] Fallback-Layout vorhanden.
- [ ] Performanceprofil erhoben.
- [ ] A11y-Review durchgeführt.

## Abhängigkeiten / Überschneidungen
- Legacy-Grid-System
- Refactoring-Roadmap

## Akzeptanzkriterien
- Migration zu flacheren Strukturen geplant.
- Screenreader können Inhalte ohne Verlust wiedergeben.
- Keine neuen Features mehr auf Nested Columns aufbauen.

## Beispiel / Code
```html
<div class="grid grid-cols-12 gap-4">
  <div class="col-span-8">
    <div class="grid grid-cols-6 gap-2">…</div>
  </div>
</div>
```

> ⚠️ Deprecated: Nicht mehr empfohlen für Mobile-First-Designs (nur zu Dokumentationszwecken).

Bewertung der Relevanz 2025

⭐⭐☆☆☆ Nur zu Dokumentationszwecken für Legacy-Layouts.
