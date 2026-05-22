\# Incident Report: Port Scan Detection



\## 1. Summary



A port scanning activity was simulated from the Kali Linux attacker machine against the lab environment. The activity was detected by Suricata and correlated in Wazuh.



\## 2. Incident Details



| Field | Value |

|---|---|

| Incident Type | Port Scanning |

| Source IP | 172.20.10.2 |

| Target Environment | pfSense / Internal Lab Network |

| Detection Source | Suricata, Wazuh |

| Severity | Medium to High |

| Status | Investigated |



\## 3. Detection Sources



\- Suricata IDS alerts

\- pfSense firewall logs

\- Wazuh correlated alerts



\## 4. Related Rules



| Rule ID | Description |

|---|---|

| 100500 | Suricata alert detected |

| 100501 | ICMP probing |

| 100502 | Scan or reconnaissance activity |

| 100510 | Repeated scan activity, redirect candidate |



\## 5. MITRE ATT\&CK Mapping



| Technique | Name |

|---|---|

| T1046 | Network Service Discovery |

| T1595 | Active Scanning |



\## 6. Investigation



The attacker performed reconnaissance against the lab network to identify reachable hosts and open ports. Suricata generated alerts related to scanning activity, and Wazuh displayed the correlated event for SOC investigation.



Key investigation questions:



\- What source IP performed the scan?

\- Which hosts and ports were targeted?

\- Was the scan repeated?

\- Did the same IP perform additional attacks after scanning?



\## 7. Evidence



Recommended evidence:



\- Kali scan output

\- Suricata alert screenshot

\- Wazuh alert screenshot

\- pfSense traffic log screenshot

\- Redirect/block evidence if active response was triggered



Evidence path:



evidence/attack-simulation/



or:



evidence/suricata/



\## 8. Response



Recommended response actions:



\- Monitor the source IP.

\- Redirect repeated scanner traffic to Honeypot.

\- Block the source IP from accessing Server-real if malicious activity continues.

\- Review related alerts from the same source IP.



\## 9. Recommendation



\- Keep IDS rules updated.

\- Enable alert correlation for repeated scanning.

\- Restrict exposed services.

\- Use firewall rules to limit unnecessary access.

\- Monitor scan activity as an early indicator of future attacks.

