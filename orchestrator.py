import sys
import json
import urllib.request
from pathlib import Path
from datetime import datetime

MODEL = "qwen2.5-coder:7b"
OLLAMA_URL = "http://localhost:11434/api/generate"

BASE = Path(__file__).parent
WORKSPACE = BASE / "workspace"
AUDIT = BASE / "audit"

WORKSPACE.mkdir(exist_ok=True)
AUDIT.mkdir(exist_ok=True)


def call_ollama(prompt: str) -> str:
    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False,
    }

    data = json.dumps(payload).encode("utf-8")

    request = urllib.request.Request(
        OLLAMA_URL,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    with urllib.request.urlopen(request) as response:
        result = json.loads(response.read().decode("utf-8"))

    return result["response"]


def log_run(agent_name: str, prompt: str, output: str):
    log_file = AUDIT / "runs.jsonl"
    entry = {
        "time": datetime.now().isoformat(),
        "agent": agent_name,
        "model": MODEL,
        "prompt": prompt,
        "output": output,
    }

    with log_file.open("a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")


def run_product_owner_agent():
    agent_name = "Product Owner Agent"

    prompt = """
Du bist der Product Owner Agent in einem lokalen Agenten-Workshop.

Aufgabe:
Erstelle eine kurze Spezifikation für ein kleines Browser-Spiel für CIOs von Hochschulen.

Rahmen:
- Das Spiel soll in einer einzigen index.html-Datei laufen.
- Keine externen Libraries.
- Thema: Hochschul-IT, Cybersecurity, Campus-Systeme oder IT-Service.
- Das Ergebnis soll in 3 Minuten erklärbar sein.
- Die Spezifikation soll für einen Developer Agent verständlich sein.

Gib aus:
1. Spieltitel
2. Kurzidee
3. Zielgruppe
4. Spielmechanik
5. Gewinn-/Verlierbedingung
6. Anforderungen an die index.html
7. Drei mögliche Erweiterungen

Schreibe klar und knapp auf Deutsch.
"""

    output = call_ollama(prompt)

    output_file = WORKSPACE / "spec.md"
    output_file.write_text(output, encoding="utf-8")

    log_run(agent_name, prompt, output)

    print("Product Owner Agent fertig.")
    print(f"Geschrieben: {output_file}")


def run_game_designer_agent():
    agent_name = "Game Designer Agent"

    spec_file = WORKSPACE / "spec.md"

    if not spec_file.exists():
        raise FileNotFoundError("workspace/spec.md fehlt. Bitte zuerst den Product Owner Agent ausführen.")

    spec = spec_file.read_text(encoding="utf-8")

    prompt = f"""
Du bist der Game Designer Agent in einem lokalen Agenten-Workshop.

Du bekommst diese Spiel-Spezifikation:

---
{spec}
---

Aufgabe:
Erstelle daraus ein konkretes Game Design für ein sehr kleines Browser-Spiel.

Rahmen:
- Eine einzige index.html-Datei.
- Kein Backend.
- Keine externen Libraries.
- Steuerung mit Maus oder Tastatur.
- Muss in 3 Minuten erklärbar und spielbar sein.
- Zielgruppe: CIOs von Hochschulen im Workshop "Hands-on agentic AI".

Gib aus:
1. Spielziel
2. Bildschirmaufbau
3. Spielobjekte
4. Regeln
5. Punkte-System
6. Ereignisse im Spiel
7. Benutzerinteraktion
8. Minimalversion für den Developer Agent
9. Nice-to-have-Erweiterungen

Schreibe klar, knapp und umsetzbar auf Deutsch.
"""

    output = call_ollama(prompt)

    output_file = WORKSPACE / "design.md"
    output_file.write_text(output, encoding="utf-8")

    log_run(agent_name, prompt, output)

    print("Game Designer Agent fertig.")
    print(f"Geschrieben: {output_file}")

def extract_html(output: str) -> str:
    """
    Falls das Modell Markdown-Codeblöcke zurückgibt, extrahieren wir den HTML-Code.
    """
    text = output.strip()

    if "```html" in text:
        start = text.find("```html") + len("```html")
        end = text.find("```", start)
        return text[start:end].strip()

    if "```" in text:
        start = text.find("```") + len("```")
        end = text.find("```", start)
        return text[start:end].strip()

    if "<!DOCTYPE html" in text:
        start = text.find("<!DOCTYPE html")
        return text[start:].strip()

    if "<html" in text:
        start = text.find("<html")
        return text[start:].strip()

    return text

def run_developer_agent():
    agent_name = "Developer Agent"

    spec_file = WORKSPACE / "spec.md"
    design_file = WORKSPACE / "design.md"

    if not spec_file.exists():
        raise FileNotFoundError("workspace/spec.md fehlt. Bitte zuerst den Product Owner Agent ausführen.")

    if not design_file.exists():
        raise FileNotFoundError("workspace/design.md fehlt. Bitte zuerst den Game Designer Agent ausführen.")

    spec = spec_file.read_text(encoding="utf-8")
    design = design_file.read_text(encoding="utf-8")

    prompt = f"""
Du bist der Developer Agent in einem lokalen Agenten-Workshop.

Du bekommst eine Spezifikation und ein Game Design.

SPEZIFIKATION:
---
{spec}
---

GAME DESIGN:
---
{design}
---

Aufgabe:
Erstelle ein vollständiges kleines Browser-Spiel als eine einzige index.html-Datei.

Strikte Anforderungen:
- Gib NUR den vollständigen HTML-Code aus.
- Keine Markdown-Erklärung.
- Keine Code-Fences.
- Alles muss in einer Datei funktionieren.
- Verwende HTML, CSS und Vanilla JavaScript.
- Keine externen Libraries.
- Kein Backend.
- Kein Internetzugriff.
- Das Spiel muss direkt im Browser laufen.
- Das Spiel soll optisch ordentlich wirken.
- Es soll einen Startbereich, Spielfeld, Punktestand, Timer oder Leben und ein Spielende geben.
- Das Thema soll zu Hochschul-IT, CIOs, Campus-Systemen oder Cybersecurity passen.
- Der Code soll robust und verständlich sein.

Erzeuge jetzt die vollständige index.html.
"""

    output = call_ollama(prompt)
    html = extract_html(output)

    output_file = WORKSPACE / "index.html"
    output_file.write_text(html, encoding="utf-8")

    log_run(agent_name, prompt, output)

    print("Developer Agent fertig.")
    print(f"Geschrieben: {output_file}")


def run_tester_agent():
    agent_name = "Tester Agent"

    html_file = WORKSPACE / "index.html"

    if not html_file.exists():
        raise FileNotFoundError("workspace/index.html fehlt. Bitte zuerst den Developer Agent ausführen.")

    html = html_file.read_text(encoding="utf-8")

    prompt = f"""
Du bist der Tester Agent in einem lokalen Agenten-Workshop.

Du bekommst den vollständigen HTML-Code eines kleinen Browser-Spiels.

HTML-CODE:
---
{html}
---

Aufgabe:
Prüfe das Spiel kritisch.

Bewerte:
1. Läuft der Code grundsätzlich im Browser?
2. Gibt es offensichtliche JavaScript-Fehler?
3. Ist das Spielziel verständlich?
4. Gibt es Start, Spielverlauf und Spielende?
5. Funktioniert die Interaktion?
6. Ist das Thema Hochschul-IT/CIO/Cybersecurity erkennbar?
7. Welche drei konkreten Verbesserungen sollte der Developer Agent umsetzen?

Wichtig:
- Schreibe einen klaren Testbericht auf Deutsch.
- Sei konkret.
- Wenn du Code-Probleme findest, benenne sie möglichst genau.
- Gib am Ende eine Entscheidung: "Freigabe", "Freigabe mit kleinen Änderungen" oder "Keine Freigabe".
"""

    output = call_ollama(prompt)

    output_file = WORKSPACE / "test-report.md"
    output_file.write_text(output, encoding="utf-8")

    log_run(agent_name, prompt, output)

    print("Tester Agent fertig.")
    print(f"Geschrieben: {output_file}")


def run_developer_revision_agent():
    agent_name = "Developer Revision Agent"

    html_file = WORKSPACE / "index.html"
    test_file = WORKSPACE / "test-report.md"

    if not html_file.exists():
        raise FileNotFoundError("workspace/index.html fehlt. Bitte zuerst den Developer Agent ausführen.")

    if not test_file.exists():
        raise FileNotFoundError("workspace/test-report.md fehlt. Bitte zuerst den Tester Agent ausführen.")

    html = html_file.read_text(encoding="utf-8")
    test_report = test_file.read_text(encoding="utf-8")

    prompt = f"""
Du bist der Developer Revision Agent in einem lokalen Agenten-Workshop.

Du bekommst den aktuellen HTML-Code eines Browser-Spiels und den Testbericht des Tester Agents.

AKTUELLER HTML-CODE:
---
{html}
---

TESTBERICHT:
---
{test_report}
---

Aufgabe:
Verbessere die index.html anhand des Testberichts.

Strikte Anforderungen:
- Gib NUR den vollständigen verbesserten HTML-Code aus.
- Keine Markdown-Erklärung.
- Keine Code-Fences.
- Alles muss weiterhin in einer einzigen Datei funktionieren.
- Verwende nur HTML, CSS und Vanilla JavaScript.
- Keine externen Libraries.
- Kein Backend.
- Kein Internetzugriff.
- Behalte das Thema Hochschul-IT/CIO/Cybersecurity bei.
- Verbessere Verständlichkeit, Spielbarkeit und Robustheit.

Erzeuge jetzt die vollständige verbesserte index.html.
"""

    output = call_ollama(prompt)
    html = extract_html(output)

    output_file = WORKSPACE / "index.html"
    output_file.write_text(html, encoding="utf-8")

    log_run(agent_name, prompt, output)

    print("Developer Revision Agent fertig.")
    print(f"Verbessert: {output_file}")



def show_help():
    print("""
Local Agent Game Studio

Verwendung:
  python orchestrator.py product   Erstellt workspace/spec.md
  python orchestrator.py design    Erstellt workspace/design.md
  python orchestrator.py develop   Erstellt workspace/index.html
  python orchestrator.py test      Erstellt workspace/test-report.md
  python orchestrator.py revise    Verbessert workspace/index.html anhand des Testberichts
  python orchestrator.py all       Führt alle Agenten nacheinander aus
""")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        show_help()
        sys.exit(0)

    command = sys.argv[1].lower()

    if command == "product":
        run_product_owner_agent()

    elif command == "design":
        run_game_designer_agent()

    elif command == "develop":
        run_developer_agent()

    elif command == "test":
        run_tester_agent()

    elif command == "revise":
        run_developer_revision_agent()

    elif command == "all":
        run_product_owner_agent()
        run_game_designer_agent()
        run_developer_agent()
        run_tester_agent()
        run_developer_revision_agent()

    else:
        print(f"Unbekannter Befehl: {command}")
        show_help()