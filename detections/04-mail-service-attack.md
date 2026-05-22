\# Mail Service Attack Detection



\## Overview



This use case detects suspicious activity against mail-related services such as SMTP, POP3, and IMAP.



Attackers often probe mail services to identify open relays, weak credentials, or exposed mailboxes.



\## ATT\&CK Mapping



| Technique | Name |

|---|---|

| T1110 | Brute Force |

| T1595 | Active Scanning |

| T1021 | Remote Services |



\## Data Sources



| Source | Purpose |

|---|---|

| Heralding | Captures SMTP, POP3, and IMAP interactions |

| mail.log | Captures mail service activity |

| mail.err | Captures mail service errors |

| Wazuh | Correlates suspicious mail service events |



\## Attack Simulation



Attacker machine:



\- Kali Linux

\- Source IP: 172.20.10.2



Typical test activity:



\- SMTP probing

\- POP3 login attempts

\- IMAP login attempts

\- Repeated credential attempts



\## Detection Logic



Relevant Wazuh rule examples:



| Rule ID | Purpose |

|---|---|

| 100122 | Heralding authentication attempt |

| 100123 | Heralding suspected brute-force |

| 100500 | Suricata alert detected if traffic is suspicious |



\## SOC Investigation Questions



\- What source IP accessed the mail service?

\- Which protocol was targeted?

\- Were credentials attempted?

\- Did the same source IP attempt multiple services?

\- Was the activity repeated?

\- Should the source IP be redirected or blocked?



\## Expected Evidence



Recommended screenshots should be placed in:



evidence/honeypot-logs/



or:



evidence/wazuh-dashboard/



Recommended evidence:



\- Heralding SMTP/POP3/IMAP logs

\- Wazuh alert

\- Source IP summary

\- Mail service log if applicable



\## Response



Possible response actions:



\- Redirect suspicious source IP to Honeypot.

\- Block confirmed malicious IP from Server-real.

\- Disable unnecessary mail services.

\- Monitor for repeated authentication failures.

\- Review mail relay configuration.

