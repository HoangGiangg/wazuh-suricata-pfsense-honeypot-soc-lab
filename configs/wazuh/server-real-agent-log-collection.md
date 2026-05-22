\# Server-real Wazuh Agent Log Collection



\## Purpose



The Server-real is the protected internal server in this SOC lab. Wazuh Agent is installed on this host to collect authentication logs, web logs, audit logs, and file integrity monitoring events.



\## Host Information



| Field | Value |

|---|---|

| Host | Server-real |

| IP Address | 192.168.200.50 |

| Wazuh Role | Agent |

| Log Destination | Wazuh Manager |



\## Collected Logs



| Log Source | Purpose |

|---|---|

| auth.log | Detect SSH login failures and sudo activity |

| nginx access log | Detect web probing and suspicious web requests |

| nginx error log | Detect web server errors |

| auditd logs | Monitor security-relevant system actions |

| FIM events | Detect unauthorized file modification |



\## Detection Purpose



Server-real logs support the following detections:



\- SSH login failure

\- SSH brute-force attempts

\- Successful sudo activity

\- Sensitive sudo command execution

\- Web probing

\- Repeated suspicious web requests

\- Nginx configuration changes

\- Web content modification

\- Possible post-exploitation activity



\## Hardening Context



The Server-real should be hardened using:



\- SSH key authentication

\- Restricted SSH access

\- Host firewall rules

\- Nginx version hiding

\- HTTP security headers

\- File integrity monitoring

\- Audit logging



\## Redaction Notes



Before uploading logs or screenshots, redact:



\- Usernames

\- Passwords

\- Internal secrets

\- Hostnames if sensitive

\- Public IP addresses

\- SSH key material

