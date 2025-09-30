Layout: Chat Interface

Beschreibung

Dialoglayout mit Nachrichtenblasen und Eingabefeld.

Warum dieses Layout?

Für Support-Chats oder Messaging. Stärke: Echtzeitkommunikation; Schwäche: hohe Interaktionsanforderungen.

Anforderungen & Besonderheiten

Nachrichtenliste, Input, Statusanzeigen.

Responsiveness

Input fix am unteren Rand, Liste flexibel.

Accessibility

Live-Regionen für neue Nachrichten, Tastaturkürzel.

SEO

Für Web-Apps nicht relevant, aber strukturierter HTML für Indexierung.

Design-Guidelines

Unterscheidbare Sende- und Empfangsblasen.

Rechtliche / technische Randbedingungen (falls relevant)

DSGVO bei Chat-Logs beachten.

Umsetzung – Technische Leitplanken

Mobile First

Virtuelle Tastaturen berücksichtigen.

Accessibility

Screenreaderfreundliche Updates.

SEO

Kein SEO-Fokus, aber semantische Struktur.

Best Practices

Flexbox für Nachrichtenliste mit column.

Checkliste

[ ] zentrale Punkte prüfen

[ ] mobile Darstellung

[ ] Performance

[ ] Accessibility

Abhängigkeiten / Überschneidungen

Message-Komponente, Input, Presence-Status.

Akzeptanzkriterien

Fertig, wenn Nachrichtenliste scrollt, Eingabe funktioniert und Live-Region validiert ist.

Beispiel / Code

```html
<section class="chat">
  <ul class="messages">
    <li class="message message--in">Hallo</li>
  </ul>
  <form class="composer">
    <input type="text" placeholder="Antwort">
  </form>
</section>
```

Bewertung der Relevanz 2025

⭐⭐⭐⭐⭐
