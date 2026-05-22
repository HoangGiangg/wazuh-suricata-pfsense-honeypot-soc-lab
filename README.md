\# Wazuh Suricata pfSense Honeypot SOC Lab



\## Overview



This project documents a proactive SOC lab using Wazuh SIEM, Suricata IDS/IPS, pfSense firewall, and multiple Honeypot services.



The lab was built to detect, monitor, analyze, and respond to common attack scenarios in an isolated environment.



\## Main Components



| Component | Role |

|---|---|

| Kali Linux | Attacker machine |

| pfSense | Firewall, NAT, traffic routing, redirection |

| Suricata | IDS/IPS network monitoring |

| Wazuh | SIEM, log collection, alerting, dashboard |

| Cowrie | SSH Honeypot |

| Heralding | FTP, SMTP, POP3, IMAP Honeypot |

| Snare/Tanner | Web Honeypot |

| Server-real | Protected real server |

| Mail/FTP Server | Service simulation and attack testing |



\## Detection Use Cases



\- Port scanning detection

\- SSH brute-force detection

\- FTP brute-force detection

\- Mail service attack detection

\- SQL Injection detection

\- XSS detection

\- Path Traversal detection

\- Command execution detection

\- Suspicious file download detection

\- Unauthorized file modification detection

\- AI-based alert risk classification



\## Active Response



The lab implements automated response mechanisms:



\- Redirect suspicious attackers to Honeypot

\- Block malicious IPs from accessing the real server

\- Send email alerts for high-risk incidents



\## Repository Structure



\- `architecture/`: Network topology and data flow diagrams

\- `setup/`: Step-by-step setup documentation

\- `rules/`: Wazuh and Suricata detection rules

\- `configs/`: Redacted configuration examples

\- `scripts/`: Active response and AI scripts

\- `detections/`: Detection engineering writeups

\- `reports/`: SOC incident report examples

\- `evidence/`: Screenshots and lab evidence



\## Disclaimer



This project was built in an isolated lab environment for educational and defensive cybersecurity purposes only. No real third-party systems were targeted.

