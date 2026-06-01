1. **Spielziel:**
   Spieler müssen ein Computer-Virus von einem Hochschulnetzwerk entfernen, indem sie verschiedene IT-Services nutzen und Entscheidungen treffen.

2. **Bildschirmaufbau:**
   - Oben: Netzwerkstatus (Graphik), Ressourcen (CPU, Speicher)
   - Mitte: Buttons für IT-Aktionen (Firewall, Anti-Virus, Malware-Scan)
   - unten: Punktzahl und Spielstand

3. **Spielobjekte:**
   - Virus (Symbol): Die Bedrohung
   - IT-Service-Slots: Für Spieleraktionen
   - Netzwerkgrafik: Anzeige des Netzwerkstatus

4. **Regeln:**
   - Jede Aktion verbraucht Ressourcen.
   - Der Virus beeinträchtigt den Netzwerkstatus und benötigt Ressourcen, um weiterhin anzumachen.
   - Spieler müssen entscheiden, welche IT-Service zu nutzen sind.

5. **Punkte-System:**
   - 1 Punkt für jedes erfolgreich gelöste Virus
   - Verlust von Punkten bei übermäßiger Nutzung von Ressourcen

6. **Ereignisse im Spiel:**
   - Regelmäßige Einführung von neuen Virusen
   - Cyber-Angreifer können zufällig neue Bedrohungen verursachen
   - Ressourcenverschwendung führt zu langsameren Netzwerkstatus

7. **Benutzerinteraktion:**
   - Klicken auf Buttons für IT-Actions
   - Anzeige des Netzwerkstatus und der verfügbaren Ressourcen in realem Zeit

8. **Minimalversion für den Developer Agent:**
   ```html
   <!DOCTYPE html>
   <html lang="de">
   <head>
       <meta charset="UTF-8">
       <title>Campus CyberQuest</title>
       <style>
           body { font-family: Arial, sans-serif; text-align: center; }
           .network-status { margin-top: 20px; font-size: 24px; color: red; }
           .resources { margin-top: 10px; }
           .button { padding: 10px 20px; margin: 5px; cursor: pointer; }
       </style>
   </head>
   <body>
       <div id="network-status">Netzwerkstatus: 100%</div>
       <div class="resources">
           CPU: 100%<br>Speicher: 90%
       </div>
       <button class="button" onclick="action('firewall')">Firewall</button>
       <button class="button" onclick="action('antivirus')">Anti-Virus</button>
       <button class="button" onclick="action('malware-scan')">Malware-Scan</button>

       <script>
           let networkStatus = 100;
           let cpuUsage = 100;
           let memoryUsage = 90;

           function action(service) {
               if (service === 'firewall') {
                   if (cpuUsage > 20) {
                       cpuUsage -= 10;
                       updateNetworkStatus();
                       alert('Firewall erfolgreich angewendet!');
                   } else {
                       alert('Nicht genügend CPU-Ressourcen!');
                   }
               } else if (service === 'antivirus') {
                   if (memoryUsage > 20) {
                       memoryUsage -= 10;
                       updateNetworkStatus();
                       alert('Anti-Virus erfolgreich angewendet!');
                   } else {
                       alert('Nicht genügend Speicher-Ressourcen!');
                   }
               } else if (service === 'malware-scan') {
                   if (cpuUsage > 30 && memoryUsage > 20) {
                       cpuUsage -= 15;
                       memoryUsage -= 10;
                       updateNetworkStatus();
                       alert('Malware-Scan erfolgreich angewendet!');
                   } else {
                       alert('Nicht genügend Ressourcen!');
                   }
               }

               // Zufalls-Virus-Eintritt
               if (Math.random() < 0.1) {
                   networkStatus -= 5;
                   updateNetworkStatus();
                   alert('Neuer Virus!');
               }

               // Netzwerkstatus überprüfen
               if (networkStatus <= 0) {
                   alert('Game Over! Netzwerk verloren.');
                   resetGame();
               }
           }

           function updateNetworkStatus() {
               document.getElementById('network-status').innerText = 'Netzwerkstatus: ' + networkStatus + '%';
               document.querySelector('.resources CPU').innerText = 'CPU: ' + cpuUsage + '%';
               document.querySelector('.resources Speicher').innerText = 'Speicher: ' + memoryUsage + '%';
           }

           function resetGame() {
               networkStatus = 100;
               cpuUsage = 100;
               memoryUsage = 90;
               updateNetworkStatus();
           }
       </script>
   </body>
   </html>
   ```

9. **Nice-to-have-Erweiterungen:**
   - Multiplayer-Funktionalität
   - Ressourcen-Management
   - Schwierigkeitsstufen