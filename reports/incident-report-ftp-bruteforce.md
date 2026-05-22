\# Incident Report: FTP Brute Force Detection



\## 1. Summary



An FTP brute-force activity was simulated from Kali Linux. Heralding captured credential attempts, and Wazuh generated alerts based on repeated authentication behavior.



\## 2. Incident Details



| Field | Value |

|---|---|

| Incident Type | FTP Brute Force |

| Source IP | 172.20.10.2 |

| Target | Heralding FTP Honeypot / FTP Service |

| Detection Source | Heralding, Wazuh |

| Severity | High |

| Status | Investigated |



\## 3. Detection Sources



\- Heralding authentication logs

\- Wazuh custom rules

\- Wazuh Dashboard alerts

\- pfSense traffic logs if available



\## 4. Related Rules



| Rule ID | Description |

|---|---|

| 100122 | Heralding authentication attempt |

| 100123 | Heralding suspected brute-force |



\## 5. MITRE ATT\&CK Mapping



| Technique | Name |

|---|---|

| T1110 | Brute Force |

| T1021 | Remote Services |



\## 6. Investigation



The attacker attempted multiple FTP authentication attempts. The activity was captured by Heralding and forwarded to Wazuh for alerting and analysis.



Key investigation questions:



\- What source IP attempted FTP authentication?

\- What usernames were attempted?

\- How many authentication attempts occurred?

\- Did the same IP target other services?

\- Was the activity isolated or part of a larger attack chain?



\## 7. Evidence



Recommended evidence:



\- Heralding FTP log

\- Wazuh brute-force alert

\- Source IP activity timeline

\- pfSense NAT or traffic log if available



Evidence path:



evidence/honeypot-logs/



\## 8. Response



Recommended response actions:



\- Redirect attacker to Honeypot.

\- Block source IP from Server-real if repeated activity continues.

\- Disable anonymous FTP.

\- Enforce strong credentials.

\- Monitor other services for the same source IP.



\## 9. Recommendation



\- Avoid exposing FTP when not required.

\- Use SFTP or secure alternatives.

\- Enforce strong password policies.

\- Monitor credential attacks across multiple services.

