**1. Spielziel:**  
Der Spieler optimiert einen Hochschulverwaltungsprozess durch gezielte Automatisierung innerhalb von 2 Minuten – um den höchsten Wert (Effizienz) zu erreichen.

---

**2. Bildschirmaufbau:**  
- **Oberer Bereich:** Timer (2:00), Punktestand, Spielstatus („Laufend“ / „Beendet“)  
- **Mittlerer Bereich:** Liste der Prozesse mit Spalten:  
  - Name des Prozesses  
  - Zeit (in Minuten)  
  - Wert (Punkte)  
  - Automatisierungspunkte (Eingabefeld 0–10)  
- **Unterer Bereich:**  
  - Start-/Neustart-Button  
  - „Zusammenfassung“ (nach Spielende): Erreichte Punkte, Prozentualer Erfolg  

---

**3. Spielobjekte:**  
- **Prozess:** Ein Objekt mit Eigenschaften: Name, Zeit, Wert, Automatisierungspunkte  
- **Timer:** Zählt rückwärts von 2:00  
- **Punktestand:** Summe aller erreichten Werte basierend auf der Verteilung der Punkte  
- **Automatisierungspunkte:** Verfügbare Ressourcen (max. 10 pro Prozess)  

---

**4. Regeln:**  
- Spieler verteilt 0–10 Automatisierungspunkte auf jeden Prozess  
- Jeder Prozess kann maximal 10 Punkte erhalten  
- Punkte werden nur vergeben, wenn der Prozess automatisiert wurde (d.h. mindestens 1 Punkt zugewiesen)  
- Die Summe aller Punkte ist der erreichte Wert  
- Spiel endet bei Ablauf des Timers oder bei vollständiger Automatisierung aller Prozesse  

---

**5. Punkte-System:**  
- **Basiswert:** Wert des Prozesses × (Zugewiesene Punkte / 10)  
- **Bonuspunkte:**  
  - Bei optimaler Verteilung (maximaler Wert mit minimaler Zeit): +10% Bonus  
  - Schnelle Entscheidungen (innerhalb von 30 Sekunden): +5% Bonus  

---

**6. Ereignisse im Spiel:**  
- **Zeitdruck:** Timer läuft, Spieler muss schnell entscheiden  
- **Zufallsereignis:** Einmalig in der Mitte des Spiels:  
  - „Systemfehler“ – 10 Sekunden Pause, 2 Prozesse werden „zerstört“ (nicht mehr automatisierbar)  
- **Optimale Verteilung:** Bei korrekter Strategie wird ein „Performance Bonus“ freigeschaltet  

---

**7. Benutzerinteraktion:**  
- Eingabe von Automatisierungspunkten per Tastatur oder Maus (Eingabefelder)  
- Start-Button zum Beginn  
- Neustart-Button zum Wiederholen  
- Spielstatus wird in Echtzeit aktualisiert  

---

**8. Minimalversion für den Developer Agent:**  
- index.html mit Timer, Prozessliste, Eingabefeldern, Punkteanzeige  
- JavaScript zur Steuerung des Timers, Verteilung und Bewertung  
- Keine externe Bibliothek – nur HTML, CSS, JS  
- Responsive Layout (funktioniert auf Desktop und Mobil)  

---

**9. Nice-to-have-Erweiterungen:**  
1. **Level-Up:** 3 Schwierigkeitsstufen mit mehr Prozessen und komplexeren Abläufen  
2. **Zufallsereignisse:** Mehr Systemfehler, Serverprobleme, Störungen  
3. **Bewertungssystem:** Spielergebnis wird als „Effizienz-Index“ bewertet (Punkte / Zeit)  
4. **Grafik-Upgrade:** Minimalistische Icons für Prozesse, Farbcodierung für Zeit/Wert  
5. **Lokalisierung:** Deutsch und Englisch  

---