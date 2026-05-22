\# AI Alert Risk Classification Pipeline



\## Overview



This directory contains the AI pipeline used to classify Wazuh security alerts by risk level.



The pipeline extracts Wazuh alerts, normalizes the alert fields, builds machine learning features, labels the dataset, trains a Random Forest model, and generates AI-based risk alerts.



\## Pipeline Files



| File | Purpose |

|---|---|

| extract\_alerts.py | Extracts relevant Wazuh alerts from alerts.json |

| normalize\_alerts.py | Normalizes alert fields into a consistent JSONL format |

| build\_features.py | Builds machine learning features from normalized alerts |

| label\_dataset.py | Assigns risk labels based on rule IDs |

| train\_model.py | Trains a Random Forest classifier |

| predict\_ai.py | Predicts alert risk and writes AI alert output |

| requirements.txt | Python dependencies |



\## Pipeline Flow



Wazuh alerts.json

\-> extract\_alerts.py

\-> raw\_alerts.jsonl

\-> normalize\_alerts.py

\-> normalized\_alerts.jsonl

\-> build\_features.py

\-> features.csv

\-> label\_dataset.py

\-> training\_dataset.csv

\-> train\_model.py

\-> rf\_model.joblib

\-> predict\_ai.py

\-> ai\_alerts.jsonl



\## Input and Output Paths



The lab uses the following default paths:



| Path | Purpose |

|---|---|

| /var/ossec/logs/alerts/alerts.json | Wazuh alert source |

| /opt/ai-sec/data/raw\_alerts.jsonl | Extracted raw alerts |

| /opt/ai-sec/data/normalized\_alerts.jsonl | Normalized alerts |

| /opt/ai-sec/data/features.csv | Feature dataset |

| /opt/ai-sec/data/training\_dataset.csv | Labeled training dataset |

| /opt/ai-sec/models/rf\_model.joblib | Trained Random Forest model |

| /opt/ai-sec/output/ai\_alerts.jsonl | AI-generated risk alerts |



\## Risk Labels



The model classifies alerts into the following risk levels:



| Risk Level | Meaning |

|---|---|

| medium | Suspicious or early-stage activity |

| high | High-risk attack behavior |

| critical | Critical activity such as malware, sensitive file change, or severe alert |



\## Feature Engineering



The feature extraction step creates indicators such as:



\- Login failure

\- Brute-force behavior

\- Web attack behavior

\- SQL Injection indicator

\- XSS indicator

\- Path Traversal / LFI indicator

\- Command execution

\- Malware command behavior

\- File download behavior

\- Sensitive sudo usage

\- Web probing

\- File modification

\- Same source IP event count

\- Distinct modules associated with the same IP



\## Model



The training script uses a Random Forest classifier with categorical encoding and balanced class weights.



\## How to Run



Install dependencies:



pip install -r requirements.txt



Run the pipeline:



python3 extract\_alerts.py

python3 normalize\_alerts.py

python3 build\_features.py

python3 label\_dataset.py

python3 train\_model.py

python3 predict\_ai.py



\## Wazuh Integration



The output file `ai\_alerts.jsonl` can be monitored by Wazuh Agent or Wazuh Manager. Custom Wazuh rules can then generate alerts based on predicted risk levels.



\## Security Notes



\- Do not upload real alert datasets containing sensitive information.

\- Do not upload trained models if they were trained on sensitive production data.

\- Redact IP addresses, usernames, passwords, hostnames, and payloads before publishing sample data.

\- This AI pipeline is intended for lab and educational use.

