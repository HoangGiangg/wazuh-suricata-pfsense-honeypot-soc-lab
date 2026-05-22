\# Wazuh All-in-One Deployment



\## Purpose



Wazuh is deployed as the central SIEM platform in this SOC lab. It collects logs from multiple sources, analyzes security events, generates alerts, and provides dashboard visualization for investigation.



\## Wazuh Role in the Lab



| Component | Role |

|---|---|

| Wazuh Manager | Receives and analyzes events from agents |

| Wazuh Indexer | Stores and indexes alerts |

| Wazuh Dashboard | Provides visualization and investigation interface |

| Wazuh Agent | Collects logs from monitored hosts |



\## Deployment Model



This lab uses the Wazuh All-in-One deployment model.



All main Wazuh components are installed on a single Ubuntu Server VM.



| Host | IP Address | Role |

|---|---|---|

| Wazuh Server | 192.168.200.30 | SIEM server |



\## Main Responsibilities



\- Collect logs from Honeypot services.

\- Collect Suricata alerts from the Suricata Collector.

\- Collect system and application logs from Server-real.

\- Collect Mail and FTP service logs.

\- Monitor file integrity changes.

\- Apply custom detection rules.

\- Generate alerts for suspicious activities.

\- Support dashboard-based investigation.

\- Trigger active response workflows.



\## High-Level Deployment Steps



1\. Prepare Ubuntu Server 22.04.

2\. Install Wazuh All-in-One.

3\. Access Wazuh Dashboard.

4\. Add Wazuh Agents for monitored hosts.

5\. Verify agent connectivity.

6\. Configure log collection sources.

7\. Configure custom rules.

8\. Verify alerts in Wazuh Dashboard.



\## Monitored Hosts



| Host | IP Address | Collected Logs |

|---|---|---|

| Honeypot | 192.168.200.20 | Cowrie, Heralding, Snare/Tanner |

| Suricata Collector | 192.168.200.40 | Suricata EVE/alert logs |

| Server-real | 192.168.200.50 | auth.log, nginx logs, auditd, FIM |

| Mail/FTP Server | Lab internal IP | mail.log, mail.err, vsftpd.log, auth.log |



\## Detection Coverage



Wazuh is used to detect:



\- SSH brute-force attempts

\- FTP brute-force attempts

\- Mail service probing

\- Web attack attempts

\- Port scanning alerts from Suricata

\- Suspicious command execution

\- Malware download behavior

\- Unauthorized file modification

\- High-risk alert patterns



\## Evidence



Recommended screenshots should be placed in:



evidence/wazuh-dashboard/



Recommended evidence:



\- Wazuh Dashboard login page

\- Wazuh agent list

\- Honeypot agent connected

\- Suricata Collector agent connected

\- Server-real agent connected

\- Alert dashboard

\- Example Wazuh alert



\## Security Notes



\- Do not upload Wazuh passwords or generated credentials to GitHub.

\- Do not upload real client.keys.

\- Do not upload real ossec.conf files if they contain sensitive values.

\- Redact usernames, public IP addresses, tokens, and emails from screenshots.

