\# Incident Report: Unauthorized File Modification



\## 1. Summary



An unauthorized file modification event was detected on the protected Server-real using Wazuh File Integrity Monitoring.



This type of event may indicate web defacement, configuration tampering, privilege abuse, or post-exploitation activity.



\## 2. Incident Details



| Field | Value |

|---|---|

| Incident Type | Unauthorized File Modification |

| Target | Server-real |

| Detection Source | Wazuh FIM, auditd |

| Severity | Critical |

| Status | Investigated |



\## 3. Detection Sources



\- Wazuh File Integrity Monitoring

\- auditd logs

\- Server-real system logs

\- Nginx logs if related to web content



\## 4. Related Rules



| Rule ID | Description |

|---|---|

| 100230 | Server-real Nginx configuration change |

| 100231 | Server-real web content modification |

| 100240 | Privilege escalation plus Nginx change |

| 100241 | Web probing plus web content modification |



\## 5. MITRE ATT\&CK Mapping



| Technique | Name |

|---|---|

| T1565 | Data Manipulation |

| T1491 | Defacement |

| T1547 | Boot or Logon Autostart Execution |



\## 6. Investigation



Wazuh detected a modification to a monitored file or directory on Server-real. The event should be investigated with related authentication, sudo, web, and audit logs.



Key investigation questions:



\- What file was modified?

\- When was it modified?

\- Was the change expected?

\- Which user or process modified the file?

\- Was there suspicious login activity before the change?

\- Was there web probing before the modification?

\- Could this indicate defacement or persistence?



\## 7. Evidence



Recommended evidence:



\- Wazuh FIM alert

\- Modified file path

\- File change timeline

\- Related SSH or sudo alert

\- Related web probing alert

\- Server-real log context



Evidence path:



evidence/server-real/



\## 8. Response



Recommended response actions:



\- Investigate the modified file.

\- Restore file from a trusted backup if needed.

\- Block related suspicious source IP.

\- Review SSH and sudo activity.

\- Review web access logs before the modification.

\- Harden file permissions and service configuration.



\## 9. Recommendation



\- Monitor critical files and directories with Wazuh FIM.

\- Restrict write permissions.

\- Review sudo usage regularly.

\- Harden web server configuration.

\- Correlate file changes with login and web access events.

