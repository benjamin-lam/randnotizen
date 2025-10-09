## 🗂️ Shopify Theme Struktur – Ordnerübersicht

### 1. `layout/` – Globale Layout-Dateien
Diese definieren das Grundgerüst jeder Seite.

| Datei                        | Zweck                                                                 |
|-----------------------------|-----------------------------------------------------------------------|
| `theme.liquid`              | Hauptlayout für alle Seiten, enthält Header, Footer, Content-Wrapper |
| `checkout.liquid`           | Layout für den Checkout (nur bei Plus-Shops editierbar)              |
| `password.liquid`           | Layout für Passwortseite bei geschlossenen Shops                     |

**Nice to have:**
- `gift_card.liquid` – Layout für Geschenkkarten
- `email.liquid` – Basislayout für E-Mail-Vorlagen

---

### 2. `templates/` – Seitenvorlagen

| Datei                        | Zweck                                                                 |
|-----------------------------|-----------------------------------------------------------------------|
| `index.liquid`              | Startseite                                                            |
| `product.liquid`            | Produktdetailseite                                                    |
| `collection.liquid`         | Collection-Seite                                                      |
| `cart.liquid`               | Warenkorb                                                             |
| `search.liquid`             | Suchergebnisse                                                        |
| `page.liquid`               | Inhaltsseite                                                          |
| `blog.liquid` / `article.liquid` | Blog-Übersicht und Artikel                                    |

**Nice to have:**
- `404.liquid` – Fehlerseite
- `customers/login.liquid` – Login-Seite
- `customers/register.liquid` – Registrierung
- `customers/account.liquid` – Kundenkonto
- `list-collections.liquid` – Übersicht aller Kollektionen

---

### 3. `sections/` – Inhaltsmodule (modular & dynamisch)

| Datei                        | Zweck                                                                 |
|-----------------------------|-----------------------------------------------------------------------|
| `header.liquid`             | Navigationsleiste, Logo, Menü                                         |
| `footer.liquid`             | Footer mit Links, Newsletter, Social Icons                           |
| `featured-products.liquid`  | Produktliste (z. B. Bestseller)                                       |
| `image-banner.liquid`       | Hero-Bild mit Text                                                    |
| `rich-text.liquid`          | Textblock mit Formatierung                                            |
| `collection-list.liquid`    | Anzeige mehrerer Kollektionen                                         |
| `video.liquid`              | Video-Embed                                                           |

**Nice to have:**
- `newsletter.liquid` – Newsletter-Anmeldung
- `map.liquid` – Standortkarte
- `testimonial.liquid` – Kundenmeinungen
- `countdown.liquid` – Countdown-Timer für Aktionen
- `faq.liquid` – FAQ-Bereich
- `custom-html.liquid` – Freier HTML-Block

---

### 4. `blocks/` – Kleinere Bausteine innerhalb von Sections

| Datei                        | Zweck                                                                 |
|-----------------------------|-----------------------------------------------------------------------|
| `text-block.liquid`         | Einfache Textanzeige                                                  |
| `image-block.liquid`        | Einzelbild                                                            |
| `button-block.liquid`       | Call-to-Action Button                                                 |
| `product-card.liquid`       | Einzelnes Produkt in einer Liste                                      |

**Nice to have:**
- `icon-block.liquid` – SVG/Icon-Anzeige
- `rating-block.liquid` – Sternebewertungen
- `accordion-block.liquid` – Aufklappbare Inhalte

---

### 5. `snippets/` – Wiederverwendbare Code-Fragmente

| Datei                        | Zweck                                                                 |
|-----------------------------|-----------------------------------------------------------------------|
| `price.liquid`              | Preisformatierung                                                     |
| `product-grid-item.liquid`  | Einzelnes Produkt in Grid                                             |
| `social-icons.liquid`       | Social Media Icons                                                    |
| `breadcrumbs.liquid`        | Navigationspfad                                                       |
| `form-errors.liquid`        | Fehleranzeige für Formulare                                           |

**Nice to have:**
- `meta-tags.liquid` – SEO-Metadaten
- `lazy-image.liquid` – Lazy Loading für Bilder
- `wishlist-button.liquid` – Wunschliste
- `quick-add.liquid` – Schnellkauf-Button

---

### 6. `assets/` – Statische Dateien

| Datei                        | Zweck                                                                 |
|-----------------------------|-----------------------------------------------------------------------|
| `theme.css` / `theme.scss`  | Haupt-Stylesheet                                                      |
| `theme.js`                  | JavaScript für Interaktionen                                          |
| `fonts/`                    | Webfonts                                                              |
| `images/`                   | Logos, Icons, Banner                                                  |

**Nice to have:**
- `custom.js` – Eigene Skripte
- `animations.css` – Animationen
- `svg/` – Inline-SVGs

