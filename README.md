# Wazuh Suricata pfSense Honeypot SOC Lab

## Overview

This project documents a proactive SOC monitoring lab using Wazuh SIEM, Suricata IDS/IPS, pfSense firewall, and multiple Honeypot services.

The lab was built to detect, monitor, analyze, and respond to common attack scenarios in an isolated environment.

## Architecture

The lab combines firewall, IDS/IPS, SIEM, deception technology, host monitoring, active response, and AI-based alert prioritization.

| Component | Role |
|---|---|
| Kali Linux | Attacker machine |
| pfSense | Firewall, NAT, traffic routing, redirection, blocking |
| Suricata | IDS/IPS network monitoring |
| Wazuh | SIEM, log collection, alerting, dashboard |
| Cowrie | SSH Honeypot |
| Heralding | FTP, SMTP, POP3, IMAP Honeypot |
| Snare/Tanner | Web Honeypot |
| Server-real | Protected real server |
| Suricata Collector | Collects Suricata logs |
| AI Pipeline | Alert risk classification |
| Local Chatbot | Analyst support for AI alert lookup |

## Lab Network

| Machine | IP Address | Role |
|---|---|---|
| Kali Linux | 172.20.10.2 | Attacker machine |
| pfSense WAN | 172.20.10.4 | WAN interface |
| pfSense LAN | 192.168.200.1 | LAN gateway |
| Wazuh Server | 192.168.200.30 | SIEM server |
| Honeypot | 192.168.200.20 | Honeypot services |
| Suricata Collector | 192.168.200.40 | Suricata log collector |
| Server-real | 192.168.200.50 | Protected real server |

## Detection Use Cases

- Port scanning detection
- SSH brute-force detection
- FTP brute-force detection
- Mail service attack detection
- SQL Injection detection
- XSS detection
- Path Traversal detection
- Command execution detection
- Suspicious file download detection
- Unauthorized file modification detection
- AI-based alert risk classification

## Active Response

The lab implements automated response mechanisms:

- Redirect suspicious attackers to Honeypot
- Block malicious IPs from accessing Server-real
- Block malicious IPs locally on Server-real
- Send email alerts for high-risk incidents

## Repository Structure

| Directory | Description |
|---|---|
| architecture/ | Network topology and data flow documentation |
| setup/ | Step-by-step deployment documentation |
| rules/ | Wazuh and Suricata rule documentation |
| configs/ | Redacted configuration examples |
| scripts/ | Active response and AI scripts |
| detections/ | Detection engineering use cases |
| reports/ | SOC incident report examples |
| evidence/ | Screenshots and lab evidence |
| docs/ | Project overview, scope, threat model, lessons learned |

## Project Progress

| Phase | Status |
|---|---|
| Repository structure | Done |
| Project overview and architecture | Done |
| pfSense and Suricata documentation | Done |
| Honeypot deployment documentation | Done |
| Wazuh SIEM integration | Done |
| Custom Wazuh detection rules | Done |
| Active response automation | Done |
| AI alert classification pipeline | Done |
| Detection use case writeups | Done |
| Incident report templates | Done |
| MITRE ATT&CK mapping | Done |

## MITRE ATT&CK Mapping

| Scenario | Technique |
|---|---|
| Port scanning | T1046 - Network Service Discovery |
| Active scanning | T1595 - Active Scanning |
| SSH/FTP brute-force | T1110 - Brute Force |
| SSH remote service abuse | T1021.004 - Remote Services: SSH |
| Web exploitation | T1190 - Exploit Public-Facing Application |
| Command execution | T1059 - Command and Scripting Interpreter |
| Suspicious file download | T1105 - Ingress Tool Transfer |
| File modification | T1565 - Data Manipulation |
| Web defacement | T1491 - Defacement |

## Key Features

- Multi-layer SOC monitoring lab
- Honeypot-based attacker behavior collection
- Wazuh SIEM log correlation
- Suricata IDS/IPS monitoring
- pfSense firewall segmentation and NAT
- Custom Wazuh rules
- Automated redirect and IP blocking
- AI-based alert risk classification
- Local chatbot for AI alert lookup
- Incident reports and MITRE mapping

## Security and Privacy Notes

This repository intentionally does not include:

- VM disk files
- Private SSH keys
- Passwords
- Tokens
- Raw sensitive logs
- Raw PCAP files
- Real production data
- Full pfSense backup files

All public documentation and evidence should be redacted before publishing.

## Disclaimer

This project was built in an isolated lab environment for educational and defensive cybersecurity purposes only. No real third-party systems were targeted.