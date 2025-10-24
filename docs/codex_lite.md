# Codex Lite – 11 Rules (Condensed)

1. Load only: `docs/governance_master.md`, `AGENTS.md`, `workspace_spec.yaml`, `docs/plan/PLAN.txt`, `docs/plan/feature_plan.jsonl`.  
2. Identify target capsule (checkpoint → plan → override).  
3. Write **only** inside Allowed Surface of that capsule.  
4. Idempotent writes only; edits via unified diff.  
5. Respect Output Contract – rationale ≤ 6 lines per block.  
6. No secrets or lockfiles.  
7. Max budget: 700 LOC / 12 files; if exceeded → STOP + checkpoint.  
8. Report after each capsule (progress / status / report).  
9. Optional Self-Eval after batch (10 gates).  
10. On off-surface write → abort and save checkpoint.  
11. **Language:** All outputs must be English (en-US).  
