# Login / Registrierung

## Kundenanforderung  
Als Nutzer:in möchte ich mich registrieren oder einloggen können, damit ich Bestellungen durchführen, Wunschlisten nutzen oder meinen Account verwalten kann.

## Warum ist das so?  
Identifikation ermöglicht Personalisierung, Kundenbindung, Verlaufsspeicherung und schnelleren Checkout.

## Anforderungen & Besonderheiten  
- E-Mail-Verifizierung  
- Passwort-Reset / Sicherheitsregeln  
- Option für Social Login (OAuth, Google, Facebook etc.)  
- Datenschutz: keine ungewollte Profilverknüpfung ohne Zustimmung  

## Umsetzung – Technische Leitplanken  
- **Mobile First:** Eingabeformulare für kleine Bildschirme optimieren  
- **Accessibility:** Labels, ARIA, Fehlermeldungen klar und fokussierbar  
- **SEO:** Login-/Registrierungsseiten nicht indexieren  
- **Best Practices:**  
 • Validierung client + serverseitig  
 • Captcha / Bot-Schutz  
 • Session Handling sicher & langlebig  

## Checkliste  
- [ ] Registrierung möglich  
- [ ] Login mit E-Mail & Passwort  
- [ ] Social Login optional  
- [ ] E-Mail-Verifizierung  
- [ ] Reset-Funktion  

## Abhängigkeiten / Überschneidungen  
- Nutzer- / Auth-System  
- Session / Token-System  
- E-Mail-Service  

## Akzeptanzkriterien  
- Registrierung & Login funktionieren  
- Sicherheitsstandards erfüllt  
- Mobile & Desktop getestet  

---

## Bewertung der Relevanz 2025  
⭐⭐⭐⭐⭐  
Grundfunktion in nahezu jedem Shop – Sicherheit, UX & Datenschutz sind mittlerweile streng.  

