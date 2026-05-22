#!/usr/bin/env python3
import json
import pandas as pd
import joblib
from pathlib import Path
from datetime import datetime

MODEL = Path("/opt/ai-sec/models/rf_model.joblib")
SRC = Path("/opt/ai-sec/data/features.csv")
OUT = Path("/opt/ai-sec/output/ai_alerts.jsonl")

def clean_value(val):
    if pd.isna(val):
        return ""
    return str(val)

def main():
    clf = joblib.load(MODEL)
    df = pd.read_csv(SRC)
    if df.empty:
        print("[WARN] features.csv is empty")
        return

    X = df.drop(columns=["description", "src_ip"], errors="ignore")
    preds = clf.predict(X)
    probs = clf.predict_proba(X)

    OUT.parent.mkdir(parents=True, exist_ok=True)

    with OUT.open("w", encoding="utf-8") as fout:
        for i, row in df.iterrows():
            item = {
                "timestamp": datetime.now().astimezone().isoformat(),
                "src_ip": clean_value(row.get("src_ip", "")),
                "module": clean_value(row.get("module", "")),
                "original_rule_id": clean_value(row.get("rule_id", "")),
                "original_description": clean_value(row.get("description", "")),
                "predicted_risk": clean_value(preds[i]),
                "confidence": float(probs[i].max()),
                "model": "random_forest_v1"
            }
            fout.write(json.dumps(item, ensure_ascii=False) + "\n")

    print(f"[OK] ai output written to {OUT}")

if __name__ == "__main__":
    main()
