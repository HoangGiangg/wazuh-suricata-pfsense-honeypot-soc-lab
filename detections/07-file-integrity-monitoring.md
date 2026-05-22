\# File Integrity Monitoring Detection



\## Overview



This use case detects unauthorized file modification on the protected Server-real using Wazuh File Integrity Monitoring.



File modification events may indicate web defacement, persistence, privilege abuse, or post-exploitation activity.



\## ATT\&CK Mapping



| Technique | Name |

|---|---|

| T1565 | Data Manipulation |

| T1491 | Defacement |

| T1547 | Boot or Logon Autostart Execution |



\## Data Sources



| Source | Purpose |

|---|---|

| Wazuh FIM | Detects monitored file changes |

| auditd | Records system-level activity |

| Server-real logs | Provides host context |

| Nginx logs | Provides web activity context |



\## Monitored Areas



| Path Type | Purpose |

|---|---|

| Web root directory | Detect web content modification |

| Nginx configuration | Detect web server configuration tampering |

| System account files | Detect account or privilege changes |

| sudo configuration | Detect privilege-related changes |



\## Detection Logic



Relevant Wazuh rule examples:



| Rule ID | Purpose |

|---|---|

| 100230 | Server-real Nginx configuration change |

| 100231 | Server-real web content modification |

| 100240 | Privilege escalation plus Nginx change |

| 100241 | Web probing plus web content modification |



\## SOC Investigation Questions



\- What file was modified?

\- When was it modified?

\- Which host generated the alert?

\- Was the change expected?

\- Was there suspicious login activity before the change?

\- Was there web probing before the change?

\- Could this indicate defacement or post-exploitation?



\## Expected Evidence



Recommended screenshots should be placed in:



evidence/server-real/



Recommended evidence:



\- Wazuh FIM alert

\- Modified file path

\- File change timeline

\- Related SSH or web alerts

\- Server-real log context



\## Response



Possible response actions:



\- Investigate the modified file.

\- Restore file from a trusted backup if needed.

\- Block related suspicious source IP.

\- Review SSH and sudo activity.

\- Review web access logs before the modification.

\- Harden file permissions and service configuration.

