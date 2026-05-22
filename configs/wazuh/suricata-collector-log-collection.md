\# Suricata Collector Wazuh Log Collection



\## Purpose



The Suricata Collector receives Suricata logs from pfSense and forwards them to Wazuh using Wazuh Agent.



This design separates firewall/IDS log collection from the Wazuh Server and makes Suricata alert ingestion easier to manage.



\## Host Information



| Field | Value |

|---|---|

| Host | Suricata Collector |

| IP Address | 192.168.200.40 |

| Wazuh Role | Agent |

| Log Source | pfSense Suricata |

| Log Destination | Wazuh Manager |



\## Log Flow



pfSense Suricata

\-> syslog-ng

\-> Suricata Collector

\-> local Suricata log file

\-> Wazuh Agent

\-> Wazuh Manager

\-> Wazuh Dashboard



\## Collected Log Types



| Log Type | Purpose |

|---|---|

| Suricata alert events | Detect scan, reconnaissance, and attacks |

| Suricata HTTP events | Analyze suspicious web requests |

| Suricata flow events | Understand network connections |

| Suricata DNS events | Investigate suspicious domains if enabled |



\## Detection Purpose



Suricata logs support the following detections:



\- ICMP probing

\- Port scanning

\- Nmap activity

\- Reconnaissance

\- Suspicious HTTP traffic

\- Web attack signatures

\- High-severity IDS alerts

\- Dropped or blocked traffic



\## Public Documentation Notes



Do not upload raw eve.json or full alert logs if they contain sensitive traffic data.



Use redacted examples or screenshots instead.

