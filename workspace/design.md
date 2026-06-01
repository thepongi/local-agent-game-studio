1. **Spielziel**:
   Spieler müssen IT-Systeme einer virtuellen Universität vor Cyberangriffen schützen, indem sie verschiedene Sicherheitsmaßnahmen mit ihrem Budget ankaufen und implementieren.

2. **Bildschirmaufbau**:
   - oben: Spielbrett mit IT-Systemen (z.B., Server, Router)
   - mittig: Budget-Balken
   - unten: Ankaufsliste von Sicherheitsmaßnahmen

3. **Spielobjekte**:
   - IT-Systeme (Server, Router, Firewall, Anti-Virus-Software)
   - Cyberangriffe (DDoS-Angriff, Phishing-Mail)

4. **Regeln**:
   - Spieler haben ein Startbudget.
   - Sie können Sicherheitsmaßnahmen kaufen und auf dem Spielbrett installieren.
   - Cyberangriffe werden zufällig simuliert.
   - Bei erfolgreichen Angriffen verliert der Spieler Budget und beschädigt IT-Systeme.
   - Das Spiel gewinnt, wenn alle Systeme vor Attacken geschützt sind.

5. **Punkte-System**:
   - Punkte für erfolgreich abwehrende Maßnahmen.
   - Punkte für jede verhinderte Cyberangriff.

6. **Ereignisse im Spiel**:
   - Zufällige Cyberangriffe
   - Eventuell: Ressourcenupgrade-Events (z.B., neue IT-Systeme verfügbar)
   - Zeit-limited Events (z.B., erhöhter Angreifungsindex)

7. **Benutzerinteraktion**:
   - Mausklick zum Kaufr und Installieren von Sicherheitsmaßnahmen
   - Klicken auf Cyberangriffe zur Visualisierung der Angriffsversuche

8. **Minimalversion für den Developer Agent**:
   ```html
   <!DOCTYPE html>
   <html lang="de">
   <head>
       <meta charset="UTF-8">
       <title>CampusTech: Cybersecurity Challenge</title>
       <style>
           body { font-family: Arial, sans-serif; }
           .budget { width: 300px; height: 20px; background-color: lightblue; margin-bottom: 10px; }
           .system { width: 50px; height: 50px; border: 1px solid black; display: inline-block; margin-right: 10px; cursor: pointer; }
       </style>
   </head>
   <body>
       <h1>CampusTech: Cybersecurity Challenge</h1>
       <div class="budget" id="budget">Budget: $1000</div>
       <div id="systems">
           <div class="system server"></div>
           <div class="system router"></div>
       </div>
       <script>
           const budget = document.getElementById('budget');
           let currentBudget = 1000;

           function updateBudget(amount) {
               currentBudget += amount;
               budget.textContent = `Budget: $${currentBudget}`;
           }

           document.querySelectorAll('.system').forEach(system => {
               system.addEventListener('click', () => {
                   if (currentBudget >= 100) {
                       updateBudget(-100);
                       alert(`Sicherheitsmaßnahme auf ${system.classList[1]} installiert`);
                   } else {
                       alert("Nicht genügend Budget");
                   }
               });
           });
       </script>
   </body>
   </html>
   ```

9. **Nice-to-have-Erweiterungen**:
   - Multiplayer-Version mit Teams-Wettbewerbe
   - Schwierigkeitsgradsteuerung durch verschiedene IT-Systeme
   - Anpassbare Budgetgrenzen je nach Institutionstyp
   - Leaderboard zum Vergleichen von Teamleistungen