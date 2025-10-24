🧠 Codex Template Repository

Stand: 2025-10-23
Version: 2.0

Dieses Repository dient als Governance-gestütztes Template für KI-entwickelte Softwareprojekte mit GPT-5-Codex.
Es enthält alle Dateien, die für automatisches Scaffolding, Governance-Checks, CI-Validierung und Deployment benötigt werden.


---

🚀 Zweck

Ziel ist es, neue Projekte deterministisch und prüfbar aufzubauen.
Codex erzeugt und validiert Code, Dokumentation und Deploy-Artefakte nach festen Regeln, definiert in workspace_spec.yaml.

Leitprinzipien

Single-Stack-Policy (z. B. Spring + React)

Allowed-Surface-Prüfungen auf PR-Ebene

Vollständige ENV↔YAML-Spiegelung

Kein manuelles Nachbearbeiten von generierten Dateien



---

🧩 Projektstruktur

Root

.env.sample / application.yml.example – Environment-Spiegel

Railway.toml / railway.yml – Deployment-Konfiguration

.github/ – CI-Workflows & PR-Checklisten

docs/ – Governance-, Planungs- und Status-Dateien

scripts/policy/ – Python-Validierungstools

workspace_spec.yaml – zentrale Projektdefinition



---

⚙️ Vorgehen

1️⃣ Neues Projekt starten

1. Repository als Template verwenden („Use this template“).


2. Datei workspace_spec.yaml ausfüllen (Name, Beschreibung, Domain etc.).


3. Committen.



2️⃣ Initial-Lauf starten

Starte Codex im Setup-Modus mit folgendem Prompt:

> Execute the file prompts/start_continue_workspace_setup.prompt in the repository 
Finish as much as possible in one session. Dont create and Productive files, Not Frontend Not backend, Just the planning files under the generate Section.
When your done, dont do anything and Report Back with "Done" or any other in the repository mentioned word/sentence.


3️⃣ Planung & Umsetzung

Nach erfolgreichem Setup:

docs/plan/PLAN.txt und feature_plan.jsonl enthalten alle Kapseln.

PR-Titel müssen KAP-XXX: enthalten.

Jede Kapsel darf nur Dateien ändern, die in allowed_surface angegeben sind.


4️⃣ Governance & CI

allowed_surface.yml prüft Änderungen automatisch bei jedem Pull Request.

scripts/policy/allowed_surface_check.py vergleicht Diff ↔ Feature-Plan.

.github/pull_request_template.md enthält die DoD-Checkliste.

.env.sample und application.yml.example werden regelmäßig auf Konsistenz geprüft.


5️⃣ Deployment

Standard-Ziel ist Railway.
Nach erfolgreichem Build kann direkt deployt werden:

railway up
railway logs


---

📂 Ordner /prompts/ – Prompt-Vorlagen

Diese Prompt-Dateien steuern die automatisierten Codex-Läufe:

Datei	Zweck

start_continue_workspace_setup.prompt	Baut den Workspace auf und setzt fort, bis alle generierten Dateien existieren
auto_task_planning.prompt	Erstellt und aktualisiert PLAN/feature_plan/tasks idempotent
execute_continue_tasks.prompt	Führt Kapseln sequenziell aus, stoppt bei Governance-Verstößen


Hinweise

Lädt nur die Dateien workspace_spec.yaml, docs/governance_master.md, AGENTS.md, docs/plan/PLAN.txt, docs/plan/feature_plan.jsonl.

Schreibt niemals außerhalb der Allowed Surface des aktiven Kapsels.

Wenn das Tokenlimit erreicht ist, schreibt Codex automatisch docs/plan/CHECKPOINT.json und setzt mit demselben Prompt fort.



---

☁️ Governance-Richtlinien

Die vollständigen Regeln findest du in:

docs/governance_master.md (Kanonische Governance-Datei)

docs/codex_lite.md (Kurzfassung für Codex-Läufe)

AGENTS.md (Agentenrollen & Zuständigkeiten)



---

📜 Lizenz

MIT License – 2025 Coder-Viking

Möchtest du sie zusätzlich als echte Download-Datei (README_TemplateRepo.md)? Dann kann ich sie dir direkt als Link ausgeben.
