# Local Agent Game Studio
**Hands-on agentic AI Workshop im Rahmen des 11. Hochschu-CIO-Kongresses 2026 in Göttingen**
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
- Python (https://www.python.org/downloads/)
- Ollama (https://ollama.com/download)


## Erste Schritte:
- Sprachmodell(e) installieren, zum Beispiel: ollama pull codellama:7b 
- Installierte Sprachmodelle prüfen: ollama list

## Aufruf in Shell
- Anzeige der Agenten: python orchestrator.py
- Ausführen des Product Owner Agenten: python orchestrator.py product -> es sollte \local-agent-game-studio-main\workspace\spec.md erstellt werden; Dauer je nach GPU/CPU Leistung von wenigen Sekunden bis einigen Minuten.
- 
