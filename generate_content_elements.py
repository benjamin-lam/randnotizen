from pathlib import Path
base = Path('content-elements')
base.mkdir(exist_ok=True)

def write(entry):
    path = base / entry['file']
    example = entry['example_html'].strip('\n')
    content = f"# Content-Element: {entry['title']}\n\n"
    content += "## Beschreibung\n" + entry['description'] + "\n\n"
    content += "## Warum dieses Element?\n"
    for uc in entry['use_cases']:
        content += f"- {uc}\n"
    content += f"- {entry['tradeoff']}\n\n"
    content += "## Anforderungen & Besonderheiten\n"
    content += f"- **Responsiveness:** {entry['responsiveness']}\n"
    content += f"- **Accessibility:** {entry['accessibility']}\n"
    content += f"- **SEO:** {entry['seo']}\n"
    content += f"- **Design-Guidelines:** {entry['design']}\n"
    content += f"- **Rechtliches:** {entry['legal']}\n\n"
    content += "## Umsetzung – Technische Leitplanken\n"
    content += f"- **Mobile First:** {entry['mobile_first']}\n"
    content += f"- **Accessibility:** {entry['accessibility_impl']}\n"
    content += f"- **SEO:** {entry['seo_impl']}\n"
    content += "- **Best Practices:**\n"
    for bp in entry['best_practices']:
        content += f"  - {bp}\n"
    content += "\n## Checkliste\n"
    content += "- [ ] Darstellung auf allen Breakpoints geprüft\n"
    content += "- [ ] Barrierefreiheit (Fokus, ARIA, Kontrast) OK\n"
    content += "- [ ] Semantik korrekt (HTML)\n"
    content += "- [ ] Performance optimiert (Lazyload/Kompression)\n\n"
    content += "## Abhängigkeiten / Überschneidungen\n"
    content += f"- {entry['dependencies']}\n\n"
    content += "## Akzeptanzkriterien\n"
    content += "- Technische Funktion OK\n"
    content += "- Konsistenz zum Designsystem\n"
    content += "- A11y & rechtliche Vorgaben erfüllt\n\n"
    content += "## Beispiel / Code\n```html\n<!-- Minimales, valides HTML-Beispiel -->\n"
    content += example + "\n```\n\n"
    content += "Bewertung der Relevanz 2025\n\n"
    content += entry['rating'] + "\n"
    path.write_text(content, encoding='utf-8')

