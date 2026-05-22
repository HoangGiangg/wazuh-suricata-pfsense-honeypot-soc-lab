\# Web Attack Detection



\## Overview



This use case detects suspicious web requests and common web attack patterns against the web Honeypot and Server-real.



The lab focuses on common web attack patterns such as SQL Injection, Cross-Site Scripting, Path Traversal, Local File Inclusion, and command execution attempts.



\## ATT\&CK Mapping



| Technique | Name |

|---|---|

| T1190 | Exploit Public-Facing Application |

| T1059 | Command and Scripting Interpreter |



\## Data Sources



| Source | Purpose |

|---|---|

| Snare/Tanner | Captures web Honeypot requests |

| Nginx access log | Records web requests to Server-real |

| Nginx error log | Records web application errors |

| Suricata | Detects network-level web attack signatures |

| Wazuh | Correlates web attack events |



\## Attack Simulation



Attacker machine:



\- Kali Linux

\- Source IP: 172.20.10.2



Typical test payloads:



\- SQL Injection pattern

\- XSS pattern

\- Path Traversal pattern

\- Command execution-like pattern

\- Web directory probing



\## Detection Logic



Relevant Wazuh rule examples:



| Rule ID | Purpose |

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



\## SOC Investigation Questions



\- What source IP sent the suspicious request?

\- What URL path was requested?

\- What payload was used?

\- Was the request detected by Honeypot, Suricata, or Server-real?

\- Was the attack repeated?

\- Did the same IP perform scanning before web attacks?

\- Should the IP be redirected or blocked?



\## Expected Evidence



Recommended screenshots should be placed in:



evidence/honeypot-logs/



or:



evidence/attack-simulation/



Recommended evidence:



\- Web request from Kali Linux

\- Snare/Tanner log

\- Nginx access log

\- Suricata alert

\- Wazuh web attack alert

\- Redirect result if triggered



\## Response



Possible response actions:



\- Redirect suspicious web attacker to Honeypot.

\- Block repeated attacker from Server-real.

\- Review web access logs.

\- Harden Nginx configuration.

\- Add or tune Wazuh web detection rules.

