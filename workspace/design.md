1. **Spielziel**: Der Spieler (CIO) muss durch eine IT-Umgebung navigieren, indem er verschiedene Aufgaben wie Firewall-Einstellungen, Antivirus-Updates und Benutzersicherheit löst. Das Ziel ist es, alle Systempunkte zu sichern und das Campus-System erfolgreich einzurichten.

2. **Bildschirm aufbau**:
   - Links: Menu mit Spielstart und Optionen (Multiplayer, Zeitbonus, Herausforderungsmodus)
   - Mitte: IT-Umgebung mit Rätseln und Zufallsereignissen
   - Rechts: Statusleiste für Systempunkte, Zeit und aktuellen Task

3. **Spielobjekte**:
   - IT-Umgebung (Network Diagramm, Firewall, Antivirus-Updates)
   - Benutzer-Sicherheitsprüfungsfenster
   - Rätselbrett mit Aufgaben (z.B., Passwort entschlüsseln, Security-Patch installieren)

4. **Regeln**:
   - Der Spieler navigiert durch die IT-Umgebung indem er auf bestimmte Bereiche klickt.
   - Jeder Aufgabe zugeordnet ist ein Riddle oder eine Entscheidung, die gelöst werden muss.
   - Falsche Antworten verursachen einen Fehler und können das Systempunktestand sinken.
   - Korrekte Antworten erhöhen den Punktestand.

5. **Punktesystem**:
   - 10 Punkte pro korrekter Lösung
   - Bonuspunkte (20) für schnelle und korrekte Antworten
   - Jeder Fehler verursacht eine Verzerrung des Systempunktestands um 5%

6. **Ereignisse im Spiel**:
   - Zufallsereignisse wie IT-Ausfälle, Phishing-Angriffe oder Benutzer-Sicherheitsprobleme, die gelöst werden müssen.
   - Herausforderungen wie Simultan mehrere Aufgaben zu lösen.

7. **Benutzerinteraktion**:
   - Mausklicks für die Navigationspunkte und das Interagieren mit dem IT-Umgebung
   - Eingaben für Passwörter oder Codeeinträge

8. **Minimalversion für den Developer Agent**:
   ```html
   <!DOCTYPE html>
   <html lang="de">
   <head>
       <meta charset="UTF-8">
       <title> Campus CyberQuest </title>
       <style>
           /* CSS hier einfügen */
           body { margin: 0; padding: 0; overflow: hidden; }
           #gameArea { position: relative; width: 100vw; height: 100vh; background-color: #f8f9fa; }
           .menu { /* Menu-Stil hier einfügen */ }
           .status { /* Statusleiste-Stil hier einfügen */ }
       </style>
   </head>
   <body>
       <div id="gameArea">
           <!-- IT-Umgebung hier einfügen -->
       </div>
       <div class="menu">Start | Multiplayer | Zeitbonus</div>
       <div class="status">Punkte: 0 | Zeit: 60s</div>

       <script>
           // JavaScript hier einfügen
           document.addEventListener('DOMContentLoaded', () => {
               // Spielinitialisierung hier durchführen
           });

           function handleAction(action) {
               // Handhabung der Spieleraktionen hier durchführen
           }
       </script>
   </body>
   </html>
   ```

9. **Nice-to-have-Erweiterungen**:
   - Multiplayer-Modus: CIOs können sich gegenseitig ansetzen.
   - Zeitbonus: Spieler erhalten bonuspunkte für schnelle und korrekte Antworten.
   - Herausforderungsmodus: Erhöhte Anzahl von Rätseln und schwierigeren Entscheidungen.