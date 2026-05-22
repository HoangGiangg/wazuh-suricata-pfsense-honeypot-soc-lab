\# Data Flow



\## Overview



This document describes how attack traffic, logs, alerts, and response actions flow through the SOC lab.



\## Attack Traffic Flow



Kali Linux

\-> pfSense Firewall

\-> Honeypot Services

\-> Server-real

\-> Suricata IDS/IPS



\## Log Collection Flow



Cowrie Logs

Heralding Logs

Snare/Tanner Logs

Server-real Logs

Suricata Logs

\-> Wazuh Agent / Collector

\-> Wazuh Manager

\-> Wazuh Indexer

\-> Wazuh Dashboard



\## Suricata Log Flow



pfSense + Suricata

\-> syslog-ng

\-> Suricata Collector

\-> Wazuh Agent

\-> Wazuh Dashboard



\## Honeypot Log Flow



Attacker

\-> Honeypot Service

\-> Cowrie SSH logs

\-> Heralding authentication and session logs

\-> Snare/Tanner web logs

\-> Wazuh Agent

\-> Wazuh Manager

\-> Wazuh Dashboard



\## Server-real Log Flow



Server-real

\-> auth.log

\-> nginx access and error logs

\-> auditd logs

\-> FIM events

\-> Wazuh Agent

\-> Wazuh Manager

\-> Wazuh Dashboard



\## Alert Correlation Flow



Raw Logs

\-> Wazuh Decoders

\-> Custom Wazuh Rules

\-> Alerts

\-> Dashboard / Email / Active Response



\## Data Sources



| Source | Log Type | Purpose |

|---|---|---|

| Suricata | Network IDS alerts | Detect scan and network attacks |

| Cowrie | SSH session logs | Capture SSH brute-force and commands |

| Heralding | Authentication and session logs | Capture FTP, SMTP, POP3, IMAP credential attacks |

| Snare/Tanner | Web request logs | Capture SQLi, XSS, path traversal |

| Server-real | System and web logs | Monitor protected server |

| auditd / FIM | File change events | Detect unauthorized modification |



\## Notes



All logs used for public documentation must be redacted before being uploaded to GitHub.

