# Layout: Tabbed Interface

## Beschreibung
Inhalte werden in Reitern organisiert und lassen sich per Tabs wechseln. Ideal für vergleichbare Inhalte, Produktdetails oder komprimierte Informationsbereiche.

## Warum dieses Layout?
- Strukturiert komplexe Inhalte übersichtlich.
- Reduziert Scrollwege und zeigt relevante Informationen kontextuell.
- Versteckt Inhalte hinter Interaktion, daher gute Kommunikation nötig.

## Anforderungen & Besonderheiten
- **Responsiveness:** Tabs sind horizontal oder in Dropdowns/Accordions überführbar.
- **Accessibility:** WAI-ARIA Tabs-Pattern mit role=tablist, tab und aria-controls nutzen.
- **SEO:** Wichtige Inhalte bleiben crawlbar und werden nicht verzögert nachgeladen.
- **Design-Guidelines:** Aktiver Tab klar markiert, konsistente Abstände und Hover/Fokus-Zustände.

## Umsetzung – Technische Leitplanken
- **Mobile First:** Tabs stapeln oder in ein horizontales Scroll-Menü wechseln.
- **Accessibility:** Keyboard-Steuerung mit Pfeiltasten, Home/End und Fokus-Management implementieren.
- **SEO:** Tab-Inhalte im DOM belassen, optional lazy load sekundärer Ressourcen.
- **Best Practices:** ARIA-Attribute korrekt setzen, Fokus sichtbar halten, State in URL optional spiegeln

## Checkliste
- [ ] Tab-Reihenfolge ist logisch und beschriftet.
- [ ] Fokus springt beim Wechsel zum aktiven Panel.
- [ ] Mobile Darstellung bleibt bedienbar.
- [ ] Accessibility- und Performance-Tests abgeschlossen.

## Abhängigkeiten / Überschneidungen
- Tabs-Komponente
- State-Management oder Router

## Akzeptanzkriterien
- Tabs erfüllen WAI-ARIA-Authoring-Practices.
- Aktives Panel wird beim Wechsel sofort sichtbar.
- Screenreader kündigen Tab-Status korrekt an.

## Beispiel / Code
```html
<div class="tabs" role="tablist">
  <button role="tab" aria-controls="panel-1" aria-selected="true">Tab 1</button>
  <button role="tab" aria-controls="panel-2">Tab 2</button>
</div>
<section id="panel-1" role="tabpanel">Inhalt 1</section>
<section id="panel-2" role="tabpanel" hidden>Inhalt 2</section>
```

Bewertung der Relevanz 2025

⭐⭐⭐⭐⭐ Beliebtes Muster zur Verdichtung thematisch verwandter Inhalte.
