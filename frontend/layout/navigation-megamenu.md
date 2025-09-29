# Navigation & Mega-Menu

## Kundenanforderung  
Als Nutzer:in möchte ich eine klare, intuitive Navigation mit Kategorien und Unterkategorien sehen, idealerweise mit Vorschaufunktion (Mega-Menu), damit ich schnell finde, was mich interessiert.

## Warum ist das so?  
In großen Shops gibt es viele Kategorien. Nutzer:innen wollen möglichst wenig klicken, um zu relevanten Produkten zu kommen. Ein Mega-Menu bietet Übersicht über Unterkategorien, Promotions und wichtige Seiten.  

## Anforderungen & Besonderheiten  
- Für Mobilgeräte: eventuell Off-Canvas oder Dropdown statt Mega-Menu.  
- Barrierefreiheit: Keyboard-Navigation, Fokussteuerung, ARIA-Rollen.  
- SEO: Kategorien und Unterseiten sollten crawlfähig bleiben.  
- Performance: Menüs sollten asynchron geladen werden (z. B. via AJAX).  
- Contentpflege: Menüstruktur sollte im Backend / CMS pflegbar sein.

## Umsetzung – Technische Leitplanken  
- **Mobile First:** für kleinere Bildschirme das Mega-Menu in mobile Variante (Side Drawer).  
- **Accessibility:** ARIA-Attribute (aria-haspopup, aria-expanded), Fokus-Management, Escape-Verhalten.  
- **SEO:** Menülinks sind echte `<a>`-Links, keine reinen JS-Handler.  
- **Best Practices:**  
 • Lazy load tieferer Ebenen  
 • Caching von Menüstruktur  
 • Verwendung von CSS statt JS, wo möglich  
 • Maximale Tiefe sinnvoll begrenzen  

## Checkliste  
- [ ] Alle Kategorien und Unterkategorien erreichbar  
- [ ] Keyboard-Navigation möglich  
- [ ] Menüstruktur im CMS editierbar  
- [ ] Menü in Mobil-Variante nutzbar  

## Abhängigkeiten / Überschneidungen  
- Kategorie-Struktur / Taxonomie  
- CMS / Backend  
- SEO (Kategorieseiten)  
- Responsive-Design-Komponenten  

## Akzeptanzkriterien  
- Navigation funktioniert mit Maus & Tastatur  
- Kein Überlagern von Inhalten oder Scrollprobleme  
- Menüstruktur korrekt im Backend editierbar  
- Ladezeit im Menü akzeptabel (kein Fake-Lag)  

---

## Bewertung der Relevanz 2025  
⭐⭐⭐⭐☆  
Hoch – in großen Shops fast unverzichtbar, aber für kleine Shops eher simplified Navigation.  

