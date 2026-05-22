#!/usr/bin/env python3
import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
import joblib

SRC = Path("/opt/ai-sec/data/training_dataset.csv")
MODEL_OUT = Path("/opt/ai-sec/models/rf_model.joblib")

def main():
    df = pd.read_csv(SRC)
    if df.empty:
        raise RuntimeError("training_dataset.csv is empty")

    drop_cols = ["label", "description", "src_ip"]
    X = df.drop(columns=drop_cols, errors="ignore")
    y = df["label"]

    cat_cols = [c for c in X.columns if X[c].dtype == "object"]
    num_cols = [c for c in X.columns if c not in cat_cols]

    preprocessor = ColumnTransformer(
        transformers=[
            ("cat", OneHotEncoder(handle_unknown="ignore"), cat_cols),
            ("num", "passthrough", num_cols),
        ]
    )

    model = RandomForestClassifier(
        n_estimators=200,
        random_state=42,
        class_weight="balanced"
    )

    clf = Pipeline(steps=[
        ("preprocessor", preprocessor),
        ("model", model)
    ])

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)

    print("[METRIC] accuracy =", accuracy_score(y_test, y_pred))
    print("\n[REPORT]")
    print(classification_report(y_test, y_pred))
    print("[CONFUSION MATRIX]")
    print(confusion_matrix(y_test, y_pred))

    MODEL_OUT.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(clf, MODEL_OUT)
    print(f"[OK] model saved to {MODEL_OUT}")

if __name__ == "__main__":
    main()
