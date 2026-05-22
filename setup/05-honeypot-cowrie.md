\# Cowrie SSH Honeypot Deployment



\## Purpose



Cowrie is deployed as an SSH Honeypot in this SOC lab. Its purpose is to emulate an SSH service, attract attackers, and capture authentication attempts and post-login activities.



Cowrie helps collect attacker behavior such as brute-force attempts, usernames, passwords, source IP addresses, executed commands, downloaded files, and session activity.



\## Role in the Lab



| Component | Description |

|---|---|

| Honeypot Type | SSH Honeypot |

| Tool | Cowrie |

| Host | Honeypot VM |

| IP Address | 192.168.200.20 |

| Exposed Through | pfSense NAT / Port Forwarding |

| Log Destination | Wazuh SIEM |



\## Deployment Goals



\- Emulate an SSH service.

\- Capture SSH brute-force attempts.

\- Record attacker source IP addresses.

\- Record attempted usernames and passwords.

\- Capture commands executed by attackers.

\- Collect downloaded files or suspicious payload references.

\- Forward Cowrie logs to Wazuh for centralized analysis.



\## High-Level Deployment Steps



1\. Create a dedicated Cowrie user.

2\. Clone the Cowrie repository.

3\. Install required dependencies.

4\. Configure Cowrie service options.

5\. Start Cowrie.

6\. Configure pfSense NAT to expose the SSH Honeypot.

7\. Test SSH access from Kali Linux.

8\. Verify Cowrie logs.

9\. Configure Wazuh Agent to read Cowrie logs.

10\. Verify Cowrie events in Wazuh Dashboard.



\## Log Sources



Typical Cowrie log files include:



| Log File | Purpose |

|---|---|

| cowrie.json | Structured JSON events |

| cowrie.log | General Cowrie runtime log |

| tty logs | Recorded attacker terminal sessions |



\## Example Events Captured



| Event Type | Description |

|---|---|

| SSH connection | Attacker connects to the fake SSH service |

| Failed login | Attacker attempts invalid credentials |

| Successful fake login | Attacker enters the simulated shell |

| Command execution | Attacker runs commands inside the Honeypot |

| File download | Attacker attempts to download scripts or malware |



\## Wazuh Integration



Cowrie logs are collected by Wazuh Agent installed on the Honeypot VM.



The Wazuh Agent monitors Cowrie log files and forwards events to the Wazuh Manager. Wazuh then applies decoders and custom rules to generate alerts.



\## Detection Use Cases



Cowrie supports the following detection use cases:



\- SSH brute-force detection

\- Suspicious login attempts

\- Post-compromise command monitoring

\- Reconnaissance command detection

\- Malware download behavior detection

\- Attacker session analysis



\## Example SOC Questions



\- What source IP connected to the SSH Honeypot?

\- What usernames were attempted?

\- How many failed login attempts occurred?

\- Did the attacker reach the fake shell?

\- What commands did the attacker execute?

\- Did the attacker attempt to download a file?

\- Should the source IP be redirected or blocked?



\## Evidence



Recommended screenshots should be placed in:



evidence/honeypot-logs/



Recommended evidence:



\- Cowrie service running

\- pfSense NAT rule for Cowrie

\- SSH connection test from Kali Linux

\- Cowrie log output

\- Cowrie events in Wazuh Dashboard

\- Wazuh alert generated from Cowrie logs



\## Security Notes



\- Cowrie should be deployed only in an isolated lab environment.

\- Do not expose the Honeypot to the public Internet unless proper containment is implemented.

\- Do not upload raw logs containing real public IPs, credentials, or sensitive data.

\- Redact usernames, passwords, and source IPs before publishing screenshots or logs.

