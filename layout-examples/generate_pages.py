"""Generate layout example pages from descriptors."""
from __future__ import annotations

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
REPO_ROOT = BASE_DIR.parent

BASE_TEMPLATE = """<!DOCTYPE html>
<html lang=\"de\">
<head>
  <meta charset=\"utf-8\" />
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
  <title>Layout Beispiel – {title}</title>
  <meta name=\"description\" content=\"{description}\" />
  <link rel=\"preconnect\" href=\"https://fonts.googleapis.com\" />
  <link rel=\"preconnect\" href=\"https://fonts.gstatic.com\" crossorigin />
  <link href=\"https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap\" rel=\"stylesheet\" />
  <link rel=\"stylesheet\" href=\"assets/base.css\" />
{style_block}
</head>
<body>
  <a class=\"skip-link\" href=\"#main\">Zum Inhalt springen</a>
  <header class=\"site-header\" role=\"banner\">
    <div class=\"site-header__inner\">
      <span class=\"site-header__title\">{title}</span>
    </div>
  </header>

  <main id=\"main\" class=\"content-width layout-page\" tabindex=\"-1\">
    <section class=\"layout-intro\">
      <p class=\"badge\">{badge}</p>
      <h1 class=\"section-title\">{title}</h1>
      <p class=\"prose\">{intro}</p>
    </section>
{main}
  </main>

  <footer class=\"site-footer site-header\" role=\"contentinfo\">
    <div class=\"site-nav\">
      <a href=\"#main\">Nach oben</a>
    </div>
  </footer>

  <script src=\"assets/base.js\"></script>
{script_block}
</body>
</html>
"""

STYLE_TEMPLATE = "  <style>\n{styles}\n  </style>"
SCRIPT_TEMPLATE = "  <script>\n{script}\n  </script>"

