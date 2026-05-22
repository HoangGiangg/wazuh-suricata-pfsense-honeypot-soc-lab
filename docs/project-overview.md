\# Project Overview



\## Project Name



Wazuh Suricata pfSense Honeypot SOC Lab



\## Description



This project demonstrates a proactive cybersecurity monitoring lab that combines SIEM, IDS/IPS, firewall, honeypot, and automated response mechanisms.



The system is designed to detect, monitor, analyze, and respond to common attack behaviors in an isolated lab environment.



\## Main Objectives



\- Build a multi-layer security monitoring lab.

\- Deploy pfSense as the firewall and network gateway.

\- Use Suricata as the IDS/IPS engine for network-based detection.

\- Use Wazuh as the central SIEM platform for log collection, alerting, and dashboard visualization.

\- Deploy multiple Honeypot services to collect attacker behavior.

\- Simulate common attacks such as port scanning, SSH brute-force, FTP brute-force, web attacks, suspicious file download, and unauthorized file modification.

\- Implement automated response mechanisms such as redirecting suspicious attackers to Honeypot and blocking malicious IP addresses.

\- Map detection scenarios to MITRE ATT\&CK techniques.



\## Key Components



| Component | Role |

|---|---|

| Kali Linux | Attacker machine |

| pfSense | Firewall, NAT, routing, traffic redirection |

| Suricata | IDS/IPS network monitoring |

| Wazuh | SIEM, log collection, alerting, dashboard |

| Cowrie | SSH Honeypot |

| Heralding | FTP, SMTP, POP3, IMAP Honeypot |

| Snare/Tanner | Web Honeypot |

| Server-real | Protected real server |

| Mail/FTP Server | Service simulation and attack testing |

| Suricata Collector | Collects Suricata logs and forwards them to Wazuh |



\## Detection Scenarios



\- Port scanning detection

\- SSH brute-force detection

\- FTP brute-force detection

\- Mail service attack detection

\- Web attack detection: SQL Injection, XSS, Path Traversal

\- Suspicious command execution

\- Suspicious file download

\- File integrity monitoring

\- AI-based alert risk classification



\## Active Response



The system includes automated response workflows:



\- Redirect suspicious attackers to Honeypot

\- Block malicious IPs from accessing the real server

\- Send email alerts for high-risk events



\## Disclaimer



This lab was built in an isolated environment for educational and defensive cybersecurity purposes only. No real third-party systems were targeted.

