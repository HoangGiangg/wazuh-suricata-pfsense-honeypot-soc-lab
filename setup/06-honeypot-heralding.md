\# Heralding Honeypot Deployment



\## Purpose



Heralding is deployed to emulate multiple authentication-based services. In this lab, it is used to capture credential attacks against FTP, SMTP, POP3, and IMAP services.



Heralding is useful for collecting usernames, passwords, source IP addresses, destination ports, protocols, and session information from attackers.



\## Role in the Lab



| Component | Description |

|---|---|

| Honeypot Type | Multi-service credential Honeypot |

| Tool | Heralding |

| Host | Honeypot VM |

| IP Address | 192.168.200.20 |

| Exposed Through | pfSense NAT / Port Forwarding |

| Log Destination | Wazuh SIEM |



\## Emulated Services



| Service | Protocol | Purpose |

|---|---|---|

| FTP | File Transfer Protocol | Capture FTP login attempts |

| SMTP | Simple Mail Transfer Protocol | Capture mail service probing |

| POP3 | Post Office Protocol | Capture mailbox login attempts |

| IMAP | Internet Message Access Protocol | Capture mailbox login attempts |



\## Deployment Goals



\- Emulate common exposed services.

\- Capture credential-based attacks.

\- Record attacker source IP addresses.

\- Record attempted usernames and passwords.

\- Record destination ports and protocols.

\- Forward Heralding logs to Wazuh for centralized analysis.



\## High-Level Deployment Steps



1\. Create a dedicated Heralding user.

2\. Clone the Heralding repository.

3\. Install required dependencies.

4\. Configure services to listen on selected ports.

5\. Start Heralding.

6\. Configure pfSense NAT for FTP, SMTP, POP3, and IMAP.

7\. Test service access from Kali Linux.

8\. Verify Heralding logs.

9\. Configure Wazuh Agent to read Heralding logs.

10\. Verify Heralding events in Wazuh Dashboard.



\## Log Sources



Typical Heralding logs include:



| Log File | Purpose |

|---|---|

| log\_session.json | Session information |

| log\_auth.csv | Authentication attempts |



\## Example Events Captured



| Event Type | Description |

|---|---|

| FTP login attempt | Attacker tries FTP credentials |

| SMTP interaction | Attacker probes mail service |

| POP3 login attempt | Attacker tries mailbox credentials |

| IMAP login attempt | Attacker tries mailbox credentials |

| Repeated authentication failures | Possible brute-force activity |



\## Wazuh Integration



Heralding logs are collected by Wazuh Agent installed on the Honeypot VM.



The Wazuh Agent monitors Heralding log files and forwards events to the Wazuh Manager. Wazuh custom rules can then detect repeated authentication attempts and possible brute-force attacks.



\## Detection Use Cases



Heralding supports the following detection use cases:



\- FTP brute-force detection

\- Mail service attack detection

\- Credential attack monitoring

\- Service probing detection

\- Suspicious authentication behavior



\## Example SOC Questions



\- What source IP attempted authentication?

\- Which protocol was targeted?

\- Which destination port was accessed?

\- What usernames were attempted?

\- How many authentication attempts occurred?

\- Did the same IP attack multiple services?

\- Should the source IP be redirected or blocked?



\## Evidence



Recommended screenshots should be placed in:



evidence/honeypot-logs/



Recommended evidence:



\- Heralding service running

\- pfSense NAT rules for FTP, SMTP, POP3, and IMAP

\- Connection test from Kali Linux

\- Heralding log output

\- Heralding events in Wazuh Dashboard

\- Wazuh alert generated from Heralding logs



\## Security Notes



\- Heralding should be deployed only in an isolated lab environment.

\- Do not publish raw credential logs without redaction.

\- Redact usernames, passwords, source IPs, and session IDs before uploading evidence.

\- Do not expose this Honeypot to the public Internet without containment controls.

