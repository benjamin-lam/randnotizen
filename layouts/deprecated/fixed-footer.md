# Layout: Fixed Footer

## Beschreibung
Ein dauerhaft fixierter Footer verdeckt auf mobilen Geräten häufig Inhalte oder Steuerungen und wird daher nicht mehr empfohlen.

## Warum dieses Layout?
- Kann für spezielle App-Bars genutzt werden.
- Bietet permanente Sichtbarkeit für Aktionen.
- Verhindert sichtbaren Content und verursacht Bedienprobleme.

## Anforderungen & Besonderheiten
- **Responsiveness:** Nur in Ausnahmen aktivieren, ausreichend Abstand zum Content einplanen.
- **Accessibility:** Fokus und Screenreader dürfen nicht blockiert werden, Inhalte müssen erreichbar bleiben.
- **SEO:** Kein direkter Mehrwert, eher Risiko für schlechte UX.
- **Design-Guidelines:** Wenn unvermeidlich, transparente Hintergründe und ausreichende Höhen nutzen.

## Umsetzung – Technische Leitplanken
- **Mobile First:** Fixed Footer deaktivieren und stattdessen Sticky- oder Inline-Alternativen wählen.
- **Accessibility:** Skip-Link oder Close-Button bereitstellen, wenn Footer unvermeidlich.
- **SEO:** Keine übermäßigen Links im Footer platzieren.
- **Best Practices:** Nur kontextuell einsetzen, Touch-Ziele groß halten, CLS vermeiden

## Checkliste
- [ ] Footer kann bei Bedarf ausgeblendet werden.
- [ ] Inhalte bleiben vollständig sichtbar.
- [ ] Tastaturfokus nicht blockiert.
- [ ] A11y- und Performance-Check dokumentiert.

## Abhängigkeiten / Überschneidungen
- Legacy-App-Bars
- CTA-Module

## Akzeptanzkriterien
- Alternatives Pattern liegt vor.
- Screenreader können Inhalte hinter dem Footer erreichen.
- Stakeholder stimmen dem Rückbau zu.

## Beispiel / Code
```html
<footer class="fixed bottom-0 inset-x-0">
  <nav>…</nav>
</footer>
```

> ⚠️ Deprecated: Nicht mehr empfohlen für Mobile-First-Designs (nur zu Dokumentationszwecken).

Bewertung der Relevanz 2025

⭐⭐☆☆☆ Nur für Spezialfälle mit großer Vorsicht nutzen.
