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


if __name__ == "__main__":
    run_product_owner_agent()