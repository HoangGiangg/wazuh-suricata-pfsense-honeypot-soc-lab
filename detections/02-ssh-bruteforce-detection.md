\# SSH Brute Force Detection



\## Overview



This use case detects repeated SSH authentication attempts against the SSH Honeypot or the protected Server-real.



SSH brute-force attacks are commonly used to guess valid credentials and gain unauthorized access.



\## ATT\&CK Mapping



| Technique | Name |

|---|---|

| T1110 | Brute Force |

| T1021.004 | Remote Services: SSH |



\## Data Sources



| Source | Purpose |

|---|---|

| Cowrie | Captures SSH Honeypot login attempts and commands |

| Server-real auth.log | Captures SSH login attempts on the real server |

| Wazuh | Correlates authentication events and generates alerts |



\## Attack Simulation



Attacker machine:



\- Kali Linux

\- Source IP: 172.20.10.2



Typical test activity:



\- SSH login attempt

\- Repeated failed SSH logins

\- Hydra-based brute-force simulation

\- Fake successful login into Cowrie



\## Detection Logic



Relevant Wazuh rule examples:



| Rule ID | Purpose |

|---|---|

| 100130 | Cowrie SSH login failure |

| 100131 | Cowrie suspected SSH brute-force |

| 100132 | Cowrie successful fake login |

| 100200 | Server-real SSH login failure |

| 100201 | Server-real suspected SSH brute-force |



\## SOC Investigation Questions



\- What source IP attempted SSH authentication?

\- Which usernames were attempted?

\- How many login failures occurred?

\- Was there a successful login after repeated failures?

\- Did the activity target Cowrie or Server-real?

\- Did the attacker execute commands after login?

\- Should the IP be redirected or blocked?



\## Expected Evidence



Recommended screenshots should be placed in:



evidence/honeypot-logs/



or:



evidence/wazuh-dashboard/



Recommended evidence:



\- Cowrie login attempt logs

\- Wazuh SSH brute-force alert

\- Server-real auth.log alert

\- Source IP timeline

\- Active response result if triggered



\## Response



Possible response actions:



\- Redirect attacker to Cowrie.

\- Block the source IP from Server-real.

\- Enforce SSH key authentication.

\- Disable password-based SSH login on Server-real.

\- Restrict SSH access to administrator IPs.

