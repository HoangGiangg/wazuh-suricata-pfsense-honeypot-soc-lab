\# AI Alert Risk Classification



\## Overview



This detection use case uses a Random Forest model to classify Wazuh security alerts into risk levels.



The purpose is to assist SOC analysts by prioritizing alerts based on rule ID, module, protocol, destination port, attack indicators, source IP frequency, and related features.



\## Data Sources



| Source | Purpose |

|---|---|

| Wazuh alerts.json | Original alert source |

| Custom Wazuh rules | Rule IDs used for feature extraction and labeling |

| Honeypot alerts | Cowrie, Heralding, Snare/Tanner activity |

| Suricata alerts | Network IDS events |

| Server-real alerts | Host-based and web events |



\## Pipeline



Wazuh alerts

\-> alert extraction

\-> normalization

\-> feature engineering

\-> labeling

\-> Random Forest training

\-> prediction

\-> AI alert generation



\## Risk Levels



| Risk | Description |

|---|---|

| medium | Initial suspicious activity such as connection, probing, or scan |

| high | Strong attack behavior such as brute-force, web attack, or privilege-related activity |

| critical | Severe activity such as malware behavior, high severity alert, or unauthorized file modification |



\## Detection Logic



The model uses engineered features such as:



\- Rule level

\- Rule ID

\- Module

\- Protocol

\- Destination port

\- Brute-force indicator

\- Web attack indicator

\- SQL Injection indicator

\- XSS indicator

\- Path Traversal indicator

\- Command execution indicator

\- Malware behavior indicator

\- File download indicator

\- File change indicator

\- Source IP frequency

\- Number of distinct modules associated with the same source IP



\## Output



The AI module writes predicted alerts to:



/opt/ai-sec/output/ai\_alerts.jsonl



Each AI alert contains:



\- timestamp

\- source IP

\- module

\- original rule ID

\- original description

\- predicted risk

\- confidence

\- model name



\## SOC Questions



\- What is the predicted risk level?

\- What original rule generated the event?

\- What source IP triggered the alert?

\- What module produced the original event?

\- How confident is the model?

\- Should the analyst investigate or block the source IP?



\## Evidence



Recommended screenshots should be placed in:



evidence/wazuh-dashboard/



or:



evidence/attack-simulation/



Recommended evidence:



\- Feature CSV generation

\- Training result

\- Model accuracy/report

\- AI alert output

\- AI alert shown in Wazuh

\- Chatbot explanation of latest alert



\## Security Notes



\- This model is for lab use and educational purposes.

\- The model should not be used as the only decision source for blocking.

\- Human analyst review is still required.

\- Training data should be reviewed and redacted before publishing.

