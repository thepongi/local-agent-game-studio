1. **Spielziel**: 
   Spieler müssen das Netzwerk des Universitätscampuses schützen, indem sie Ressourcen wie Firewall-Punkte und Sicherheitskräfte nutzen, um Cyberangriffe abzuwehren.

2. **Bildschirmaufbau**:
   - Oben: Textfeld für die Anzeige der aktuellen Punktzahl
   - Mitte: Canvas zur Darstellung des Campus-Netzwerks mit Systemn节点和连线
   - Unten: Buttons für die Auswahl von Aktionen (z.B. "Angriff verhindern", "Ressourcen hinzufügen")

3. **Spielobjekte**:
   - **Systeme**: Die Knoten des Netzwerks, die sich gegen Angriffe schützen können
   - **Firewall-Punkte**: Ressourcen, die zum Schutz der Systeme beitragen
   - **Sicherheitskräfte**: Ressourcen, die für das Verwalten und Erhöhen der Sicherheit des Netzwerks sorgen

4. **Regeln**:
   - Spieler können Firewall-Punkte und Sicherheitskräfte auf bestimmte Systeme anwenden
   - Jede erfolgreiche Aktion erhöht die Punktzahl
   - Jeder fehlgeschlagene Angriff vermindert die Punktzahl
   - Spielende, wenn Netzwerk vollständig gesichert ist oder eine kritische Angriffslinie geschlagen wird

5. **Punkte-System**:
   - +10 Punkte für jede erfolgreiche Aktion
   - -5 Punkte für jeden fehlgeschlagenen Angriff

6. **Ereignisse im Spiel**:
   - Kritische Angriffslinien erschienen, die das Netzwerk bedrohen
   - Spieler erhalten hinweise zur Stärkung des Netzwerks
   - Zufällige Events (z.B. neue Ressourcen verfügbar)

7. **Benutzerinteraktion**:
   - Mausklick auf Systeme für Aktionen wählen
   - Tastaturkürzel für schnelle Befehle (z.B. "F" für Firewall-Punkt hinzufügen, "S" für Sicherheitskraft hinzufügen)

8. **Minimalversion für den Developer Agent**:
   ```html
   <!DOCTYPE html>
   <html lang="de">
   <head>
       <meta charset="UTF-8">
       <title>Campus-Security-Challenge</title>
       <style>
           canvas { border: 1px solid black; }
       </style>
   </head>
   <body>
       <div id="score">Punkte: 0</div>
       <canvas id="network" width="800" height="600"></canvas>
       <button onclick="addFirewall()">Firewall hinzufügen</button>
       <button onclick="addSecurityForce()">Sicherheitskraft hinzufügen</button>
       
       <script>
           const canvas = document.getElementById('network');
           const ctx = canvas.getContext('2d');
           let score = 0;
           
           function addFirewall() {
               // Logik zur Hinzufügung einer Firewall-Punkte
               updateScore(10);
           }
           
           function addSecurityForce() {
               // Logik zur Hinzufügung einer Sicherheitskraft
               updateScore(10);
           }
           
           function updateScore(points) {
               score += points;
               document.getElementById('score').innerText = 'Punkte: ' + score;
           }
           
           function gameLoop() {
               // Spiellogik und Renderloop
               requestAnimationFrame(gameLoop);
           }
           
           gameLoop();
       </script>
   </body>
   </html>
   ```

9. **Nice-to-have-Erweiterungen**:
   - Multiplayer Modus: CIOs können sich gegenseitig anbieten, um die IT-Sicherheit einer Universitätsnetzwerk zu verstärken.
   - Ressourcen Verwaltung: Spieler müssen Ressourcen wie Firewall-Punkte oder Sicherheitskräfte verwalten, um das Netzwerk robust zu halten.
   - Custom-Levels: Entwickler können benutzerdefinierte IT-Umgebungen erstellen, um die Schwierigkeit des Spiels variieren zu lassen.