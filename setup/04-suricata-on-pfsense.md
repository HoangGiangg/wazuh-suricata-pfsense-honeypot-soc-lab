\# Suricata IDS/IPS on pfSense



\## Purpose



Suricata is deployed on pfSense to monitor network traffic and detect suspicious activities from the attacker network.



In this lab, Suricata provides network-based detection for port scanning, reconnaissance, web attack attempts, and other suspicious traffic patterns.



\## Deployment Location



Suricata is enabled on the pfSense WAN interface to monitor traffic coming from the attacker network.



\## Main Functions



\- Network intrusion detection

\- Network traffic monitoring

\- Signature-based alerting

\- Detection of scanning and attack patterns

\- Log generation for Wazuh analysis



\## Ruleset



The lab uses the Emerging Threats Open ruleset for detecting common attack behaviors.



Example detection categories:



\- Port scanning

\- Reconnaissance

\- Web attacks

\- Suspicious network traffic

\- Malware-related indicators



\## Recommended pfSense Settings



\### 1. Install Suricata Package



Install Suricata from pfSense Package Manager.



Path:



System > Package Manager > Available Packages



Search for:



suricata



\### 2. Enable Suricata on WAN



Navigate to:



Services > Suricata > Interfaces



Enable Suricata on the WAN interface.



\### 3. Enable Logging



Enable logging options for:



\- Alerts

\- HTTP logs

\- DNS logs if needed

\- EVE JSON logs if supported



\### 4. Disable Hardware Offloading



For accurate packet inspection in virtualized environments, disable:



\- Hardware checksum offloading

\- Hardware TCP segmentation offloading

\- Hardware large receive offloading



Path:



System > Advanced > Networking



\## Suricata Log Forwarding



Suricata alerts are forwarded to a Suricata Collector using syslog-ng. The collector stores logs and forwards them to Wazuh Agent for centralized analysis.



\## Log Flow



pfSense Suricata

\-> syslog-ng

\-> Suricata Collector

\-> Wazuh Agent

\-> Wazuh Manager / Indexer / Dashboard



\## Detection Examples



| Scenario | Expected Detection |

|---|---|

| Nmap scan | Port scan or reconnaissance alert |

| SYN scan | Suspicious scan activity |

| Web attack payload | Web attack signature |

| Repeated suspicious traffic | High-risk network alert |



\## Security Notes



\- Tune Suricata rules to reduce false positives.

\- Avoid enabling too many rules at once on low-resource VMs.

\- Store only redacted sample logs in GitHub.

\- Do not upload raw eve.json if it contains sensitive information.



\## Evidence



Recommended screenshots should be placed in:



evidence/suricata/



Recommended evidence:



\- Suricata package installation

\- WAN interface monitoring

\- Ruleset selection

\- Hardware offloading disabled

\- Suricata alert example

\- Suricata log shown in Wazuh

