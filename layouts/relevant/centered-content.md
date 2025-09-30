# Layout: Centered Content

## Beschreibung
Der Inhalt wird auf eine begrenzte Breite zentriert, um den Fokus auf Texte oder Formulare zu lenken. Besonders nützlich für Storytelling-Seiten, Knowledge-Base-Einträge oder Conversion-Formulare.

## Warum dieses Layout?
- Steigert Lesbarkeit und Konzentration auf den Kerninhalt.
- Funktioniert hervorragend mit langen Texten oder wichtigen Interaktionen.
- Bietet wenig Raum für flankierende Elemente wie Werbung oder Toolbars.

## Anforderungen & Besonderheiten
- **Responsiveness:** Max-width im Bereich 68–76ch, adaptive Ränder und Padding.
- **Accessibility:** Ausreichender Zeilenabstand, klare Linkzustände und großzügige Schriftgrößen.
- **SEO:** Semantische Struktur mit klarer Priorisierung von Überschriften und Abschnitten.
- **Design-Guidelines:** Konsistentes Spacing, ruhige Farbpalette und typografische Hierarchie.

## Umsetzung – Technische Leitplanken
- **Mobile First:** Startet vollbreit und begrenzt ab größeren Breakpoints die Breite.
- **Accessibility:** Sorgt für ausreichende Kontrastwerte und unterstützt dynamische Schriftgrößen.
- **SEO:** Heading- und Absatzstruktur orientiert sich an inhaltlicher Priorität.
- **Best Practices:** max-width über clamp(), Padding per Spacing-Token, line-height von mindestens 1.5

## Checkliste
- [ ] Max-width zwischen 68–76 Zeichenbreite gesetzt.
- [ ] Kontraste für Text und Links geprüft.
- [ ] Content bleibt bei größerer Schriftgröße nutzbar.
- [ ] Core Web Vitals erreichen Zielwerte.

## Abhängigkeiten / Überschneidungen
- Typografie-Token
- Formular- und Content-Komponenten

## Akzeptanzkriterien
- Inhalte bleiben zentriert ohne horizontale Scrollleisten.
- Screenreader geben die Struktur logisch wieder.
- Responsives Verhalten für Formulare und Medien verifiziert.

## Beispiel / Code
```html
<main class="mx-auto max-w-prose p-4">…</main>
```

Bewertung der Relevanz 2025

⭐⭐⭐⭐⭐ Bewährtes Setup für fokussierte Inhalte und Formulare.
