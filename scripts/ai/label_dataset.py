#!/usr/bin/env python3
import pandas as pd
from pathlib import Path

SRC = Path("/opt/ai-sec/data/features.csv")
OUT = Path("/opt/ai-sec/data/training_dataset.csv")

MEDIUM_IDS = {
    "100102", "100110", "100111", "100122",
    "100500", "100501", "100502", "100510"
}

HIGH_IDS = {
    "100123", "100130", "100131", "100132",
    "100140", "100141", "100142", "100143", "100144",
    "100149", "100150",
    "100200", "100201",
    "100210",
    "100220", "100221",
    "100503", "100504", "100511"
}

CRITICAL_IDS = {
    "100151", "100152", "100153",
    "100211",
    "100230", "100231", "100240", "100241",
    "100505", "100512"
}

VALID_IDS = MEDIUM_IDS | HIGH_IDS | CRITICAL_IDS

def assign_label(rule_id):
    rid = str(rule_id)
    if rid in CRITICAL_IDS:
        return "critical"
    if rid in HIGH_IDS:
        return "high"
    if rid in MEDIUM_IDS:
        return "medium"
    return None

def main():
    df = pd.read_csv(SRC)
    if df.empty:
        print("[WARN] features.csv is empty")
        df.to_csv(OUT, index=False)
        return

    df["rule_id"] = df["rule_id"].astype(str)

    # Chỉ giữ rule liên quan trực tiếp đến đề tài
    df = df[df["rule_id"].isin(VALID_IDS)].copy()

    df["label"] = df["rule_id"].apply(assign_label)
    df = df.dropna(subset=["label"])

    df.to_csv(OUT, index=False)

    print(f"[OK] labeled dataset written to {OUT}")
    print(df["label"].value_counts())
    print("\n[INFO] rule_id used:")
    print(df["rule_id"].value_counts().sort_index())

if __name__ == "__main__":
    main()