---

### 7. `config/` – Theme-Einstellungen

| Datei                        | Zweck                                                                 |
|-----------------------------|-----------------------------------------------------------------------|
| `settings_schema.json`      | Definiert alle editierbaren Einstellungen im Theme Editor             |
| `settings_data.json`        | Speichert aktuelle Einstellungen                                      |

**Nice to have:**
- `presets.json` – Vordefinierte Layouts für Sections

---

### 8. `locales/` – Übersetzungen

| Datei                        | Zweck                                                                 |
|-----------------------------|-----------------------------------------------------------------------|
| `en.default.json`           | Englische Standardübersetzung                                         |
| `de.default.json`           | Deutsche Übersetzung                                                  |

**Nice to have:**
- `fr.default.json`, `es.default.json`, etc. – Weitere Sprachen

## 🧩 Empfohlene Snippets für UI-Elemente (erweitert)

| Snippet-Datei                  | Zweck / Inhalt                                  | Typisches HTML/Liquid-Element |
|-------------------------------|--------------------------------------------------|-------------------------------|
| `input-text.liquid`           | Einfaches Textfeld                              | `<input type="text">` |
| `input-email.liquid`          | E-Mail-Feld mit Validierung                     | `<input type="email">` |
| `input-password.liquid`       | Passwortfeld                                    | `<input type="password">` |
| `input-number.liquid`         | Zahlenfeld (z. B. Menge, Alter)                 | `<input type="number">` |
| `textarea.liquid`             | Mehrzeiliges Eingabefeld                        | `<textarea>` |
| `select-dropdown.liquid`      | Dropdown-Auswahl                                | `<select>` |
| `checkbox.liquid`             | Checkbox für Zustimmung etc.                   | `<input type="checkbox">` |
| `radio-group.liquid`          | Gruppe von Radio-Buttons                        | `<input type="radio">` |
| `submit-button.liquid`        | Absende-Button                                 | `<input type="submit">` oder `<button>` |
| `button.liquid`               | Wiederverwendbarer Button                      | `<button class="btn">...</button>` |
| `label.liquid`                | Beschriftung für Felder                        | `<label for="...">...</label>` |
| `form-errors.liquid`          | Anzeige von Formularfehlern                    | `{% if form.errors %}...{% endif %}` |
| `form-success.liquid`         | Erfolgsnachricht nach Absenden                 | `<p>Danke für Ihre Nachricht!</p>` |
| `icon.liquid`                 | SVG oder Font-Icon                             | `<svg>...</svg>` oder `<i class="...">` |
| `tooltip.liquid`              | Hilfetext bei Hover                            | `<span class="tooltip">...</span>` |
| `rating-stars.liquid`         | Sternebewertung                                | ⭐⭐⭐⭐⭐ |
| `accordion.liquid`            | Aufklappbare Inhalte                           | `<details><summary>...</summary></details>` |
| `modal.liquid`                | Popup-Fenster                                  | `<div class="modal">...</div>` |
| `spinner.liquid`              | Ladeanimation                                  | `<div class="spinner">...</div>` |
| `progress-bar.liquid`         | Fortschrittsanzeige                            | `<progress value="..." max="100">` |
| `badge.liquid`                | Label für Aktionen, z. B. „Sale“               | `<span class="badge">Sale</span>` |
| `card.liquid`                 | Container für Inhalte (z. B. Produktkarte)      | `<div class="card">...</div>` |
| `image.liquid`                | Responsive Bild mit Lazy Loading               | `<img src="{{ image | img_url: 'medium' }}" loading="lazy">` |
| `video.liquid`                | Video-Embed (z. B. YouTube, MP4)               | `<video src="..." controls>` |
| `breadcrumbs.liquid`          | Navigationspfad                                | `Home › Kategorie › Produkt` |
| `social-icons.liquid`         | Social Media Icons                             | `<a href="..."><i class="icon-facebook"></i></a>` |
| `wishlist-button.liquid`      | Wunschliste hinzufügen                         | `<button>Add to Wishlist</button>` |
| `quick-add.liquid`            | Schnellkauf-Button                             | `<button>Add to Cart</button>` |
| `compare-toggle.liquid`       | Produktvergleich aktivieren                    | `<input type="checkbox"> Vergleichen` |
| `notification.liquid`         | Toast oder Hinweisbox                          | `<div class="notification">...</div>` |
| `tabs.liquid`                 | Reiter-Navigation für Inhalte                  | `<ul class="tabs">...</ul>` |
| `carousel.liquid`             | Bild- oder Produkt-Slider                      | `<div class="carousel">...</div>` |
| `countdown.liquid`            | Countdown-Timer für Aktionen                   | `<span id="countdown">...</span>` |

---
