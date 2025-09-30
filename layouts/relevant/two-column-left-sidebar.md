Layout: Two Column Left Sidebar

Beschreibung

Zweispaltiges Layout mit linker Sidebar für Navigation oder Meta-Informationen.

Warum dieses Layout?

Eignet sich für Wissensbasen oder Dokumentationen, in denen sekundäre Informationen links verankert bleiben. Stärke: schnelle Orientierung; Schwäche: eingeschränkter Platz auf sehr kleinen Displays. Historisch aus Desktop-Portalen bekannt.

Anforderungen & Besonderheiten

Flexible Spaltenbreiten mit Priorisierung des Hauptinhalts.

Responsiveness

Sidebar unter Hauptinhalt stapeln, sobald wenig Platz vorhanden ist.

Accessibility

Sidebar als <nav> oder <aside> kennzeichnen und Sprunglinks vorsehen.

SEO

Klare Überschriftenstruktur im Content-Bereich, Breadcrumbs optional.

Design-Guidelines

Sidebar visuell absetzen, aber nicht dominieren lassen.

Rechtliche / technische Randbedingungen (falls relevant)

Bei Navigation rechtliche Pflichtlinks aufnehmen.

Umsetzung – Technische Leitplanken

Mobile First

Sidebar per Accordion ausklappbar machen.

Accessibility

Tab-Reihenfolge von links nach rechts prüfen.

SEO

Vermeide Duplicate Content zwischen Sidebar und Main.

Best Practices

CSS Grid oder Flexbox nutzen, keine Float-Layouts.

Checkliste

[ ] zentrale Punkte prüfen

[ ] mobile Darstellung

[ ] Performance

[ ] Accessibility

Abhängigkeiten / Überschneidungen

Nutzt globale Navigationskomponenten und Breadcrumbs.

Akzeptanzkriterien

Fertig, wenn Sidebar auf Mobilgeräten einklappbar und Tastaturbedienung geprüft ist.

Beispiel / Code

```html
<div class="layout layout--two-col-left">
  <aside>Sidebar</aside>
  <main>Inhalt</main>
</div>
```

Bewertung der Relevanz 2025

⭐⭐⭐⭐☆
