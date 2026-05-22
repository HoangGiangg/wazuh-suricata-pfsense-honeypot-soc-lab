\# Local AI Alert Chatbot



\## Overview



This directory contains a local Streamlit chatbot used to assist with AI alert analysis.



The chatbot reads AI-generated alerts from `ai\_alerts.jsonl` and helps the analyst query the latest alerts, risk levels, dangerous source IPs, and module statistics.



\## File



| File | Purpose |

|---|---|

| chatbot\_local.py | Streamlit chatbot for local AI alert analysis |

| requirements.txt | Python dependencies |



\## Data Source



Default AI alert file:



/opt/ai-sec/output/ai\_alerts.jsonl



\## Supported Questions



The chatbot supports questions such as:



\- latest alert

\- latest critical alert

\- latest high alert

\- latest medium alert

\- explain this alert

\- summarize IP activity

\- total alert count

\- critical alert count

\- most dangerous IP

\- top 5 IPs

\- most frequent module

\- risk statistics

\- module statistics



\## How to Run



Install dependencies:



pip install -r requirements.txt



Run the chatbot:



streamlit run chatbot\_local.py



\## Analyst Use Cases



\- Quickly review the latest AI alert.

\- Understand why an alert was classified as medium, high, or critical.

\- Identify the most dangerous source IP.

\- Review risk distribution.

\- Review alert distribution by module.



\## Security Notes



\- The chatbot is designed for local lab use.

\- Do not expose it publicly without authentication.

\- Do not upload real AI alert output containing sensitive data.

\- Redact IP addresses, usernames, hostnames, and payloads before sharing screenshots.

