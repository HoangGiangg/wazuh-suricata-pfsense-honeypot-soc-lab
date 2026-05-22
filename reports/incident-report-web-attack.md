\# Incident Report: Web Attack Detection



\## 1. Summary



Suspicious web attack attempts were simulated against the web Honeypot and/or Server-real. The attacks included SQL Injection, Cross-Site Scripting, Path Traversal, and suspicious web probing patterns.



\## 2. Incident Details



| Field | Value |

|---|---|

| Incident Type | Web Attack |

| Source IP | 172.20.10.2 |

| Target | Snare/Tanner Web Honeypot / Server-real |

| Detection Source | Snare/Tanner, Nginx, Suricata, Wazuh |

| Severity | High |

| Status | Investigated |



\## 3. Detection Sources



\- Snare/Tanner web Honeypot logs

\- Nginx access logs

\- Suricata IDS alerts

\- Wazuh custom rules



\## 4. Related Rules



| Rule ID | Description |

|---|---|

| 100140 | Tanner suspicious web request |

| 100141 | Tanner suspected SQL Injection |

| 100142 | Tanner suspected XSS |

| 100143 | Tanner suspected Path Traversal or LFI |

| 100144 | Repeated suspicious web requests |

| 100220 | Server-real web probing |

| 100221 | Repeated Server-real web probing |

| 100503 | Suricata web attack alert |

| 100511 | Repeated web attack, redirect candidate |



\## 5. MITRE ATT\&CK Mapping



| Technique | Name |

|---|---|

| T1190 | Exploit Public-Facing Application |

| T1059 | Command and Scripting Interpreter |



\## 6. Investigation



The attacker sent suspicious HTTP requests that matched common web attack patterns. Logs from Snare/Tanner, Nginx, Suricata, and Wazuh were used to investigate the activity.



Key investigation questions:



\- What source IP sent the suspicious request?

\- What URL path was requested?

\- What payload was used?

\- Was the request related to SQL Injection, XSS, or Path Traversal?

\- Did the same IP send repeated suspicious requests?

\- Was the traffic redirected to Honeypot?



\## 7. Evidence



Recommended evidence:



\- Suspicious web request screenshot

\- Snare/Tanner log output

\- Nginx access log

\- Suricata alert

\- Wazuh web attack alert

\- Redirect result if triggered



Evidence path:



evidence/honeypot-logs/



or:



evidence/attack-simulation/



\## 8. Response



Recommended response actions:



\- Redirect suspicious web attacker to Honeypot.

\- Block repeated attacker from Server-real.

\- Review web server logs.

\- Harden Nginx configuration.

\- Add detection rules for repeated payloads.

\- Review whether any file modification occurred after the web attack.



\## 9. Recommendation



\- Validate input on web applications.

\- Use security headers.

\- Hide server version information.

\- Monitor suspicious paths and payloads.

\- Correlate web probing with file modification alerts.

