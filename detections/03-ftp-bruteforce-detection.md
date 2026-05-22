\# FTP Brute Force Detection



\## Overview



This use case detects repeated FTP authentication attempts against the FTP Honeypot or FTP service.



FTP brute-force attacks attempt to guess valid usernames and passwords for file transfer services.



\## ATT\&CK Mapping



| Technique | Name |

|---|---|

| T1110 | Brute Force |

| T1021 | Remote Services |



\## Data Sources



| Source | Purpose |

|---|---|

| Heralding | Captures FTP credential attempts |

| vsftpd.log | Captures FTP activity on the FTP server |

| Wazuh | Correlates authentication attempts and generates alerts |



\## Attack Simulation



Attacker machine:



\- Kali Linux

\- Source IP: 172.20.10.2



Typical test activity:



\- FTP login attempt

\- Repeated FTP credential attempts

\- Hydra-based FTP brute-force simulation



\## Detection Logic



Relevant Wazuh rule examples:



| Rule ID | Purpose |

|---|---|

| 100122 | Heralding authentication attempt |

| 100123 | Heralding suspected brute-force |

| 100500 | Suricata alert detected if network activity is observed |



\## SOC Investigation Questions



\- What source IP attempted FTP authentication?

\- Which usernames were attempted?

\- How many attempts occurred?

\- Was the same IP also attacking SSH or mail services?

\- Did the attack target Honeypot or real service?

\- Should the source IP be redirected or blocked?



\## Expected Evidence



Recommended screenshots should be placed in:



evidence/honeypot-logs/



Recommended evidence:



\- Heralding FTP log

\- Wazuh brute-force alert

\- Source IP activity timeline

\- pfSense NAT log if available



\## Response



Possible response actions:



\- Redirect attacker to Honeypot.

\- Block source IP from Server-real.

\- Disable anonymous FTP.

\- Enforce strong authentication.

\- Monitor repeated credential attacks from the same IP.

