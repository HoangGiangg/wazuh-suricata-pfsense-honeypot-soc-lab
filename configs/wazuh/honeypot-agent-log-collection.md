\# Honeypot Wazuh Agent Log Collection



\## Purpose



This document describes the log sources collected from the Honeypot VM by Wazuh Agent.



The Honeypot VM runs Cowrie, Heralding, and Snare/Tanner. These services generate logs that help detect attacker behavior.



\## Host Information



| Field | Value |

|---|---|

| Host | Honeypot VM |

| IP Address | 192.168.200.20 |

| Wazuh Role | Agent |

| Log Destination | Wazuh Manager |



\## Cowrie Logs



| Log Source | Purpose |

|---|---|

| cowrie.json | Structured SSH Honeypot events |

| cowrie.log | Runtime and service logs |

| tty logs | Attacker session replay and command analysis |



\## Heralding Logs



| Log Source | Purpose |

|---|---|

| log\_session.json | Session information |

| log\_auth.csv | Authentication attempts |



\## Snare/Tanner Logs



| Log Source | Purpose |

|---|---|

| Snare access logs | HTTP request activity |

| Tanner report logs | Web attack classification |

| Tanner runtime logs | Backend processing information |



\## Detection Purpose



These logs support the following detections:



\- SSH brute-force attempts

\- FTP brute-force attempts

\- SMTP/POP3/IMAP credential attacks

\- Web probing

\- SQL Injection attempts

\- XSS attempts

\- Path Traversal attempts

\- Suspicious command execution

\- Malware download behavior



\## Redaction Notes



Before uploading evidence to GitHub, redact:



\- Source IP addresses if sensitive

\- Usernames

\- Passwords

\- Session IDs

\- Downloaded file names if sensitive

\- Hostnames

