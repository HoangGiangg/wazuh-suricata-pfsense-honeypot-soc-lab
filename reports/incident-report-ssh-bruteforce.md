\# Incident Report: SSH Brute Force Detection



\## 1. Summary



An SSH brute-force attack was simulated from Kali Linux against the SSH Honeypot and/or Server-real. The activity was detected using Cowrie logs, Server-real authentication logs, and Wazuh correlation rules.



\## 2. Incident Details



| Field | Value |

|---|---|

| Incident Type | SSH Brute Force |

| Source IP | 172.20.10.2 |

| Target | Cowrie SSH Honeypot / Server-real |

| Detection Source | Cowrie, auth.log, Wazuh |

| Severity | High |

| Status | Investigated |



\## 3. Detection Sources



\- Cowrie SSH Honeypot logs

\- Server-real auth.log

\- Wazuh custom rules

\- Wazuh Dashboard alerts



\## 4. Related Rules



| Rule ID | Description |

|---|---|

| 100130 | Cowrie SSH login failure |

| 100131 | Cowrie suspected SSH brute-force |

| 100132 | Cowrie successful fake login |

| 100200 | Server-real SSH login failure |

| 100201 | Server-real suspected SSH brute-force |



\## 5. MITRE ATT\&CK Mapping



| Technique | Name |

|---|---|

| T1110 | Brute Force |

| T1021.004 | Remote Services: SSH |



\## 6. Investigation



The attacker attempted multiple SSH logins using different username and password combinations. The activity matched brute-force behavior and triggered Wazuh detection rules.



Key investigation questions:



\- What source IP attempted SSH authentication?

\- Which usernames were attempted?

\- How many failed attempts occurred?

\- Was there a successful login?

\- Were commands executed after login?

\- Did the same IP trigger other alerts?



\## 7. Evidence



Recommended evidence:



\- Cowrie login attempt logs

\- Wazuh SSH brute-force alert

\- Server-real auth.log alert

\- Source IP timeline

\- Active response output if triggered



Evidence path:



evidence/honeypot-logs/



or:



evidence/wazuh-dashboard/



\## 8. Response



Recommended response actions:



\- Redirect attacker to Cowrie Honeypot.

\- Block source IP from Server-real.

\- Enforce SSH key authentication.

\- Disable password-based SSH login on Server-real.

\- Restrict SSH access to trusted administrator IPs.



\## 9. Recommendation



\- Use SSH key-based authentication.

\- Disable root login.

\- Restrict SSH by source IP.

\- Monitor repeated authentication failures.

\- Apply temporary blocking for repeated brute-force behavior.

