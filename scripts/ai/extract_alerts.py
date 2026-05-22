#1
#!/usr/bin/env python3
import json
from pathlib import Path

SRC = Path("/var/ossec/logs/alerts/alerts.json")
OUT = Path("/opt/ai-sec/data/raw_alerts.jsonl")

VALID_PREFIXES = ("100",)  

def get_rule_id(obj):
    try:
        return str(obj.get("rule", {}).get("id", ""))
    except:
        return ""

def is_relevant(obj):
    rule = obj.get("rule", {})
    desc = str(rule.get("description", ""))
    rid = get_rule_id(obj)

    if rid.startswith("1018"):
        return False

    if "AI alert" in desc:
        return False

    if not rid.startswith("100"):
        return False

    return True

def main():
    scanned = 0
    extracted = 0

    OUT.parent.mkdir(parents=True, exist_ok=True)

    with open(SRC, "r", encoding="utf-8") as fin, \
         open(OUT, "w", encoding="utf-8") as fout:

        for line in fin:
            scanned += 1
            line = line.strip()
            if not line:
                continue

            try:
                obj = json.loads(line)
            except:
                continue

            if not is_relevant(obj):
                continue

            fout.write(json.dumps(obj, ensure_ascii=False) + "\n")
            extracted += 1

    print(f"[OK] scanned={scanned}, extracted={extracted}, output={OUT}")

if __name__ == "__main__":
    main()