LAYOUTS: dict[str, dict[str, str]] = {
    "accordion-layout": {
        "title": "Accordion Layout",
        "description": "Mobile-First FAQ Muster mit semantischen Details-Elementen und progressiver Offenlegung.",
        "intro": (
            "Dieses Muster eignet sich für umfangreiche FAQ oder Richtlinien. Es nutzt native Details-Elemente, "
            "deaktiviert parallele Öffnungen und bleibt komplett tastaturbedienbar."
        ),
        "badge": "Interaktives Layout",
        "markdown_link": "../layouts/relevant/accordion-layout.md",
        "styles": """
    #preview.layout-accordion {
      display: grid;
      gap: clamp(1.25rem, 4vw, 2rem);
    }

    #preview.layout-accordion details {
      border-radius: var(--radius-lg);
      background: var(--color-card);
      border: 1px solid color-mix(in srgb, var(--color-border) 55%, transparent);
      box-shadow: var(--shadow-soft);
      transition: border-color 0.3s ease, box-shadow 0.3s ease;
    }

    #preview.layout-accordion details[open] {
      border-color: color-mix(in srgb, var(--color-primary) 55%, var(--color-border));
      box-shadow: var(--shadow-hard);
    }

    #preview.layout-accordion summary {
      list-style: none;
      cursor: pointer;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 1rem;
      padding: clamp(1rem, 3vw, 1.5rem) clamp(1rem, 3vw, 1.75rem);
      font-weight: 600;
    }

    #preview.layout-accordion summary::-webkit-details-marker {
      display: none;
    }

    #preview.layout-accordion .summary-icon {
      inline-size: 1.5rem;
      block-size: 1.5rem;
      border-radius: 999px;
      display: grid;
      place-items: center;
      background: color-mix(in srgb, var(--color-primary) 12%, transparent);
      color: var(--color-primary);
      transition: transform 0.3s ease, background 0.3s ease, color 0.3s ease;
    }

    #preview.layout-accordion details[open] .summary-icon {
      transform: rotate(45deg);
      background: var(--color-primary);
      color: var(--color-primary-contrast);
    }

    #preview.layout-accordion details p {
      padding: 0 clamp(1.25rem, 4vw, 2rem) clamp(1.25rem, 4vw, 2rem);
      color: var(--color-muted);
      margin: 0;
    }
        """,
        "main": """
    <section id=\"preview\" class=\"layout-accordion\" data-accordion aria-labelledby=\"accordion-heading\">
      <h2 id=\"accordion-heading\" class=\"sr-only\">Akkordeon Beispiel</h2>
      <details open>
        <summary>
          <span>Wie stelle ich Barrierefreiheit sicher?</span>
          <span class=\"summary-icon\" aria-hidden=\"true\">+</span>
        </summary>
        <p>
          Verwenden Sie native HTML-Elemente, definieren Sie logische Überschriften und stellen Sie sicher, dass jeweils nur
          eine Sektion geöffnet ist. Fokuszustände werden automatisch berücksichtigt.
        </p>
      </details>
      <details>
        <summary>
          <span>Welche Inhalte eignen sich?</span>
          <span class=\"summary-icon\" aria-hidden=\"true\">+</span>
        </summary>
        <p>
          Richtlinien, Support-Fragen oder Tutorial-Schritte lassen sich modular strukturieren. Jede Einheit bleibt unabhängig
          adressierbar.
        </p>
      </details>
      <details>
        <summary>
          <span>Wie skaliert das Layout?</span>
          <span class=\"summary-icon\" aria-hidden=\"true\">+</span>
        </summary>
        <p>
          Mobile-First vollbreit, ab größeren Viewports sorgt <code>clamp()</code> für eine maximale Breite von 72ch und
          großzügige Weißräume.
        </p>
      </details>
    </section>
        """,
    },
    "asymmetric-layout": {
        "title": "Asymmetrisches Layout",
        "description": "Asymmetrische Grid-Struktur mit dominanter Story-Spalte und begleitenden Insights.",
        "intro": (
            "Ideal für Feature-Artikel oder Produktgeschichten: Die Hauptspalte nutzt großzügige Typografie, die Nebenspalte "
            "fasst Kennzahlen und Learnings zusammen."
        ),
        "badge": "Editorial Layout",
        "markdown_link": "../layouts/relevant/asymmetric-layout.md",
        "styles": """
    #preview.layout-asymmetric {
      display: grid;
      gap: clamp(1.5rem, 4vw, 3rem);
    }

    @media (min-width: 56rem) {
      #preview.layout-asymmetric {
        grid-template-columns: minmax(0, 1.1fr) minmax(0, 0.8fr);
        align-items: start;
      }
    }

    #preview.layout-asymmetric figure {
      position: relative;
      border-radius: var(--radius-lg);
      overflow: hidden;
      isolation: isolate;
      box-shadow: var(--shadow-soft);
    }

    #preview.layout-asymmetric figcaption {
      position: absolute;
      inset: auto clamp(1rem, 4vw, 2rem) clamp(1rem, 4vw, 2rem);
      background: color-mix(in srgb, var(--color-card) 82%, transparent);
      backdrop-filter: blur(16px);
      border-radius: var(--radius-lg);
      padding: clamp(0.75rem, 3vw, 1.25rem);
      box-shadow: var(--shadow-soft);
      max-width: min(20rem, 80%);
    }

    #preview.layout-asymmetric aside {
      display: grid;
      gap: clamp(1rem, 3vw, 1.75rem);
    }

    #preview.layout-asymmetric .insight {
      background: var(--color-card);
      padding: clamp(1rem, 3vw, 1.5rem);
      border-radius: var(--radius-lg);
      border: 1px solid color-mix(in srgb, var(--color-border) 55%, transparent);
      box-shadow: var(--shadow-soft);
    }
        """,
        "main": """
    <section id=\"preview\" class=\"layout-asymmetric\" aria-labelledby=\"asymmetric-heading\">
      <div>
        <h2 id=\"asymmetric-heading\">Fallstudie: Circular Design Sprint</h2>
        <p>
          Ein interdisziplinäres Team entwickelte in fünf Tagen eine nachhaltige Produktvision. Das Hauptnarrativ nutzt eine
          breite Spalte mit großzügiger Typografie und Illustrationen.
        </p>
        <figure>
          <img src=\"/assets/agents-and-robots.png\" alt=\"Agentin und Roboter in einer futuristischen Stadt bei Nacht\" />
          <figcaption>
            Prototyping Tag 3: Moderierte Remote-Tests, dokumentiert via Live-Notetaking.
          </figcaption>
        </figure>
        <p>
          Die Bildunterschrift setzt auf Glas-Morphism, der sowohl in hellen als auch dunklen Themes funktioniert.
        </p>
      </div>
      <aside aria-label=\"Insights\">
        <article class=\"insight\">
          <h3>Impact Kennzahlen</h3>
          <p>+34% Conversion im Beta-Test, 92% Completion-Rate beim Onboarding.</p>
        </article>
        <article class=\"insight\">
          <h3>Team Setup</h3>
          <p>Service Design, Research, Produkt, Engineering und Circular-Economy-Expertise.</p>
        </article>
        <article class=\"insight\">
          <h3>Lessons Learned</h3>
          <p>Asymmetrische Layouts lenken Aufmerksamkeit und bleiben dennoch gut lesbar.</p>
        </article>
      </aside>
    </section>
        """,
    },
    "blog-layout": {
        "title": "Blog Layout",
        "description": "Klassisches Blog-Layout mit Featured-Artikel, Beitragssammlung und Sticky-Metadaten.",
        "intro": (
            "Die Startseite bündelt einen herausgehobenen Artikel und listet weitere Beiträge in einer flexiblen Kartenansicht."
        ),
        "badge": "Publikationslayout",
        "markdown_link": "../layouts/relevant/blog-layout.md",
        "styles": """
    #preview.layout-blog {
      display: grid;
      gap: clamp(2rem, 5vw, 3rem);
    }

    #preview.layout-blog .feature {
      display: grid;
      gap: clamp(1rem, 3vw, 1.75rem);
      background: var(--color-card);
      border-radius: var(--radius-lg);
      padding: clamp(1.5rem, 4vw, 2.5rem);
      border: 1px solid color-mix(in srgb, var(--color-border) 55%, transparent);
      box-shadow: var(--shadow-soft);
    }

    #preview.layout-blog .feature figure {
      border-radius: var(--radius-lg);
      overflow: hidden;
    }

    #preview.layout-blog .posts {
      display: grid;
      gap: clamp(1.5rem, 4vw, 2rem);
    }

    @media (min-width: 62rem) {
      #preview.layout-blog .posts {
        grid-template-columns: repeat(3, minmax(0, 1fr));
      }
    }

    #preview.layout-blog article {
      display: grid;
      gap: 0.75rem;
      background: var(--color-card);
      border-radius: var(--radius-lg);
      padding: clamp(1.25rem, 4vw, 1.75rem);
      border: 1px solid color-mix(in srgb, var(--color-border) 55%, transparent);
      box-shadow: var(--shadow-soft);
    }

    #preview.layout-blog .meta {
      display: flex;
      flex-wrap: wrap;
      gap: 0.5rem 1rem;
      color: var(--color-muted);
      font-size: 0.9rem;
    }
        """,
        "main": """
    <section id=\"preview\" class=\"layout-blog\" aria-labelledby=\"blog-heading\">
      <div class=\"feature\">
        <p class=\"badge\">Featured</p>
        <h2 id=\"blog-heading\">Designsysteme im Regelbetrieb</h2>
        <div class=\"meta\">
          <span>12. Februar 2025</span>
          <span>6 Min. Lesezeit</span>
          <span>Produkt &amp; Design</span>
        </div>
        <figure>
          <img src=\"/assets/agents-and-robots.png\" alt=\"Agentin und Roboter in einer futuristischen Stadt bei Nacht\" />
        </figure>
        <p>
          Wie Design- und Engineering-Teams kollaborative Workflows etablieren, um Komponentenbibliotheken nachhaltig zu pflegen.
        </p>
        <a href=\"#\" class=\"badge\">Weiterlesen</a>
      </div>
      <div class=\"posts\" aria-label=\"Weitere Beiträge\">
        <article>
          <h3>Content Ops in 8 Wochen</h3>
          <p>Ein Erfahrungsbericht, wie strukturierte Content-Modelle Launches beschleunigen.</p>
          <div class=\"meta\">
            <span>Content Strategy</span>
            <span>4 Min.</span>
          </div>
        </article>
        <article>
          <h3>Research Backlog Priorisieren</h3>
          <p>Frameworks, um Hypothesen datenbasiert zu bewerten und Tests zu planen.</p>
          <div class=\"meta\">
            <span>User Research</span>
            <span>7 Min.</span>
          </div>
        </article>
        <article>
          <h3>Accessible Dark Mode</h3>
          <p>Kontraste, Farbsemantik und Motion-Guidelines für Dunkelmodus-Designs.</p>
          <div class=\"meta\">
            <span>Design Systems</span>
            <span>5 Min.</span>
          </div>
        </article>
      </div>
    </section>
        """,
    },
    "card-layout": {
        "title": "Card Layout",
        "description": "Karten-basierte Präsentation von Inhalten mit responsiver Grid-Anordnung.",
        "badge": "Komponentenlayout",
        "markdown_link": "../layouts/relevant/card-layout.md",
        "styles": """
    #preview.layout-card {
      display: grid;
      gap: clamp(1.5rem, 4vw, 2.5rem);
    }

    #preview.layout-card .cards {
      display: grid;
      gap: clamp(1.25rem, 3vw, 2rem);
      grid-template-columns: repeat(auto-fit, minmax(min(100%, 18rem), 1fr));
    }

    #preview.layout-card article {
      background: var(--color-card);
      border-radius: var(--radius-lg);
      padding: clamp(1.25rem, 4vw, 1.75rem);
      border: 1px solid color-mix(in srgb, var(--color-border) 55%, transparent);
      box-shadow: var(--shadow-soft);
      display: grid;
      gap: 0.75rem;
    }

    #preview.layout-card .card-footer {
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 1rem;
      font-size: 0.9rem;
      color: var(--color-muted);
    }
        """,
        "main": """
    <section id=\"preview\" class=\"layout-card\" aria-labelledby=\"card-heading\">
      <h2 id=\"card-heading\">Produkt-Features</h2>
      <div class=\"cards\">
        <article>
          <h3>Collaborative Docs</h3>
          <p>Kommentieren, Versionieren und Zuständigkeiten direkt im Dokument verwalten.</p>
          <div class=\"card-footer\">
            <span>Beta</span>
            <a href=\"#\">Mehr erfahren</a>
          </div>
        </article>
        <article>
          <h3>Automationen</h3>
          <p>Arbeitsabläufe mit No-Code-Regeln automatisieren und Statusänderungen melden.</p>
          <div class=\"card-footer\">
            <span>Stabil</span>
            <a href=\"#\">Mehr erfahren</a>
          </div>
        </article>
        <article>
          <h3>Insights Dashboard</h3>
          <p>KPIs in Echtzeit verfolgen und mit Stakeholdern teilen.</p>
          <div class=\"card-footer\">
            <span>Neu</span>
            <a href=\"#\">Mehr erfahren</a>
          </div>
        </article>
      </div>
    </section>
        """,
    },
    "centered-content": {
        "title": "Centered Content",
        "description": "Maximale Lesbarkeit durch zentrierte Inhaltsbreite und großzügige Weißräume.",
        "badge": "Leselayout",
        "markdown_link": "../layouts/relevant/centered-content.md",
        "styles": """
    #preview.layout-centered {
      display: grid;
      justify-items: center;
      text-align: center;
      gap: clamp(1.5rem, 5vw, 2.5rem);
    }

    #preview.layout-centered .prose {
      max-width: clamp(42ch, 68ch, 74ch);
    }
        """,
        "main": """
    <section id=\"preview\" class=\"layout-centered\" aria-labelledby=\"centered-heading\">
      <h2 id=\"centered-heading\">Mission Statement</h2>
      <p class=\"prose\">
        Wir entwerfen digitale Produkte, die komplexe Abläufe in einfache Routinen verwandeln. Fokus, Klarheit und Empathie
        sind die Basis für jedes Erlebnis.
      </p>
      <div class=\"cards\" role=\"list\" aria-label=\"Schwerpunkte\">
        <div class=\"badge\" role=\"listitem\">Research driven</div>
        <div class=\"badge\" role=\"listitem\">Accessible by default</div>
        <div class=\"badge\" role=\"listitem\">Continuous Discovery</div>
      </div>
    </section>
        """,
    },
    "chat-interface": {
        "title": "Chat Interface",
        "description": "Conversational UI mit Nachrichtenspuren, Composer und Präsenzinformationen.",
        "intro": "Das Layout demonstriert ein mobiles Messaging-Interface inklusive Schreibstatus und Reaktionsmöglichkeiten.",
        "badge": "Realtime Layout",
        "markdown_link": "../layouts/relevant/chat-interface.md",
        "styles": """
    #preview.layout-chat {
      display: grid;
      gap: clamp(1.25rem, 4vw, 2rem);
      background: var(--color-card);
      padding: clamp(1.25rem, 4vw, 2rem);
      border-radius: var(--radius-lg);
      border: 1px solid color-mix(in srgb, var(--color-border) 55%, transparent);
      box-shadow: var(--shadow-soft);
    }

    #preview.layout-chat .conversation {
      display: grid;
      gap: 1rem;
    }

    #preview.layout-chat .bubble {
      max-width: min(80%, 32ch);
      padding: 0.75rem 1rem;
      border-radius: 1.25rem;
      position: relative;
      line-height: 1.45;
      box-shadow: var(--shadow-soft);
    }

    #preview.layout-chat .bubble[data-variant="sent"] {
      justify-self: end;
      background: var(--color-primary);
      color: var(--color-primary-contrast);
    }

    #preview.layout-chat .bubble[data-variant="received"] {
      justify-self: start;
      background: color-mix(in srgb, var(--color-primary) 12%, transparent);
      color: var(--color-text);
    }

    #preview.layout-chat .composer {
      display: flex;
      gap: 0.75rem;
      align-items: center;
      border: 1px solid color-mix(in srgb, var(--color-border) 55%, transparent);
      border-radius: 999px;
      padding: 0.75rem 1rem;
      background: var(--color-bg);
    }

    #preview.layout-chat input[type="text"] {
      flex: 1;
      border: 0;
      background: transparent;
    }
        """,
        "main": """
    <section id=\"preview\" class=\"layout-chat\" aria-labelledby=\"chat-heading\">
      <header aria-live=\"polite\">Team Space · <span class=\"badge\">3 online</span></header>
      <div class=\"conversation\" role=\"log\" aria-live=\"polite\">
        <p class=\"bubble\" data-variant=\"received\">
          Hey! Ich teile gleich das neue Dashboard-Konzept. Fokus auf Informationshierarchie.
        </p>
        <p class=\"bubble\" data-variant=\"sent\">
          Super, ich habe direkt Feedback aus dem Research-Playback dabei.
        </p>
        <p class=\"bubble\" data-variant=\"received\">
          Perfekt. Lass uns auf Kontraste achten – wir hatten Hinweise von Screenreader-Usern.
        </p>
      </div>
      <form class=\"composer\" aria-label=\"Nachricht senden\">
        <label for=\"chat-message\" class=\"sr-only\">Nachricht</label>
        <input id=\"chat-message\" type=\"text\" name=\"message\" placeholder=\"Antwort verfassen…\" required />
        <button type=\"submit\">Senden</button>
      </form>
      <p aria-live=\"polite\">Lisa tippt …</p>
    </section>
        """,
        "script": """
    const form = document.querySelector('.composer');
    form?.addEventListener('submit', (event) => {
      event.preventDefault();
      const input = form.querySelector('input');
      if (!input?.value.trim()) return;
      const conversation = form.previousElementSibling;
      const bubble = document.createElement('p');
      bubble.className = 'bubble';
      bubble.dataset.variant = 'sent';
      bubble.textContent = input.value;
      conversation.appendChild(bubble);
      bubble.scrollIntoView({ behavior: 'smooth', block: 'end' });
      input.value = '';
    });
        """,
    },
    "cover-page": {
        "title": "Cover Page",
        "description": "Hero-Cover mit großflächigem Visual, Kernbotschaft und Call-to-Action.",
        "badge": "Hero Layout",
        "markdown_link": "../layouts/relevant/cover-page.md",
        "styles": """
    #preview.layout-cover {
      position: relative;
      border-radius: var(--radius-lg);
      overflow: hidden;
      padding: clamp(3rem, 8vw, 6rem);
      color: var(--color-primary-contrast);
      display: grid;
      gap: clamp(1rem, 4vw, 2rem);
      background: linear-gradient(135deg, rgba(37, 99, 235, 0.8), rgba(76, 29, 149, 0.8));
    }

    #preview.layout-cover::before {
      content: "";
      position: absolute;
      inset: 0;
      background: url('/assets/agents-and-robots.png') center/cover;
      opacity: 0.35;
      mix-blend-mode: screen;
      pointer-events: none;
    }

    #preview.layout-cover > * {
      position: relative;
      z-index: 1;
    }

    #preview.layout-cover .actions {
      display: flex;
      flex-wrap: wrap;
      gap: 1rem;
    }

    #preview.layout-cover a {
      padding: 0.85rem 1.75rem;
      border-radius: 999px;
      background: var(--color-primary-contrast);
      color: var(--color-primary);
      font-weight: 600;
    }
        """,
        "main": """
    <section id=\"preview\" class=\"layout-cover\" aria-labelledby=\"cover-heading\">
      <p class=\"badge\">New Release</p>
      <h2 id=\"cover-heading\">Experience Design Summit 2025</h2>
      <p>
        Drei Tage voller Keynotes, Masterclasses und Clinics rund um nachhaltige digitale Produkte.
      </p>
      <div class=\"actions\">
        <a href=\"#\">Ticket sichern</a>
        <a href=\"#\" aria-label=\"Agenda herunterladen\">Agenda (PDF)</a>
      </div>
    </section>
        """,
    },
    "dashboard-layout": {
        "title": "Dashboard Layout",
        "description": "Analytics-Dashboard mit Kacheln, Chart-Gitter und responsiven Panels.",
        "intro": "Ein flexibles Grid kombiniert Kennzahlen, Diagramme und Listen für die tägliche Steuerung.",
        "badge": "Data Layout",
        "markdown_link": "../layouts/relevant/dashboard-layout.md",
        "styles": """
    #preview.layout-dashboard {
      display: grid;
      gap: clamp(1.5rem, 4vw, 2.5rem);
    }

    #preview.layout-dashboard .kpi-grid {
      display: grid;
      gap: clamp(1rem, 3vw, 1.5rem);
      grid-template-columns: repeat(auto-fit, minmax(min(100%, 15rem), 1fr));
    }

    #preview.layout-dashboard .panel {
      background: var(--color-card);
      border-radius: var(--radius-lg);
      padding: clamp(1.25rem, 3vw, 1.75rem);
      border: 1px solid color-mix(in srgb, var(--color-border) 55%, transparent);
      box-shadow: var(--shadow-soft);
      display: grid;
      gap: 0.75rem;
    }

    #preview.layout-dashboard .grid-visuals {
      display: grid;
      gap: clamp(1rem, 3vw, 1.5rem);
    }

    @media (min-width: 70rem) {
      #preview.layout-dashboard .grid-visuals {
        grid-template-columns: 2fr 1fr;
      }
    }

    #preview.layout-dashboard svg {
      width: 100%;
      height: auto;
    }
        """,
        "main": """
    <section id=\"preview\" class=\"layout-dashboard\" aria-labelledby=\"dashboard-heading\">
      <h2 id=\"dashboard-heading\">Team Performance</h2>
      <div class=\"kpi-grid\">
        <article class=\"panel\">
          <h3>MRR</h3>
          <p class=\"section-title\" style=\"margin:0\">€ 128.400</p>
          <p class=\"badge\">+12% MoM</p>
        </article>
        <article class=\"panel\">
          <h3>Aktive Accounts</h3>
          <p class=\"section-title\" style=\"margin:0\">4.829</p>
          <p class=\"badge\">Retention 93%</p>
        </article>
        <article class=\"panel\">
          <h3>NPS</h3>
          <p class=\"section-title\" style=\"margin:0\">48</p>
          <p class=\"badge\">+6 Punkte</p>
        </article>
      </div>
      <div class=\"grid-visuals\">
        <article class=\"panel\" aria-label=\"Umsatzentwicklung\">
          <h3>Revenue Trend</h3>
          <svg viewBox=\"0 0 240 120\" role=\"img\" aria-labelledby=\"revenue-chart\">
            <title id=\"revenue-chart\">Line Chart der letzten 6 Monate</title>
            <polyline fill=\"none\" stroke=\"currentColor\" stroke-width=\"4\" points=\"0,90 40,80 80,65 120,70 160,50 200,35 240,45\"></polyline>
          </svg>
        </article>
        <article class=\"panel\">
          <h3>Aktuelle Aufgaben</h3>
          <ul>
            <li>Discovery Call vorbereiten</li>
            <li>Feedbackrunde Alpha 2</li>
            <li>Design QA Sprint 14</li>
          </ul>
        </article>
      </div>
    </section>
        """,
    },
    "ecommerce-product-grid": {
        "title": "E-Commerce Produktgrid",
        "description": "Produktübersicht mit Filterleiste, adaptivem Grid und Fokus auf Conversion.",
        "badge": "Commerce Layout",
        "markdown_link": "../layouts/relevant/ecommerce-product-grid.md",
        "styles": """
    #preview.layout-shop {
      display: grid;
      gap: clamp(1.5rem, 4vw, 2.5rem);
    }

    #preview.layout-shop .filters {
      display: flex;
      flex-wrap: wrap;
      gap: 0.75rem;
    }

    #preview.layout-shop .filters button {
      border-radius: 999px;
      border: 1px solid color-mix(in srgb, var(--color-border) 55%, transparent);
      padding: 0.5rem 1.25rem;
      background: color-mix(in srgb, var(--color-primary) 10%, transparent);
    }

    #preview.layout-shop .products {
      display: grid;
      gap: clamp(1.25rem, 3vw, 2rem);
      grid-template-columns: repeat(auto-fit, minmax(min(100%, 14rem), 1fr));
    }

    #preview.layout-shop article {
      display: grid;
      gap: 0.75rem;
      background: var(--color-card);
      border-radius: var(--radius-lg);
      padding: clamp(1rem, 3vw, 1.5rem);
      border: 1px solid color-mix(in srgb, var(--color-border) 55%, transparent);
      box-shadow: var(--shadow-soft);
    }

    #preview.layout-shop img {
      border-radius: var(--radius-lg);
    }

    #preview.layout-shop .price {
      font-weight: 600;
    }
        """,
        "main": """
    <section id=\"preview\" class=\"layout-shop\" aria-labelledby=\"shop-heading\">
      <header>
        <h2 id=\"shop-heading\">Designer Essentials</h2>
        <div class=\"filters\" role=\"list\">
          <button type=\"button\">Neu</button>
          <button type=\"button\">Beliebt</button>
          <button type=\"button\">Unter €50</button>
          <button type=\"button\">Nachhaltig</button>
        </div>
      </header>
      <div class=\"products\">
        <article>
          <img src=\"/assets/agents-and-robots.png\" alt=\"Agentin und Roboter in einer futuristischen Stadt bei Nacht\" />
          <h3>Notizbuch Re:think</h3>
          <p class=\"price\">€ 32</p>
        </article>
        <article>
          <img src=\"/assets/agents-and-robots.png\" alt=\"Agentin und Roboter in einer futuristischen Stadt bei Nacht\" />
          <h3>Hydrate Bottle</h3>
          <p class=\"price\">€ 26</p>
        </article>
        <article>
          <img src=\"/assets/agents-and-robots.png\" alt=\"Agentin und Roboter in einer futuristischen Stadt bei Nacht\" />
          <h3>Focus Headphones</h3>
          <p class=\"price\">€ 189</p>
        </article>
        <article>
          <img src=\"/assets/agents-and-robots.png\" alt=\"Agentin und Roboter in einer futuristischen Stadt bei Nacht\" />
          <h3>Glow Desk Lamp</h3>
          <p class=\"price\">€ 119</p>
        </article>
      </div>
    </section>
        """,
    },
    "full-height-layout": {
        "title": "Full Height Layout",
        "description": "Layout mit 100vh-Abschnitten, Sticky-CTA und Scroll-Indikatoren.",
        "badge": "Viewport Layout",
        "markdown_link": "../layouts/relevant/full-height-layout.md",
        "styles": """
    #preview.layout-full-height {
      display: grid;
      gap: clamp(2rem, 6vw, 3.5rem);
    }

    #preview.layout-full-height section {
      min-height: min(75vh, 42rem);
      border-radius: var(--radius-lg);
      padding: clamp(2rem, 5vw, 4rem);
      background: var(--color-card);
      border: 1px solid color-mix(in srgb, var(--color-border) 55%, transparent);
      box-shadow: var(--shadow-soft);
      display: grid;
      gap: 1rem;
    }

    #preview.layout-full-height .scroll-indicator {
      justify-self: center;
      display: inline-flex;
      flex-direction: column;
      align-items: center;
      gap: 0.5rem;
      color: var(--color-muted);
    }
        """,
        "main": """
    <div id=\"preview\" class=\"layout-full-height\" aria-labelledby=\"fullheight-heading\">
      <section aria-labelledby=\"fullheight-heading\">
        <h2 id=\"fullheight-heading\">Kick-off Sprint</h2>
        <p>Einführung, Erwartungsabgleich und Roadmap-Überblick.</p>
        <a class=\"badge\" href=\"#\">Agenda öffnen</a>
      </section>
      <p class=\"scroll-indicator\" aria-hidden=\"true\">⬇︎ Scroll</p>
      <section>
        <h3>Discovery Workshop</h3>
        <p>Hypothesen, Personas und Journey Mapping kollaborativ erarbeiten.</p>
      </section>
    </div>
        """,
    },
    "full-width-hero": {
        "title": "Full Width Hero",
        "description": "Hero-Sektion über die gesamte Breite mit Medien und CTA.",
        "badge": "Hero Layout",
        "markdown_link": "../layouts/relevant/full-width-hero.md",
        "styles": """
    #preview.layout-hero {
      display: grid;
      gap: clamp(1.5rem, 4vw, 2.5rem);
    }

    @media (min-width: 58rem) {
      #preview.layout-hero {
        grid-template-columns: 1.1fr 1fr;
        align-items: center;
      }
    }

    #preview.layout-hero .media {
      position: relative;
      border-radius: var(--radius-lg);
      overflow: hidden;
      box-shadow: var(--shadow-hard);
    }

    #preview.layout-hero .media img {
      object-fit: cover;
      width: 100%;
      height: 100%;
    }

    #preview.layout-hero .media::after {
      content: "";
      position: absolute;
      inset: 0;
      background: linear-gradient(180deg, transparent, rgba(0, 0, 0, 0.25));
    }

    #preview.layout-hero .actions {
      display: flex;
      flex-wrap: wrap;
      gap: 1rem;
    }
        """,
        "main": """
    <section id=\"preview\" class=\"layout-hero\" aria-labelledby=\"hero-heading\">
      <div>
        <h2 id=\"hero-heading\">Produktivitätsplattform für hybride Teams</h2>
        <p>
          Verbinden Sie Wissensmanagement, Projekte und Kommunikation in einem zentralen Workspace.
        </p>
        <div class=\"actions\">
          <a class=\"badge\" href=\"#\">Kostenlos testen</a>
          <a href=\"#\">Video ansehen</a>
        </div>
      </div>
      <figure class=\"media\">
        <img src=\"/assets/agents-and-robots.png\" alt=\"Agentin und Roboter in einer futuristischen Stadt bei Nacht\" />
      </figure>
    </section>
        """,
    },
    "fullscreen-layout": {
        "title": "Fullscreen Layout",
        "description": "Abschnitte im Vollbild, die per Scroll oder Pfeiltasten gewechselt werden.",
        "badge": "Immersives Layout",
        "markdown_link": "../layouts/relevant/fullscreen-layout.md",
        "styles": """
    #preview.layout-fullscreen {
      display: grid;
      gap: clamp(1.5rem, 4vw, 2.5rem);
    }

    #preview.layout-fullscreen section {
      min-height: min(85vh, 48rem);
      border-radius: var(--radius-lg);
      padding: clamp(2rem, 5vw, 4rem);
      background: var(--color-card);
      border: 1px solid color-mix(in srgb, var(--color-border) 55%, transparent);
      box-shadow: var(--shadow-soft);
      display: grid;
      align-content: center;
      gap: 1.5rem;
      text-align: center;
    }
        """,
        "main": """
    <div id=\"preview\" class=\"layout-fullscreen\" aria-labelledby=\"fullscreen-heading\">
      <section>
        <h2 id=\"fullscreen-heading\">Willkommen</h2>
        <p>Scrollen Sie für Highlights des Produktes. Jede Sektion füllt nahezu das gesamte Viewport.</p>
      </section>
      <section>
        <h3>Schneller Einstieg</h3>
        <p>Interaktive Touren, Onboarding-Checklisten und Guided Tasks helfen bei der Adoption.</p>
      </section>
    </div>
        """,
    },
    "gallery-layout": {
        "title": "Gallery Layout",
        "description": "Responsive Galerie mit adaptiven Spalten und Lightbox-Triggern.",
        "badge": "Visual Layout",
        "markdown_link": "../layouts/relevant/gallery-layout.md",
        "styles": """
    #preview.layout-gallery {
      display: grid;
      gap: clamp(1rem, 3vw, 1.75rem);
    }

    #preview.layout-gallery ul {
      list-style: none;
      padding: 0;
      margin: 0;
      display: grid;
      gap: clamp(0.75rem, 2vw, 1.5rem);
      grid-template-columns: repeat(auto-fit, minmax(min(100%, 12rem), 1fr));
    }

    #preview.layout-gallery li {
      border-radius: var(--radius-lg);
      overflow: hidden;
      box-shadow: var(--shadow-soft);
    }

    #preview.layout-gallery img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }
        """,
        "main": """
    <section id=\"preview\" class=\"layout-gallery\" aria-labelledby=\"gallery-heading\">
      <h2 id=\"gallery-heading\">Moodboard</h2>
      <ul>
        <li><img src=\"/assets/agents-and-robots.png\" alt=\"Agentin und Roboter in einer futuristischen Stadt bei Nacht\" /></li>
        <li><img src=\"/assets/agents-and-robots.png\" alt=\"Agentin und Roboter in einer futuristischen Stadt bei Nacht\" /></li>
        <li><img src=\"/assets/agents-and-robots.png\" alt=\"Agentin und Roboter in einer futuristischen Stadt bei Nacht\" /></li>
        <li><img src=\"/assets/agents-and-robots.png\" alt=\"Agentin und Roboter in einer futuristischen Stadt bei Nacht\" /></li>
      </ul>
    </section>
        """,
    },
    "grid-layout": {
        "title": "Grid Layout",
        "description": "Flexible CSS-Grid-Startseite mit modularem Aufbau über mehrere Zeilen und Spalten.",
        "badge": "Struktur Layout",
        "markdown_link": "../layouts/relevant/grid-layout.md",
        "styles": """
    #preview.layout-grid {
      display: grid;
      gap: clamp(1rem, 3vw, 1.75rem);
      grid-template-columns: repeat(auto-fit, minmax(min(100%, 18rem), 1fr));
      grid-auto-rows: minmax(12rem, auto);
    }

    #preview.layout-grid article {
      background: var(--color-card);
      border-radius: var(--radius-lg);
      padding: clamp(1.25rem, 4vw, 1.75rem);
      border: 1px solid color-mix(in srgb, var(--color-border) 55%, transparent);
      box-shadow: var(--shadow-soft);
      display: grid;
      gap: 0.75rem;
    }

    #preview.layout-grid .wide {
      grid-column: span 2;
    }

    @media (max-width: 60rem) {
      #preview.layout-grid .wide {
        grid-column: span 1;
      }
    }
        """,
        "main": """
    <section id=\"preview\" class=\"layout-grid\" aria-labelledby=\"grid-heading\">
      <article class=\"wide\">
        <h2 id=\"grid-heading\">Hero Update</h2>
        <p>Highlights, Teaser oder Releases erhalten eine doppelte Spaltenbreite.</p>
      </article>
      <article>
        <h3>Community</h3>
        <p>Beiträge, Events und Diskussionen.</p>
      </article>
      <article>
        <h3>Guides</h3>
        <p>Schritt-für-Schritt Anleitungen für neue Features.</p>
      </article>
      <article class=\"wide\">
        <h3>Case Study</h3>
        <p>Vertiefende Insights oder Success Stories mit mehr Fläche.</p>
      </article>
    </section>
        """,
    },
    "header-content-footer": {
        "title": "Header Content Footer",
        "description": "Klassisches Dreiteiler-Layout mit Header, flexiblem Content und Footer.",
        "badge": "Standard Layout",
        "markdown_link": "../layouts/relevant/header-content-footer.md",
        "styles": """
    #preview.layout-hcf {
      display: grid;
      gap: 1rem;
    }

    #preview.layout-hcf header,
    #preview.layout-hcf main,
    #preview.layout-hcf footer {
      background: var(--color-card);
      border-radius: var(--radius-lg);
      padding: clamp(1.25rem, 4vw, 1.75rem);
      border: 1px solid color-mix(in srgb, var(--color-border) 55%, transparent);
      box-shadow: var(--shadow-soft);
    }

    #preview.layout-hcf main {
      min-height: 12rem;
    }
        """,
        "main": """
    <section id=\"preview\" class=\"layout-hcf\" aria-labelledby=\"hcf-heading\">
      <header>
        <h2 id=\"hcf-heading\">Header</h2>
        <p>Logo, Navigation, Utility-Links.</p>
      </header>
      <main>
        <h3>Hauptbereich</h3>
        <p>Semantisch korrekt mit <code>&lt;main&gt;</code> ausgezeichnet.</p>
      </main>
      <footer>
        <h3>Footer</h3>
        <p>Kontakt, rechtliche Hinweise und sekundäre Navigation.</p>
      </footer>
    </section>
        """,
    },
    "header-footer": {
        "title": "Header Footer",
        "description": "Layout mit globalem Kopf- und Fußbereich und leichtgewichtigen Inhaltsslots.",
        "badge": "Grundlayout",
        "markdown_link": "../layouts/relevant/header-footer.md",
        "styles": """
    #preview.layout-hf {
      display: grid;
      gap: 1.5rem;
    }

    #preview.layout-hf .slot {
      background: var(--color-card);
      border-radius: var(--radius-lg);
      padding: clamp(1.25rem, 4vw, 1.75rem);
      border: 1px solid color-mix(in srgb, var(--color-border) 55%, transparent);
      box-shadow: var(--shadow-soft);
    }
        """,
        "main": """
    <section id=\"preview\" class=\"layout-hf\" aria-labelledby=\"hf-heading\">
      <div class=\"slot\">
        <h2 id=\"hf-heading\">Header</h2>
      </div>
      <div class=\"slot\">
        <h3>Content Slot</h3>
        <p>Beliebig kombinierbare Komponenten.</p>
      </div>
      <div class=\"slot\">
        <h3>Footer</h3>
      </div>
    </section>
        """,
    },
    "header-sticky-navigation": {
        "title": "Header Sticky Navigation",
        "description": "Sticky Navigation mit Scrollspy und sekundären Aktionen.",
        "badge": "Navigation",
        "markdown_link": "../layouts/relevant/header-sticky-navigation.md",
        "styles": """
    #preview.layout-sticky-nav {
      position: relative;
      display: grid;
      gap: clamp(1.5rem, 4vw, 2.5rem);
    }

    #preview.layout-sticky-nav nav {
      position: sticky;
      top: 1.5rem;
      background: var(--color-card);
      border-radius: var(--radius-lg);
      padding: clamp(1rem, 3vw, 1.5rem);
      border: 1px solid color-mix(in srgb, var(--color-border) 55%, transparent);
      box-shadow: var(--shadow-soft);
      display: flex;
      flex-wrap: wrap;
      gap: 0.75rem 1.5rem;
    }

    #preview.layout-sticky-nav nav a[aria-current="true"] {
      color: var(--color-primary);
      font-weight: 600;
    }

    #preview.layout-sticky-nav section {
      background: var(--color-card);
      border-radius: var(--radius-lg);
      padding: clamp(1.5rem, 4vw, 2rem);
      border: 1px solid color-mix(in srgb, var(--color-border) 55%, transparent);
      box-shadow: var(--shadow-soft);
      min-height: 16rem;
    }
        """,
        "main": """
    <div id=\"preview\" class=\"layout-sticky-nav\" data-scrollspy aria-labelledby=\"sticky-heading\">
      <nav aria-label=\"Abschnittsnavigation\">
        <a href=\"#section-1\">Überblick</a>
        <a href=\"#section-2\">Design Tokens</a>
        <a href=\"#section-3\">Komponenten</a>
      </nav>
      <section id=\"section-1\">
        <h2 id=\"sticky-heading\">Sticky Navigation</h2>
        <p>Behält Kontext und ermöglicht schnellen Sprung zu Sektionen.</p>
      </section>
      <section id=\"section-2\">
        <h3>Design Tokens</h3>
        <p>Farbpaletten, Typografie und Spacing im Überblick.</p>
      </section>
      <section id=\"section-3\">
        <h3>Komponenten</h3>
        <p>Tabellen, Formulare und Overlays.</p>
      </section>
    </div>
        """,
    },
    "landing-page": {
        "title": "Landing Page",
        "description": "Conversions-getriebene Landingpage mit Hero, Social Proof und Feature-Highlights.",
        "badge": "Marketing Layout",
        "markdown_link": "../layouts/relevant/landing-page.md",
        "styles": """
    #preview.layout-landing {
      display: grid;
      gap: clamp(1.5rem, 4vw, 2.5rem);
    }

    #preview.layout-landing .social-proof {
      display: flex;
      flex-wrap: wrap;
      gap: 1rem;
      align-items: center;
      color: var(--color-muted);
    }

    #preview.layout-landing .features {
      display: grid;
      gap: clamp(1.25rem, 3vw, 2rem);
      grid-template-columns: repeat(auto-fit, minmax(min(100%, 18rem), 1fr));
    }

    #preview.layout-landing .feature-card {
      background: var(--color-card);
      border-radius: var(--radius-lg);
      padding: clamp(1.25rem, 4vw, 1.75rem);
      border: 1px solid color-mix(in srgb, var(--color-border) 55%, transparent);
      box-shadow: var(--shadow-soft);
      display: grid;
      gap: 0.75rem;
    }
        """,
        "main": """
    <section id=\"preview\" class=\"layout-landing\" aria-labelledby=\"landing-heading\">
      <header>
        <h2 id=\"landing-heading\">Launch schneller validieren</h2>
        <p>Von der Hypothese bis zum Beta-Feedback – alles in einem Toolkit.</p>
        <div class=\"social-proof\">
          <span class=\"badge\">Vertraut von 2.400 Teams</span>
          <span>★ ★ ★ ★ ★ 4.8 (G2)</span>
        </div>
      </header>
      <div class=\"features\">
        <article class=\"feature-card\">
          <h3>Geführte Sprints</h3>
          <p>Templates für Discovery, Delivery und Measurement.</p>
        </article>
        <article class=\"feature-card\">
          <h3>Automatisierte Reports</h3>
          <p>Stakeholder-Updates werden automatisch generiert.</p>
        </article>
        <article class=\"feature-card\">
          <h3>Integrationen</h3>
          <p>Verbinden Sie Jira, Figma und Slack ohne Reibungsverlust.</p>
        </article>
      </div>
    </section>
        """,
    },
    "magazine-layout": {
        "title": "Magazin Layout",
        "description": "Editorial Layout mit Multi-Spalten, Highlight-Bannern und Story-Kacheln.",
        "badge": "Editorial",
        "markdown_link": "../layouts/relevant/magazine-layout.md",
        "styles": """
    #preview.layout-magazine {
      display: grid;
      gap: clamp(1.5rem, 4vw, 2.5rem);
    }

    #preview.layout-magazine .lead {
      display: grid;
      gap: 1rem;
      background: var(--color-card);
      border-radius: var(--radius-lg);
      padding: clamp(1.5rem, 4vw, 2.5rem);
      border: 1px solid color-mix(in srgb, var(--color-border) 55%, transparent);
      box-shadow: var(--shadow-soft);
    }

    #preview.layout-magazine .grid {
      display: grid;
      gap: clamp(1.25rem, 3vw, 2rem);
    }

    @media (min-width: 64rem) {
      #preview.layout-magazine .grid {
        grid-template-columns: 2fr 1fr;
      }
    }

    #preview.layout-magazine article {
      background: var(--color-card);
      border-radius: var(--radius-lg);
      padding: clamp(1.25rem, 4vw, 1.75rem);
      border: 1px solid color-mix(in srgb, var(--color-border) 55%, transparent);
      box-shadow: var(--shadow-soft);
    }
        """,
        "main": """
    <section id=\"preview\" class=\"layout-magazine\" aria-labelledby=\"magazine-heading\">
      <div class=\"lead\">
        <p class=\"badge\">Titelstory</p>
        <h2 id=\"magazine-heading\">Die Renaissance des physischen Prototypings</h2>
        <p>Warum Teams wieder analog testen und wie sie Feedback schneller verarbeiten.</p>
      </div>
      <div class=\"grid\">
        <article>
          <h3>Interview</h3>
          <p>Gespräch mit einer Accessibility-Expertin über barrierefreie Messeauftritte.</p>
        </article>
        <article>
          <h3>Kolumne</h3>
          <p>Wie sich Print-Layouts auf digitale Leseflüsse übertragen lassen.</p>
        </article>
      </div>
    </section>
        """,
    },
    "masonry-layout": {
        "title": "Masonry Layout",
        "description": "Kachel-Layout mit unterschiedlichen Höhen und Masonry-Logik.",
        "badge": "Content Grid",
        "markdown_link": "../layouts/relevant/masonry-layout.md",
        "styles": """
    #preview.layout-masonry {
      column-count: 1;
      column-gap: clamp(1rem, 3vw, 1.5rem);
    }

    @media (min-width: 48rem) {
      #preview.layout-masonry {
        column-count: 2;
      }
    }

    @media (min-width: 70rem) {
      #preview.layout-masonry {
        column-count: 3;
      }
    }

    #preview.layout-masonry article {
      display: grid;
      gap: 0.75rem;
      background: var(--color-card);
      border-radius: var(--radius-lg);
      padding: clamp(1rem, 3vw, 1.5rem);
      border: 1px solid color-mix(in srgb, var(--color-border) 55%, transparent);
      box-shadow: var(--shadow-soft);
      margin-bottom: clamp(1rem, 3vw, 1.5rem);
      break-inside: avoid;
    }
        """,
        "main": """
    <div id=\"preview\" class=\"layout-masonry\" aria-labelledby=\"masonry-heading\">
      <article>
        <h2 id=\"masonry-heading\">Kuratiertes Wissen</h2>
        <p>Artikel und Visuals in variabler Höhe.</p>
      </article>
      <article>
        <h3>UX Writing</h3>
        <p>Guidelines für Microcopy und Fehlermeldungen.</p>
      </article>
      <article>
        <h3>Research Toolkit</h3>
        <p>Templates, Checklisten und Workshop-Kits.</p>
      </article>
      <article>
        <h3>Design System</h3>
        <p>Library-Updates, Figma-Komponenten und Token.</p>
      </article>
    </div>
        """,
    },
    "navigation-overlay": {
        "title": "Navigation Overlay",
        "description": "Vollflächiges Navigations-Overlay mit Fokus auf ruhige Interaktion.",
        "badge": "Overlay",
        "markdown_link": "../layouts/relevant/navigation-overlay.md",
        "styles": """
    #preview.layout-overlay {
      display: grid;
      gap: clamp(1.5rem, 4vw, 2.5rem);
    }

    #preview.layout-overlay .trigger {
      width: fit-content;
    }

    #preview.layout-overlay .overlay {
      position: fixed;
      inset: 0;
      background: color-mix(in srgb, var(--color-primary) 12%, rgba(15, 23, 42, 0.9));
      display: grid;
      place-items: center;
      backdrop-filter: blur(18px);
      transition: opacity 0.3s ease;
      opacity: 0;
      visibility: hidden;
    }

    #preview.layout-overlay .overlay[aria-hidden="false"] {
      opacity: 1;
      visibility: visible;
    }

    #preview.layout-overlay nav {
      display: grid;
      gap: 1rem;
      text-align: center;
      font-size: clamp(1.5rem, 4vw, 2.5rem);
    }
        """,
        "main": """
    <section id=\"preview\" class=\"layout-overlay\" aria-labelledby=\"overlay-heading\">
      <h2 id=\"overlay-heading\">Navigation Overlay</h2>
      <button class=\"trigger badge\" type=\"button\" data-overlay-target=\"site-overlay\">Menü öffnen</button>
      <div id=\"site-overlay\" class=\"overlay\" aria-hidden=\"true\">
        <nav aria-label=\"Overlay Navigation\">
          <a href=\"#\">Home</a>
          <a href=\"#\">Stories</a>
          <a href=\"#\">Events</a>
          <a href=\"#\">Kontakt</a>
        </nav>
        <button class=\"trigger\" type=\"button\" data-overlay-close>Schließen</button>
      </div>
    </section>
        """,
    },
    "one-column": {
        "title": "One Column",
        "description": "Einspaltiges Layout mit maximaler Lesbarkeit und ruhigem Rhythmus.",
        "badge": "Leselayout",
        "markdown_link": "../layouts/relevant/one-column.md",
        "styles": """
    #preview.layout-one-column {
      max-width: clamp(52ch, 68ch, 76ch);
      margin-inline: auto;
      display: grid;
      gap: clamp(1.25rem, 4vw, 2rem);
    }
        """,
        "main": """
    <article id=\"preview\" class=\"layout-one-column\" aria-labelledby=\"onecolumn-heading\">
      <h2 id=\"onecolumn-heading\">Lesefreundliche Seite</h2>
      <p>Großzügige Weißräume, klare Typografie und strukturierte Zwischenüberschriften.</p>
      <h3>Abschnitt</h3>
      <p>Kurze Absätze halten die Lesbarkeit hoch und unterstützen Fokus.</p>
    </article>
        """,
    },
    "portfolio-layout": {
        "title": "Portfolio Layout",
        "description": "Projekt-Showcase mit Grid, Case-Study-Vorschau und Filtertags.",
        "badge": "Showcase",
        "markdown_link": "../layouts/relevant/portfolio-layout.md",
        "styles": """
    #preview.layout-portfolio {
      display: grid;
      gap: clamp(1.5rem, 4vw, 2.5rem);
    }

    #preview.layout-portfolio .projects {
      display: grid;
      gap: clamp(1.25rem, 3vw, 2rem);
      grid-template-columns: repeat(auto-fit, minmax(min(100%, 18rem), 1fr));
    }

    #preview.layout-portfolio article {
      background: var(--color-card);
      border-radius: var(--radius-lg);
      padding: clamp(1.25rem, 4vw, 1.75rem);
      border: 1px solid color-mix(in srgb, var(--color-border) 55%, transparent);
      box-shadow: var(--shadow-soft);
      display: grid;
      gap: 0.75rem;
    }

    #preview.layout-portfolio .tags {
      display: flex;
      flex-wrap: wrap;
      gap: 0.5rem;
    }
        """,
        "main": """
    <section id=\"preview\" class=\"layout-portfolio\" aria-labelledby=\"portfolio-heading\">
      <header>
        <h2 id=\"portfolio-heading\">Ausgewählte Projekte</h2>
        <p class=\"tags\">
          <span class=\"badge\">Product Design</span>
          <span class=\"badge\">Research</span>
          <span class=\"badge\">Strategy</span>
        </p>
      </header>
      <div class=\"projects\">
        <article>
          <h3>Marketplace Redesign</h3>
          <p>Verbesserte Information Architecture und Filterlogik.</p>
        </article>
        <article>
          <h3>Health App</h3>
          <p>End-to-End Journey Mapping und Prototypen-Tests.</p>
        </article>
        <article>
          <h3>Analytics Hub</h3>
          <p>Self-Service Dashboards für Growth-Teams.</p>
        </article>
      </div>
    </section>
        """,
    },
    "responsive-flexbox": {
        "title": "Responsive Flexbox",
        "description": "Flexbox-basierte Sektionen, die Reihenfolge und Ausrichtung dynamisch anpassen.",
        "badge": "Flex Layout",
        "markdown_link": "../layouts/relevant/responsive-flexbox.md",
        "styles": """
    #preview.layout-flex {
      display: flex;
      flex-direction: column;
      gap: clamp(1.25rem, 4vw, 2rem);
    }

    #preview.layout-flex .row {
      display: flex;
      flex-direction: column;
      gap: 1rem;
      background: var(--color-card);
      border-radius: var(--radius-lg);
      padding: clamp(1.25rem, 4vw, 1.75rem);
      border: 1px solid color-mix(in srgb, var(--color-border) 55%, transparent);
      box-shadow: var(--shadow-soft);
    }

    @media (min-width: 60rem) {
      #preview.layout-flex .row {
        flex-direction: row;
        align-items: center;
        justify-content: space-between;
      }
    }
        """,
        "main": """
    <section id=\"preview\" class=\"layout-flex\" aria-labelledby=\"flex-heading\">
      <div class=\"row\">
        <h2 id=\"flex-heading\">Flexibles Layout</h2>
        <p>Elemente reihen sich mobil untereinander und orientieren sich am Viewport.</p>
      </div>
      <div class=\"row\">
        <p>Links Inhalt</p>
        <p>Rechts Aktionen</p>
      </div>
    </section>
        """,
    },
    "sidebar-dropdown-menu": {
        "title": "Sidebar Dropdown Menü",
        "description": "Seitliche Navigation mit Dropdown-Unterpunkten und Tastaturnavigation.",
        "badge": "Navigation",
        "markdown_link": "../layouts/relevant/sidebar-dropdown-menu.md",
        "styles": """
    #preview.layout-sidebar-dropdown {
      display: grid;
      gap: clamp(1.5rem, 4vw, 2.5rem);
    }

    #preview.layout-sidebar-dropdown .layout {
      display: grid;
      gap: clamp(1.25rem, 3vw, 2rem);
    }

    @media (min-width: 62rem) {
      #preview.layout-sidebar-dropdown .layout {
        grid-template-columns: minmax(14rem, 18rem) 1fr;
        align-items: start;
      }
    }

    #preview.layout-sidebar-dropdown nav {
      background: var(--color-card);
      border-radius: var(--radius-lg);
      border: 1px solid color-mix(in srgb, var(--color-border) 55%, transparent);
      box-shadow: var(--shadow-soft);
      padding: clamp(1rem, 3vw, 1.5rem);
      display: grid;
      gap: 0.5rem;
    }

    #preview.layout-sidebar-dropdown nav ul {
      list-style: none;
      margin: 0;
      padding: 0;
      display: grid;
      gap: 0.5rem;
    }

    #preview.layout-sidebar-dropdown nav button {
      border: 0;
      background: color-mix(in srgb, var(--color-primary) 6%, transparent);
      border-radius: var(--radius-sm);
      padding: 0.5rem 0.75rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
      width: 100%;
    }

    #preview.layout-sidebar-dropdown nav button[aria-expanded="true"] {
      background: color-mix(in srgb, var(--color-primary) 18%, transparent);
    }

    #preview.layout-sidebar-dropdown nav .submenu {
      display: grid;
      gap: 0.35rem;
      padding-left: 1rem;
      margin: 0.25rem 0 0;
    }

    #preview.layout-sidebar-dropdown main {
      background: var(--color-card);
      border-radius: var(--radius-lg);
      padding: clamp(1.5rem, 4vw, 2rem);
      border: 1px solid color-mix(in srgb, var(--color-border) 55%, transparent);
      box-shadow: var(--shadow-soft);
    }
        """,
        "main": """
    <section id=\"preview\" class=\"layout-sidebar-dropdown\" aria-labelledby=\"sidebar-heading\">
      <div class=\"layout\">
        <nav aria-labelledby=\"sidebar-heading\">
          <h2 id=\"sidebar-heading\">Navigation</h2>
          <ul>
            <li><a href=\"#\">Dashboard</a></li>
            <li>
              <button type=\"button\" data-dropdown-button aria-controls=\"projects-menu\" aria-expanded=\"false\">
                <span>Projekte</span>
                <span aria-hidden=\"true\">▾</span>
              </button>
              <div id=\"projects-menu\" class=\"submenu\" hidden>
                <a href=\"#\">Aktive</a>
                <a href=\"#\">Archiv</a>
              </div>
            </li>
            <li><a href=\"#\">Einstellungen</a></li>
          </ul>
        </nav>
        <main>
          <h3>Projektübersicht</h3>
          <p>Details zu ausgewählten Projekten erscheinen hier.</p>
        </main>
      </div>
    </section>
        """,
    },
    "spa-layout": {
        "title": "SPA Layout",
        "description": "Single-Page-Layout mit App-Shell, Tabs und Content-Routing.",
        "badge": "App Layout",
        "markdown_link": "../layouts/relevant/spa-layout.md",
        "styles": """
    #preview.layout-spa {
      display: grid;
      gap: clamp(1.5rem, 4vw, 2.5rem);
      background: var(--color-card);
      border-radius: var(--radius-lg);
      padding: clamp(1.5rem, 4vw, 2.25rem);
      border: 1px solid color-mix(in srgb, var(--color-border) 55%, transparent);
      box-shadow: var(--shadow-soft);
    }

    #preview.layout-spa .tablist {
      display: inline-flex;
      gap: 0.5rem;
      border-radius: 999px;
      background: color-mix(in srgb, var(--color-primary) 12%, transparent);
      padding: 0.35rem;
    }

    #preview.layout-spa [role="tab"] {
      border: 0;
      background: transparent;
      padding: 0.6rem 1.25rem;
      border-radius: 999px;
    }

    #preview.layout-spa [role="tab"][aria-selected="true"] {
      background: var(--color-primary);
      color: var(--color-primary-contrast);
    }
        """,
        "main": """
    <section id=\"preview\" class=\"layout-spa\" aria-labelledby=\"spa-heading\">
      <header>
        <h2 id=\"spa-heading\">Analytics App</h2>
        <div class=\"tablist\" role=\"tablist\" aria-label=\"Bereiche\">
          <button role=\"tab\" aria-controls=\"spa-overview\" aria-selected=\"true\">Überblick</button>
          <button role=\"tab\" aria-controls=\"spa-reports\" aria-selected=\"false\">Reports</button>
          <button role=\"tab\" aria-controls=\"spa-settings\" aria-selected=\"false\">Einstellungen</button>
        </div>
      </header>
      <article id=\"spa-overview\" role=\"tabpanel\">
        <p>Key Metrics, Alerts und zuletzt gesehene Dashboards.</p>
      </article>
      <article id=\"spa-reports\" role=\"tabpanel\" hidden>
        <p>Report Builder mit drag &amp; drop.</p>
      </article>
      <article id=\"spa-settings\" role=\"tabpanel\" hidden>
        <p>App Einstellungen und Berechtigungen.</p>
      </article>
    </section>
        """,
    },
    "split-screen": {
        "title": "Split Screen",
        "description": "Geteiltes Layout mit gleichwertigen Paneelen und kontrastierenden Inhalten.",
        "badge": "Split Layout",
        "markdown_link": "../layouts/relevant/split-screen.md",
        "styles": """
    #preview.layout-split {
      display: grid;
      gap: clamp(1.5rem, 4vw, 2.5rem);
    }

    @media (min-width: 60rem) {
      #preview.layout-split {
        grid-template-columns: repeat(2, minmax(0, 1fr));
      }
    }

    #preview.layout-split article {
      background: var(--color-card);
      border-radius: var(--radius-lg);
      padding: clamp(1.5rem, 4vw, 2.25rem);
      border: 1px solid color-mix(in srgb, var(--color-border) 55%, transparent);
      box-shadow: var(--shadow-soft);
    }
        """,
        "main": """
    <section id=\"preview\" class=\"layout-split\" aria-labelledby=\"split-heading\">
      <article>
        <h2 id=\"split-heading\">Produkt</h2>
        <p>Leistungsmerkmale, USPs und Differenzierung.</p>
      </article>
      <article>
        <h2>Service</h2>
        <p>Implementierung, Training und Erfolgsmessung.</p>
      </article>
    </section>
        """,
    },
    "sticky-sidebar": {
        "title": "Sticky Sidebar",
        "description": "Hauptinhalt mit fixierter Sidebar für Kontextinfos oder TOC.",
        "badge": "Leselayout",
        "markdown_link": "../layouts/relevant/sticky-sidebar.md",
        "styles": """
    #preview.layout-sticky-sidebar {
      display: grid;
      gap: clamp(1.5rem, 4vw, 2.5rem);
    }

    @media (min-width: 64rem) {
      #preview.layout-sticky-sidebar {
        grid-template-columns: minmax(12rem, 18rem) 1fr;
        align-items: start;
      }
    }

    #preview.layout-sticky-sidebar aside {
      position: sticky;
      top: 1.5rem;
      background: var(--color-card);
      border-radius: var(--radius-lg);
      padding: clamp(1rem, 3vw, 1.5rem);
      border: 1px solid color-mix(in srgb, var(--color-border) 55%, transparent);
      box-shadow: var(--shadow-soft);
    }

    #preview.layout-sticky-sidebar main {
      background: var(--color-card);
      border-radius: var(--radius-lg);
      padding: clamp(1.5rem, 4vw, 2rem);
      border: 1px solid color-mix(in srgb, var(--color-border) 55%, transparent);
      box-shadow: var(--shadow-soft);
    }
        """,
        "main": """
    <section id=\"preview\" class=\"layout-sticky-sidebar\" aria-labelledby=\"sticky-sidebar-heading\">
      <aside aria-labelledby=\"sticky-sidebar-heading\">
        <h2 id=\"sticky-sidebar-heading\">Inhaltsverzeichnis</h2>
        <ol>
          <li>Einführung</li>
          <li>Leitlinien</li>
          <li>Checkliste</li>
        </ol>
      </aside>
      <main>
        <h3>Artikel</h3>
        <p>Langform-Inhalte profitieren von einer fixierten Sidebar zur schnellen Navigation.</p>
      </main>
    </section>
        """,
    },
    "tabbed-interface": {
        "title": "Tabbed Interface",
        "description": "Registerkarten-Layout für strukturierte Informationsarchitektur.",
        "badge": "Interaktiv",
        "markdown_link": "../layouts/relevant/tabbed-interface.md",
        "styles": """
    #preview.layout-tabs {
      display: grid;
      gap: clamp(1.5rem, 4vw, 2.5rem);
      background: var(--color-card);
      border-radius: var(--radius-lg);
      padding: clamp(1.5rem, 4vw, 2rem);
      border: 1px solid color-mix(in srgb, var(--color-border) 55%, transparent);
      box-shadow: var(--shadow-soft);
    }

    #preview.layout-tabs [role="tablist"] {
      display: flex;
      flex-wrap: wrap;
      gap: 0.5rem;
    }

    #preview.layout-tabs [role="tab"] {
      border: 1px solid color-mix(in srgb, var(--color-border) 55%, transparent);
      border-radius: 999px;
      padding: 0.5rem 1.25rem;
      background: transparent;
    }

    #preview.layout-tabs [role="tab"][aria-selected="true"] {
      background: var(--color-primary);
      color: var(--color-primary-contrast);
      border-color: transparent;
    }
        """,
        "main": """
    <section id=\"preview\" class=\"layout-tabs\" aria-labelledby=\"tabs-heading\">
      <h2 id=\"tabs-heading\">Produktbereiche</h2>
      <div role=\"tablist\" aria-label=\"Tabs\">
        <button role=\"tab\" aria-controls=\"tab-one\" aria-selected=\"true\">Übersicht</button>
        <button role=\"tab\" aria-controls=\"tab-two\" aria-selected=\"false\">Roadmap</button>
        <button role=\"tab\" aria-controls=\"tab-three\" aria-selected=\"false\">Support</button>
      </div>
      <article id=\"tab-one\" role=\"tabpanel\">
        <p>Key Metrics und Statusupdates.</p>
      </article>
      <article id=\"tab-two\" role=\"tabpanel\" hidden>
        <p>Nächste Meilensteine und Releases.</p>
      </article>
      <article id=\"tab-three\" role=\"tabpanel\" hidden>
        <p>Support-Artikel, Kontaktoptionen.</p>
      </article>
    </section>
        """,
    },
    "timeline-layout": {
        "title": "Timeline Layout",
        "description": "Chronologische Darstellung von Meilensteinen mit visueller Achse.",
        "badge": "Storytelling",
        "markdown_link": "../layouts/relevant/timeline-layout.md",
        "styles": """
    #preview.layout-timeline {
      display: grid;
      gap: clamp(1.5rem, 4vw, 2.5rem);
    }

    #preview.layout-timeline ol {
      list-style: none;
      margin: 0;
      padding: 0;
      position: relative;
      display: grid;
      gap: clamp(1rem, 3vw, 1.75rem);
    }

    #preview.layout-timeline ol::before {
      content: "";
      position: absolute;
      inset: 0 auto 0 calc(0.75rem);
      width: 2px;
      background: color-mix(in srgb, var(--color-primary) 35%, var(--color-border));
    }

    #preview.layout-timeline li {
      padding-left: 2.5rem;
      position: relative;
    }

    #preview.layout-timeline li::before {
      content: "";
      position: absolute;
      left: 0.5rem;
      top: 0.2rem;
      width: 0.85rem;
      height: 0.85rem;
      border-radius: 50%;
      background: var(--color-primary);
      box-shadow: 0 0 0 4px color-mix(in srgb, var(--color-primary) 20%, transparent);
    }
        """,
        "main": """
    <section id=\"preview\" class=\"layout-timeline\" aria-labelledby=\"timeline-heading\">
      <h2 id=\"timeline-heading\">Projektverlauf</h2>
      <ol>
        <li>
          <h3>Q1: Discovery</h3>
          <p>Research, Hypothesen und Opportunity Solution Trees.</p>
        </li>
        <li>
          <h3>Q2: Beta</h3>
          <p>Prototyping, Tests und erste Rollouts.</p>
        </li>
        <li>
          <h3>Q3: Scale</h3>
          <p>Rollout an alle Kunden, Messung der KPIs.</p>
        </li>
      </ol>
    </section>
        """,
    },
    "two-column-equal-width": {
        "title": "Zweispaltig (gleich breit)",
        "description": "Zweispaltiges Layout mit gleich breiten Spalten und responsive Stack.",
        "badge": "Grid",
        "markdown_link": "../layouts/relevant/two-column-equal-width.md",
        "styles": """
    #preview.layout-two-col {
      display: grid;
      gap: clamp(1.5rem, 4vw, 2.5rem);
    }

    @media (min-width: 56rem) {
      #preview.layout-two-col {
        grid-template-columns: repeat(2, minmax(0, 1fr));
      }
    }

    #preview.layout-two-col article {
      background: var(--color-card);
      border-radius: var(--radius-lg);
      padding: clamp(1.25rem, 4vw, 1.75rem);
      border: 1px solid color-mix(in srgb, var(--color-border) 55%, transparent);
      box-shadow: var(--shadow-soft);
    }
        """,
        "main": """
    <section id=\"preview\" class=\"layout-two-col\" aria-labelledby=\"two-col-heading\">
      <article>
        <h2 id=\"two-col-heading\">Inhalt A</h2>
        <p>Beschreibung für linke Spalte.</p>
      </article>
      <article>
        <h2>Inhalt B</h2>
        <p>Beschreibung für rechte Spalte.</p>
      </article>
    </section>
        """,
    },
    "two-column-left-sidebar": {
        "title": "Zweispaltig mit linker Sidebar",
        "description": "Layout mit schmaler Sidebar links und Content rechts.",
        "badge": "Layout",
        "markdown_link": "../layouts/relevant/two-column-left-sidebar.md",
        "styles": """
    #preview.layout-left-sidebar {
      display: grid;
      gap: clamp(1.5rem, 4vw, 2.5rem);
    }

    @media (min-width: 64rem) {
      #preview.layout-left-sidebar {
        grid-template-columns: minmax(12rem, 16rem) 1fr;
        align-items: start;
      }
    }

    #preview.layout-left-sidebar aside,
    #preview.layout-left-sidebar main {
      background: var(--color-card);
      border-radius: var(--radius-lg);
      padding: clamp(1.25rem, 4vw, 1.75rem);
      border: 1px solid color-mix(in srgb, var(--color-border) 55%, transparent);
      box-shadow: var(--shadow-soft);
    }
        """,
        "main": """
    <section id=\"preview\" class=\"layout-left-sidebar\" aria-labelledby=\"left-sidebar-heading\">
      <aside>
        <h2 id=\"left-sidebar-heading\">Sidebar</h2>
        <p>Navigation oder Zusatzinfos.</p>
      </aside>
      <main>
        <h3>Inhaltsbereich</h3>
        <p>Großzügige Breite für Artikel oder Formulare.</p>
      </main>
    </section>
        """,
    },
    "two-column-right-sidebar": {
        "title": "Zweispaltig mit rechter Sidebar",
        "description": "Layout mit Hauptinhalt links und sekundärer Spalte rechts.",
        "badge": "Layout",
        "markdown_link": "../layouts/relevant/two-column-right-sidebar.md",
        "styles": """
    #preview.layout-right-sidebar {
      display: grid;
      gap: clamp(1.5rem, 4vw, 2.5rem);
    }

    @media (min-width: 64rem) {
      #preview.layout-right-sidebar {
        grid-template-columns: 1fr minmax(12rem, 16rem);
        align-items: start;
      }
    }

    #preview.layout-right-sidebar aside,
    #preview.layout-right-sidebar main {
      background: var(--color-card);
      border-radius: var(--radius-lg);
      padding: clamp(1.25rem, 4vw, 1.75rem);
      border: 1px solid color-mix(in srgb, var(--color-border) 55%, transparent);
      box-shadow: var(--shadow-soft);
    }
        """,
        "main": """
    <section id=\"preview\" class=\"layout-right-sidebar\" aria-labelledby=\"right-sidebar-heading\">
      <main>
        <h2 id=\"right-sidebar-heading\">Content</h2>
        <p>Primärer Inhalt links.</p>
      </main>
      <aside>
        <h3>Sidebar</h3>
        <p>CTA, Werbung oder Support-Infos.</p>
      </aside>
    </section>
        """,
    },
    "fixed-footer": {
        "title": "Fixed Footer",
        "description": "Layout mit fixiertem Footer für permanente Aktionen.",
        "badge": "Deprecated",
        "markdown_link": "../layouts/deprecated/fixed-footer.md",
        "styles": """
    #preview.layout-fixed-footer {
      min-height: 18rem;
      padding-bottom: 4rem;
      position: relative;
      display: grid;
      gap: 1rem;
    }

    #preview.layout-fixed-footer footer {
      position: sticky;
      bottom: 0;
      border-radius: var(--radius-lg);
      background: var(--color-card);
      padding: 1rem 1.5rem;
      border: 1px solid color-mix(in srgb, var(--color-border) 55%, transparent);
      box-shadow: var(--shadow-hard);
    }
        """,
        "main": """
    <section id=\"preview\" class=\"layout-fixed-footer\" aria-labelledby=\"fixed-footer-heading\">
      <h2 id=\"fixed-footer-heading\">Fixierter Footer</h2>
      <p>Wird auf kleinen Screens oft als störend wahrgenommen, daher obsolet.</p>
      <footer>
        <button type=\"button\">Jetzt kaufen</button>
      </footer>
    </section>
        """,
    },
    "horizontal-scrolling": {
        "title": "Horizontal Scrolling",
        "description": "Horizontale Scrollbereiche für Navigationsleisten.",
        "badge": "Deprecated",
        "markdown_link": "../layouts/deprecated/horizontal-scrolling.md",
        "styles": """
    #preview.layout-horizontal {
      display: grid;
      gap: 1rem;
    }

    #preview.layout-horizontal .scroller {
      display: flex;
      gap: 1rem;
      overflow-x: auto;
      padding: 1rem;
      background: var(--color-card);
      border-radius: var(--radius-lg);
      border: 1px solid color-mix(in srgb, var(--color-border) 55%, transparent);
    }
        """,
        "main": """
    <section id=\"preview\" class=\"layout-horizontal\" aria-labelledby=\"horizontal-heading\">
      <h2 id=\"horizontal-heading\">Horizontales Scrollen</h2>
      <div class=\"scroller\">
        <a href=\"#\">Link 1</a>
        <a href=\"#\">Link 2</a>
        <a href=\"#\">Link 3</a>
        <a href=\"#\">Link 4</a>
      </div>
    </section>
        """,
    },
    "nested-columns": {
        "title": "Nested Columns",
        "description": "Mehrfach verschachtelte Spaltenstrukturen.",
        "badge": "Deprecated",
        "markdown_link": "../layouts/deprecated/nested-columns.md",
        "styles": """
    #preview.layout-nested {
      display: grid;
      gap: 1rem;
    }

    #preview.layout-nested .outer {
      display: grid;
      gap: 1rem;
    }

    @media (min-width: 60rem) {
      #preview.layout-nested .outer {
        grid-template-columns: repeat(3, minmax(0, 1fr));
      }
    }

    #preview.layout-nested .inner {
      display: grid;
      gap: 0.75rem;
    }
        """,
        "main": """
    <section id=\"preview\" class=\"layout-nested\" aria-labelledby=\"nested-heading\">
      <h2 id=\"nested-heading\">Verschachtelte Spalten</h2>
      <div class=\"outer\">
        <div class=\"inner\">
          <p>Inner Column 1</p>
          <p>Inner Column 1b</p>
        </div>
        <div class=\"inner\">
          <p>Inner Column 2</p>
        </div>
        <div class=\"inner\">
          <p>Inner Column 3</p>
          <p>Inner Column 3b</p>
        </div>
      </div>
    </section>
        """,
    },
    "sidebar-navigation": {
        "title": "Sidebar Navigation",
        "description": "Fixierte Sidebar ohne mobile Optimierung.",
        "badge": "Deprecated",
        "markdown_link": "../layouts/deprecated/sidebar-navigation.md",
        "styles": """
    #preview.layout-sidebar-nav {
      display: grid;
      gap: 1.5rem;
    }

    #preview.layout-sidebar-nav .layout {
      display: grid;
      gap: 1rem;
    }

    @media (min-width: 70rem) {
      #preview.layout-sidebar-nav .layout {
        grid-template-columns: 16rem 1fr;
      }
    }

    #preview.layout-sidebar-nav nav {
      background: var(--color-card);
      border-radius: var(--radius-lg);
      padding: 1.25rem;
      border: 1px solid color-mix(in srgb, var(--color-border) 55%, transparent);
      box-shadow: var(--shadow-soft);
      height: 100vh;
    }
        """,
        "main": """
    <section id=\"preview\" class=\"layout-sidebar-nav\" aria-labelledby=\"sidebar-nav-heading\">
      <h2 id=\"sidebar-nav-heading\">Starre Sidebar</h2>
      <div class=\"layout\">
        <nav>
          <ul>
            <li><a href=\"#\">Home</a></li>
            <li><a href=\"#\">Projekte</a></li>
            <li><a href=\"#\">Kontakt</a></li>
          </ul>
        </nav>
        <article>
          <p>Keine mobile Adaption – deshalb deprecated.</p>
        </article>
      </div>
    </section>
        """,
    },
    "split-header": {
        "title": "Split Header",
        "description": "Geteilter Header mit zwei Ebenen, schwer zugänglich auf mobilen Geräten.",
        "badge": "Deprecated",
        "markdown_link": "../layouts/deprecated/split-header.md",
        "styles": """
    #preview.layout-split-header {
      display: grid;
      gap: 1rem;
    }

    #preview.layout-split-header header {
      display: flex;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 1rem;
      background: var(--color-card);
      border-radius: var(--radius-lg);
      padding: 1rem 1.5rem;
      border: 1px solid color-mix(in srgb, var(--color-border) 55%, transparent);
      box-shadow: var(--shadow-soft);
    }
        """,
        "main": """
    <section id=\"preview\" class=\"layout-split-header\" aria-labelledby=\"split-header-heading\">
      <h2 id=\"split-header-heading\">Split Header</h2>
      <header>
        <div>Logo + Suche</div>
        <nav><a href=\"#\">Link A</a> · <a href=\"#\">Link B</a></nav>
      </header>
      <p>Auf mobilen Geräten schwer skalierbar.</p>
    </section>
        """,
    },
    "three-columns": {
        "title": "Three Columns",
        "description": "Dreispaltiges Layout ohne mobile Strategie.",
        "badge": "Deprecated",
        "markdown_link": "../layouts/deprecated/three-columns.md",
        "styles": """
    #preview.layout-three-columns {
      display: grid;
      gap: 1rem;
    }

    @media (min-width: 70rem) {
      #preview.layout-three-columns {
        grid-template-columns: repeat(3, minmax(0, 1fr));
      }
    }

    #preview.layout-three-columns article {
      background: var(--color-card);
      border-radius: var(--radius-lg);
      padding: 1.25rem;
      border: 1px solid color-mix(in srgb, var(--color-border) 55%, transparent);
      box-shadow: var(--shadow-soft);
    }
        """,
        "main": """
    <section id=\"preview\" class=\"layout-three-columns\" aria-labelledby=\"three-columns-heading\">
      <h2 id=\"three-columns-heading\">Drei Spalten</h2>
      <article>Spalte 1</article>
      <article>Spalte 2</article>
      <article>Spalte 3</article>
    </section>
        """,
    },
}


