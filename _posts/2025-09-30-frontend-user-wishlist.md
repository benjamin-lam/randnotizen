---
title: "Wishlist: Randnotiz"
date: 2025-09-30
tags: [UI, Komponente, Webentwicklung]
excerpt: "Warum Wishlist unsere Frontend-Notizen inspiriert."
layout: post
categories: [frontend]
slug: frontend-user-wishlist
original_path: frontend/user/wishlist.md
---

## Einleitung
Es fühlt sich an wie ein Fund in einer verstaubten Prototyp-Schublade: **Wishlist** passte heute perfekt in unsere Frontend-Gedanken, und plötzlich roch der Raum nach Whiteboard-Markern und frisch gebrühtem Kaffee.

## Technischer Kern
Technisch betrachtet verlangt Wishlist nach klaren Leitplanken. Ich habe die ursprüngliche Beschreibung unten angeheftet und mit Kommentaren versehen, damit der Transfer in das neue Blog sichtbar bleibt.

### Originalnotizen
# Wunschliste / Merkliste

## Kundenanforderung  
Als registrierte:r Nutzer:in möchte ich Produkte auf eine Wunschliste setzen, um sie später zu überblicken oder zu teilen.

## Warum ist das so?  
Nutzer nutzen Wishlist zur Planung, zum Vergleich, zur Erinnerung – und oftmals wird später daraus ein Kauf. Es erhöht Engagement.

## Anforderungen & Besonderheiten  
- Bestände mitberücksichtigen  
- Nutzerbindung & Synchronisation (z. B. zwischen Geräten)  
- Teilen-Funktionen (optional)  
- Datenschutz bei Teil-Links  

## Umsetzung – Technische Leitplanken  
- **Mobile First:** Button „Zur Wunschliste“ prominent erreichbar  
- **Accessibility:** ARIA-Labels, Zustände (aktiv/inaktiv)  
- **SEO:** Kein indexierter Link (Wunschlistenseiten privat)  
- **Best Practices:**  
 • Real-time Feedback („hinzugefügt“)  
 • Synchronisation mit Nutzerkonto  
 • Fallback für Gäste (Session-basiert)  

## Checkliste  
- [ ] Produkte zur Wunschliste hinzufügen / entfernen  
- [ ] Wunschliste persistiert zwischen Sitzungen  
- [ ] Synchronisation über Geräte  
- [ ] Teilen-Option (falls geplant)  

## Abhängigkeiten / Überschneidungen  
- Nutzerkonto / Auth  
- Produktdaten / API  
- Session / Cache  

## Akzeptanzkriterien  
- Wunschliste editierbar  
- Sichtbarkeit & Status korrekt  
- Performance unter hoher Last  

---

## Bewertung der Relevanz 2025  
⭐⭐⭐⭐☆  
Mittel bis hoch – in vielen Shops bereits erwartet. Für kleinere Shops optional.

## Anekdoten & Nerd-Zitate
Michael Crichton hätte wahrscheinlich eine komplette Katastrophensimulation um Wishlist gestrickt, nur um zu zeigen, wie viele Dinge gleichzeitig schiefgehen können. Douglas Coupland würde dagegen eine Slack-Konversation voller Insider-Gags daraus machen. Und irgendwo zwinkert eine alte RFC dazu, weil die Nerd-Fakten selten stillstehen.

## Best Practices
- A11y: Wishlist tastatur- und screenreader-freundlich gestalten.
- Performance: Wishlist nur laden, wenn der Kontext es wirklich braucht.
- Wartbarkeit: Entscheidungen zu Wishlist direkt neben dem Code dokumentieren.

## Fazit
Wishlist bleibt ein schönes Beispiel dafür, wie Frontend-Elemente Geschichten erzählen können, wenn man sie ernst nimmt und trotzdem mit Humor betrachtet.
