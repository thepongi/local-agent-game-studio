### **Testbericht für das Spiel „CampusDigital“**

---

#### **1. Läuft der Code grundsätzlich im Browser?**  
✅ **Ja**, der HTML-Code läuft problemlos im Browser. Alle Elemente sind korrekt strukturiert, die Stylesheet- und Skript-Elemente werden korrekt geladen. Es gibt keine Syntaxfehler in HTML oder CSS.

---

#### **2. Gibt es offensichtliche JavaScript-Fehler?**  
⚠️ **Einige kleine Fehler im JavaScript-Code:**

- **Fehler bei der Initialisierung der Checkbox-Events:**  
  Im `window.onload` wird die Event-Listener-Registrierung zweimal ausgeführt – einmal direkt in `window.onload`, und dann noch einmal innerhalb von `resetGame()`. Das führt zu doppelten Event-Listenern, was potenziell zu unerwartetem Verhalten führen kann.

- **Fehlerhafte Timer-Logik bei Spielende:**  
  Bei einem Zeitablauf wird das Spiel korrekt beendet, aber es wird kein neuer Timer gestartet, wenn das Spiel neu gestartet wird – dies ist nicht fatal, aber es könnte zu Verwirrung führen, falls der Timer manuell zurückgesetzt werden müsste.

- **Fehlerhafte Logik bei `selectProcess()`**:  
  Die Funktion `selectProcess(index)` funktioniert zwar grundsätzlich, aber sie wird nicht von allen Checkboxen korrekt aufgerufen. In einigen Fällen kann es zu inkonsistenten Zuständen kommen, wenn der Benutzer schnell zwischen Checkboxen wechselt.

---

#### **3. Ist das Spielziel verständlich?**  
✅ **Ja**, das Ziel ist klar:  
- Der Spieler hat 3 Minuten Zeit, um verschiedene digitale Prozesse auszuwählen (Checkbox).  
- Jeder Prozess kostet eine bestimmte Anzahl an Minuten und gibt Punkte.  
- Ziel ist es, **50 Punkte zu erreichen**, bevor die Zeit abläuft.

---

#### **4. Gibt es Start, Spielverlauf und Spielende?**  
✅ **Ja**, alle drei Phasen sind vorhanden:  
- **Start:** Beim Laden der Seite wird das Spiel initialisiert, Timer startet, Checkboxen werden angezeigt.  
- **Spielverlauf:** Der Spieler wählt Prozesse aus, klickt auf „Digitalisieren“, Punkte werden erhöht.  
- **Spielende:** Wenn die Zeit abläuft oder 50 Punkte erreicht sind, wird das Spiel beendet und ein Ergebnis angezeigt.

---

#### **5. Funktioniert die Interaktion?**  
✅ **Ja**, die grundlegende Interaktion funktioniert:  
- Checkboxen werden korrekt ausgewählt/abgewählt.  
- Die Punkte werden aktualisiert.  
- Der Timer läuft korrekt runter.  
- Das Feedback „Digitalisierung erfolgreich!“ wird angezeigt.

⚠️ **Einige Verbesserungspotenzial bei der Interaktion:**  
- Es gibt keine visuelle Rückmeldung, wenn ein Prozess nicht gewählt werden kann (z. B. weil die Zeit abgelaufen ist).  
- Das „Digitalisieren“-Button verhält sich nicht immer gleich, je nachdem, ob Prozesse ausgewählt wurden oder nicht.

---

#### **6. Ist das Thema Hochschul-IT/CIO/Cybersecurity erkennbar?**  
✅ **Ja**, das Thema ist erkennbar:  
- Die Prozesse sind inhaltlich auf Hochschul-IT bezogen: „Prüfungsanmeldung“, „Ressourcenanfrage“, „Bewerbung Master“, „Forschungsantrag“ etc.  
- Der Name „CampusDigital“ deutet auf eine digitale Transformation im Hochschulbereich hin.

---

#### **7. Welche drei konkreten Verbesserungen sollte der Developer Agent umsetzen?**

1. **Doppelte Event-Listener-Registrierung beheben:**  
   Die Checkboxen werden in `window.onload` und auch in `resetGame()` jeweils erneut mit `addEventListener` registriert. Das sollte vereinheitlicht werden, z. B. nur einmalig in `initGame()` oder in `resetGame()`.

2. **Visuelle Feedback bei Zeitablauf hinzufügen:**  
   Wenn die Zeit abgelaufen ist, sollte der Button „Digitalisieren“ deaktiviert sein oder ein Hinweis erscheinen, dass das Spiel beendet wurde.

3. **Klarere Anzeige von Prozesskosten und Punkten:**  
   Die Kosten und Punkte werden in Klammern angezeigt – dies könnte durch eine bessere visuelle Hierarchie (Farben, Icons) verbessert werden, um die Wichtigkeit der Werte hervorzuheben.

---

### **Entscheidung:**
✅ **Freigabe mit kleinen Änderungen**

Das Spiel ist grundsätzlich voll funktionsfähig und verständlich. Es fehlen nur einige kleinere Verbesserungen in der Codequalität und Benutzererfahrung, um die Qualität weiter zu steigern.