def generate_page(slug: str, config: dict[str, str]) -> str:
  """Return rendered HTML for given layout."""
  style_block = STYLE_TEMPLATE.format(styles=config.get("styles", "").strip()) if config.get("styles") else ""
  script_block = SCRIPT_TEMPLATE.format(script=config.get("script", "").strip()) if config.get("script") else ""
  main = config.get("main", "").rstrip()
  return BASE_TEMPLATE.format(
      title=config["title"],
      description=config["description"],
      badge=config.get("badge", "Layout Beispiel"),
      intro=config.get("intro", config["description"]),
      main=main,
      style_block=style_block,
      script_block=script_block,
  )


def build_index(layouts: dict[str, dict[str, str]]) -> str:
  """Return HTML index page for all layout demos."""
  items: list[str] = []
  for slug, config in sorted(layouts.items(), key=lambda entry: entry[1]["title"].lower()):
    category = "Deprecated" if "/deprecated/" in config["markdown_link"] else "Relevant"
    items.append(
        f"        <li><a href=\"{slug}.html\">{config['title']}</a> "
        f"<span class=\"badge\">{category}</span></li>"
    )

  items_markup = "\n".join(items)
  template = """<!DOCTYPE html>
<html lang=\"de\">
<head>
  <meta charset=\"utf-8\" />
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
  <title>Layout Beispiele Index</title>
  <meta name=\"description\" content=\"Übersicht über alle Layout-Demos aus den Randnotizen." />
  <link rel=\"preconnect\" href=\"https://fonts.googleapis.com\" />
  <link rel=\"preconnect\" href=\"https://fonts.gstatic.com\" crossorigin />
  <link href=\"https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap\" rel=\"stylesheet\" />
  <link rel=\"stylesheet\" href=\"assets/base.css\" />
  <style>
    main {
      display: grid;
      gap: clamp(1.5rem, 4vw, 2.5rem);
      padding-block: clamp(2.5rem, 6vw, 5rem);
    }

    ul.layout-list {
      list-style: none;
      padding: 0;
      margin: 0;
      display: grid;
      gap: 0.75rem;
    }

    ul.layout-list li {
      background: var(--color-card);
      border-radius: var(--radius-lg);
      padding: 1rem 1.5rem;
      border: 1px solid color-mix(in srgb, var(--color-border) 55%, transparent);
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 1rem;
    }
  </style>
</head>
<body>
  <a class=\"skip-link\" href=\"#main\">Zum Inhalt springen</a>
  <header class=\"site-header\" role=\"banner\">
    <div class=\"site-header__inner\">
      <span class=\"site-header__title\">Layout Demos</span>
    </div>
  </header>
  <main id=\"main\" class=\"content-width\" tabindex=\"-1\">
    <section class=\"layout-intro\">
      <p class=\"badge\">Übersicht</p>
      <h1 class=\"section-title\">Layout Demos</h1>
      <p class=\"prose\">Alle Layout-Beispiele aus den Markdown-Beschreibungen – mobil optimiert und vanilla HTML/CSS/JS.</p>
    </section>
    <ul class=\"layout-list\">
{items}
    </ul>
  </main>
  <footer class=\"site-footer site-header\" role=\"contentinfo\">
    <div class=\"site-nav\">
      <a href=\"#main\">Nach oben</a>
    </div>
  </footer>
  <script src=\"assets/base.js\"></script>
</body>
</html>
"""
  return template.replace("{items}", items_markup)


def main() -> None:
  target_dir = REPO_ROOT / "layout-examples"
  for slug, config in LAYOUTS.items():
    html = generate_page(slug, config)
    file_path = target_dir / f"{slug}.html"
    file_path.write_text(html, encoding="utf-8")
    print(f"Generated {file_path.relative_to(REPO_ROOT)}")
  index_html = build_index(LAYOUTS)
  (target_dir / "index.html").write_text(index_html, encoding="utf-8")
  print("Generated layout-examples/index.html")


if __name__ == "__main__":
  main()
