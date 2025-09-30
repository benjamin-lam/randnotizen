Layout: Tabbed Interface

Beschreibung

Registerkarten zur Strukturierung von Inhalten auf begrenztem Raum.

Warum dieses Layout?

Geeignet für Produktdetails oder Settings. Stärke: spart Platz; Schwäche: Inhalte hinter Tabs können übersehen werden.

Anforderungen & Besonderheiten

ARIA-konforme Tab-Navigation, Content-Panels.

Responsiveness

Tabs bei wenig Platz in Accordion überführen.

Accessibility

ARIA roles tablist, tab, tabpanel implementieren.

SEO

Wichtige Inhalte serverseitig rendern, nicht verstecken.

Design-Guidelines

Aktiven Tab klar hervorheben.

Rechtliche / technische Randbedingungen (falls relevant)

Vertragsrelevante Infos nicht verstecken.

Umsetzung – Technische Leitplanken

Mobile First

Tabs horizontal scrollbar oder Accordion.

Accessibility

Keyboard-Unterstützung für Pfeiltasten.

SEO

Inhalte indexierbar halten.

Best Practices

ARIA Authoring Practices folgen.

Checkliste

[ ] zentrale Punkte prüfen

[ ] mobile Darstellung

[ ] Performance

[ ] Accessibility

Abhängigkeiten / Überschneidungen

Tab-Komponente, Panel-Komponente.

Akzeptanzkriterien

Fertig, wenn Tabs klick- und per Tastatur bedienbar sind.

Beispiel / Code

```html
<div class="tabs">
  <button role="tab" aria-selected="true">Tab 1</button>
  <section role="tabpanel">Inhalt</section>
</div>
```

Bewertung der Relevanz 2025

⭐⭐⭐⭐☆
