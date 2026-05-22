\# Active Response Automation



\## Overview



This directory contains active response scripts used in the SOC lab.



The active response workflow automatically redirects suspicious attackers to Honeypot and blocks malicious IP addresses from accessing the protected Server-real.



\## Scripts



| File | Purpose |

|---|---|

| honey\_redirect\_daemon.py | Monitors Wazuh alerts and triggers redirect/block actions |

| serverreal-block-ip.sh | Adds or removes malicious IPs from the Server-real local block list |

| .env.example | Example deployment variables |



\## Trigger Rule IDs



| Rule ID | Meaning |

|---|---|

| 100510 | Repeated scan activity, redirect candidate |

| 100511 | Repeated web attack activity, redirect candidate |

| 100512 | High severity alert, immediate redirect candidate |



\## Response Flow



Wazuh Alert

\-> honey\_redirect\_daemon.py

\-> Extract source IP

\-> Check whitelist

\-> Add IP to pfSense HONEY\_REDIRECT

\-> Add IP to pfSense BLOCK\_REALSERVER

\-> Kill active connection state

\-> Add IP to Server-real local block list

\-> Remove IP after TTL expires



\## pfSense Response



The daemon connects to pfSense over SSH and updates:



\- HONEY\_REDIRECT

\- BLOCK\_REALSERVER



These aliases or pf tables are used to redirect suspicious traffic to Honeypot and block access to the real server.



\## Server-real Response



The daemon connects to Server-real over SSH and calls:



/usr/local/sbin/serverreal-block-ip.sh



This script uses ipset and iptables to block malicious source IPs locally.



\## Whitelist



The daemon should maintain a whitelist to prevent trusted internal systems from being blocked.



Example whitelist entries:



\- 127.0.0.1

\- 192.168.200.1

\- 192.168.200.20

\- 192.168.200.30

\- 192.168.200.40

\- 192.168.200.50



\## Security Notes



\- Do not commit private SSH keys.

\- Do not commit production credentials.

\- Do not expose pfSense SSH access to untrusted networks.

\- Use least-privilege accounts for automation.

\- Test active response only in an isolated lab environment.

\- Use TTL-based blocking to avoid permanent accidental blocks.



\## Evidence



Recommended screenshots should be placed in:



evidence/active-response/



Recommended evidence:



\- pfSense HONEY\_REDIRECT alias

\- pfSense BLOCK\_REALSERVER alias

\- Wazuh alert that triggered response

\- Daemon output

\- Server-real ipset block list

\- Blocked traffic test result

