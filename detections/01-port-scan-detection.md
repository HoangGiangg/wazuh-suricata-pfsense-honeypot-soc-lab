\# Port Scan Detection



\## Overview



This use case detects port scanning and reconnaissance activity from an attacker machine against the lab environment.



Port scanning is commonly used by attackers to discover live hosts, open ports, and exposed services before launching further attacks.



\## ATT\&CK Mapping



| Technique | Name |

|---|---|

| T1046 | Network Service Discovery |

| T1595 | Active Scanning |



\## Data Sources



| Source | Purpose |

|---|---|

| Suricata | Detects scan and reconnaissance traffic |

| pfSense | Records firewall and traffic activity |

| Wazuh | Correlates Suricata alerts and generates detections |



\## Attack Simulation



Attacker machine:



\- Kali Linux

\- Source IP: 172.20.10.2



Typical test activity:



\- ICMP probing

\- TCP SYN scan

\- Service version scan

\- Full port scan



\## Detection Logic



The detection relies on Suricata alerts forwarded to Wazuh.



Relevant Wazuh rule examples:



| Rule ID | Purpose |

|---|---|

| 100500 | Suricata alert detected |

| 100501 | ICMP probing |

| 100502 | Scan or reconnaissance activity |

| 100510 | Repeated scan activity, redirect candidate |



\## SOC Investigation Questions



\- What source IP performed the scan?

\- What target IP was scanned?

\- Which ports were targeted?

\- Was the scan repeated?

\- Did Suricata generate alerts?

\- Did Wazuh correlate the activity?

\- Should the source IP be redirected to Honeypot?



\## Expected Evidence



Recommended screenshots should be placed in:



evidence/attack-simulation/



or:



evidence/suricata/



Recommended evidence:



\- Kali scan command output

\- Suricata alert

\- Wazuh alert

\- pfSense traffic log

\- Redirect action if triggered



\## Response



Possible response actions:



\- Monitor the source IP.

\- Redirect repeated scanner to Honeypot.

\- Block the source IP from accessing Server-real.

\- Review additional activity from the same source IP.

