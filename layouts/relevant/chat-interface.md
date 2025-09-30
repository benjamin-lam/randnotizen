# Layout: Chat Interface

## Beschreibung
Ein Chat-Layout kombiniert Nachrichtenverlauf, Eingabefeld und Statusanzeigen für Echtzeitkommunikation.

## Warum dieses Layout?
- Schafft vertraute Interaktionsmuster für Support und Messaging.
- Unterstützt Live-Feedback durch Typing- und Online-Indikatoren.
- Erfordert DSGVO-konforme Speicherung und Logging-Konzepte.

## Anforderungen & Besonderheiten
- **Responsiveness:** Nachrichtenblasen passen sich an Breite an und erlauben Scrollen in der Historie.
- **Accessibility:** Live-Regionen für neue Nachrichten, klare Fokusführung und Tastaturkürzel.
- **SEO:** Für öffentliche Chats irrelevant, bei Chat-Logs optional strukturierte Daten.
- **Design-Guidelines:** Konsistente Bubble-Styles, Abstände und Statusfarben.

## Umsetzung – Technische Leitplanken
- **Mobile First:** Chat-Verlauf füllt Bildschirmhöhe, Eingabe bleibt fixiert.
- **Accessibility:** Role=log oder aria-live verwenden, Eingabefeld mit Label versehen.
- **SEO:** Server-Side-Rendering für Chat-Transkripte nur falls indexiert.
- **Best Practices:** Virtuelles Scrolling für lange Verläufe, Upload-Komponenten klar kennzeichnen, Shortcuts dokumentieren

## Checkliste
- [ ] Neue Nachrichten werden angekündigt ohne Fokus zu stehlen.
- [ ] Scroll-Position bei History-Load stabil.
- [ ] Eingabefeld funktioniert mit Tastaturkürzeln.
- [ ] Security/Privacy-Checks (Logging, Masking) abgeschlossen.

## Abhängigkeiten / Überschneidungen
- Realtime-/Websocket-Layer
- UI-Komponenten für Bubbles und Status

## Akzeptanzkriterien
- Chat bleibt auch bei hohem Nachrichtenaufkommen performant.
- Screenreader erhalten Updates über neue Nachrichten.
- Eingabefeld erfüllt Barrierefreiheitsanforderungen.

## Beispiel / Code
```html
<section class="chat">
  <div class="messages" role="log" aria-live="polite">
    <div class="message">Hallo</div>
  </div>
  <form class="composer">
    <input type="text" aria-label="Nachricht schreiben" />
    <button>Senden</button>
  </form>
</section>
```

Bewertung der Relevanz 2025

⭐⭐⭐⭐☆ Wesentlich für Service- und Collaboration-Produkte.
