# **Game Design: CampusDigital**

## 1. Spielziel  
Der Spieler übernimmt die Rolle eines IT-Administrators und muss innerhalb von **3 Minuten** so viele **Bürokratieprozesse wie möglich digitalisieren**, um Studierende und Mitarbeiter effizienter zu unterstützen. Ziel ist es, ein bestimmtes **Punkteziel** zu erreichen – bei Erfolg gewinnt man, bei Misserfolg verliert man.

---

## 2. Bildschirmaufbau  
**Bildschirmgröße:** Vollbild oder responsive Fenster (Desktop & Mobile)  
**Layout:**

- **Oben:** Timer (3:00), Punkte-Anzeige, Level/Status  
- **Mitte:** Liste der Prozesse mit Checkbox (auswählbar)  
- **Unten:** „Digitalisieren“-Button, Feedback-Bereich  

---

## 3. Spielobjekte  
- **Prozesskarte:**  
  - Name (z. B. „Prüfungsanmeldung“)  
  - Digitalisierungsgrad (0–100%)  
  - Zeit-/Ressourcen-Kosten (z. B. 2 Min, 1 Punkt)  
  - Checkbox zum Auswählen  

- **Timer:**  
  - Countdown von 3:00 Minuten  

- **Punkteanzeige:**  
  - Aktuelle Punkte und Ziel  

- **Feedback-Balken:**  
  - Visualisierung der Effizienz (z. B. Zeitersparnis für Studierende)  

---

## 4. Regeln  
- Spieler wählt Prozesse aus, die er digitalisieren möchte (Checkbox).  
- Jeder Prozess hat eine **Zeit-/Ressourcenkosten** und einen **Punktegewinn**.  
- Die **Zeit läuft immer**, Prozesse müssen schnell ausgewählt werden.  
- Wenn **Timer abläuft** oder **Punkteziel nicht erreicht** wird → **Verlust**.  
- Spieler kann **nur so viele Prozesse auswählen, wie er Zeit hat**.  

---

## 5. Punkte-System  
- **Pro Prozess:**  
  - Punkte = Digitalisierungsgrad × Effizienz-Faktor (1–3)  
- **Bonuspunkte:**  
  - Vollständige Digitalisierung eines Prozesses → +5 Punkte  
  - Zeitbonus: Je weniger Zeit, desto mehr Punkte  
- **Ziel:** Mindestens **20 Punkte** innerhalb von 3 Minuten  

---

## 6. Ereignisse im Spiel  
- **Timer läuft runter** (rot wird, wenn < 30 Sekunden)  
- **Prozess ausgewählt → Checkbox aktiviert**  
- **Digitalisierung startet → Animation oder Balken füllt sich**  
- **Punkte werden aktualisiert**  
- **Nach Spielende:** Erfolg/Verlustmeldung, Score und Option zum Neustart  

---

## 7. Benutzerinteraktion  
- **Maus:** Klick auf Checkbox → Prozess auswählen  
- **Tastatur:**  
  - `Enter` = Digitalisieren bestätigen  
  - `Space` = Neustart  
- **Buttons:**  
  - „Digitalisieren“ Button → Startet die Aktion  
  - „Neustart“ Button → Spiel zurücksetzen  

---

## 8. Minimalversion für den Developer Agent  
**index.html mit:**

```html
<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>CampusDigital</title>
  <style>
    body { font-family: Arial; padding: 20px; }
    #timer { font-size: 2em; color: red; }
    .process { margin: 10px 0; }
    button { margin-top: 20px; padding: 10px; }
  </style>
</head>
<body>
  <h1>CampusDigital</h1>
  <div id="timer">3:00</div>
  <div id="points">Punkte: 0</div>
  <div id="processes"></div>
  <button onclick="startProcess()">Digitalisieren</button>
  <button onclick="resetGame()">Neustart</button>

  <script>
    const processes = [
      { name: "Prüfungsanmeldung", cost: 2, points: 10 },
      { name: "Ressourcenanfrage", cost: 3, points: 15 },
      { name: "Anmeldung Studiengang", cost: 4, points: 20 }
    ];
    let selected = [];
    let points = 0;
    let timeLeft = 180; // 3 Minuten in Sekunden
    let timer;

    function initGame() {
      const processList = document.getElementById("processes");
      processes.forEach((p, i) => {
        const div = document.createElement("div");
        div.className = "process";
        div.innerHTML = `
          <input type="checkbox" id="proc-${i}" />
          <label for="proc-${i}">${p.name}</label> (${p.cost} Min, ${p.points} Punkte)
        `;
        processList.appendChild(div);
      });
      updateTimer();
    }

    function updateTimer() {
      const minutes = Math.floor(timeLeft / 60);
      const seconds = timeLeft % 60;
      document.getElementById("timer").innerText = `${minutes}:${seconds < 10 ? '0' : ''}${seconds}`;
      if (timeLeft <= 0) endGame(false);
    }

    function startTimer() {
      timer = setInterval(() => {
        timeLeft--;
        updateTimer();
        if (timeLeft <= 0) clearInterval(timer);
      }, 1000);
    }

    function startProcess() {
      const checkboxes = document.querySelectorAll('input[type="checkbox"]:checked');
      checkboxes.forEach(cb => {
        const index = parseInt(cb.id.split('-')[2]);
        points += processes[index].points;
        document.getElementById("points").innerText = `Punkte: ${points}`;
        cb.checked = false;
      });
    }

    function endGame(success) {
      clearInterval(timer);
      alert(`Spiel beendet. ${success ? 'Gewonnen!' : 'Verloren.'} Punkte: ${points}`);
    }

    function resetGame() {
      points = 0;
      timeLeft = 180;
      document.getElementById("points").innerText = "Punkte: 0";
      startTimer();
      initGame();
    }

    window.onload = () => {
      initGame();
      startTimer();
    };
  </script>
</body>
</html>
```

---

## 9. Nice-to-have-Erweiterungen  
1. **Level-System:**  
   - Einfach → Mittel → Schwer (komplexere Prozesse)  

2. **Multiplayer-Modus:**  
   - Mehrere Spieler gleichzeitig digitalisieren → gemeinsames Punkteziel  

3. **Feedback-System:**  
   - Visualisierung der Zeitersparnis (z. B. Balken für Studierende)  

4. **Soundeffekte:**  
   - Timer-Ton, Bestätigungsgeräusch bei Digitalisierung  

5. **Animationen:**  
   - Prozess wird „digitalisiert“ → einfache Animation oder Farbwechsel  

--- 

**Zusammenfassung:**  
CampusDigital ist ein **kurzes, interaktives Browser-Spiel**, das in **3 Minuten** strategisch und schnell entscheidend ist. Es zeigt die **Wichtigkeit digitaler Prozesse in Hochschulen** – ideal für CIOs im Workshop "Hands-on agentic AI".