#3
#!/usr/bin/env python3
import json
from pathlib import Path
from collections import Counter
import pandas as pd

SRC = Path("/opt/ai-sec/data/normalized_alerts.jsonl")
OUT = Path("/opt/ai-sec/data/features.csv")

BRUTEFORCE_IDS = {"100123", "100131", "100201"}
WEB_ATTACK_IDS = {"100140", "100141", "100142", "100143", "100144", "100220", "100221"}
MALWARE_IDS = {"100151", "100152", "100153", "100240", "100241", "100512"}
COMMAND_IDS = {"100149", "100150"}
FILE_CHANGE_IDS = {"100230", "100231", "100240", "100241"}
SCAN_IDS = {"100501", "100502", "100510"}
HIGH_SURICATA_IDS = {"100504", "100512"}

def main():
    rows = []
    with SRC.open("r", encoding="utf-8", errors="ignore") as fin:
        for line in fin:
            line = line.strip()
            if not line:
                continue
            rows.append(json.loads(line))

    if not rows:
        print("[WARN] no normalized data")
        pd.DataFrame().to_csv(OUT, index=False)
        return

    ip_counter = Counter(r.get("src_ip", "") for r in rows if r.get("src_ip"))
    module_counter_by_ip = {}
    for r in rows:
        ip = r.get("src_ip", "")
        mod = r.get("module", "")
        if not ip:
            continue
        module_counter_by_ip.setdefault(ip, set()).add(mod)

    feature_rows = []
    for r in rows:
        rid = str(r.get("rule_id", ""))
        ip = r.get("src_ip", "")
        msg = (r.get("raw_message", "") or "").lower()
        desc = (r.get("description", "") or "").lower()

        feature_rows.append({
            "module": r.get("module", ""),
            "rule_id": rid,
            "rule_level": int(r.get("rule_level", 0) or 0),
            "protocol": r.get("protocol", ""),
            "dest_port": int(r.get("dest_port", 0) or 0),

            "is_login_fail": int("login failed" in desc or "authentication failed" in desc),
            "is_bruteforce": int(rid in BRUTEFORCE_IDS),
            "is_web_attack": int(rid in WEB_ATTACK_IDS),
            "is_sqli": int(rid == "100141" or "sql injection" in desc or "sql" in msg),
            "is_xss": int(rid == "100142" or "xss" in desc or "<script>" in msg),
            "is_lfi": int(rid == "100143" or "traversal" in desc or "lfi" in desc or "/etc/passwd" in msg),
            "is_command_exec": int(rid in COMMAND_IDS or rid == "100149"),
            "is_recon_cmd": int(rid == "100150"),
            "is_malware_cmd": int(rid in MALWARE_IDS or rid in HIGH_SURICATA_IDS),
            "is_file_download": int(rid == "100152" or "wget" in msg or "curl " in msg),
            "is_sensitive_sudo": int(rid == "100211"),
            "is_web_probe": int(rid in {"100220", "100221", "100140", "100144"}),
            "is_file_change": int(rid in FILE_CHANGE_IDS),

            "same_ip_count": int(ip_counter.get(ip, 0)),
            "same_ip_distinct_modules": int(len(module_counter_by_ip.get(ip, set()))),

            "description": r.get("description", ""),
            "src_ip": ip,
        })

    df = pd.DataFrame(feature_rows)
    df.to_csv(OUT, index=False)
    print(f"[OK] features={len(df)}, output={OUT}")

if __name__ == "__main__":
    main()
