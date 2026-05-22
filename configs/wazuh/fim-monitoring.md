\# File Integrity Monitoring



\## Purpose



File Integrity Monitoring is used to detect unauthorized changes on the protected Server-real.



In this lab, Wazuh monitors important web and system files to detect possible defacement, configuration tampering, and post-exploitation activity.



\## Monitored Areas



| Path | Purpose |

|---|---|

| Web root directory | Detect web content modification |

| Nginx configuration directory | Detect web server configuration changes |

| System account files | Detect unauthorized account changes |

| sudo configuration | Detect privilege-related changes |



\## Detection Goals



\- Detect unauthorized web content modification.

\- Detect changes to Nginx configuration.

\- Detect suspicious changes to system account files.

\- Detect privilege-related configuration changes.

\- Generate Wazuh alerts when monitored files are modified.



\## Example Alert Scenarios



| Scenario | Meaning |

|---|---|

| Web file modified | Possible web defacement |

| Nginx config modified | Possible service tampering |

| System account file changed | Possible privilege abuse |

| sudoers modified | Possible persistence or privilege escalation |



\## SOC Questions



\- What file was modified?

\- When was the file modified?

\- Which host generated the alert?

\- Was the change expected or suspicious?

\- Did the change happen after a login or web attack?

\- Should the source IP be blocked?



\## Evidence



Recommended screenshots should be placed in:



evidence/server-real/



Recommended evidence:



\- FIM configuration

\- Wazuh FIM alert

\- Modified file details

\- Timeline of related activity

