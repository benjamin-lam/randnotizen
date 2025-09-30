# Layout: Sidebar Dropdown Menu

## Beschreibung
Eine vertikale Navigation mit ausklappbaren Unterpunkten strukturiert tiefe Inhaltsarchitekturen. Geeignet für Dokumentationen, Intranets oder komplexe Applikationen.

## Warum dieses Layout?
- Bietet schnellen Zugriff auf tiefe Hierarchien.
- Lässt sich mit Such- und Filterfunktionen kombinieren.
- Auf mobilen Geräten ist oft ein Off-Canvas-Pattern sinnvoller.

## Anforderungen & Besonderheiten
- **Responsiveness:** Sidebar kann zu Off-Canvas, Drawer oder Dropdown zusammenfallen.
- **Accessibility:** Menü folgt WAI-ARIA-Menü- oder Treeview-Pattern, Fokusmanagement klar geregelt.
- **SEO:** Interne Verlinkung stärkt Informationsarchitektur, aber Priorität liegt auf Hauptinhalten.
- **Design-Guidelines:** Indentation, Icons und aktive Zustände klar definieren.

## Umsetzung – Technische Leitplanken
- **Mobile First:** Navigation als Drawer oder Akkordeon ausspielen.
- **Accessibility:** Tab- und Pfeiltastensteuerung implementieren, sichtbare Fokusrahmen.
- **SEO:** Linktexte beschreibend formulieren und Hierarchie reflektieren.
- **Best Practices:** Maximal zwei Ebenen expandierbar, Suchfeld optional integrieren, Aktiven Pfad hervorheben

## Checkliste
- [ ] Dropdowns lassen sich Tastatur-gesteuert öffnen und schließen.
- [ ] Aktiver Navigationspfad ist visuell markiert.
- [ ] Mobile Darstellung ist getestet.
- [ ] A11y- und Performance-Checks dokumentiert.

## Abhängigkeiten / Überschneidungen
- Navigation-/Tree-Komponente
- Suche oder Filtermodul

## Akzeptanzkriterien
- Alle Ebenen sind mit Screenreader zugänglich.
- Fokus kehrt beim Schließen zum auslösenden Element zurück.
- Navigation kollidiert nicht mit Content-Scroll.

## Beispiel / Code
```html
<nav class="sidebar" aria-label="Hauptnavigation">
  <button aria-expanded="false" aria-controls="nav-1">Bereich</button>
  <ul id="nav-1" hidden>
    <li><a href="#">Unterpunkt</a></li>
  </ul>
</nav>
```

Bewertung der Relevanz 2025

⭐⭐⭐⭐☆ Wichtig für umfangreiche Inhaltsstrukturen auf Desktop.
