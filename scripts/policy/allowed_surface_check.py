#!/usr/bin/env python3
import argparse, json, subprocess, sys, re, pathlib

def load_allowed_surface(plan_path: str, capsule: str):
    surfaces = []
    with open(plan_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
            except Exception:
                continue
            cid = obj.get("id") or obj.get("kap_id")
            if cid == capsule:
                surfaces = obj.get("allowed_surface", [])
                break
    if not surfaces:
        print(f"[ERROR] Capsule {capsule} not found or has no allowed_surface in {plan_path}", file=sys.stderr)
        sys.exit(2)
    return surfaces

def git_changed_files(base: str, head: str):
    cmd = ["git", "diff", "--name-only", f"{base}...{head}"]
    out = subprocess.check_output(cmd, encoding="utf-8")
    return [ln.strip() for ln in out.splitlines() if ln.strip()]

def path_matches(path: str, pattern: str):
    # very small glob: ** = any subpath, * = any segment
    # normalize
    p = pathlib.PurePosixPath(path)
    pat = pattern.replace("\\", "/")
    # Quick accepts for exact file
    if pat == path:
        return True
    # Convert to regex
    pat = re.escape(pat)
    pat = pat.replace(r"\\*\\*", r".*").replace(r"\\*", r"[^/]*")
    return re.fullmatch(pat, str(p)) is not None

def is_allowed(path: str, surfaces):
    for pat in surfaces:
        if path_matches(path, pat):
            return True
    return False

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--capsule", required=True)
    ap.add_argument("--plan", required=True)
    ap.add_argument("--base", required=True)
    ap.add_argument("--head", required=True)
    args = ap.parse_args()

    allowed = load_allowed_surface(args.plan, args.capsule)
    changed = git_changed_files(args.base, args.head)

    violations = [p for p in changed if not is_allowed(p, allowed)]
    if violations:
        print("❌ Allowed Surface violations for", args.capsule)
        print("Allowed patterns:", allowed)
        print("Violating files:")
        for v in violations:
            print(" -", v)
        sys.exit(1)
    else:
        print("✅ Allowed Surface OK for", args.capsule)
        sys.exit(0)

if __name__ == "__main__":
    main()
