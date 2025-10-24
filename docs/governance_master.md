# Governance Master (CONDENSED v3.1 – English Edition)
# Purpose: A single, compact governance framework for all AI runs (Planning + Execution).
# This file replaces scattered governance fragments.
# Please replace placeholders:
# <PROJECT_NAME>, <PROJECT_CODE>, <REPO_URL>, <STACK>, <DB_KIND>, <DEPLOY_TARGET>

## 1) Core Guardrails (always active)
- **Single-Stack:** exactly one technology stack: <STACK> (no mixed artifacts).
- **Idempotency:** generate only missing files; modify existing ones exclusively via unified diff.
- **Allowed Surface per Capsule:** write only inside paths defined in `docs/plan/feature_plan.jsonl` for the active capsule.
- **Output Contract:** new files must appear as `PATH: <relative>` blocks with full content; edits must appear as unified diffs; each rationale ≤ 6 lines.
- **No secrets** in repository. Do not generate lockfiles or caches (e.g., `package-lock.json`, `.m2/`).  
  Instead, output an instruction like “install locally”.
- **Checkpointing:** upon reaching token/time/resource limits, **STOP** and write `docs/plan/CHECKPOINT.json`.

---

## 2) ENV / YAML / Deploy (mirror rules)
- `.env.sample` must contain **no duplicate keys** and mirror all variables referenced in `application.yml.example`:  
  - `OPENAI_API_KEY`, `OPENAI_MODEL`, `GITHUB_APP_ID`, `GITHUB_APP_PRIVATE_KEY`,  
  - `DATABASE_URL` (format consistent with the chosen stack), `DB_USER`, `DB_PASSWORD`,  
  - `BACKEND_PORT`, `FRONTEND_PORT`.
- **Railway configurations:** exactly one start command per service; backend healthcheck `/actuator/health` (Spring) or equivalent for the stack.
- **README minimum sections:** must include `stack`, `how_to_run`, and `plan_links`.

---

## 3) Capsule Selection & Order
- **Default:** choose the **next open** capsule from `docs/plan/CHECKPOINT.json` → `remaining[0]`.
- **Fallback:** first open capsule in `docs/plan/feature_plan.jsonl` (lowest `KAP-xxx` with no artifacts).
- **Override:** if a specific `KAP-xxx` appears in the prompt or branch name, use that one.

---

## 4) Execution Mode (Two-Pass)
- **Pass A (Skeleton):** minimal compilable structures per capsule (classes / routes / configs).
- **Pass B (Small):** lightweight tests and documentation, only if token / LOC budget remains.
- **Budgets (default):** ≤ 700 LOC, ≤ 12 files, rationale ≤ 6 lines per block.

---

## 5) Reporting (mandatory after each capsule)
- **`docs/progress.md`:** ISO date, capsule ID, short status line.  
- **`docs/status.md`:** two sections – `overview` (percentages 0–100) and `risks` (list); no duplicates.  
- **`docs/plan/REPORT.md`:** must append a section “Executed: KAP-xxx” with artifact list.

---

## 6) Self-Evaluation (optional after a batch)
Generate `docs/plan/SELF_EVAL.md` with the following 10 gates:

1. Single-Stack  
2. Allowed Surface  
3. Idempotency  
4. ENV / YAML mirror consistency  
5. Railway artifacts  
6. README minimum sections  
7. Governance mandatory files  
8. Plan artifacts existence  
9. Output Contract compliance  
10. Template residue check  

Each failed gate must produce a minimal fix (unified diff / PATH block).

---

## 7) Agent Roles (short summary)
- **Planner:** reads Spec / Plan; determines target capsule.  
- **Builder:** writes only within Allowed Surface paths.  
- **Governance:** aborts on off-surface write and creates `CHECKPOINT.json`.  
- **Reviewer:** formats output (PATH / diff).  
- **Reporter:** updates Progress / Status / Report.  

---

## 8) Prompt Snippets (for reuse)
- **“ONE-CAPSULE EXECUTION (STRICT v3.1)”** – executes exactly one capsule (next open), applies budgets and stop conditions.  
- **“RESUME FROM CHECKPOINT”** – continues from `CHECKPOINT.json`.  
Both enforce: no lockfiles, no secrets, deterministic artifacts.
