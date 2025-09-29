# Gast-Checkout

## Kundenanforderung  
Als Nutzer:in möchte ich auch ohne Registrierung Bestellungen tätigen können, um Friktion zu vermeiden und den Kaufprozess zu beschleunigen.

## Warum ist das so?  
Viele Kunden wollen nicht erst ein Konto anlegen. Gast-Checkout reduziert Abbrüche insbesondere im Kaufprozess.

## Anforderungen & Besonderheiten  
- Speicherung der Versand-/Rechnungsadresse temporär  
- Möglichkeit später Konto anzulegen / Informationen übertragen  
- Datenschutz: Daten nur so lange wie nötig speichern  
- Grenzen: kein komplettes Nutzerprofil möglich  

## Umsetzung – Technische Leitplanken  
- **Mobile First:** Checkout als einspaltiger Fluss  
- **Accessibility:** Formularfelder klar beschriftet  
- **SEO:** Checkout-Seiten nicht indexieren  
- **Best Practices:**  
 • Option „Konto anlegen aus Gastdaten“ anbieten  
 • Warnung / Hinweis zur Registrierung  

## Checkliste  
- [ ] Gastbestellung möglich  
- [ ] Adresseingabe & Validierung  
- [ ] Optional Registrierung nachträglich  
- [ ] Session sauber beendet  

## Abhängigkeiten / Überschneidungen  
- Checkout-Modul  
- Nutzerkonto-System  
- E-Mail-Service  

## Akzeptanzkriterien  
- Bestellung funktioniert als Gast  
- Daten korrekt übergeben  
- Möglichkeit zur späteren Registrierung  

---

## Bewertung der Relevanz 2025  
⭐⭐⭐⭐☆  
Sehr relevant – besonders für Erstkäufer oder unentschlossene Nutzer.  

