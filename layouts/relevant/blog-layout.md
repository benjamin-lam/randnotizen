# Layout: Blog Layout

## Beschreibung
Dieses Layout kombiniert Listenansicht und Detailseite für Blogartikel. Es unterstützt Content-Marketing, Knowledge-Sharing und redaktionelle Veröffentlichungen.

## Warum dieses Layout?
- Optimiert für längere Texte mit klarer Leseführung.
- Ermöglicht flexible Kombination aus Karten, Prosa und Inhaltsverzeichnissen.
- Braucht sorgfältige Inhaltsplanung, um TL;DR-Effekte zu vermeiden.

## Anforderungen & Besonderheiten
- **Responsiveness:** Einspaltige Lesespalte mit optionalen Karten für Teaser und verwandte Artikel.
- **Accessibility:** Prose-Stile mit ausreichend Zeilenabstand und semantische Überschriften.
- **SEO:** Schema.org Article, OG-/Twitter-Tags und sprechende URLs.
- **Design-Guidelines:** Lesefreundliche Typografie, klare Trennung von Metadaten und Inhalt.

## Umsetzung – Technische Leitplanken
- **Mobile First:** Reduziert Nebenelemente und fokussiert auf den Artikelinhalt.
- **Accessibility:** Inhaltsverzeichnis als Navigationshilfe implementieren.
- **SEO:** Meta-Daten, strukturierte Daten und interne Verlinkung pflegen.
- **Best Practices:** Bildlazyloading, Lesefortschrittsanzeige optional, Semantische <article>-Elemente nutzen

## Checkliste
- [ ] Inhaltsverzeichnis verlinkt korrekt zu Abschnitten.
- [ ] Bilder besitzen Alt-Texte und Bildunterschriften.
- [ ] Lesefluss bleibt auch auf mobilen Geräten erhalten.
- [ ] SEO- und Accessibility-Prüfung bestanden.

## Abhängigkeiten / Überschneidungen
- Card- und Prosa-Komponenten
- Markdown/Content-Pipeline

## Akzeptanzkriterien
- Artikel lädt performant trotz langer Inhalte.
- Screenreader navigieren problemlos durch Überschriften.
- Verwandte Artikel werden semantisch korrekt ausgezeichnet.

## Beispiel / Code
```html
<main class="prose max-w-3xl mx-auto">
  <article>
    <h1>Titel</h1>
    <p>…</p>
  </article>
</main>
```

Bewertung der Relevanz 2025

⭐⭐⭐⭐⭐ Standard für Content-Marketing und Wissensvermittlung.
