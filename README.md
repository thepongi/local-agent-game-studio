# Local Agent Game Studio
**Hands-on Agentic AI Workshop im Rahmen des 11. Hochschul-CIO-Kongresses 2026 in Göttingen**</br>
Lokale, gekapselte KI-Agenten entwickeln gemeinsam ein kleines Browser-Spiel.</br>
Anhand des basalen Ansatzes soll examplarisch gezeigt werden, wie mehrere spezialisierte Agenten zusammenarbeiten. Das Ziel ist nicht, ein perfektes Spiel erstellen zu lassen, sondern zu verstehen, wie agentische KI-Systeme strukturiert werden können. Dazu gehören eine klare Rollen Verteilung, begrenzte Zuständigkeiten, überprüfbare Zwischenergebnisse, Governance und Auditierbarkeit. Wünschenswert können auch eine lokale Ausführung und menschliche Freigabepunkte sein.

Beispiele für mögliche Agenten:
- Product Owner Agent erstellt eine Spiel-Spezifikation
- Game Designer Agent erstellt darauf aufbauend ein Game Design
- Developer Agent erzeugt eine spielbare index.html
- Tester Agent prüft das Ergebnis
- Developer Revision Agent verbessert das Spiel
- Governance Agent bewertet den Agentenprozess

Alle Schritte sollen auch lokal auf dem eigenen Rechner mit Ollama und Python ausführbar sein.

## Notwendige Software:
- Python Version 3.14.x (https://www.python.org/downloads/)
- Ollama (https://ollama.com/download)
- optional: Git https://git-scm.com/install/windows, Editor z.B. https://github.com/vscodium/vscodium/releases

## Erste Schritte:
- Sprachmodell(e) installieren, zum Beispiel: ollama pull codellama:7b 
- Installierte Sprachmodelle prüfen: ollama list

## Aufruf in Shell
- Anzeige der Agenten: python orchestrator.py
- Ausführen des Product Owner Agenten: python orchestrator.py product -> es sollte \local-agent-game-studio-main\workspace\spec.md erstellt werden; Dauer je nach GPU/CPU Leistung von wenigen Sekunden bis einigen Minuten.

## Agenten starten
Im Projektordner: python orchestrator.py
Nun werden die verfügbaren Optionen angezeigt.

Einzelne Agenten können auch direkt gestartet werden:
- python orchestrator.py product
- python orchestrator.py design
- python orchestrator.py develop
- python orchestrator.py test
- python orchestrator.py revise
- python orchestrator.py governance

**Alle Agenten nacheinander starten: python orchestrator.py all**
Dauer je nach GPU/CPU Leistung von wenigen Sekunden bis einigen/vielen Minuten.

## Ergebnis prüfen
Das Spiel wird unter ./workspace/index.html erzeugt und sollte direkt mit dem Browser aufgerufen werden können.

## Wichtige Dateien
orchestrator.py                  Hauptskript für die Agenten </br>
workspace/spec.md                Spezifikation des Product Owner Agent</br>
workspace/design.md              Game Design</br>
workspace/index.html             erzeugtes Browser-Spiel</br>
workspace/test-report.md         Test-Report</br>
workspace/governance-review.md   Rückmeldung vom Governance Agenten</br>
audit/runs.jsonl                 Audit-Ergebnisse</br>
