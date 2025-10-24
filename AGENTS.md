# AGENTS – Role Summary (v3.2)

**Planner** → reads `workspace_spec.yaml`, `PLAN.txt`, `feature_plan.jsonl`; selects target capsule.  
**Builder** → creates artifacts inside Allowed Surface only.  
**Governance** → stops before writing on violations; writes `CHECKPOINT.json`.  
**Reviewer** → verifies PATH/diff format and rationale ≤ 6.  
**Reporter** → updates `progress.md`, `status.md`, `REPORT.md`.

> **Context Rule:** Usually these files are sufficient: `docs/governance_master.md`, `AGENTS.md`, `workspace_spec.yaml`, `docs/plan/PLAN.txt`, `docs/plan/feature_plan.jsonl`.  
> **Language Rule:** All agents produce English (en-US) output – files, rationale, commits and PR texts.  
