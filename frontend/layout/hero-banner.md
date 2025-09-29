# Hero Banner

## Kundenanforderung  
Als Besucher:in der Website möchte ich direkt beim Laden der Seite eine prägnante visuelle Botschaft (z. B. Kampagne, Angebot, Markenimage) sehen, damit ich schnell erfasse, worum es hier geht und motiviert werde, weiterzuscrollen.

## Warum ist das so?  
Der Hero-Bereich ist oft der erste visuelle Eindruck. Ein starkes Hero-Banner fokussiert Aufmerksamkeit, kommuniziert zentralen USP oder Aktion und hilft, die Customer Journey direkt zu steuern (Call-to-Action). Für viele Shops ist der Hero der Einstiegspunkt in die Hauptnavigation.  

## Anforderungen & Besonderheiten  
- Bilder oder Videos im Hero sollten performant geladen werden (Lazy-Loading, Responsive, optimierte Formate).  
- Für Barrierefreiheit: Alternativtexte, Texte auch als echtes HTML-Overlay, nicht nur eingebettet ins Bild.  
- Im EU-Kontext: keine automatische Einbindung externer Skripte (z. B. Tracking, Video) ohne Einwilligung gemäß Datenschutz / DSGVO.  
- In vielen Shops wird der Hero dynamisch aus Daten (CMS, Content-Modul) befüllbar sein müssen.  
- Rücksicht auf mobile Devices: verkürzte Versionen oder andere Motive pro Breakpoint.

## Umsetzung – Technische Leitplanken  
- **Mobile First:** Verschiedene Bildgrößen je Breakpoint, `srcset` / `<picture>` mit WebP/AVIF.  
- **Accessibility:** Alt-Attribute, kontrastreiche Texte, Fokus-Management, Stop/Pause-Option bei Animationen.  
- **SEO:** Texte als HTML (nicht in Bild gerendert), Überschriften (H1 / H2) falls sinnvoll im Overlay.  
- **Best Practices:**  
 • Bildoptimierung und Kompression  
 • Lazy Loading / Intersection Observer  
 • A/B-Testing von Varianten  
 • Fallback-Banner falls Bild ausfällt  
 • Konsistenter Aspect-Ratio für verschiedene Geräte  

## Checkliste  
- [ ] Hauptmotiv in allen Breakpoints sichtbar  
- [ ] Alt-Text gesetzt  
- [ ] CTA-Button korrekt verlinkt  
- [ ] Performance-Score > Zielwert  
- [ ] Overlay-Text korrekt positioniert  

## Abhängigkeiten / Überschneidungen  
- CMS / Content-Module  
- Marketing / Kampagnensteuerung  
- SEO / Copywriting  
- Responsive-Design-Grid  

## Akzeptanzkriterien  
- Banner lädt und zeigt korrekt in Desktop / Tablet / Mobile  
- Text & CTA über dem Bild gut lesbar (Kontrast)  
- Kein Layout-Verschieben (CLS minimal)  
- CMS-fähig für Nicht-Entwickler:innen  

---

## Bewertung der Relevanz 2025  
⭐⭐⭐⭐⭐  
Sehr hoch – Hero-Banner bleiben Standard, aber werden 2025 stark durch Performance (Core Web Vitals) und Barrierefreiheit beeinflusst.  

