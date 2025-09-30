# Layout: Split Screen

## Beschreibung
Zwei Bereiche teilen sich die Breite, häufig Text und Bild oder ein Formular neben einer Vorschau. Ideal für Produktvorstellungen, Kampagnen oder Vergleichsdarstellungen.

## Warum dieses Layout?
- Erzeugt einen starken visuellen Kontrast zwischen Inhalt und Medien.
- Eignet sich für Storytelling mit parallelen Informationssträngen.
- Erfordert auf kleinen Screens sauberes Stapeln, damit nichts verloren geht.

## Anforderungen & Besonderheiten
- **Responsiveness:** Bricht auf mobilen Geräten in eine vertikale Reihenfolge um.
- **Accessibility:** DOM-Reihenfolge folgt der gewünschten Leselogik, Bilder mit aussagekräftigen Alternativtexten.
- **SEO:** Klare Überschriftenstruktur und relevante Meta-Texte für beide Bereiche.
- **Design-Guidelines:** Ausreichende Abstände, harmonische Typografie und abgestimmte Bildkomposition.

## Umsetzung – Technische Leitplanken
- **Mobile First:** Startet gestapelt und erweitert sich ab mittleren Breakpoints auf zwei Spalten.
- **Accessibility:** Sorgt für erkennbare Fokuszustände und sinnvolle Reihenfolge bei Tastaturbedienung.
- **SEO:** Betont wichtige Botschaften im Textbereich und nutzt beschreibende Alt-Texte.
- **Best Practices:** grid md:grid-cols-2 einsetzen, Bilder responsive laden, Scroll-Hinweise optional ergänzen

## Checkliste
- [ ] Bilder sind in passenden Größen optimiert.
- [ ] Text bleibt auch bei Reduktion der Breite lesbar.
- [ ] Tastaturnavigation folgt der inhaltlichen Reihenfolge.
- [ ] Performance- und Accessibility-Check dokumentiert.

## Abhängigkeiten / Überschneidungen
- Medien- und CTA-Komponenten
- Responsive Grid-Utilities

## Akzeptanzkriterien
- Split-Layout skaliert von mobil bis Desktop ohne Überlappungen.
- Bild und Text erhalten ausreichenden Kontrast.
- Screenreader greifen auf eine logische Reihenfolge zu.

## Beispiel / Code
```html
<section class="grid md:grid-cols-2">
  <div>Text</div>
  <div><img src="../../assets/agents-and-robots.png" alt="Agentin und Roboter in einer futuristischen Stadt bei Nacht" /></div>
</section>
```

Bewertung der Relevanz 2025

⭐⭐⭐⭐☆ Starkes Muster für bildstarke Kampagnen und Vergleiche.
