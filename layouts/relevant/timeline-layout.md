# Layout: Timeline Layout

## Beschreibung
Ein Zeitstrahl stellt Meilensteine, Prozesse oder Historien in chronologischer Reihenfolge dar.

## Warum dieses Layout?
- Visualisiert Abläufe und Entwicklungen klar.
- Unterstützt Storytelling mit Zeitbezug.
- Kann bei zu viel Text unübersichtlich werden.

## Anforderungen & Besonderheiten
- **Responsiveness:** Timeline wechselt von horizontaler/zweispaltiger Darstellung zu vertikal gestapelten Events.
- **Accessibility:** Semantisch als Liste oder geordnete Sektionen markieren, beschreibende Labels verwenden.
- **SEO:** Events mit Datum, Überschrift und optionalen strukturierten Daten (Event/HowTo).
- **Design-Guidelines:** Klare Marker, konsistente Abstände und ausreichender Kontrast zwischen Linien und Hintergrund.

## Umsetzung – Technische Leitplanken
- **Mobile First:** Beginnt als vertikale Liste mit deutlich gekennzeichneten Zeitpunkten.
- **Accessibility:** Fokusreihenfolge entlang des zeitlichen Verlaufs, Screenreader-Labels für Zeitangaben.
- **SEO:** Zeiteinträge mit <time>-Elementen versehen.
- **Best Practices:** Icons sparsam einsetzen, Tooltips für Details nur ergänzend, Scroll-Spy optional

## Checkliste
- [ ] Zeitpunkte sind chronologisch korrekt sortiert.
- [ ] Lesbarkeit auf kleinen Screens gewährleistet.
- [ ] Kontrastwerte der Marker geprüft.
- [ ] Accessibility- und Performance-Test erledigt.

## Abhängigkeiten / Überschneidungen
- Timeline-Komponente
- Icon- und Typografie-Tokens

## Akzeptanzkriterien
- Timeline lässt sich sowohl mit Maus als auch Tastatur durchlaufen.
- Screenreader geben Datum und Beschreibung verständlich wieder.
- Layout bricht auf mobilen Geräten nicht um.

## Beispiel / Code
```html
<ol class="timeline">
  <li>
    <time datetime="2024-01-01">Jan 2024</time>
    <p>Meilenstein</p>
  </li>
</ol>
```

Bewertung der Relevanz 2025

⭐⭐⭐⭐☆ Perfekt für Prozessdarstellungen und Unternehmenshistorien.
