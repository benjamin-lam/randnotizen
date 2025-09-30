from __future__ import annotations

COMPONENTS: dict[str, dict[str, object]] = {
    "audio-embed": {
        "meta": [
            "Keyboardsteuerung",
            "ARIA Live Feedback",
            "Responsive Layout"
        ],
        "example": """
<div class="audio-player" data-audio-player>
  <section class="card" aria-label="Aktuelle Episode">
    <div class="audio-player__meta">
      <img class="audio-player__cover" src="https://images.unsplash.com/photo-1525182008055-f88b95ff7980?auto=format&fit=crop&w=320&q=80" alt="Podcast Cover: Remote Culture" loading="lazy">
      <div>
        <p class="text-muted">Remote Culture • Episode 12</p>
        <h3 class="callout__title">Async Workflows, die funktionieren</h3>
        <p class="text-muted">Mit Host Mara und Gast Daniel Fuchs</p>
      </div>
    </div>
    <audio controls preload="metadata" data-audio-element aria-describedby="audio-status">
      <source src="https://upload.wikimedia.org/wikipedia/commons/4/4e/BWV_543-fugue.ogg" type="audio/ogg">
      <source src="https://upload.wikimedia.org/wikipedia/commons/4/4e/BWV_543-fugue.ogg" type="audio/mpeg">
      Ihr Browser unterstützt das Audio-Element nicht. <a href="https://upload.wikimedia.org/wikipedia/commons/4/4e/BWV_543-fugue.ogg">Episode herunterladen</a>.
    </audio>
    <div id="audio-status" class="visually-hidden" aria-live="polite"></div>
  </section>
  <section class="audio-tracklist" role="list" aria-label="Weitere Episoden">
    <button class="audio-track is-current" type="button" role="listitem" data-audio-track data-src="https://upload.wikimedia.org/wikipedia/commons/4/4e/BWV_543-fugue.ogg" data-title="Async Workflows, die funktionieren" aria-pressed="true">
      <span>Async Workflows, die funktionieren</span>
      <span class="text-muted">24:32</span>
    </button>
    <button class="audio-track" type="button" role="listitem" data-audio-track data-src="https://upload.wikimedia.org/wikipedia/commons/c/c8/Example.ogg" data-title="Führung auf Distanz" aria-pressed="false">
      <span>Führung auf Distanz</span>
      <span class="text-muted">18:05</span>
    </button>
    <button class="audio-track" type="button" role="listitem" data-audio-track data-src="https://upload.wikimedia.org/wikipedia/commons/3/32/Example_3.ogg" data-title="Async Feedback Loops" aria-pressed="false">
      <span>Async Feedback Loops</span>
      <span class="text-muted">21:11</span>
    </button>
  </section>
</div>
""",
    },
    "breadcrumbs": {
        "meta": [
            "Semantische Navigation",
            "Touch-Ziele optimiert",
            "SR-Label"
        ],
        "example": """
<nav class="card" aria-label="Brotkrumen">
  <ol class="breadcrumbs">
    <li class="breadcrumbs__item"><a href="#">Startseite</a></li>
    <li class="breadcrumbs__item"><a href="#">Dokumentation</a></li>
    <li class="breadcrumbs__item"><a href="#">Designsystem</a></li>
    <li class="breadcrumbs__item" aria-current="page"><span>Content Elemente</span></li>
  </ol>
</nav>
""",
    },
    "callout-box": {
        "meta": [
            "ARIA Rollen",
            "Kontrast geprüft",
            "Icon dekorativ"
        ],
        "example": """
<aside class="callout callout--info" aria-label="Hinweis">
  <div class="flex-between">
    <div class="stack-sm">
      <h3 class="callout__title">Backup nicht vergessen</h3>
      <p>Planen Sie automatische Sicherungen, um Ihre Inhalte jederzeit wiederherstellen zu können.</p>
    </div>
    <svg class="callout__icon" aria-hidden="true" viewBox="0 0 24 24" fill="none">
      <circle cx="12" cy="12" r="11" stroke="currentColor" stroke-width="2"></circle>
      <path d="M12 7v6" stroke="currentColor" stroke-width="2" stroke-linecap="round"></path>
      <circle cx="12" cy="17" r="1" fill="currentColor"></circle>
    </svg>
  </div>
</aside>
""",
    },
    "code-snippets": {
        "meta": [
            "Copy to Clipboard",
            "ARIA Live Regionen",
            "Syntax freundlich"
        ],
        "example": """
<figure class="code-snippet" data-code-snippet>
  <figcaption>POST-Anfrage gegen die Content API</figcaption>
  <pre class="code-snippet__body"><code id="snippet-js" data-language="bash">curl --request POST \\
  --url https://api.example.com/v1/entries \\
  --header 'Content-Type: application/json' \\
  --data '{"title": "Accessibility first"}'</code></pre>
  <button class="btn copy-button" type="button" data-copy-button data-copy-target="snippet-js" aria-live="polite">Code kopieren</button>
  <output class="visually-hidden" aria-live="polite" data-copy-feedback></output>
</figure>
""",
    },
    "contact-form": {
        "meta": [
            "Form Validation",
            "Mobile optimiert",
            "Fokusführung"
        ],
        "example": """
<form class="contact-form" data-contact-form novalidate>
  <div class="contact-form__grid">
    <div class="input-group">
      <label for="cf-name">Name</label>
      <input class="input" id="cf-name" name="name" type="text" autocomplete="name" required>
      <p class="form-help">Pflichtfeld – mindestens 2 Zeichen.</p>
    </div>
    <div class="input-group">
      <label for="cf-email">E-Mail</label>
      <input class="input" id="cf-email" name="email" type="email" autocomplete="email" inputmode="email" required>
    </div>
  </div>
  <div class="input-group">
    <label for="cf-topic">Thema</label>
    <select class="input" id="cf-topic" name="topic">
      <option value="support">Technischer Support</option>
      <option value="sales">Beratung &amp; Angebote</option>
      <option value="feedback">Feedback</option>
    </select>
  </div>
  <div class="input-group">
    <label for="cf-message">Nachricht</label>
    <textarea class="input" id="cf-message" name="message" rows="4" maxlength="500" required></textarea>
    <p class="form-help">Maximal 500 Zeichen.</p>
  </div>
  <div class="flex-between">
    <label class="input-group" style="flex-direction: row; gap: 0.5rem; align-items: center;">
      <input type="checkbox" name="privacy" required>
      <span>Ich akzeptiere die <a href="#">Datenschutzerklärung</a>.</span>
    </label>
    <button class="btn" type="submit">Absenden</button>
  </div>
  <p class="form-help" aria-live="polite" data-form-feedback></p>
</form>
""",
    },
    "cookie-consent": {
        "meta": [
            "Consent Kategorien",
            "Persistenz Demo",
            "Barrierefrei"
        ],
        "example": """
<section class="cookie-banner" role="dialog" aria-modal="true" aria-live="assertive" data-cookie-banner>
  <div class="stack-md">
    <h2>Wir respektieren Ihre Privatsphäre</h2>
    <p>Wir verwenden Cookies, um Ihr Erlebnis zu verbessern. Passen Sie Ihre Auswahl jederzeit an.</p>
    <details>
      <summary>Details anzeigen</summary>
      <ul class="stack-sm" style="margin: 0; padding-left: 1rem;">
        <li><strong>Essentiell:</strong> notwendig für die Seitennutzung.</li>
        <li><strong>Statistik:</strong> hilft uns, Inhalte zu optimieren.</li>
        <li><strong>Marketing:</strong> personalisierte Angebote.</li>
      </ul>
    </details>
  </div>
  <div class="cookie-banner__actions">
    <button class="btn" type="button" data-consent-action="accept">Alle akzeptieren</button>
    <button class="btn btn--ghost" type="button" data-consent-action="essentials">Nur essentielle</button>
    <button class="btn btn--ghost" type="button" data-consent-open-settings>Individuell</button>
  </div>
</section>
""",
    },
    "date-picker": {
        "meta": [
            "WAI-ARIA Grid",
            "Tastatur Navigation",
            "Locale aware"
        ],
        "example": """
<div class="date-picker" data-date-picker data-start-month="2025-05">
  <div class="input-group">
    <label for="date-input">Reisedatum</label>
    <input class="input" id="date-input" name="date" type="text" autocomplete="off" inputmode="numeric" placeholder="TT.MM.JJJJ" data-date-input aria-describedby="date-hint">
    <p id="date-hint" class="form-help">Mit Pfeiltasten durch den Kalender navigieren. Native Eingabe: <input type="date" aria-label="Datum auswählen" style="display:inline-block; max-width: 150px;"></p>
  </div>
  <section class="card card--bordered" aria-labelledby="calendar-title">
    <div class="flex-between">
      <button class="icon-button" type="button" data-calendar-prev aria-label="Vorheriger Monat">
        <span aria-hidden="true">◀</span>
      </button>
      <p id="calendar-title" class="text-muted" data-calendar-title>Mai 2025</p>
      <button class="icon-button" type="button" data-calendar-next aria-label="Nächster Monat">
        <span aria-hidden="true">▶</span>
      </button>
    </div>
    <div class="calendar-weekdays" aria-hidden="true">
      <span>Mo</span><span>Di</span><span>Mi</span><span>Do</span><span>Fr</span><span>Sa</span><span>So</span>
    </div>
    <div class="calendar-grid" role="grid" aria-labelledby="calendar-title" data-calendar-grid></div>
  </section>
</div>
""",
    },
    "dropdown-select": {
        "meta": [
            "Roving Tabindex",
            "Touch friendly",
            "Hidden Input"
        ],
        "example": """
<div class="dropdown" data-dropdown>
  <label for="team-size">Teamgröße</label>
  <button class="btn dropdown__button" type="button" id="team-size" data-dropdown-toggle aria-haspopup="listbox" aria-expanded="false">
    <span data-dropdown-label>1–10 Personen</span>
    <span aria-hidden="true">▾</span>
  </button>
  <ul class="dropdown__panel" role="listbox" tabindex="-1" aria-labelledby="team-size" data-dropdown-list>
    <li><button class="dropdown__option" type="button" role="option" aria-selected="true" data-value="small">1–10 Personen</button></li>
    <li><button class="dropdown__option" type="button" role="option" aria-selected="false" data-value="medium">11–25 Personen</button></li>
    <li><button class="dropdown__option" type="button" role="option" aria-selected="false" data-value="large">26–50 Personen</button></li>
    <li><button class="dropdown__option" type="button" role="option" aria-selected="false" data-value="enterprise">Mehr als 50</button></li>
  </ul>
  <input type="hidden" name="team-size" value="small" data-dropdown-input>
</div>
""",
    },
    "empty-state": {
        "meta": [
            "Illustration inklusive",
            "Handlungsaufforderung",
            "Screenreader Text"
        ],
        "example": """
<section class="empty-state" role="status" aria-live="polite">
  <svg viewBox="0 0 64 64" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2">
    <circle cx="32" cy="32" r="30" opacity="0.2"></circle>
    <path d="M18 38h28" stroke-linecap="round"></path>
    <path d="M24 30l8-10 8 10" stroke-linecap="round" stroke-linejoin="round"></path>
  </svg>
  <h2>Keine Ergebnisse – noch.</h2>
  <p>Versuchen Sie es mit anderen Filtern oder erstellen Sie einen neuen Eintrag.</p>
  <div class="share-buttons" role="group">
    <button class="btn" type="button">Filter zurücksetzen</button>
    <button class="btn btn--ghost" type="button">Eintrag erstellen</button>
  </div>
</section>
""",
    },
    "file-uploader": {
        "meta": [
            "Drag & Drop",
            "Fortschrittsanzeige",
            "Mehrere Dateien"
        ],
        "example": """
<section class="file-uploader" data-file-uploader>
  <div class="dropzone" tabindex="0" role="button" aria-label="Dateien hier ablegen oder klicken" data-dropzone>
    <p><strong>Dateien auswählen</strong></p>
    <p class="text-muted">Ziehen Sie Dateien hierher oder klicken Sie, um zu wählen. Maximal 10 Dateien.</p>
    <input class="visually-hidden" type="file" name="documents" id="documents" multiple data-file-input>
  </div>
  <div class="upload-list" aria-live="polite" data-upload-list></div>
</section>
""",
    },
    "filter-facets": {
        "meta": [
            "Akkordeon",
            "Checkbox Gruppen",
            "Keyboard Fokus"
        ],
        "example": """
<aside class="facets" aria-label="Filter">
  <details open>
    <summary>Rollen</summary>
    <div class="facets__options">
      <label><input type="checkbox" name="role" value="design" checked> Design</label>
      <label><input type="checkbox" name="role" value="engineering"> Engineering</label>
      <label><input type="checkbox" name="role" value="product"> Produkt</label>
    </div>
  </details>
  <details>
    <summary>Standorte</summary>
    <div class="facets__options">
      <label><input type="checkbox" name="location" value="remote"> Remote</label>
      <label><input type="checkbox" name="location" value="berlin"> Berlin</label>
      <label><input type="checkbox" name="location" value="muenchen"> München</label>
    </div>
  </details>
</aside>
""",
    },
    "image-carousel": {
        "meta": [
            "Swipe-ready",
            "ARIA Live",
            "Lazy Loading"
        ],
        "example": """
<section class="carousel" data-carousel aria-roledescription="Karussell" aria-label="Produktbilder">
  <div class="carousel__slides" data-carousel-track>
    <figure class="carousel__slide" data-carousel-slide>
      <img src="https://images.unsplash.com/photo-1582719478250-c89cae4dc85b?auto=format&fit=crop&w=900&q=80" alt="Offenes, helles Wohnzimmer" loading="lazy">
      <figcaption class="visually-hidden">Wohnbereich mit natürlichem Licht</figcaption>
    </figure>
    <figure class="carousel__slide" data-carousel-slide>
      <img src="https://images.unsplash.com/photo-1586023492125-27b2c045efd7?auto=format&fit=crop&w=900&q=80" alt="Moderne Küche mit Holzdekor" loading="lazy">
      <figcaption class="visually-hidden">Moderne Küche</figcaption>
    </figure>
    <figure class="carousel__slide" data-carousel-slide>
      <img src="https://images.unsplash.com/photo-1505691723518-36a5ac3be353?auto=format&fit=crop&w=900&q=80" alt="Gemütliches Schlafzimmer mit Pflanzen" loading="lazy">
      <figcaption class="visually-hidden">Schlafzimmer mit Pflanzen</figcaption>
    </figure>
  </div>
  <div class="carousel__controls" aria-hidden="true">
    <button class="icon-button" type="button" data-carousel-prev aria-label="Vorheriges Bild">◀</button>
    <button class="icon-button" type="button" data-carousel-next aria-label="Nächstes Bild">▶</button>
  </div>
</section>
<div class="carousel__dots" role="tablist" data-carousel-dots>
  <button class="carousel__dot" type="button" role="tab" aria-controls="slide-1" aria-current="true"></button>
  <button class="carousel__dot" type="button" role="tab" aria-controls="slide-2"></button>
  <button class="carousel__dot" type="button" role="tab" aria-controls="slide-3"></button>
</div>
""",
    },
    "image-with-caption": {
        "meta": [
            "Figure &amp; Figcaption",
            "Responsive Bilder",
            "Lazy loading"
        ],
        "example": """
<figure class="figure">
  <picture>
    <source srcset="https://images.unsplash.com/photo-1521737604893-d14cc237f11d?auto=format&fit=crop&w=900&q=80" media="(min-width: 800px)">
    <img src="https://images.unsplash.com/photo-1521737604893-d14cc237f11d?auto=format&fit=crop&w=600&q=80" alt="Team, das gemeinsam an einem Tisch arbeitet" loading="lazy">
  </picture>
  <figcaption>Team Sync im Workspace Berlin – Foto: <a href="https://unsplash.com" rel="noopener">Unsplash</a></figcaption>
</figure>
""",
    },
    "input-field": {
        "meta": [
            "Inline Fehlermeldung",
            "Charakterbegrenzung",
            "State Styling"
        ],
        "example": """
<section class="input-field" aria-live="polite">
  <div class="input-group">
    <label for="input-username">Benutzername</label>
    <input class="input" id="input-username" name="username" type="text" placeholder="z. B. ux-nerd" minlength="3" maxlength="20" required data-input-with-counter>
    <p class="form-help"><span data-input-counter>0</span>/20 Zeichen</p>
  </div>
  <div class="input-group">
    <label for="input-password">Passwort</label>
    <div style="position: relative;">
      <input class="input" id="input-password" name="password" type="password" required aria-describedby="password-hint">
      <button class="btn btn--ghost" type="button" data-toggle-password style="position:absolute; top:50%; right:0.5rem; transform:translateY(-50%);">Anzeigen</button>
    </div>
    <p id="password-hint" class="form-help">Mindestens 8 Zeichen, Groß-/Kleinschreibung sowie Zahl.</p>
  </div>
</section>
""",
    },
    "loading-spinner": {
        "meta": [
            "Reduced Motion",
            "Role Status",
            "Contrast optimiert"
        ],
        "example": """
<div class="card" role="status" aria-live="polite">
  <div class="spinner" aria-hidden="true"></div>
  <p>Daten werden geladen …</p>
  <p class="form-help">Sollte der Vorgang länger dauern als 30 Sekunden, aktualisieren Sie die Seite.</p>
</div>
""",
    },
    "map-embed": {
        "meta": [
            "Iframe Titel",
            "Fallback Link",
            "Lazy Loading"
        ],
        "example": """
<section class="card">
  <h2>Büro Berlin</h2>
  <p class="text-muted">Invalidenstraße 91, 10115 Berlin</p>
  <iframe class="map-frame" loading="lazy" src="https://www.openstreetmap.org/export/embed.html?bbox=13.3789%2C52.5294%2C13.3839%2C52.5324&amp;layer=mapnik" title="Karte des Büros in Berlin"></iframe>
  <p><a href="https://www.openstreetmap.org/?mlat=52.531&amp;mlon=13.381#map=18/52.5310/13.3810" target="_blank" rel="noopener">Auf OpenStreetMap öffnen</a></p>
</section>
""",
    },
    "mini-cart": {
        "meta": [
            "Live Aktualisierung",
            "Accessible Pricing",
            "Keyboard ready"
        ],
        "example": """
<section class="mini-cart" data-mini-cart aria-label="Mini Warenkorb">
  <div class="cart-item" data-cart-item>
    <img src="https://images.unsplash.com/photo-1523275335684-37898b6baf30?auto=format&fit=crop&w=200&q=80" alt="Kabellose Kopfhörer" loading="lazy">
    <div>
      <p>Kabellose Kopfhörer</p>
      <p class="text-muted">Lieferung in 2-3 Tagen</p>
      <label class="visually-hidden" for="item-1">Anzahl</label>
      <input class="input" id="item-1" type="number" min="1" value="1" data-item-qty>
    </div>
    <strong data-item-price="129.90">129,90 €</strong>
  </div>
  <div class="cart-item" data-cart-item>
    <img src="https://images.unsplash.com/photo-1512496015851-a90fb38ba796?auto=format&fit=crop&w=200&q=80" alt="Leder Schreibtischunterlage" loading="lazy">
    <div>
      <p>Leder Desk Pad</p>
      <p class="text-muted">Nachhaltiges Leder</p>
      <label class="visually-hidden" for="item-2">Anzahl</label>
      <input class="input" id="item-2" type="number" min="1" value="2" data-item-qty>
    </div>
    <strong data-item-price="59.90">59,90 €</strong>
  </div>
  <div class="cart-summary">
    <span>Zwischensumme</span>
    <span data-cart-total>249,70 €</span>
  </div>
  <button class="btn" type="button">Zur Kasse</button>
</section>
""",
    },
    "modal": {
        "meta": [
            "Focus Trap",
            "Escape schließt",
            "Aria Beschriftung"
        ],
        "example": """
<section class="modal-demo">
  <button class="btn" type="button" data-open-modal="#newsletter-modal">Neuigkeiten abonnieren</button>
  <dialog class="modal" id="newsletter-modal" role="dialog" aria-modal="true" aria-labelledby="modal-title">
    <div class="modal__dialog">
      <header class="modal__header">
        <h2 id="modal-title">Wöchentlicher Newsletter</h2>
        <button class="icon-button" type="button" data-close-modal aria-label="Modal schließen">✕</button>
      </header>
      <p>Erhalten Sie Updates zu Produkt-Releases und Best Practices direkt in Ihr Postfach.</p>
      <form class="newsletter-form" data-newsletter-modal>
        <label class="visually-hidden" for="modal-email">E-Mail-Adresse</label>
        <input class="input" id="modal-email" type="email" name="email" placeholder="name@example.com" required>
        <button class="btn" type="submit">Abonnieren</button>
      </form>
    </div>
  </dialog>
</section>
""",
    },
    "multi-step-wizard": {
        "meta": [
            "ARIA Current",
            "Progressive Disclosure",
            "Keyboard Navigation"
        ],
        "example": """
<section class="wizard" data-wizard>
  <div class="wizard__steps" role="list" aria-label="Setup Schritte">
    <span class="wizard__step" role="listitem" aria-current="step">Profil</span>
    <span class="wizard__step" role="listitem">Team</span>
    <span class="wizard__step" role="listitem">Bestätigung</span>
  </div>
  <form class="card" data-wizard-step="0">
    <div class="input-group">
      <label for="wizard-name">Name</label>
      <input class="input" id="wizard-name" required>
    </div>
    <div class="input-group">
      <label for="wizard-role">Rolle</label>
      <select class="input" id="wizard-role">
        <option>Produktmanager:in</option>
        <option>Designer:in</option>
        <option>Developer:in</option>
      </select>
    </div>
    <div class="flex-between">
      <span></span>
      <button class="btn" type="button" data-wizard-next>Weiter</button>
    </div>
  </form>
  <form class="card" hidden data-wizard-step="1">
    <div class="input-group">
      <label for="wizard-team-size">Teamgröße</label>
      <input class="input" id="wizard-team-size" type="number" min="1" value="5">
    </div>
    <div class="flex-between">
      <button class="btn btn--ghost" type="button" data-wizard-prev>Zurück</button>
      <button class="btn" type="button" data-wizard-next>Weiter</button>
    </div>
  </form>
  <form class="card" hidden data-wizard-step="2">
    <p>Alles bereit! Wir senden Ihnen einen Bestätigungslink.</p>
    <div class="flex-between">
      <button class="btn btn--ghost" type="button" data-wizard-prev>Zurück</button>
      <button class="btn" type="submit">Setup abschließen</button>
    </div>
  </form>
</section>
""",
    },
    "newsletter-optin": {
        "meta": [
            "Double Opt-in Hinweis",
            "Inline Validierung",
            "Success Feedback"
        ],
        "example": """
<form class="newsletter-form" data-newsletter>
  <div class="newsletter-form__fields">
    <div class="input-group">
      <label for="newsletter-email">E-Mail-Adresse</label>
      <input class="input" id="newsletter-email" name="email" type="email" placeholder="you@example.com" required>
      <p class="form-help">Wir senden einen Double-Opt-in-Link.</p>
    </div>
    <button class="btn" type="submit">Anmelden</button>
  </div>
  <label class="input-group" style="flex-direction: row; gap: 0.5rem; align-items: center;">
    <input type="checkbox" name="news-privacy" required>
    <span>Ich stimme dem Erhalt des Newsletters zu.</span>
  </label>
  <p class="form-help" data-newsletter-feedback aria-live="polite"></p>
</form>
""",
    },
    "notification-banner": {
        "meta": [
            "Role Status",
            "Close Button",
            "Keyboard Fokus"
        ],
        "example": """
<section class="notification-banner" role="status" data-notification-banner>
  <div class="flex-between">
    <div>
      <strong>Neue Version verfügbar!</strong>
      <p class="text-muted" style="color: rgba(255,255,255,0.8);">Aktualisieren Sie jetzt, um von Performance-Optimierungen zu profitieren.</p>
    </div>
    <button class="icon-button" type="button" aria-label="Benachrichtigung schließen" data-dismiss-banner>✕</button>
  </div>
</section>
""",
    },
    "pagination": {
        "meta": [
            "ARIA Labels",
            "Erweiterte Klickflächen",
            "Responsives Layout"
        ],
        "example": """
<nav aria-label="Seiten Navigation">
  <ul class="pagination">
    <li class="pagination__item"><a class="pagination__link" href="#" aria-label="Vorherige Seite">‹</a></li>
    <li class="pagination__item"><a class="pagination__link" href="#">1</a></li>
    <li class="pagination__item"><a class="pagination__link" href="#" aria-current="page">2</a></li>
    <li class="pagination__item"><a class="pagination__link" href="#">3</a></li>
    <li class="pagination__item"><a class="pagination__link" href="#" aria-label="Nächste Seite">›</a></li>
  </ul>
</nav>
""",
    },
    "popover": {
        "meta": [
            "Focus Management",
            "Auto Close",
            "ARIA Controls"
        ],
        "example": """
<div class="popover" data-popover>
  <button class="btn btn--ghost" type="button" data-popover-toggle aria-expanded="false" aria-controls="popover-panel">Mehr Infos</button>
  <div class="popover__panel" id="popover-panel" role="dialog">
    <p><strong>Warum wir fragen:</strong></p>
    <p class="text-muted">Wir nutzen Ihre Angaben, um personalisierte Empfehlungen zu erstellen. Ihre Daten bleiben privat.</p>
    <button class="btn btn--ghost" type="button" data-popover-close>Verstanden</button>
  </div>
</div>
""",
    },
    "price-comparison": {
        "meta": [
            "Responsive Karten",
            "Highlight Tarif",
            "Semantische Listen"
        ],
        "example": """
<section class="price-comparison">
  <article class="plan-card" aria-label="Starter Tarif">
    <span class="badge">Starter</span>
    <p class="plan-card__price">19 €<span class="text-muted" style="font-size:0.9rem;">/Monat</span></p>
    <ul class="stack-sm" style="padding-left: 1rem; margin: 0;">
      <li>Bis zu 5 Projekte</li>
      <li>E-Mail Support</li>
      <li>Community Zugang</li>
    </ul>
    <button class="btn btn--ghost" type="button">Jetzt starten</button>
  </article>
  <article class="plan-card plan-card--highlight" aria-label="Professional Tarif">
    <span class="badge badge--success">Beliebt</span>
    <p class="plan-card__price">39 €<span class="text-muted" style="font-size:0.9rem;">/Monat</span></p>
    <ul class="stack-sm" style="padding-left: 1rem; margin: 0;">
      <li>Unbegrenzte Projekte</li>
      <li>Fortgeschrittene Automatisierung</li>
      <li>Priorisierter Support</li>
    </ul>
    <button class="btn" type="button">Kostenlos testen</button>
  </article>
  <article class="plan-card" aria-label="Enterprise Tarif">
    <span class="badge badge--warning">Enterprise</span>
    <p class="plan-card__price">Auf Anfrage</p>
    <ul class="stack-sm" style="padding-left: 1rem; margin: 0;">
      <li>Dedizierte Betreuung</li>
      <li>Single Sign-On</li>
      <li>Custom SLAs</li>
    </ul>
    <button class="btn btn--ghost" type="button">Kontakt aufnehmen</button>
  </article>
</section>
""",
    },
    "product-card": {
        "meta": [
            "Bildverhältnis",
            "Preis Hervorhebung",
            "Bewertung"
        ],
        "example": """
<article class="product-card">
  <div class="product-card__image">
    <img src="https://images.unsplash.com/photo-1512499617640-c2f999098c01?auto=format&fit=crop&w=800&q=80" alt="Minimalistischer Bürostuhl in Grau" loading="lazy">
  </div>
  <div class="product-card__body">
    <div class="review-stars">
      <div class="review-stars__stars" aria-label="4,8 von 5 Sternen">
        <span aria-hidden="true">★ ★ ★ ★ ☆</span>
      </div>
      <span class="text-muted">(128)</span>
    </div>
    <h2>Ergonomischer Chair One</h2>
    <p class="text-muted">Atmungsaktives Mesh, 4D Armlehnen, Sitzhöhenverstellung.</p>
    <p class="product-card__price">349 €</p>
    <div class="share-buttons" role="group" aria-label="Produktaktionen">
      <button class="btn" type="button">In den Warenkorb</button>
      <button class="btn btn--ghost" type="button">Merken</button>
    </div>
  </div>
</article>
""",
    },
    "progress-stepper": {
        "meta": [
            "ARIA Current",
            "Responsives Scrolling",
            "Iconische Darstellung"
        ],
        "example": """
<nav class="stepper" aria-label="Bestellfortschritt">
  <span class="stepper__item" aria-current="step">
    <span aria-hidden="true">1</span>
    <span>Adresse</span>
  </span>
  <span class="stepper__item">
    <span aria-hidden="true">2</span>
    <span>Versand</span>
  </span>
  <span class="stepper__item">
    <span aria-hidden="true">3</span>
    <span>Zahlung</span>
  </span>
</nav>
""",
    },
    "radio-checkbox-toggle": {
        "meta": [
            "ARIA Checked",
            "Benutzerdefinierte Toggle",
            "Form Integration"
        ],
        "example": """
<fieldset class="toggle-group">
  <legend>Benachrichtigungen</legend>
  <div class="toggle">
    <input type="checkbox" id="toggle-email" name="notifications" value="email" checked>
    <label for="toggle-email">E-Mail</label>
  </div>
  <div class="toggle">
    <input type="checkbox" id="toggle-push" name="notifications" value="push">
    <label for="toggle-push">Push</label>
  </div>
  <div class="toggle">
    <input type="radio" id="toggle-daily" name="digest" value="daily" checked>
    <label for="toggle-daily">Täglich</label>
  </div>
  <div class="toggle">
    <input type="radio" id="toggle-weekly" name="digest" value="weekly">
    <label for="toggle-weekly">Wöchentlich</label>
  </div>
</fieldset>
""",
    },
    "review-form": {
        "meta": [
            "Live Rating",
            "Form Feedback",
            "Validierung"
        ],
        "example": """
<form class="review-form" data-review-form>
  <div class="input-group">
    <label for="review-title">Titel Ihrer Bewertung</label>
    <input class="input" id="review-title" required maxlength="80">
  </div>
  <fieldset class="stack-md" aria-describedby="rating-desc">
    <legend>Sternebewertung</legend>
    <p id="rating-desc" class="form-help">Mit Pfeiltasten auswählen. Aktuell: <span data-rating-output>0</span> Sterne.</p>
    <div class="rating-inputs" role="radiogroup">
      <input type="radio" id="rating-5" name="rating" value="5">
      <label for="rating-5" aria-label="5 Sterne">★</label>
      <input type="radio" id="rating-4" name="rating" value="4">
      <label for="rating-4" aria-label="4 Sterne">★</label>
      <input type="radio" id="rating-3" name="rating" value="3">
      <label for="rating-3" aria-label="3 Sterne">★</label>
      <input type="radio" id="rating-2" name="rating" value="2">
      <label for="rating-2" aria-label="2 Sterne">★</label>
      <input type="radio" id="rating-1" name="rating" value="1">
      <label for="rating-1" aria-label="1 Stern">★</label>
    </div>
  </fieldset>
  <div class="input-group">
    <label for="review-comment">Ihre Erfahrung</label>
    <textarea class="input" id="review-comment" rows="4" required></textarea>
  </div>
  <button class="btn" type="submit">Bewertung senden</button>
  <p class="form-help" aria-live="polite" data-review-feedback></p>
</form>
""",
    },
    "review-stars": {
        "meta": [
            "Visuelle Bewertung",
            "Accessible Text",
            "Kontrast"
        ],
        "example": """
<div class="review-stars" aria-label="Durchschnittliche Bewertung 4,6 von 5 Sternen">
  <div class="review-stars__stars" aria-hidden="true">
    <svg class="review-stars__star" viewBox="0 0 20 20" fill="currentColor"><polygon points="10 1 12.6 7.1 19.2 7.3 14 11.6 15.8 18 10 14.3 4.2 18 6 11.6 0.8 7.3 7.4 7.1"></polygon></svg>
    <svg class="review-stars__star" viewBox="0 0 20 20" fill="currentColor"><polygon points="10 1 12.6 7.1 19.2 7.3 14 11.6 15.8 18 10 14.3 4.2 18 6 11.6 0.8 7.3 7.4 7.1"></polygon></svg>
    <svg class="review-stars__star" viewBox="0 0 20 20" fill="currentColor"><polygon points="10 1 12.6 7.1 19.2 7.3 14 11.6 15.8 18 10 14.3 4.2 18 6 11.6 0.8 7.3 7.4 7.1"></polygon></svg>
    <svg class="review-stars__star" viewBox="0 0 20 20" fill="currentColor"><polygon points="10 1 12.6 7.1 19.2 7.3 14 11.6 15.8 18 10 14.3 4.2 18 6 11.6 0.8 7.3 7.4 7.1"></polygon></svg>
    <svg class="review-stars__star" viewBox="0 0 20 20" fill="currentColor" opacity="0.4"><polygon points="10 1 12.6 7.1 19.2 7.3 14 11.6 15.8 18 10 14.3 4.2 18 6 11.6 0.8 7.3 7.4 7.1"></polygon></svg>
  </div>
  <span>4,6/5 (267 Rezensionen)</span>
</div>
""",
    },
    "search": {
        "meta": [
            "Autocomplete ready",
            "Submit CTA",
            "ARIA Live"
        ],
        "example": """
<form class="search-form" role="search" data-search>
  <label class="visually-hidden" for="site-search">Website durchsuchen</label>
  <div class="search-form__field">
    <input class="input" id="site-search" name="q" type="search" placeholder="Wonach suchen Sie?" autocomplete="off" data-search-input aria-describedby="search-suggestions">
    <button class="btn" type="submit">Suchen</button>
  </div>
  <ul id="search-suggestions" class="stack-sm" aria-live="polite" data-search-suggestions role="listbox"></ul>
  <p class="form-help" data-search-feedback aria-live="polite"></p>
</form>
""",
    },
    "share-buttons": {
        "meta": [
            "Web Share API",
            "Fallback Copy",
            "SR Feedback"
        ],
        "example": """
<div class="share-buttons" data-share-buttons aria-label="Inhalte teilen">
  <button class="btn" type="button" data-share-action="native">Teilen</button>
  <button class="btn btn--ghost" type="button" data-share-action="copy">Link kopieren</button>
  <output class="visually-hidden" aria-live="polite" data-share-feedback></output>
</div>
""",
    },
    "skeleton-loader": {
        "meta": [
            "Animation steuerbar",
            "Semantische Rolle",
            "Design Tokens"
        ],
        "example": """
<section class="skeleton-card" role="status" aria-live="polite">
  <div class="skeleton" style="height: 160px; border-radius: var(--radius-md);"></div>
  <div class="skeleton" style="width: 70%;"></div>
  <div class="skeleton" style="width: 50%;"></div>
</section>
""",
    },
    "table": {
        "meta": [
            "Sticky Header",
            "Scroll Container",
            "Caption"
        ],
        "example": """
<div class="table-wrapper">
  <table class="data-table" role="table">
    <caption>Performance Kennzahlen Q1</caption>
    <thead>
      <tr>
        <th scope="col">Metrik</th>
        <th scope="col">Januar</th>
        <th scope="col">Februar</th>
        <th scope="col">März</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <th scope="row">Aktive Nutzer</th>
        <td>12.430</td>
        <td>13.105</td>
        <td>14.890</td>
      </tr>
      <tr>
        <th scope="row">Conversion Rate</th>
        <td>3,2 %</td>
        <td>3,5 %</td>
        <td>3,8 %</td>
      </tr>
      <tr>
        <th scope="row">Net Promoter Score</th>
        <td>41</td>
        <td>44</td>
        <td>46</td>
      </tr>
    </tbody>
  </table>
</div>
""",
    },
    "table-of-contents": {
        "meta": [
            "Toggle mobil",
            "Scrollspy ready",
            "Semantische nav"
        ],
        "example": """
<nav class="toc" data-toc aria-label="Inhaltsverzeichnis">
  <button class="btn btn--ghost toc__toggle" type="button" data-toc-toggle aria-expanded="false">
    <span>Inhaltsverzeichnis</span>
    <span aria-hidden="true">▾</span>
  </button>
  <ol class="toc__list" data-toc-list hidden>
    <li><a href="#abschnitt-1">1. Einleitung</a></li>
    <li><a href="#abschnitt-2">2. Umsetzung</a></li>
    <li><a href="#abschnitt-3">3. Ergebnisse</a></li>
  </ol>
</nav>
""",
    },
    "tags-badges": {
        "meta": [
            "Mehrfarbig",
            "Responsives Wrapping",
            "ARIA Gruppe"
        ],
        "example": """
<div class="badge-collection" role="list">
  <span class="badge" role="listitem">UX Writing</span>
  <span class="badge badge--success" role="listitem">Accessibility</span>
  <span class="badge badge--warning" role="listitem">Research</span>
  <span class="badge" role="listitem">Component Library</span>
</div>
""",
    },
    "toast": {
        "meta": [
            "Aria Live",
            "Auto Dismiss",
            "Mehrere Toaster"
        ],
        "example": """
<div class="stack-md">
  <button class="btn" type="button" data-toast-trigger>Toast anzeigen</button>
  <div class="toast-region" role="status" aria-live="polite" data-toast-region></div>
</div>
""",
    },
    "tooltip": {
        "meta": [
            "Hover &amp; Focus",
            "Aria Expanded",
            "Kurztexte"
        ],
        "example": """
<div class="tooltip" aria-expanded="false" data-tooltip>
  <button class="icon-button" type="button" aria-describedby="tooltip-1" data-tooltip-trigger>?</button>
  <span class="tooltip__bubble" role="tooltip" id="tooltip-1">Wir speichern Ihre Einstellungen sicher verschlüsselt.</span>
</div>
""",
    },
    "trust-badges": {
        "meta": [
            "SVG Icons",
            "Screenreader Text",
            "Responsives Grid"
        ],
        "example": """
<section class="trust-badges" aria-label="Vertrauenssiegel">
  <span class="trust-badge">
    <svg viewBox="0 0 32 32" aria-hidden="true"><path d="M4 6l12-4 12 4v8c0 8-5.3 12.7-12 16-6.7-3.3-12-8-12-16z" fill="currentColor" opacity="0.1"></path><path d="M10 14l4 4 8-8" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round"></path></svg>
    <span>Trusted Shop</span>
  </span>
  <span class="trust-badge">
    <svg viewBox="0 0 32 32" aria-hidden="true"><circle cx="16" cy="16" r="14" fill="currentColor" opacity="0.1"></circle><path d="M10 16l4 4 8-8" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round"></path></svg>
    <span>SSL Secure</span>
  </span>
  <span class="trust-badge">
    <svg viewBox="0 0 32 32" aria-hidden="true"><rect x="6" y="6" width="20" height="20" rx="6" fill="currentColor" opacity="0.1"></rect><path d="M12 16h8" stroke="currentColor" stroke-width="2"></path><path d="M16 12v8" stroke="currentColor" stroke-width="2"></path></svg>
    <span>30 Tage Rückgabe</span>
  </span>
</section>
""",
    },
    "typography": {
        "meta": [
            "Skalierende Fonts",
            "Lesbare Länge",
            "Zitate"
        ],
        "example": """
<article class="typography-demo">
  <header>
    <h1>Designsystem Playbook 2025</h1>
    <p>Ein Leitfaden für skalierbare Content- und UI-Strukturen.</p>
  </header>
  <h2 id="abschnitt-1">Einleitung</h2>
  <p>Klare Typografie schafft Orientierung und steigert die Lesbarkeit auf allen Geräten. Unsere Skala folgt einem modularen System.</p>
  <h3>Listen &amp; Gliederung</h3>
  <ul>
    <li>Definierte Hierarchien</li>
    <li>Kontrastreiche Linkstile</li>
    <li>Klare Abstände</li>
  </ul>
  <blockquote id="abschnitt-2">„Design ist nicht nur wie es aussieht und sich anfühlt. Design ist wie es funktioniert.“ – Steve Jobs</blockquote>
  <pre><code>npm install @acme/content-kit</code></pre>
</article>
""",
    },
    "video-embed": {
        "meta": [
            "Responsive Wrapper",
            "Titel &amp; Transcript",
            "Lazy Loading"
        ],
        "example": """
<section class="card">
  <h2>Produktdemo</h2>
  <div class="video-frame">
    <iframe src="https://www.youtube.com/embed/dQw4w9WgXcQ" title="Produktdemo Video" loading="lazy" allowfullscreen></iframe>
  </div>
  <details>
    <summary>Transkript anzeigen</summary>
    <p class="text-muted">In diesem Video erfahren Sie, wie das Onboarding in weniger als fünf Minuten funktioniert.</p>
  </details>
</section>
""",
    },
}
