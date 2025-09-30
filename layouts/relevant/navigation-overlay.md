Layout: Navigation Overlay

Beschreibung

Vollflächiges Navigations-Overlay, das auf Klick geöffnet wird.

Warum dieses Layout?

Für minimalistische Seiten oder mobile-first Menüs. Stärke: Fokus auf Navigation; Schwäche: zusätzlicher Klick.

Anforderungen & Besonderheiten

Overlay mit Animation, Close-Action, Fokus-Management.

Responsiveness

Mobile Standard, Desktop optional als Mega-Menü.

Accessibility

Fokus-Trap, aria-modal.

SEO

Links klar strukturiert, Crawler-freundlich.

Design-Guidelines

Kontrastreich, klare Linktypografie.

Rechtliche / technische Randbedingungen (falls relevant)

Pflichtlinks im Overlay zugänglich machen.

Umsetzung – Technische Leitplanken

Mobile First

Transition performant umsetzen.

Accessibility

Escape schließt Overlay.

SEO

Links serverseitig rendern.

Best Practices

Use dialog-Element als Basis.

Checkliste

[ ] zentrale Punkte prüfen

[ ] mobile Darstellung

[ ] Performance

[ ] Accessibility

Abhängigkeiten / Überschneidungen

Navigation, Button, Focus-Manager.

Akzeptanzkriterien

Fertig, wenn Overlay schnell reagiert und Fokus nach Schließen zurückkehrt.

Beispiel / Code

```html
<button data-overlay-open>Menü</button>
<nav class="overlay" hidden>
  <a href="#">Link</a>
</nav>
```

Bewertung der Relevanz 2025

⭐⭐⭐⭐☆
