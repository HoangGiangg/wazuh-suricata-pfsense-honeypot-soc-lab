\# Snare and Tanner Web Honeypot Deployment



\## Purpose



Snare and Tanner are deployed as a web Honeypot solution in this SOC lab.



Snare acts as the web frontend that serves the fake website to attackers. Tanner acts as the backend analysis service that receives and processes web requests.



This setup is used to capture suspicious web requests, web scanning behavior, and common web attack payloads such as SQL Injection, Cross-Site Scripting, Path Traversal, and command execution attempts.



\## Role in the Lab



| Component | Description |

|---|---|

| Honeypot Type | Web Honeypot |

| Frontend | Snare |

| Backend | Tanner |

| Host | Honeypot VM |

| IP Address | 192.168.200.20 |

| Exposed Through | pfSense NAT / Port Forwarding |

| Log Destination | Wazuh SIEM |



\## Deployment Goals



\- Emulate a web application.

\- Attract suspicious web traffic.

\- Capture HTTP requests from attackers.

\- Detect suspicious URL paths and payloads.

\- Record source IP addresses and request details.

\- Forward web Honeypot logs to Wazuh for centralized analysis.



\## High-Level Deployment Steps



1\. Create a dedicated user for Snare/Tanner.

2\. Clone the Tanner repository.

3\. Install Tanner dependencies.

4\. Start Tanner backend service.

5\. Clone the Snare repository.

6\. Prepare a fake web seed or cloned website.

7\. Configure Snare to serve the fake web application.

8\. Bind Snare/Tanner to the correct network interface.

9\. Configure pfSense NAT for web access.

10\. Test web access from Kali Linux.

11\. Verify Snare and Tanner logs.

12\. Configure Wazuh Agent to read web Honeypot logs.

13\. Verify web Honeypot events in Wazuh Dashboard.



\## Log Sources



Typical Snare/Tanner logs include:



| Log Source | Purpose |

|---|---|

| Snare access logs | HTTP request activity |

| Tanner report logs | Web attack classification and analysis |

| Tanner runtime logs | Backend processing information |



\## Example Events Captured



| Event Type | Description |

|---|---|

| Web probing | Attacker accesses suspicious paths |

| SQL Injection attempt | Request contains SQLi payload |

| XSS attempt | Request contains script-based payload |

| Path Traversal | Request attempts to access sensitive files |

| Command execution pattern | Request contains command-like payload |

| Automated scanning | Multiple suspicious requests in a short time |



\## Wazuh Integration



Snare and Tanner logs are collected by Wazuh Agent installed on the Honeypot VM.



The Wazuh Agent monitors web Honeypot log files and forwards events to the Wazuh Manager. Custom Wazuh rules can then classify suspicious web requests and generate alerts.



\## Detection Use Cases



Snare/Tanner supports the following detection use cases:



\- Web probing detection

\- SQL Injection detection

\- Cross-Site Scripting detection

\- Path Traversal detection

\- Local File Inclusion detection

\- Command execution attempt detection

\- Automated web scanning detection



\## Example SOC Questions



\- What source IP accessed the web Honeypot?

\- What URL path was requested?

\- What payload was sent?

\- Was the request related to SQL Injection?

\- Was the request related to XSS?

\- Was the request related to Path Traversal?

\- Did the same IP send multiple suspicious requests?

\- Should the source IP be redirected or blocked?



\## Evidence



Recommended screenshots should be placed in:



evidence/honeypot-logs/



Recommended evidence:



\- Tanner service running

\- Snare service running

\- Fake web page served by Snare

\- pfSense NAT rule for web Honeypot

\- Web access test from Kali Linux

\- Snare/Tanner log output

\- Web Honeypot events in Wazuh Dashboard

\- Wazuh alert generated from web Honeypot logs



\## Security Notes



\- Snare/Tanner should be deployed only in an isolated lab environment.

\- Do not publish raw logs that contain sensitive payloads without review.

\- Redact source IPs, hostnames, usernames, and session identifiers before uploading evidence.

\- Avoid exposing the web Honeypot to the public Internet without containment and monitoring.