entries = []
entries.extend([
    {
        "file": "typography.md",
        "title": "Typography",
        "description": "Basis-Elemente für Textstruktur wie Überschriften, Absätze, Listen und Zitate, die Inhalte lesbar und hierarchisch gliedern.",
        "use_cases": [
            "Landingpages und Blogposts klar strukturieren.",
            "Dokumentationen und Wissensdatenbanken gliedern."
        ],
        "tradeoff": "Trade-off: Zu viele Formatvarianten erschweren Konsistenz und Pflege.",
        "responsiveness": "Schriftgrößen und Zeilenabstände fluid skalieren, Lesbarkeit auf allen Viewports sicherstellen.",
        "accessibility": "Semantische Heading-Hierarchie, ausreichender Kontrast, Fokusreihenfolge für Sprungmarken.",
        "seo": "Korrekte H-Struktur, strukturierte Inhalte, Schema für Zitate optional.",
        "design": "Definierte Typografie-Skala, konsistente Margins und Zeilenhöhen, Zustände für Links.",
        "legal": "Keine speziellen Anforderungen.",
        "mobile_first": "Basisgrößen für kleine Screens festlegen und nach oben progressiv vergrößern.",
        "accessibility_impl": "Screenreader-freundliche Hierarchie, Skip-Links für lange Inhalte.",
        "seo_impl": "Nur ein H1 pro Seite, Überschriften nicht für reines Styling missbrauchen.",
        "best_practices": [
            "Systemschrift-Fallbacks definieren.",
            "Zeilenlänge auf 60–80 Zeichen begrenzen.",
            "Listen mit `ul`/`ol` semantisch korrekt einsetzen."
        ],
        "dependencies": "Layout-Raster, Komponentenbibliothek",
        "example_html": "<article>\n  <h1>Überschrift H1</h1>\n  <p>Absatztext mit <strong>Betonung</strong> und <a href=\"#\">Link</a>.</p>\n  <h2>Liste</h2>\n  <ul>\n    <li>Listenpunkt</li>\n  </ul>\n  <blockquote>Zitat mit Quellenangabe.</blockquote>\n</article>",
        "rating": "⭐⭐⭐⭐⭐ Typografie bleibt Grundlage für jede Content-Seite und beeinflusst Lesbarkeit sowie SEO direkt."
    },
    {
        "file": "code-snippets.md",
        "title": "Code Snippets",
        "description": "Darstellung von Codebeispielen als Inline- oder Block-Elemente inkl. Kopierfunktion.",
        "use_cases": [
            "Developer-Dokumentationen und API-Referenzen präsentieren.",
            "How-to-Artikel mit konkreten Codeausschnitten anreichern."
        ],
        "tradeoff": "Trade-off: Syntax-Highlighting kann Performance und Barrierefreiheit beeinträchtigen, wenn schlecht umgesetzt.",
        "responsiveness": "Codeblöcke horizontal scrollbar machen, Inline-Code mit Wrap-Strategien versehen.",
        "accessibility": "ARIA-Labels für Kopier-Buttons, Screenreader-kompatible Spracheinstellung, ausreichender Kontrast.",
        "seo": "Strukturierte Daten für Code (`<pre><code>`) korrekt einsetzen, optionale `<figure>`-Einbettung.",
        "design": "Monospace-Fonts, dezente Hintergrundflächen, klare Abstände und Hover-/Focus-States für Aktionen.",
        "legal": "Keine speziellen Anforderungen.",
        "mobile_first": "Kurze Codezeilen bevorzugen, ansonsten Scrollcontainer mit sichtbarer Scrollbarkeit.",
        "accessibility_impl": "`aria-live`-Feedback für erfolgreiche Kopieraktionen, Fokusreihenfolge beibehalten.",
        "seo_impl": "Konsistente Sprachangabe per `lang`-Attribut, nicht renderrelevanten Code vermeiden.",
        "best_practices": [
            "Syntax-Highlighting serverseitig oder per leichtgewichtiges Skript.",
            "Kopier-Button erst nach dem Code rendern, um Tab-Reihenfolge logisch zu halten.",
            "Codeblöcke in `<figure>` mit `<figcaption>` erläutern."
        ],
        "dependencies": "Buttons, Clipboard-API, Syntax-Highlighting-Utility",
        "example_html": "<figure class=\"code-snippet\">\n  <figcaption>cURL-Beispiel</figcaption>\n  <pre><code>curl https://api.example.com/v1</code></pre>\n  <button type=\"button\" aria-label=\"Code kopieren\">Copy</button>\n</figure>",
        "rating": "⭐⭐⭐⭐⭐ Codebeispiele bleiben essenziell für Developer-Content und Wissensvermittlung."
    },
    {
        "file": "callout-box.md",
        "title": "Callout Box",
        "description": "Hervorgehobene Boxen für Hinweise, Warnungen oder Erfolgsnachrichten innerhalb von Inhalten.",
        "use_cases": [
            "Wichtige Hinweise in Dokumentationen oder Anleitungen hervorheben.",
            "Statusmeldungen in Knowledge-Base-Artikeln kommunizieren."
        ],
        "tradeoff": "Trade-off: Übermäßiger Einsatz verringert Aufmerksamkeit und führt zu Informationsrauschen.",
        "responsiveness": "Breite und Padding an Viewport anpassen, Icons skalierbar halten.",
        "accessibility": "Korrekte Rollen (`status`, `alert`) je nach Kontext, ausreichender Kontrast und Fokus für Links.",
        "seo": "Klarer Kontext im Fließtext, optionale `<aside>`-Semantik.",
        "design": "Farbcodierte Varianten (Info, Warnung, Erfolg), konsistente Typografie und Iconografie.",
        "legal": "Keine speziellen Anforderungen.",
        "mobile_first": "Vertikale Layouts bevorzugen, Icons oberhalb des Textes platzieren, wenn Platz fehlt.",
        "accessibility_impl": "Rollen nur bei dynamischen Updates setzen, sonst semantisch neutral halten.",
        "seo_impl": "Boxen nicht für kritische Überschriften missbrauchen, semantisch im Textfluss belassen.",
        "best_practices": [
            "Varianten in Designsystem definieren.",
            "Icons als dekorativ markieren (`aria-hidden`).",
            "Nicht mehr als zwei Callouts pro Bildschirmhöhe verwenden."
        ],
        "dependencies": "Iconset, Alert-Komponenten",
        "example_html": "<aside class=\"callout callout--info\">\n  <h3 class=\"callout__title\">Hinweis</h3>\n  <p>Bitte sichern Sie Ihre Daten regelmäßig.</p>\n</aside>",
        "rating": "⭐⭐⭐⭐ Callouts unterstützen Lesbarkeit, sollten aber gezielt eingesetzt werden."
    },
    {
        "file": "table-of-contents.md",
        "title": "Table of Contents",
        "description": "Strukturierte Liste von Ankern, die durch längere Inhalte navigiert.",
        "use_cases": [
            "Lange Blog- oder Doku-Artikel navigierbar machen.",
            "FAQ- oder Richtlinientexte schnell erschließen."
        ],
        "tradeoff": "Trade-off: Pflegeaufwand, wenn Überschriften dynamisch generiert oder häufig geändert werden.",
        "responsiveness": "Sticky-Verhalten auf Desktop, ausklappbar auf Mobile.",
        "accessibility": "ARIA-Labeling für Navigation, Fokusreihenfolge beachten, Skip-Link anbieten.",
        "seo": "Sprungmarken unterstützen Sitelinks und Rich Snippets.",
        "design": "Klarer Abstand zum Inhalt, aktive Zustände markieren, dezente Typografie.",
        "legal": "Keine speziellen Anforderungen.",
        "mobile_first": "Als Akkordeon oder Dropdown starten und auf größeren Screens erweitern.",
        "accessibility_impl": "`nav` mit `aria-label` nutzen, Fokuszustände gut sichtbar machen.",
        "seo_impl": "Anker-IDs sprechend benennen, keine doppelten IDs.",
        "best_practices": [
            "Automatisierte Generierung aus der H-Struktur.",
            "Aktuelle Sektion via Intersection Observer hervorheben.",
            "Scroll-Offset für Fixed Header berücksichtigen."
        ],
        "dependencies": "Anchor-Links, Sticky-Header, Scrollspy",
        "example_html": "<nav class=\"toc\" aria-label=\"Inhaltsverzeichnis\">\n  <ol>\n    <li><a href=\"#section-1\">Einleitung</a></li>\n    <li><a href=\"#section-2\">Details</a></li>\n  </ol>\n</nav>",
        "rating": "⭐⭐⭐⭐ Längere Inhalte bleiben verbreitet, daher ist eine gute Orientierung weiter wichtig."
    },
    {
        "file": "table.md",
        "title": "Table",
        "description": "Tabellarische Darstellung von Daten mit Headern, Spalten und optionaler Sortierung.",
        "use_cases": [
            "Vergleichstabellen für Spezifikationen oder Features.",
            "Reporting- oder Statistik-Daten innerhalb von Artikeln darstellen."
        ],
        "tradeoff": "Trade-off: Viele Spalten auf kleinen Screens erschweren Lesbarkeit, erfordern alternative Layouts.",
        "responsiveness": "Scrollbare Container oder Kartenlayout für mobile Endgeräte bereitstellen.",
        "accessibility": "Korrekte `<th>`-Zuordnungen, `scope`/`headers` einsetzen, ausreichend Kontrast.",
        "seo": "Saubere Tabellenstruktur unterstützt Featured Snippets.",
        "design": "Konsistente Zellabstände, zebra stripes optional, klare Sortier-Icons.",
        "legal": "Keine speziellen Anforderungen.",
        "mobile_first": "Wichtige Spalten priorisieren, horizontales Scrollen klar kennzeichnen.",
        "accessibility_impl": "Sortier-Buttons mit `aria-sort` pflegen, Tabellenzusammenfassung (`caption`) nutzen.",
        "seo_impl": "Relevante Keywords in Header-Zellen platzieren, keine leeren Zellen.",
        "best_practices": [
            "Tabellen mit `<caption>` einführen.",
            "Responsives Verhalten testen (Stacking, Scroll).",
            "Sortierung und Filterung server- oder clientseitig konsistent halten."
        ],
        "dependencies": "Filter, Sortier-Controls, Datenquellen",
        "example_html": "<table class=\"data-table\">\n  <caption>Leistungsdaten</caption>\n  <thead>\n    <tr><th scope=\"col\">Feature</th><th scope=\"col\">Wert</th></tr>\n  </thead>\n  <tbody>\n    <tr><th scope=\"row\">Latenz</th><td>120 ms</td></tr>\n  </tbody>\n</table>",
        "rating": "⭐⭐⭐⭐ Datenvisualisierung bleibt kritisch, responsive Tabellen sind unverzichtbar."
    }
])
entries.extend([
    {
        "file": "image-with-caption.md",
        "title": "Image with Caption",
        "description": "Bilddarstellung mit erläuternder Bildunterschrift.",
        "use_cases": [
            "Produktfotos oder Screenshots mit erklärender Caption einsetzen.",
            "Blogartikel mit Bildnachweisen oder Quellenangaben versehen."
        ],
        "tradeoff": "Trade-off: Große Bilder beeinflussen Ladezeiten, erfordern Optimierung.",
        "responsiveness": "Fluides Verhalten, `srcset`/`sizes` nutzen, Captions unterhalb anordnen.",
        "accessibility": "Alternativtexte bereitstellen, Caption als ergänzende Beschreibung, ausreichender Kontrast.",
        "seo": "Alt-Texte und strukturierte Daten (`figure`, `figcaption`) verbessern Bild-Sichtbarkeit.",
        "design": "Bildgrößen definieren, Weißraum um Caption, Typografie harmonisch.",
        "legal": "Bildrechte beachten, Quellenangabe bei Lizenzanforderung integrieren.",
        "mobile_first": "Bilder zunächst klein laden, progressive Vergrößerung via `srcset`.",
        "accessibility_impl": "Kontrast für Text auf Caption-Hintergrund sicherstellen, keine rein dekorativen Captions.",
        "seo_impl": "Dateinamen beschreibend, Lazyloading (`loading=\"lazy\"`) einsetzen.",
        "best_practices": [
            "Moderne Formate (WebP/AVIF) mit Fallback anbieten.",
            "Responsive Container mit `max-width` begrenzen.",
            "Caption optional mit Quellenlink versehen."
        ],
        "dependencies": "Bild-CDN, Lightbox (optional)",
        "example_html": "<figure class=\"image\">\n  <img src=\"/assets/agents-and-robots.png\" alt=\"Agentin und Roboter in einer futuristischen Stadt bei Nacht\" loading=\"lazy\">\n  <figcaption>Agentin und Roboter beobachten die Stadtlichter.</figcaption>\n</figure>",
        "rating": "⭐⭐⭐⭐ Bilder mit Kontext bleiben wichtig für Storytelling und Compliance."
    },
    {
        "file": "image-carousel.md",
        "title": "Image Carousel",
        "description": "Slider-Komponente für mehrere Bilder mit optionaler Lightbox.",
        "use_cases": [
            "Produktgalerien auf E-Commerce-Seiten.",
            "Event- oder Referenz-Slideshows auf Landingpages."
        ],
        "tradeoff": "Trade-off: Zu viele Slides reduzieren Aufmerksamkeit, Interaktion oft gering.",
        "responsiveness": "Touch- und Mausbedienung, Breakpoints für Anzahl sichtbarer Slides.",
        "accessibility": "Fokusreihenfolge, `aria-live` für Slide-Wechsel, Pause-/Play-Controls.",
        "seo": "Bilder mit Alt-Text und Lazyload, Lightbox nicht indexrelevant.",
        "design": "Navigationselemente konsistent, Dot-/Arrow-Styling, Übergänge dezent.",
        "legal": "Bildrechte beachten, Tracking in Lightbox vermeiden.",
        "mobile_first": "Einzelne Slides, Swipe-Gesten, geringe Dateigrößen.",
        "accessibility_impl": "Autoplay standardmäßig deaktiviert, klare Fokusindikatoren.",
        "seo_impl": "`loading=\"lazy\"`, strukturierte Daten für Produktbilder möglich.",
        "best_practices": [
            "Slides per Keyboard navigierbar machen.",
            "Progressive Enhancement bei deaktiviertem JS.",
            "Bildvorab-Laden für nächstes Slide optimieren."
        ],
        "dependencies": "Slider-Library, Lightbox, Bild-CDN",
        "example_html": "<div class=\"carousel\" aria-roledescription=\"Karussell\">\n  <button class=\"carousel__prev\" aria-label=\"Vorheriges Bild\">‹</button>\n  <ul class=\"carousel__track\">\n    <li class=\"carousel__slide\"><img src=\"/assets/agents-and-robots.png\" alt=\"Agentin und Roboter in einer futuristischen Stadt bei Nacht\" loading=\"lazy\"></li>\n  </ul>\n  <button class=\"carousel__next\" aria-label=\"Nächstes Bild\">›</button>\n</div>",
        "rating": "⭐⭐⭐⭐ Karussells bleiben gängig, müssen jedoch nutzerzentriert optimiert werden."
    },
    {
        "file": "video-embed.md",
        "title": "Video Embed",
        "description": "Einbettung von Videos mit Poster, Controls und optionaler Lazyload-Lösung.",
        "use_cases": [
            "Produktdemos oder Tutorials direkt im Content zeigen.",
            "Kundenreferenzen oder Interviews einbetten."
        ],
        "tradeoff": "Trade-off: Streaming kann Performance belasten und Datenschutzpflichten auslösen.",
        "responsiveness": "Aspect-Ratio-Container, adaptive Playergröße.",
        "accessibility": "Untertitel, Transkript und Tastaturbedienbarkeit sicherstellen.",
        "seo": "Schema.org VideoObject, sprechende Titles und Thumbnails.",
        "design": "Posterbild definieren, Player-Farben ans Designsystem anpassen.",
        "legal": "Einbettung externer Plattformen nur mit DSGVO-konformer Einwilligung und Hinweis auf Datenübertragung.",
        "mobile_first": "Automatisch muted starten, adaptive Bitrate, Bandbreite berücksichtigen.",
        "accessibility_impl": "`controls` aktivieren, Untertiteldateien (`track`) anbieten, Fokusmanagement prüfen.",
        "seo_impl": "Lazyload über Consent-Gate lösen, strukturierte Daten bereitstellen.",
        "best_practices": [
            "Posterbilder optimiert bereitstellen (WebP).",
            "Fallback-Link zum Download oder externen Player anbieten.",
            "Consent-Management für YouTube/Vimeo integrieren."
        ],
        "dependencies": "Consent-Tool, CDN/Player, Transkript",
        "example_html": "<figure class=\"video\">\n  <video controls preload=\"none\" poster=\"video-poster.webp\">\n    <source src=\"demo.mp4\" type=\"video/mp4\">\n    <track kind=\"captions\" src=\"demo-de.vtt\" srclang=\"de\" label=\"Deutsch\">\n    Ihr Browser unterstützt das Video-Element nicht.\n  </video>\n  <figcaption>Kurze Produktdemo.</figcaption>\n</figure>",
        "rating": "⭐⭐⭐⭐ Videoinhalte gewinnen weiter an Relevanz, müssen aber datenschutzkonform bereitgestellt werden."
    },
    {
        "file": "audio-embed.md",
        "title": "Audio Embed",
        "description": "Einbettung eines Audio- oder Podcast-Players.",
        "use_cases": [
            "Podcastepisoden im Blog bereitstellen.",
            "Audio-Zitate oder Interviews ergänzend zum Text anbieten."
        ],
        "tradeoff": "Trade-off: Autoplay oder zu große Dateien beeinträchtigen Nutzererlebnis.",
        "responsiveness": "Player skalierbar, Bedienelemente ausreichend groß.",
        "accessibility": "Transkripte bereitstellen, Tastaturbedienung sicherstellen.",
        "seo": "Schema.org AudioObject, sprechende Dateinamen.",
        "design": "Player-Farben und States definieren, Fortschrittsanzeige klar.",
        "legal": "Urheberrechte, Lizenzen und ggf. GEMA-Klärung beachten.",
        "mobile_first": "Streaming adaptiv, Download-Option optional.",
        "accessibility_impl": "`aria-labels` für Buttons, Lautstärkeregelung per Tastatur erreichbar.",
        "seo_impl": "Transkript als HTML bereitstellen, Metadaten im Head ergänzen.",
        "best_practices": [
            "Ladezeiten durch Kompression (AAC/Opus) optimieren.",
            "Player erst nach Interaktion laden (Lazyload).",
            "Download-Link und Episodennotizen bereitstellen."
        ],
        "dependencies": "Media-Player, CDN, Transkript",
        "example_html": "<figure class=\"audio\">\n  <figcaption>Podcast Folge 12</figcaption>\n  <audio controls preload=\"none\">\n    <source src=\"podcast-12.mp3\" type=\"audio/mpeg\">\n    Ihr Browser unterstützt das Audio-Element nicht.\n  </audio>\n</figure>",
        "rating": "⭐⭐⭐⭐ Audio ist für Content-Marketing weiterhin relevant, vor allem für barrierefreie Alternativen."
    },
    {
        "file": "map-embed.md",
        "title": "Map Embed",
        "description": "Interaktive Karte zur Standortanzeige oder Wegbeschreibung.",
        "use_cases": [
            "Standortübersicht auf Kontakt- oder Filialseiten.",
            "Event-Locations oder Veranstaltungsorte darstellen."
        ],
        "tradeoff": "Trade-off: Externe Maps erhöhen Ladezeit und bergen Datenschutzrisiken.",
        "responsiveness": "Adaptive Höhe/Breite, Touch-Gesten unterstützen.",
        "accessibility": "Alternativbeschreibung und Adresse als Text, Fokusfalle vermeiden.",
        "seo": "Strukturierte Daten für Organisation/LocalBusiness, statische Karte als Fallback.",
        "design": "Kartenrahmen, Marker-Branding, klare Buttons.",
        "legal": "DSGVO-konforme Einwilligung vor Laden externer Dienste (Google Maps), Datenschutzhinweis bereitstellen.",
        "mobile_first": "Statische Karte oder Screenshot bis Interaktion, geringe Datenlast.",
        "accessibility_impl": "Tastaturbedienung prüfen, Zoomkontrollen beschriftet, Adresse zusätzlich in HTML.",
        "seo_impl": "`loading=\"lazy\"` für iframes, strukturierte Adresse in Microdata.",
        "best_practices": [
            "Privacy-Proxy oder Selbsthosting (OSM) bevorzugen.",
            "Fallback-Link zu Routenplanung anbieten.",
            "Interaktion nur nach Consent aktivieren."
        ],
        "dependencies": "Consent-Tool, Map-Provider, Standortdaten",
        "example_html": "<section class=\"map\">\n  <button type=\"button\" data-action=\"load-map\">Karte laden (externer Inhalt)</button>\n  <p>Adresse: Beispielstraße 1, 12345 Musterstadt</p>\n</section>",
        "rating": "⭐⭐⭐⭐ Standortinformationen bleiben wichtig, Datenschutzanforderungen steigen jedoch."
    },
    {
        "file": "tooltip.md",
        "title": "Tooltip",
        "description": "Kurze Hilfetexte, die bei Hover oder Fokus zusätzliche Informationen geben.",
        "use_cases": [
            "Formularfelder mit Kontextinformationen versehen.",
            "Tabellenwerte oder Icons erläutern, ohne Layout zu überladen."
        ],
        "tradeoff": "Trade-off: Nicht auf Touch-Geräten verfügbar, daher alternative Darstellung nötig.",
        "responsiveness": "Positionierung relativ zum Trigger, auf Mobile ggf. als Inline-Hinweis.",
        "accessibility": "`aria-describedby` verwenden, Fokus-Management beachten.",
        "seo": "Kein direkter Einfluss, Inhalte sollten auch ohne Tooltip verfügbar sein.",
        "design": "Klarer Kontrast, dezente Animation, Pfeile optional.",
        "legal": "Keine speziellen Anforderungen.",
        "mobile_first": "Tooltip als Click-to-toggle oder Inline-Expand umsetzen.",
        "accessibility_impl": "Tooltip bei Fokus sichtbar halten, Escape zum Schließen ermöglichen.",
        "seo_impl": "Tooltip-Inhalte nicht exklusiv halten, immer auch im Fließtext erwähnen.",
        "best_practices": [
            "Trigger als Button oder Link deklarieren.",
            "Tooltip mit `role=\"tooltip\"` und IDs verknüpfen.",
            "Autohide mit Verzögerung, um Flickern zu vermeiden."
        ],
        "dependencies": "Popover-System, Focus-Management",
        "example_html": "<button type=\"button\" aria-describedby=\"tip-id\">?\n</button>\n<span id=\"tip-id\" role=\"tooltip\">Erklärt das Feld</span>",
        "rating": "⭐⭐⭐⭐ Tooltips bleiben relevant, solange Touch-Alternativen berücksichtigt werden."
    },
    {
        "file": "popover.md",
        "title": "Popover",
        "description": "Kontextbezogene Overlays mit weiterführenden Inhalten oder Aktionen.",
        "use_cases": [
            "Detailinformationen in Tabellen oder Dashboards anzeigen.",
            "Kleine Formulare oder Aktionen ohne Seitenwechsel anbieten."
        ],
        "tradeoff": "Trade-off: Zu komplexe Inhalte in kleinen Overlays beeinträchtigen Usability.",
        "responsiveness": "Auf Mobile bildschirmfüllend oder als Bottom Sheet darstellen.",
        "accessibility": "Fokusmanagement, `aria-modal` bei exklusiven Popovern, Escape zum Schließen.",
        "seo": "Dynamische Inhalte nicht indexrelevant, daher im DOM verfügbar halten.",
        "design": "Schatten, Abstände, Pfeile anpassen, klare Close-Icons.",
        "legal": "Keine speziellen Anforderungen.",
        "mobile_first": "Popover als Vollbild-Overlay oder expandierbaren Bereich planen.",
        "accessibility_impl": "Fokus auf erstes interaktives Element setzen, Rücksprung zum Trigger ermöglichen.",
        "seo_impl": "Inhalte serverseitig rendern, falls für SEO wichtig.",
        "best_practices": [
            "Offene Popover schließen, wenn außerhalb geklickt wird.",
            "Transitions kurz halten (<200 ms).",
            "Popover-Größe begrenzen und Scroll innerhalb erlauben."
        ],
        "dependencies": "Dialog-System, Overlay-Layer, Focus-Trap",
        "example_html": "<button type=\"button\" aria-haspopup=\"dialog\" aria-expanded=\"false\">Details</button>\n<div class=\"popover\" role=\"dialog\" hidden>\n  <h3>Mehr Infos</h3>\n  <p>Zusätzliche Details.</p>\n  <button type=\"button\" class=\"popover__close\">Schließen</button>\n</div>",
        "rating": "⭐⭐⭐⭐ Popover bleiben vielseitig, benötigen aber klare Regeln für Mobile und A11y."
    },
    {
        "file": "modal.md",
        "title": "Modal",
        "description": "Dialog-Overlay, das den restlichen Inhalt überlagert und fokussierte Interaktion verlangt.",
        "use_cases": [
            "Bestätigungsdialoge oder wichtige Hinweise anzeigen.",
            "Formulare oder Medien ohne Seitenwechsel bereitstellen."
        ],
        "tradeoff": "Trade-off: Unterbrechung des Nutzerflusses, daher sparsam einsetzen.",
        "responsiveness": "Auf kleinen Screens fullscreen, auf Desktop zentriert mit max-width.",
        "accessibility": "Focus-Trap, `aria-modal`, Escape-Handling, beschreibende Titel.",
        "seo": "Kein direkter Einfluss, Inhalte sollten auch anderweitig zugänglich sein.",
        "design": "Overlay-Opacity, Schatten, Close-Icon, klare Buttons.",
        "legal": "Bei rechtlich relevanten Hinweisen (z. B. AGB) Dokumentation der Zustimmung sichern.",
        "mobile_first": "Fullwidth-Layout, große Touch-Ziele, Scrollverhalten prüfen.",
        "accessibility_impl": "Fokus beim Öffnen auf Heading setzen, beim Schließen zum Trigger zurückführen.",
        "seo_impl": "Modal-Inhalte indexierbar im DOM halten oder serverseitig rendern.",
        "best_practices": [
            "Schließen per ESC, Button und Overlay-Klick ermöglichen.",
            "Hintergrund scrollbar sperren.",
            "Eindeutige Beschriftung (Heading) verwenden."
        ],
        "dependencies": "Overlay-System, Focus-Trap, Scroll-Lock",
        "example_html": "<button type=\"button\" data-open=\"modal\">Modal öffnen</button>\n<div id=\"modal\" class=\"modal\" role=\"dialog\" aria-modal=\"true\" aria-labelledby=\"modal-title\" hidden>\n  <div class=\"modal__content\">\n    <h2 id=\"modal-title\">Hinweis</h2>\n    <p>Bitte bestätigen Sie die Aktion.</p>\n    <button type=\"button\" data-close>Schließen</button>\n  </div>\n</div>",
        "rating": "⭐⭐⭐⭐ Modale Dialoge bleiben Standard, wenn sie zugänglich und sparsam eingesetzt werden."
    },
    {
        "file": "toast.md",
        "title": "Toast",
        "description": "Kurzlebige Benachrichtigungen, die temporär eingeblendet werden.",
        "use_cases": [
            "Feedback nach Formularaktionen geben.",
            "Hintergrundprozesse wie Speichern oder Sync bestätigen."
        ],
        "tradeoff": "Trade-off: Können von Screenreadern überhört werden, wenn nicht korrekt implementiert.",
        "responsiveness": "Position adaptiv, ausreichend Abstand vom Rand, Stapel auf Mobile vermeiden.",
        "accessibility": "`role=\"status\"` oder `role=\"alert\"`, sichtbare und hörbare Dauer.",
        "seo": "Kein Einfluss.",
        "design": "Farbvarianten, dezente Animation, Close-Icon optional.",
        "legal": "Keine speziellen Anforderungen.",
        "mobile_first": "Zentrierte oder untere Platzierung, Buttons groß genug.",
        "accessibility_impl": "Lesezeit ausreichend (mind. 5 Sekunden), Fokus nicht unerwartet verschieben.",
        "seo_impl": "Nicht relevant, da dynamisch.",
        "best_practices": [
            "Toast-Queue begrenzen.",
            "Manuelles Schließen ermöglichen.",
            "Animationen reduziert und bevorzugt per CSS implementieren."
        ],
        "dependencies": "Notification-System, Event-Bus",
        "example_html": "<div class=\"toast toast--success\" role=\"status\" aria-live=\"polite\">Erfolg gespeichert.</div>",
        "rating": "⭐⭐⭐⭐ Kurze Benachrichtigungen bleiben wichtig für Feedback in Webanwendungen."
    }
])
entries.extend([
    {
        "file": "input-field.md",
        "title": "Input Field",
        "description": "Standardisierte Eingabefelder für Text, E-Mail oder Nummern mit optionalen Masken.",
        "use_cases": [
            "Kontakt- und Registrierungsformulare erstellen.",
            "Datenpflege in internen Tools ermöglichen."
        ],
        "tradeoff": "Trade-off: Falsche Masken oder Validierungen frustrieren Nutzer.",
        "responsiveness": "Volle Breite auf Mobile, angepasste Feldbreiten auf Desktop.",
        "accessibility": "Label-Verknüpfung, Fehlermeldungen beschreiben, ausreichende Touch-Ziele.",
        "seo": "Relevanz nur bei Formular-Landingpages (Micro-Conversions).",
        "design": "Konsistente Höhen, Zustände für Fokus/Fehler, lesbare Typografie.",
        "legal": "Datenschutz bei personenbezogenen Daten beachten (z. B. TLS, Speicherung).",
        "mobile_first": "Passende Keyboard-Typen (`inputmode`, `type`) definieren.",
        "accessibility_impl": "Fehlerhinweise via `aria-live`, Pflichtfelder kennzeichnen.",
        "seo_impl": "Formulare beschleunigen Conversion-Rate, Schema.org `ContactPoint` optional.",
        "best_practices": [
            "AutoComplete-Attribute setzen.",
            "Masken nur bei klaren Formaten nutzen.",
            "Client- und Server-Validierung kombinieren."
        ],
        "dependencies": "Form-Validation, Masking-Library",
        "example_html": "<label for=\"email\">E-Mail</label>\n<input id=\"email\" name=\"email\" type=\"email\" required inputmode=\"email\">",
        "rating": "⭐⭐⭐⭐⭐ Eingabefelder sind Kernbausteine jeder Interaktion und bleiben unverzichtbar."
    },
    {
        "file": "dropdown-select.md",
        "title": "Dropdown Select",
        "description": "Auswahlliste als Native-Select oder erweiterte Combobox.",
        "use_cases": [
            "Filter- oder Sortieroptionen bereitstellen.",
            "Formulareingaben mit vorgegebenen Werten strukturieren."
        ],
        "tradeoff": "Trade-off: Custom Selects können A11y-Probleme verursachen, wenn native Funktionen ersetzt werden.",
        "responsiveness": "Volle Breite auf kleinen Screens, Listenhöhe begrenzen.",
        "accessibility": "`label`-Zuordnung, `aria-expanded`, Tastaturnavigation.",
        "seo": "Kein direkter Einfluss.",
        "design": "Pfeil-Icon, States (hover/focus/disabled), konsistente Höhe.",
        "legal": "Keine speziellen Anforderungen.",
        "mobile_first": "Native Select bevorzugen, da optimierte Mobile UI vorhanden.",
        "accessibility_impl": "Combobox-Rollen nur verwenden, wenn Funktionalität vollständig unterstützt.",
        "seo_impl": "Nicht relevant.",
        "best_practices": [
            "Optionen logisch gruppieren (`optgroup`).",
            "Leeren Default-State klar kennzeichnen.",
            "Maximale Optionsanzahl begrenzen oder Suche anbieten."
        ],
        "dependencies": "Form-Controller, Such-API (optional)",
        "example_html": "<label for=\"country\">Land</label>\n<select id=\"country\" name=\"country\">\n  <option value=\"\">Bitte wählen</option>\n  <option value=\"de\">Deutschland</option>\n</select>",
        "rating": "⭐⭐⭐⭐ Dropdowns bleiben häufig, doch Usability hängt von sauberer Umsetzung ab."
    },
    {
        "file": "radio-checkbox-toggle.md",
        "title": "Radio / Checkbox / Toggle",
        "description": "Steuerelemente für Einzel- oder Mehrfachauswahl inklusive Switches.",
        "use_cases": [
            "Einstellungen oder Präferenzen erfassen.",
            "Filteroptionen in Listen oder Formularen anbieten."
        ],
        "tradeoff": "Trade-off: Custom Styles ohne native Elemente können Barrieren erzeugen.",
        "responsiveness": "Gruppen vertikal auf Mobile, horizontal auf Desktop.",
        "accessibility": "Labels klickbar, Status per Screenreader lesbar, Tastaturnavigation.",
        "seo": "Keine direkte Wirkung.",
        "design": "Klar sichtbare Zustände, Gruppierung, Abstände.",
        "legal": "Bei Einwilligungen Nachweisbarkeit sicherstellen.",
        "mobile_first": "Touch-Ziele mind. 44 px, Gruppierungen logisch.",
        "accessibility_impl": "Fieldset/Legend für Gruppen, `aria-checked` bei Custom Controls pflegen.",
        "seo_impl": "Nicht relevant.",
        "best_practices": [
            "Native Inputs verwenden und visuell stylen.",
            "States (hover/focus/disabled) testen.",
            "Toggles nur für sofort wirksame Aktionen nutzen."
        ],
        "dependencies": "Form-Validation, State-Management",
        "example_html": "<fieldset>\n  <legend>Newsletter Frequenz</legend>\n  <label><input type=\"radio\" name=\"freq\" value=\"weekly\"> Wöchentlich</label>\n  <label><input type=\"radio\" name=\"freq\" value=\"monthly\"> Monatlich</label>\n</fieldset>",
        "rating": "⭐⭐⭐⭐ Auswahlkontrollen bleiben Standard und benötigen sorgfältige Gestaltung."
    },
    {
        "file": "file-uploader.md",
        "title": "File Uploader",
        "description": "Komponente zum Hochladen von Dateien inklusive Fortschritt und Validierung.",
        "use_cases": [
            "Bewerbungs- oder Support-Uploads ermöglichen.",
            "Medienverwaltung in CMS oder Kundenportalen."
        ],
        "tradeoff": "Trade-off: Große Dateien erfordern Chunking, Sicherheit und Storage-Kosten.",
        "responsiveness": "Drag-and-Drop-Bereich skalierbar, Fortschrittsanzeigen gut lesbar.",
        "accessibility": "Klare Statusmeldungen, Tastaturbedienung, Screenreader-freundliche Feedbacks.",
        "seo": "Keine direkte Relevanz.",
        "design": "Drop-Zonen, Buttons, Fortschrittsbalken konsistent gestalten.",
        "legal": "Datenschutz und sichere Übertragung (TLS), Dateitypen-Policy, ggf. AV-Verträge.",
        "mobile_first": "Dateiauswahl über native Picker, klare Hinweise zur Maximalgröße.",
        "accessibility_impl": "Statusupdates via `aria-live`, Fehler klar beschreiben.",
        "seo_impl": "Nicht relevant.",
        "best_practices": [
            "Serverseitige Validierung ergänzen.",
            "Uploads pausieren/fortsetzen ermöglichen.",
            "Virenscan oder Sicherheitschecks einplanen."
        ],
        "dependencies": "Storage-Service, Validation, Progress-API",
        "example_html": "<form class=\"uploader\">\n  <label for=\"file\" class=\"uploader__dropzone\">Datei hier ablegen oder klicken</label>\n  <input id=\"file\" name=\"file\" type=\"file\" hidden>\n  <progress value=\"0\" max=\"100\" aria-live=\"polite\"></progress>\n</form>",
        "rating": "⭐⭐⭐⭐ Datei-Uploads sind häufig und erfordern hohe UX- und Sicherheitsstandards."
    },
    {
        "file": "date-picker.md",
        "title": "Date Picker",
        "description": "Komponente zur Auswahl einzelner Daten oder Zeitspannen.",
        "use_cases": [
            "Buchungen oder Terminplanungen ermöglichen.",
            "Filter nach Zeitraum in Reports oder Dashboards anbieten."
        ],
        "tradeoff": "Trade-off: Komplexe Kalenderlogik kann Fehler hervorrufen und ist schwer barrierefrei umzusetzen.",
        "responsiveness": "Kalender auf Mobile als Vollbild oder Listenansicht.",
        "accessibility": "Tastaturbedienung (Pfeiltasten), Screenreader-Beschriftungen, Ansagen der Auswahl.",
        "seo": "Keine direkte Relevanz.",
        "design": "Hervorhebung von aktiven, ausgewählten und deaktivierten Tagen, klare Navigation.",
        "legal": "Bei Buchungen gesetzliche Aufbewahrung von Daten beachten.",
        "mobile_first": "Native Picker nutzen, wenn verfügbar, oder optimierte Touch-Gesten.",
        "accessibility_impl": "`aria-live` für Monatswechsel, `aria-selected` für Tage pflegen.",
        "seo_impl": "Nicht relevant.",
        "best_practices": [
            "Min-/Max-Daten definieren.",
            "Datumsformat klar kommunizieren.",
            "Range-Auswahl mit Drag oder zwei Feldern ermöglichen."
        ],
        "dependencies": "Lokalisierung, Zeitbibliothek",
        "example_html": "<label for=\"date\">Datum</label>\n<input id=\"date\" name=\"date\" type=\"date\">",
        "rating": "⭐⭐⭐⭐ Datumsauswahl bleibt komplex, aber unverzichtbar für Transaktionen."
    },
    {
        "file": "multi-step-wizard.md",
        "title": "Multi-Step Wizard",
        "description": "Mehrschrittige Benutzerführung für komplexe Prozesse.",
        "use_cases": [
            "Onboarding oder Registrierung in Etappen aufteilen.",
            "Konfiguratoren und Formulare mit vielen Feldern strukturieren."
        ],
        "tradeoff": "Trade-off: Höherer Implementierungsaufwand und potenzielle Abbrüche zwischen Schritten.",
        "responsiveness": "Schritte vertikal stacken, Fortschritt klar anzeigen.",
        "accessibility": "Fokus zwischen Schritten managen, `aria-current` für aktiven Schritt.",
        "seo": "Kein direkter Einfluss.",
        "design": "Klare Navigation, Buttons (Weiter/Zürück), Zwischenspeicherung.",
        "legal": "Zwischenspeicherung personenbezogener Daten rechtlich absichern.",
        "mobile_first": "Jeden Schritt auf das Wesentliche reduzieren, Auto-Save integrieren.",
        "accessibility_impl": "Schrittwechsel ankündigen (`aria-live`), Escape aus Fokusfallen vermeiden.",
        "seo_impl": "Nicht relevant.",
        "best_practices": [
            "Fortschritt speichern und wiederaufnehmen ermöglichen.",
            "Zusammenfassung vor Abschluss anzeigen.",
            "Validierung pro Schritt durchführen."
        ],
        "dependencies": "Progress-Steps, Form-Validation, State-Management",
        "example_html": "<form class=\"wizard\">\n  <section aria-labelledby=\"step1\">\n    <h2 id=\"step1\">Schritt 1: Konto</h2>\n    <label>Name<input name=\"name\"></label>\n    <button type=\"button\">Weiter</button>\n  </section>\n</form>",
        "rating": "⭐⭐⭐⭐ Mehrschrittprozesse bleiben nötig, wenn komplexe Eingaben zu strukturieren sind."
    },
    {
        "file": "progress-stepper.md",
        "title": "Progress Stepper",
        "description": "Visualisierung des Fortschritts in mehreren Schritten oder Phasen.",
        "use_cases": [
            "Status in Checkouts oder Formularen anzeigen.",
            "Projekt- oder Onboarding-Fortschritt visualisieren."
        ],
        "tradeoff": "Trade-off: Falsche oder irreführende Schritte steigern Frust.",
        "responsiveness": "Horizontal auf Desktop, vertikal oder kompakt auf Mobile.",
        "accessibility": "`aria-current` für aktiven Schritt, klare Beschriftungen.",
        "seo": "Keine Relevanz.",
        "design": "Abstände, Nummern, Icons; aktive und abgeschlossene States klar differenzieren.",
        "legal": "Keine speziellen Anforderungen.",
        "mobile_first": "Text kürzen, Symbole mit Tooltips kombinieren.",
        "accessibility_impl": "Stepper in `<nav>` mit `aria-label` einbetten.",
        "seo_impl": "Nicht relevant.",
        "best_practices": [
            "Schritte anklickbar machen, wenn sinnvoll.",
            "Fortschritt synchron mit Wizard-State halten.",
            "Klar kommunizieren, wie viele Schritte folgen."
        ],
        "dependencies": "Multi-Step-Wizard, Designsystem",
        "example_html": "<ol class=\"stepper\">\n  <li class=\"stepper__item stepper__item--done\">1. Konto</li>\n  <li class=\"stepper__item stepper__item--current\" aria-current=\"step\">2. Adresse</li>\n  <li class=\"stepper__item\">3. Abschluss</li>\n</ol>",
        "rating": "⭐⭐⭐⭐ Fortschrittsanzeigen bleiben wichtig für Transparenz in Prozessen."
    }
])
entries.extend([
    {
        "file": "search.md",
        "title": "Search",
        "description": "Suchfeld mit optionaler Autosuggest-Funktion.",
        "use_cases": [
            "Produktsuche in Shops oder Verzeichnissen.",
            "Suche in Knowledge-Bases oder Blogs."
        ],
        "tradeoff": "Trade-off: Schlechte Ergebnisse oder langsame Suggests schaden Vertrauen.",
        "responsiveness": "Eingabefeld volle Breite, Suggest-Panel adaptiv.",
        "accessibility": "`aria-expanded`, `aria-controls`, Tastaturnavigation im Suggest.",
        "seo": "Interne Suche kann für Site-Search-Snippets genutzt werden.",
        "design": "Lupe-Icon, deutlicher Fokus, Loading-Indicator für Suggests.",
        "legal": "Suchlogs datenschutzkonform speichern und anonymisieren.",
        "mobile_first": "Fullscreen-Suche mit On-Screen-Keyboard, History-Vorschläge.",
        "accessibility_impl": "Ergebnisse in `role=listbox`, Items mit `role=option` versehen.",
        "seo_impl": "Suchseiten indexieren oder bewusst ausschließen (noindex).",
        "best_practices": [
            "Fehlertoleranz (Fuzzy Search) anbieten.",
            "Analytics zur Suchnutzung integrieren.",
            "Leere Ergebnisse mit Hilfestellungen versehen."
        ],
        "dependencies": "Search-API, Analytics, Autosuggest-Service",
        "example_html": "<form role=\"search\">\n  <label for=\"search\" class=\"sr-only\">Suche</label>\n  <input id=\"search\" name=\"q\" type=\"search\" placeholder=\"Suche\">\n  <button type=\"submit\">Suchen</button>\n</form>",
        "rating": "⭐⭐⭐⭐⭐ Suche bleibt zentral für Nutzerzufriedenheit und Conversions."
    },
    {
        "file": "filter-facets.md",
        "title": "Filter Facets",
        "description": "Facettierte Filtersteuerung mit Chips, Listen oder Slidern.",
        "use_cases": [
            "Produkt- oder Artikellisten zielgerichtet einschränken.",
            "Suchergebnisse nach Kategorien, Preisen oder Tags verfeinern."
        ],
        "tradeoff": "Trade-off: Zu viele Filteroptionen überfordern Nutzer und erhöhen Komplexität.",
        "responsiveness": "Auf Mobile als Akkordeon oder Off-Canvas, auf Desktop nebeneinander.",
        "accessibility": "Checkbox-/Radio-Labels klar benennen, `aria-pressed` für Chips.",
        "seo": "Filter-URLs sauber handhaben, Duplicate Content vermeiden.",
        "design": "Visuelle Hierarchie, aktive Filter hervorheben, Reset-Option.",
        "legal": "Tracking von Filterinteraktionen DSGVO-konform behandeln.",
        "mobile_first": "Filter über Button einblenden, Prioritäten setzen.",
        "accessibility_impl": "Statusänderungen per `aria-live` ankündigen, Fokus nach Anwendung sinnvoll setzen.",
        "seo_impl": "Kanonsiche URLs definieren, Parameter whitelisten.",
        "best_practices": [
            "Aktive Filter deutlich anzeigen und entfernen lassen.",
            "Filterzustand in URL speichern.",
            "Serverseitige und clientseitige Filter synchron halten."
        ],
        "dependencies": "Such-API, State-Management, Analytics",
        "example_html": "<section class=\"filters\">\n  <button type=\"button\" class=\"filter-chip\" aria-pressed=\"true\">Sofort lieferbar</button>\n  <label><input type=\"checkbox\" name=\"brand\" value=\"acme\"> ACME</label>\n</section>",
        "rating": "⭐⭐⭐⭐ Komplexe Kataloge brauchen weiterhin leistungsfähige Filtersteuerungen."
    },
    {
        "file": "contact-form.md",
        "title": "Contact Form",
        "description": "Formular zur Kontaktaufnahme mit Validierung und Spam-Schutz.",
        "use_cases": [
            "Support-Anfragen sammeln.",
            "Sales-Leads auf Landingpages generieren."
        ],
        "tradeoff": "Trade-off: Zu viele Felder senken Conversion und erhöhen Absprungrate.",
        "responsiveness": "Einspaltiges Layout auf Mobile, mehrspaltig auf Desktop möglich.",
        "accessibility": "Labels, Fehlerfeedback, Fokus-Reihenfolge, Captcha-barrierefrei.",
        "seo": "Kontaktseiten für lokale Suche optimieren (`LocalBusiness`-Markup).",
        "design": "Klare Hierarchie, Call-to-Action, Fehlermeldungen konsistent.",
        "legal": "Datenschutzhinweis und Einwilligung gem. DSGVO, Double-Opt-In optional.",
        "mobile_first": "Kurze Felder, AutoComplete nutzen, Soft-Keyboard steuern.",
        "accessibility_impl": "Serverseitige Fehler wiedergeben, `aria-live` für Bestätigungen.",
        "seo_impl": "`rel=\"noopener\"` bei externen Links, strukturierte Daten für Kontakt hinzufügen.",
        "best_practices": [
            "Spam-Schutz (Honeypot, Rate-Limiting).",
            "Erfolgsmeldung klar anzeigen.",
            "Pflichtfelder auf ein Minimum reduzieren."
        ],
        "dependencies": "Form-Backend, Spam-Schutz, CRM",
        "example_html": "<form class=\"contact-form\">\n  <label for=\"name\">Name</label>\n  <input id=\"name\" name=\"name\" required>\n  <label for=\"message\">Nachricht</label>\n  <textarea id=\"message\" name=\"message\"></textarea>\n  <button type=\"submit\">Senden</button>\n</form>",
        "rating": "⭐⭐⭐⭐ Kontaktformulare bleiben primärer Kanal für Leads und Support."
    },
    {
        "file": "newsletter-optin.md",
        "title": "Newsletter Opt-in",
        "description": "Formular zum Anmelden für einen Newsletter mit Double-Opt-In.",
        "use_cases": [
            "Newsletter-Anmeldungen auf Landingpages erhöhen.",
            "Content-Angebote oder Downloads mit E-Mail-Opt-In koppeln."
        ],
        "tradeoff": "Trade-off: Zu aggressive Platzierung kann Nutzer abschrecken und Bounce-Rate erhöhen.",
        "responsiveness": "Einspaltig, klar strukturierte Abstände, Button gut erreichbar.",
        "accessibility": "Labels, Fehlermeldungen, Fokusmanagement für Bestätigung.",
        "seo": "Nicht indexrelevant, aber kann Conversion beeinflussen.",
        "design": "Vertrauensaufbau durch Social Proof, DSGVO-Hinweis, konsistente Buttons.",
        "legal": "Double-Opt-In verpflichtend, Datenschutzhinweis und Widerrufsrecht klar kommunizieren.",
        "mobile_first": "Kurz gehaltene Texte, AutoComplete für E-Mail, schneller Abschluss.",
        "accessibility_impl": "Bestätigungen via `aria-live`, klare Checkbox für Einwilligung.",
        "seo_impl": "Nicht relevant.",
        "best_practices": [
            "Transparenz über Versandfrequenz schaffen.",
            "Captcha barrierefrei gestalten.",
            "Bestätigungsseite mit Tracking-Opt-In dokumentieren."
        ],
        "dependencies": "E-Mail-Service, Consent-Management, CRM",
        "example_html": "<form class=\"newsletter\">\n  <label for=\"newsletter-email\">E-Mail</label>\n  <input id=\"newsletter-email\" name=\"email\" type=\"email\" required>\n  <label><input type=\"checkbox\" required> Ich stimme dem Erhalt des Newsletters zu.</label>\n  <button type=\"submit\">Anmelden</button>\n</form>",
        "rating": "⭐⭐⭐⭐ Newsletter sind weiterhin wichtig, müssen aber rechtlich sauber umgesetzt werden."
    },
    {
        "file": "product-card.md",
        "title": "Product Card",
        "description": "Produktkachel mit Bild, Preis, Bewertung und CTA.",
        "use_cases": [
            "Produktlisten in Shops darstellen.",
            "Empfehlungen oder Upselling-Module einbinden."
        ],
        "tradeoff": "Trade-off: Zu viele Informationen können die Vergleichbarkeit erschweren.",
        "responsiveness": "Card-Layout responsive stacken, Bildverhältnis beibehalten.",
        "accessibility": "Komplette Karte als Link, aber Fokus auf einzelne Aktionen erlauben.",
        "seo": "Strukturierte Daten (`Product`) und Rich Snippets.",
        "design": "Bildgrößen, Typografie, Badge-Positionen, Hover-Styling.",
        "legal": "Preisangabenverordnung beachten, inkl. MwSt. und Versandhinweis.",
        "mobile_first": "Wichtige Infos priorisieren, CTA prominent.",
        "accessibility_impl": "Alt-Texte für Produktbilder, Preis als Text, klare Fokus-States.",
        "seo_impl": "`itemprop`-Attribute oder JSON-LD einsetzen.",
        "best_practices": [
            "Lazyload für Bilder.",
            "Varianten/Verfügbarkeiten klar kennzeichnen.",
            "CTA mit eindeutiger Aktion beschriften."
        ],
        "dependencies": "Bewertungen, Preis-API, Tracking",
        "example_html": "<article class=\"product-card\" itemscope itemtype=\"https://schema.org/Product\">\n  <a href=\"/produkt\" class=\"product-card__link\">\n    <img src=\"/assets/agents-and-robots.png\" alt=\"Agentin und Roboter in einer futuristischen Stadt bei Nacht\" loading=\"lazy\" itemprop=\"image\">\n    <h3 itemprop=\"name\">Sneaker X</h3>\n    <p class=\"product-card__price\" itemprop=\"offers\" itemscope itemtype=\"https://schema.org/Offer\">\n      <span itemprop=\"price\">89,90</span> €\n    </p>\n  </a>\n  <button type=\"button\">In den Warenkorb</button>\n</article>",
        "rating": "⭐⭐⭐⭐⭐ Produktkacheln sind zentral für E-Commerce und Conversion-relevant."
    },
    {
        "file": "price-comparison.md",
        "title": "Price Comparison",
        "description": "Kompakte Vergleichstabelle für Tarife oder Pakete.",
        "use_cases": [
            "SaaS-Preise oder Abos übersichtlich darstellen.",
            "Feature-Vergleich verschiedener Varianten zeigen."
        ],
        "tradeoff": "Trade-off: Komplexe Tabellen können auf Mobile schwer lesbar sein.",
        "responsiveness": "Kartenlayout für Mobile, Tabelle auf Desktop.",
        "accessibility": "Tabellenbeschriftungen, `aria-describedby` für Besonderheiten.",
        "seo": "Preisangaben mit `Product`/`Offer` Markup.",
        "design": "Highlight des empfohlenen Plans, klare Buttons, Farben abgestimmt.",
        "legal": "Preisangaben, Laufzeit, MwSt., Kündigungsfristen transparent kommunizieren.",
        "mobile_first": "Swipebare Karten oder Akkordeon für Details.",
        "accessibility_impl": "Fokus zwischen Plan-Karten steuerbar, Preisänderungen ansagen.",
        "seo_impl": "Rich Snippets für Preise, keine versteckten Kosten.",
        "best_practices": [
            "Wichtigste Unterschiede klar hervorheben.",
            "Call-to-Action pro Plan konsistent.",
            "Zahlungsintervalle wählbar machen."
        ],
        "dependencies": "Produktdaten, Analytics, CTA-Komponenten",
        "example_html": "<section class=\"pricing\">\n  <article class=\"pricing__plan pricing__plan--highlight\">\n    <h3>Pro</h3>\n    <p class=\"pricing__price\">29 € / Monat</p>\n    <ul>\n      <li>Unbegrenzte Projekte</li>\n    </ul>\n    <button type=\"button\">Jetzt starten</button>\n  </article>\n</section>",
        "rating": "⭐⭐⭐⭐ Preisvergleiche bleiben kaufentscheidend, müssen jedoch mobilfreundlich sein."
    },
    {
        "file": "mini-cart.md",
        "title": "Mini Cart",
        "description": "Warenkorb-Vorschau als Off-Canvas oder Dropdown.",
        "use_cases": [
            "Schnellen Zugriff auf Warenkorb-Inhalte bieten.",
            "Upselling im Warenkorb-Kontext ermöglichen."
        ],
        "tradeoff": "Trade-off: Zu komplexe Interaktionen im Mini-Cart können zu Fehlern führen.",
        "responsiveness": "Off-Canvas auf Mobile, Dropdown auf Desktop, Scrollbereich für lange Listen.",
        "accessibility": "`aria-modal` bei Overlays, Tastaturbedienbarkeit, Screenreader-Labels.",
        "seo": "Nicht indexrelevant.",
        "design": "Klares Layout, Produktbilder klein, Gesamtpreis deutlich, Checkout-CTA.",
        "legal": "Preisangaben (MwSt., Versand) verpflichtend anzeigen.",
        "mobile_first": "Schnell sichtbar, einfache Änderungen (Menge, Entfernen).",
        "accessibility_impl": "Änderungen per `aria-live` ankündigen, Fokus beim Öffnen setzen.",
        "seo_impl": "Nicht relevant.",
        "best_practices": [
            "Persistenten Warenkorbstatus synchronisieren.",
            "Checkout-Link deutlich hervorheben.",
            "Produkte entfernen/ändern ohne Seitenwechsel."
        ],
        "dependencies": "Cart-API, Modal-System, Analytics",
        "example_html": "<button type=\"button\" aria-haspopup=\"dialog\" aria-expanded=\"false\">Warenkorb</button>\n<aside class=\"mini-cart\" role=\"dialog\" aria-modal=\"true\" hidden>\n  <h2>Warenkorb</h2>\n  <ul>\n    <li>Produkt A ×1</li>\n  </ul>\n  <p>Summe: 89 €</p>\n  <a href=\"/checkout\">Zum Checkout</a>\n</aside>",
        "rating": "⭐⭐⭐⭐ Mini-Carts bleiben für Conversion und Übersicht essenziell."
    },
    {
        "file": "review-stars.md",
        "title": "Review Stars",
        "description": "Darstellung von Bewertungen mit Sterne-Rating.",
        "use_cases": [
            "Produktbewertungen in Listen oder Detailseiten anzeigen.",
            "Testimonials und Social Proof hervorheben."
        ],
        "tradeoff": "Trade-off: Durchschnittswerte können Erwartungen verzerren, wenn zu wenige Bewertungen vorliegen.",
        "responsiveness": "Sternegröße anpassen, Text daneben umbrechen lassen.",
        "accessibility": "`aria-label` für Bewertung, numerische Werte ausgeben.",
        "seo": "Schema.org `AggregateRating` für Rich Snippets.",
        "design": "Farbige Sterne, klarer Kontrast, optional Text (4,5/5).",
        "legal": "Echtheit der Bewertungen sicherstellen (UWG).",
        "mobile_first": "Komprimierte Darstellung, Sterne neben Text.",
        "accessibility_impl": "Bewertung zusätzlich in Textform ausgeben.",
        "seo_impl": "JSON-LD mit Review-Daten pflegen.",
        "best_practices": [
            "Anzahl der Bewertungen anzeigen.",
            "Filter oder Sortierung nach Bewertung ermöglichen.",
            "Manipulation vermeiden und Kennzeichnungspflicht beachten."
        ],
        "dependencies": "Bewertungs-API, Produktdaten, Schema-Markup",
        "example_html": "<div class=\"rating\" aria-label=\"4,5 von 5 Sternen\">\n  <span aria-hidden=\"true\">★★★★☆</span>\n  <span class=\"rating__value\">4,5/5 (120 Bewertungen)</span>\n</div>",
        "rating": "⭐⭐⭐⭐ Bewertungen bleiben kaufentscheidend und stärken Vertrauen."
    },
    {
        "file": "review-form.md",
        "title": "Review Form",
        "description": "Formular zum Abgeben von Bewertungen mit Rating und Textfeld.",
        "use_cases": [
            "Produkt- oder Service-Bewertungen einholen.",
            "Feedback auf Kurs- oder Eventseiten sammeln."
        ],
        "tradeoff": "Trade-off: Aufwendig in Moderation und Spam-Schutz.",
        "responsiveness": "Formularelemente stacken, Sterne groß genug.",
        "accessibility": "Rating per Tastatur bedienbar, Labels, Fehlermeldungen.",
        "seo": "Generierter Content steigert Sichtbarkeit, Schema.org `Review`.",
        "design": "Sternewahl, Textarea, Upload für Bilder optional, Hinweis auf Richtlinien.",
        "legal": "Transparenzpflichten, DSGVO (personenbezogene Daten) und Nutzungsbedingungen.",
        "mobile_first": "Einfache Eingabe, AutoComplete für Name/E-Mail.",
        "accessibility_impl": "Rating-Widget mit `role=\"radiogroup\"`, Fehlerfeedback via `aria-live`.",
        "seo_impl": "Reviews moderieren, Duplicate Content vermeiden.",
        "best_practices": [
            "Spam-Filter (Honeypot, Captcha) einsetzen.",
            "Richtlinien und Moderationshinweise anzeigen.",
            "Bestätigungsmail zur Verifikation senden."
        ],
        "dependencies": "Auth, Moderation, Storage",
        "example_html": "<form class=\"review-form\">\n  <fieldset role=\"radiogroup\" aria-labelledby=\"rating-label\">\n    <legend id=\"rating-label\">Bewertung</legend>\n    <label><input type=\"radio\" name=\"rating\" value=\"5\"> ★★★★★</label>\n  </fieldset>\n  <label for=\"review-text\">Ihre Erfahrung</label>\n  <textarea id=\"review-text\" name=\"review\"></textarea>\n  <button type=\"submit\">Absenden</button>\n</form>",
        "rating": "⭐⭐⭐⭐ Nutzerfeedback bleibt wertvoll, erfordert jedoch gute Moderation."
    },
    {
        "file": "trust-badges.md",
        "title": "Trust Badges",
        "description": "Sicherheits- und Vertrauenssiegel wie Zahlungsanbieter oder Zertifikate.",
        "use_cases": [
            "Checkout-Seiten mit Gütesiegeln versehen.",
            "Landingpages mit Referenzen und Zertifizierungen stärken."
        ],
        "tradeoff": "Trade-off: Zu viele Badges wirken unseriös oder ablenkend.",
        "responsiveness": "Icons skalierbar, Raster flexibel.",
        "accessibility": "Alternativtexte für Logos, dekorative Elemente mit `aria-hidden`.",
        "seo": "Alt-Texte tragen zu Markensichtbarkeit bei.",
        "design": "Konsistente Größe, ausreichender Abstand, monochrome Varianten.",
        "legal": "Nur tatsächlich vorhandene Zertifikate nutzen, Nutzungsrechte prüfen.",
        "mobile_first": "Badges gruppieren oder in Slider packen, ohne Scroll zu erzwingen.",
        "accessibility_impl": "Logos, die nur dekorativ sind, per `aria-hidden` ausblenden.",
        "seo_impl": "Dateinamen beschreibend wählen, Lazyload bei vielen Logos.",
        "best_practices": [
            "Maximal fünf relevante Badges gleichzeitig zeigen.",
            "Badges bei Bedarf verlinken (z. B. TÜV Zertifikat).",
            "Kontrast zum Hintergrund sicherstellen."
        ],
        "dependencies": "Asset-Management, Legal-Team",
        "example_html": "<ul class=\"trust-badges\">\n  <li><img src=\"/assets/agents-and-robots.png\" alt=\"Agentin und Roboter in einer futuristischen Stadt bei Nacht\"></li>\n  <li><img src=\"/assets/agents-and-robots.png\" alt=\"Agentin und Roboter in einer futuristischen Stadt bei Nacht\"></li>\n</ul>",
        "rating": "⭐⭐⭐⭐ Vertrauenssiegel beeinflussen weiterhin Conversion und Glaubwürdigkeit."
    }
])
entries.extend([
    {
        "file": "breadcrumbs.md",
        "title": "Breadcrumbs",
        "description": "Hierarchische Navigation zur Orientierung im Seitensystem.",
        "use_cases": [
            "Nutzer auf tiefen Kategoriestrukturen unterstützen.",
            "SEO-verbesserte Navigation mit strukturierter Daten-Auszeichnung bieten."
        ],
        "tradeoff": "Trade-off: Bei flacher Struktur wenig Mehrwert und zusätzlicher Pflegeaufwand.",
        "responsiveness": "Horizontale Liste, auf Mobile kürzen oder scrollen lassen.",
        "accessibility": "`nav` mit `aria-label`, Trennzeichen nur dekorativ.",
        "seo": "`BreadcrumbList`-Markup für Rich Snippets.",
        "design": "Dezente Typografie, ausreichende Abstände, Chevron-Icons optional.",
        "legal": "Keine speziellen Anforderungen.",
        "mobile_first": "Nur letzte zwei Ebenen zeigen, Rest einklappbar.",
        "accessibility_impl": "Aktuelle Seite mit `aria-current=page` kennzeichnen.",
        "seo_impl": "Links auf wichtige Kategorie-Seiten setzen, Duplicate vermeiden.",
        "best_practices": [
            "Automatisch aus URL/Navigation generieren.",
            "Home-Link immer anbieten.",
            "Trennzeichen als CSS-Pseudo-Element rendern."
        ],
        "dependencies": "Hauptnavigation, Routing",
        "example_html": "<nav aria-label=\"Breadcrumb\">\n  <ol class=\"breadcrumbs\">\n    <li><a href=\"/\">Start</a></li>\n    <li><a href=\"/shop\">Shop</a></li>\n    <li aria-current=\"page\">Sneaker</li>\n  </ol>\n</nav>",
        "rating": "⭐⭐⭐⭐ Breadcrumbs bleiben wichtig für Orientierung und SEO."
    },
    {
        "file": "pagination.md",
        "title": "Pagination",
        "description": "Seitenweise Navigation für Listen und Suchergebnisse.",
        "use_cases": [
            "Produkt- oder Bloglisten seitenweise anzeigen.",
            "Suchergebnisse strukturieren und Crawlability verbessern."
        ],
        "tradeoff": "Trade-off: Paginierte Inhalte können Nutzerfluss unterbrechen und SEO-Herausforderungen erzeugen.",
        "responsiveness": "Nummern und Buttons vergrößern, auf Mobile simplifiziert (Vor/Zurück).",
        "accessibility": "`nav` mit `aria-label`, Fokusreihenfolge, `aria-current` für aktive Seite.",
        "seo": "`rel=next/prev` (wenn sinnvoll), canonical URLs, strukturierte Daten.",
        "design": "Kontrastreiche Buttons, Hover-/Focus-States, Platz für viele Seiten.",
        "legal": "Keine speziellen Anforderungen.",
        "mobile_first": "Vor/Zurück plus Seitenanzahl anzeigen, Infinite-Scroll-Alternative prüfen.",
        "accessibility_impl": "Screenreader-Labels wie „Seite 2 von 10“ ergänzen.",
        "seo_impl": "Indexierung steuern, Parameter konsistent halten.",
        "best_practices": [
            "Aktuelle Seite klar hervorheben.",
            "First/Last optional ergänzen.",
            "Paginierung auch am Seitenende platzieren."
        ],
        "dependencies": "Routing, API-Pagination, Analytics",
        "example_html": "<nav class=\"pagination\" aria-label=\"Seiten\">\n  <a href=\"?page=1\" aria-label=\"Vorherige Seite\">«</a>\n  <a href=\"?page=1\">1</a>\n  <span aria-current=\"page\">2</span>\n  <a href=\"?page=3\">3</a>\n  <a href=\"?page=3\" aria-label=\"Nächste Seite\">»</a>\n</nav>",
        "rating": "⭐⭐⭐⭐ Klassische Pagination bleibt relevant, auch wenn Infinite Scroll zunimmt."
    },
    {
        "file": "tags-badges.md",
        "title": "Tags & Badges",
        "description": "Labels oder Chips zur Kennzeichnung von Kategorien, Status oder Highlights.",
        "use_cases": [
            "Produkte mit Attributen wie „Neu“ oder „Sale“ markieren.",
            "Blogartikel nach Themen filtern oder kategorisieren."
        ],
        "tradeoff": "Trade-off: Zu viele Tags wirken unübersichtlich und reduzieren Klarheit.",
        "responsiveness": "Chips umbrechen lassen, horizontale Scrollleisten für Tag-Listen.",
        "accessibility": "`aria-pressed` für toggelbare Chips, ausreichender Kontrast.",
        "seo": "Tags können Landingpages generieren, sollten aber gepflegt sein.",
        "design": "Farbcodierung, abgerundete Ecken, kleine Typografie, Hover-/Focus-States.",
        "legal": "Keine speziellen Anforderungen.",
        "mobile_first": "Tags als Scroll-Liste darstellen, wichtige Tags priorisieren.",
        "accessibility_impl": "Chips per Tastatur steuerbar machen, Entfernen-Buttons beschriften.",
        "seo_impl": "Tag-Seiten canonicalisieren, Duplicate Content vermeiden.",
        "best_practices": [
            "Maximale Tag-Anzahl pro Item begrenzen.",
            "Farben aus Designsystem nutzen.",
            "Optional Icons oder Prefixe für Status verwenden."
        ],
        "dependencies": "Filter-System, Design-Tokens",
        "example_html": "<ul class=\"tags\">\n  <li><span class=\"tag tag--new\">Neu</span></li>\n  <li><span class=\"tag tag--sale\">Sale</span></li>\n</ul>",
        "rating": "⭐⭐⭐⭐ Tags bleiben wichtig zur schnellen Kontextualisierung von Inhalten."
    },
    {
        "file": "notification-banner.md",
        "title": "Notification Banner",
        "description": "Seitenweite Hinweise oder Promotions am oberen Rand.",
        "use_cases": [
            "Zeitlich begrenzte Aktionen oder Rabatte kommunizieren.",
            "Systemmeldungen wie Wartungsfenster ankündigen."
        ],
        "tradeoff": "Trade-off: Dauerhafte Banner können Nutzer nerven und Banner-Blindheit erzeugen.",
        "responsiveness": "Volle Breite, Text umbrechen, Close-Button gut erreichbar.",
        "accessibility": "`role=\"region\"` mit Label, Fokus auf Dismiss-Button möglich, ausreichender Kontrast.",
        "seo": "Kein direkter Einfluss, jedoch sollte Banner den Content nicht verdecken.",
        "design": "Farbige Hintergründe, klare Typografie, optional Icon und CTA.",
        "legal": "Preisaktionen mit Bedingungen verlinken, Pflichtinformationen anzeigen.",
        "mobile_first": "Höhe minimieren, Dismiss-Button groß genug.",
        "accessibility_impl": "Banner per Tastatur schließbar, `aria-live` für zeitkritische Infos.",
        "seo_impl": "Keine Cloaking-Praktiken, Banner nicht Inhalt überdecken.",
        "best_practices": [
            "Nur eine aktive Botschaft gleichzeitig anzeigen.",
            "Dauer und Wiederholung begrenzen.",
            "Dismiss-State speichern (Cookie/LocalStorage)."
        ],
        "dependencies": "Analytics, Feature Flags, Consent (bei Tracking)",
        "example_html": "<div class=\"notification-banner\" role=\"region\" aria-label=\"Hinweis\">\n  <p>Gratis Versand bis Sonntag!</p>\n  <button type=\"button\" class=\"notification-banner__close\" aria-label=\"Banner schließen\">×</button>\n</div>",
        "rating": "⭐⭐⭐⭐ Banner bleiben ein zentrales Mittel für dringliche Kommunikation."
    },
    {
        "file": "loading-spinner.md",
        "title": "Loading Spinner",
        "description": "Animierter Indikator für laufende Prozesse.",
        "use_cases": [
            "Kurze Ladezeiten bei Formularen oder API-Calls anzeigen.",
            "Asynchrone Aktionen wie Datenabrufe visualisieren."
        ],
        "tradeoff": "Trade-off: Reine Spinner ohne Kontext frustrieren, wenn Ladezeiten länger dauern.",
        "responsiveness": "Größe skaliert mit Container, Kontrast zum Hintergrund.",
        "accessibility": "`role=\"status\"` und beschreibender Text, `aria-live=polite`.",
        "seo": "Keine Relevanz.",
        "design": "Konsistente Animation, Designsystem-konforme Farben.",
        "legal": "Keine speziellen Anforderungen.",
        "mobile_first": "Spinner nicht zu groß, damit Inhalte sichtbar bleiben.",
        "accessibility_impl": "Zusätzlichen Text wie „Lädt…“ bereitstellen.",
        "seo_impl": "Nicht relevant.",
        "best_practices": [
            "Maximale Ladezeit definieren und Fehlerzustand zeigen.",
            "Spinner erst nach 500 ms anzeigen, um Flackern zu vermeiden.",
            "Mit Skeletons kombinieren, wenn längere Wartezeiten zu erwarten sind."
        ],
        "dependencies": "Animationslibrary, State-Management",
        "example_html": "<div class=\"spinner\" role=\"status\" aria-live=\"polite\">\n  <span class=\"sr-only\">Lädt…</span>\n</div>",
        "rating": "⭐⭐⭐⭐ Ladeindikatoren bleiben Standard, sollten aber immer mit Kontext kombiniert werden."
    },
    {
        "file": "skeleton-loader.md",
        "title": "Skeleton Loader",
        "description": "Platzhalter-Layouts, die die spätere Struktur andeuten, während Inhalte laden.",
        "use_cases": [
            "Listen oder Karten während Datenabruf darstellen.",
            "Dashboard-Widgets ohne Layoutverschiebung laden."
        ],
        "tradeoff": "Trade-off: Falsche Skeletons können Erwartungen enttäuschen, wenn Inhalte anders aussehen.",
        "responsiveness": "Skeleton-Elemente spiegeln spätere Layoutgrößen, fluid skalieren.",
        "accessibility": "`aria-hidden` für Skeletons, tatsächliche Inhalte bei Verfügbarkeit ansagen.",
        "seo": "Kein direkter Einfluss, aber reduziert Cumulative Layout Shift.",
        "design": "Animierte Shimmer-Effekte dezent, Farben aus Neutraltönen.",
        "legal": "Keine speziellen Anforderungen.",
        "mobile_first": "Skeletons für kritische Bereiche priorisieren, um wahrgenommene Geschwindigkeit zu erhöhen.",
        "accessibility_impl": "Skeletons entfernen, sobald Content geladen ist, `aria-busy` nutzen.",
        "seo_impl": "Nicht relevant.",
        "best_practices": [
            "Skeletons an reale Content-Höhen anpassen.",
            "Nicht zu viele Animationen verwenden (Performance).",
            "Mit echten Ladezeiten abstimmen und Timeout setzen."
        ],
        "dependencies": "Designsystem, State-Management",
        "example_html": "<div class=\"skeleton-card\" aria-hidden=\"true\">\n  <div class=\"skeleton skeleton--image\"></div>\n  <div class=\"skeleton skeleton--text\"></div>\n</div>",
        "rating": "⭐⭐⭐⭐ Skeletons verbessern wahrgenommene Performance und bleiben relevant."
    },
    {
        "file": "empty-state.md",
        "title": "Empty State",
        "description": "Darstellung, wenn keine Daten oder Ergebnisse vorliegen.",
        "use_cases": [
            "Suche ohne Treffer informativ gestalten.",
            "Neue Nutzer in Dashboards an Funktionen heranführen."
        ],
        "tradeoff": "Trade-off: Unpassende Illustrationen oder Texte können Nutzer verwirren.",
        "responsiveness": "Illustrationen und Text skalieren, Buttons darunter anordnen.",
        "accessibility": "Alternativtexte für Illustrationen, klare Anweisungen auch in Text.",
        "seo": "Keine direkte Relevanz.",
        "design": "Illustration, Headline, Body-Text, CTA optional, konsistente Farben.",
        "legal": "Keine speziellen Anforderungen.",
        "mobile_first": "Kurze Texte, klare Handlungsoptionen, Buttons full-width.",
        "accessibility_impl": "Keine rein ikonografischen Aussagen; Text beschreibt Situation.",
        "seo_impl": "Nicht relevant.",
        "best_practices": [
            "Konkrete nächste Schritte anbieten.",
            "Optional Hilfelinks einblenden.",
            "Tonfall empathisch wählen."
        ],
        "dependencies": "Illustrationen, CTA-Komponenten",
        "example_html": "<section class=\"empty-state\">\n  <img src=\"/assets/agents-and-robots.png\" alt=\"Agentin und Roboter in einer futuristischen Stadt bei Nacht\" loading=\"lazy\">\n  <h2>Keine Ergebnisse</h2>\n  <p>Passen Sie Ihre Filter an oder starten Sie eine neue Suche.</p>\n  <button type=\"button\">Filter zurücksetzen</button>\n</section>",
        "rating": "⭐⭐⭐⭐ Gute Empty States steigern Engagement und helfen bei der Orientierung."
    },
    {
        "file": "share-buttons.md",
        "title": "Share Buttons",
        "description": "Buttons zum Teilen von Inhalten in sozialen Netzwerken oder per Link.",
        "use_cases": [
            "Blogbeiträge oder Produkte schnell teilen lassen.",
            "Eventseiten viral verbreiten."
        ],
        "tradeoff": "Trade-off: Zu viele Netzwerke verlangsamen die Seite und verwirren Nutzer.",
        "responsiveness": "Icons in flexiblen Layouts, Touch-Ziele ausreichend groß.",
        "accessibility": "Buttons beschriften (`aria-label`), Fokus sichtbar, Tastaturbedienung.",
        "seo": "Indirekter Effekt durch erhöhte Sichtbarkeit und Backlinks.",
        "design": "Markenfarben der Netzwerke oder neutrale Icons, Hover-/Focus-States.",
        "legal": "Social Plugins datenschutzkonform integrieren (2-Klick-Lösung).",
        "mobile_first": "Horizontale Scroll-Leiste oder Dropdown für zusätzliche Optionen.",
        "accessibility_impl": "Teilen-Dialog per Tastatur bedienbar, Clipboard-Option anbieten.",
        "seo_impl": "UTM-Parameter konsistent setzen, Sharing-Meta-Tags (OG, Twitter Cards) pflegen.",
        "best_practices": [
            "Nur relevante Netzwerke anzeigen.",
            "Copy-Link-Funktion anbieten.",
            "Lade Social-Skripte erst nach Interaktion."
        ],
        "dependencies": "Social APIs, Consent-Tool, Analytics",
        "example_html": "<div class=\"share\">\n  <button type=\"button\" aria-label=\"Bei LinkedIn teilen\">LinkedIn</button>\n  <button type=\"button\" aria-label=\"Link kopieren\">Link kopieren</button>\n</div>",
        "rating": "⭐⭐⭐⭐ Teilen-Funktionen bleiben wichtig, müssen aber datenschutzfreundlich umgesetzt werden."
    },
    {
        "file": "cookie-consent.md",
        "title": "Cookie Consent",
        "description": "Consent-Banner oder Layer zur Einholung der DSGVO-konformen Zustimmung für Cookies.",
        "use_cases": [
            "Tracking- und Marketing-Cookies rechtskonform einholen.",
            "Einwilligungen für externe Dienste (Maps, Videos) verwalten."
        ],
        "tradeoff": "Trade-off: Schlechte UX führt zu Ablehnung oder rechtlichen Risiken.",
        "responsiveness": "Fullscreen-Layer auf Mobile, dezenter Banner auf Desktop.",
        "accessibility": "Tastaturbedienbar, Fokus-Trap, klare Beschriftungen, Screenreader-freundlich.",
        "seo": "Consent-Banner darf Inhalte nicht dauerhaft verdecken, sonst Rankingrisiko.",
        "design": "Klares Layout, Buttons für „Akzeptieren“, „Ablehnen“, „Einstellungen“, farblich differenziert.",
        "legal": "DSGVO, TTDSG: Granulare Einwilligung, Dokumentation, Widerrufsmöglichkeit, Datenschutzerklärung verlinken.",
        "mobile_first": "Schnelle Auswahl, aber granularer Zugriff über Einstellungen gewährleisten.",
        "accessibility_impl": "Fokus auf ersten Button setzen, `aria-modal` nutzen, Einstellungsdialog beschreiben.",
        "seo_impl": "Banner erst nach Page Load anzeigen, Consent-Status serverseitig speichern.",
        "best_practices": [
            "Voreinstellungen auf technisch notwendige Cookies beschränken.",
            "Consent-Logs revisionssicher speichern.",
            "Regelmäßige rechtliche Prüfung durchführen."
        ],
        "dependencies": "Consent-Management-Plattform, Tag-Manager, Legal",
        "example_html": "<div class=\"cookie-consent\" role=\"dialog\" aria-modal=\"true\" aria-labelledby=\"cookie-title\">\n  <h2 id=\"cookie-title\">Datenschutz-Einstellungen</h2>\n  <p>Wir verwenden Cookies, um unsere Website zu verbessern.</p>\n  <div class=\"cookie-consent__actions\">\n    <button type=\"button\">Alle akzeptieren</button>\n    <button type=\"button\">Nur notwendige</button>\n    <button type=\"button\">Einstellungen</button>\n  </div>\n</div>",
        "rating": "⭐⭐⭐⭐ Cookie-Consent bleibt rechtlich zwingend und entwickelt sich weiter."
    }
])
for entry in entries:
    write(entry)
