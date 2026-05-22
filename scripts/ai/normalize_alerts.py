#2
#!/usr/bin/env python3
import json
from pathlib import Path

SRC = Path("/opt/ai-sec/data/raw_alerts.jsonl")
OUT = Path("/opt/ai-sec/data/normalized_alerts.jsonl")

def guess_module(obj):
    rule_desc = str(obj.get("rule", {}).get("description", "")).lower()
    agent_name = str(obj.get("agent", {}).get("name", "")).lower()
    location = str(obj.get("location", "")).lower()
    decoder_name = str(obj.get("decoder", {}).get("name", "")).lower()

    full = " ".join([rule_desc, agent_name, location, decoder_name])

    # Ưu tiên rule server-real trước để tránh bị text khác làm nhiễu
    if "server-real" in rule_desc or "nginx" in rule_desc or "syscheck" in rule_desc:
        return "server"
    if "cowrie" in full:
        return "cowrie"
    if "heralding" in full:
        return "heralding"
    if "tanner" in full or "snare" in full:
        return "tanner"
    if "suricata" in full:
        return "suricata"
    return "unknown"

def get_src_ip(obj):
    candidates = [
        obj.get("data", {}).get("src_ip"),
        obj.get("srcip"),
        obj.get("src_ip"),
        obj.get("peer", {}).get("ip"),
        obj.get("source_ip"),
    ]
    for x in candidates:
        if x:
            return str(x)
    return ""

def get_dest_port(obj):
    candidates = [
        obj.get("data", {}).get("dest_port"),
        obj.get("dstport"),
        obj.get("dest_port"),
        obj.get("destination_port"),
    ]
    for x in candidates:
        if x not in (None, ""):
            try:
                return int(x)
            except Exception:
                return 0
    return 0

def get_protocol(obj):
    candidates = [
        obj.get("data", {}).get("proto"),
        obj.get("protocol"),
        obj.get("network", {}).get("protocol"),
    ]
    for x in candidates:
        if x:
            return str(x).lower()
    return ""

def get_raw_message(obj):
    if obj.get("full_log"):
        return str(obj.get("full_log"))
    if obj.get("data", {}).get("command"):
        return str(obj.get("data", {}).get("command"))
    return json.dumps(obj, ensure_ascii=False)

def main():
    count = 0
    OUT.parent.mkdir(parents=True, exist_ok=True)

    with SRC.open("r", encoding="utf-8", errors="ignore") as fin, \
         OUT.open("w", encoding="utf-8") as fout:
        for line in fin:
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
            except json.JSONDecodeError:
                continue

            norm = {
                "timestamp": obj.get("@timestamp") or obj.get("timestamp") or "",
                "src_ip": get_src_ip(obj),
                "dest_port": get_dest_port(obj),
                "protocol": get_protocol(obj),
                "module": guess_module(obj),
                "rule_id": str(obj.get("rule", {}).get("id", "")),
                "rule_level": int(obj.get("rule", {}).get("level", 0) or 0),
                "description": str(obj.get("rule", {}).get("description", "")),
                "raw_message": get_raw_message(obj),
            }

            fout.write(json.dumps(norm, ensure_ascii=False) + "\n")
            count += 1

    print(f"[OK] normalized={count}, output={OUT}")

if __name__ == "__main__":
    main()
