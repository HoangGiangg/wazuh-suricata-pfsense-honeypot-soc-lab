\# Active Response Flow



\## Overview



The lab implements automated response mechanisms to move from passive detection to proactive defense.



When Wazuh detects suspicious or malicious activity, response scripts can redirect attackers to Honeypot or block them from accessing the real server.



\## Response Types



| Response | Purpose |

|---|---|

| Redirect to Honeypot | Move suspicious attackers away from Server-real |

| Block IP | Prevent malicious IPs from accessing Server-real |

| Email Alert | Notify administrator about high-risk events |



\## Redirect Flow



Wazuh Alert

\-> honey\_redirect\_daemon.py

\-> Extract source IP

\-> Check whitelist

\-> Add IP to pfSense HONEY\_REDIRECT alias or table

\-> Kill existing connection state

\-> Future traffic is redirected to Honeypot



\## Block Flow



Wazuh Alert

\-> Active Response Script

\-> Extract malicious source IP

\-> Check whitelist

\-> Add IP to BLOCK\_REALSERVER

\-> Block access to Server-real



\## Server-real Local Block Flow



Wazuh Alert

\-> Block script on Server-real

\-> Add source IP to ipset or iptables

\-> Drop malicious traffic locally



\## Email Alert Flow



High-risk Wazuh Alert

\-> Email alert rule

\-> Mail relay / SMTP

\-> Administrator mailbox



\## Whitelist Logic



Before redirecting or blocking an IP address, the script should check whether the IP belongs to trusted administrators or internal systems.



Example whitelist:



\- 192.168.200.0/24

\- 127.0.0.1

\- trusted administrator IP



\## Response Conditions



| Detection | Response |

|---|---|

| Repeated port scanning | Redirect to Honeypot |

| Repeated SSH brute-force | Redirect or block |

| Repeated web attack attempts | Redirect to Honeypot |

| High severity Suricata alert | Redirect immediately |

| Confirmed malicious activity | Block from Server-real |



\## Safety Notes



\- Do not block trusted administrator IPs.

\- Always maintain a whitelist.

\- Use TTL for temporary blocking or redirection.

\- Log every automated response action.

\- Test active response in an isolated lab only.



\## Evidence



Recommended screenshots should be placed in:



evidence/active-response/



Recommended evidence:



\- pfSense alias HONEY\_REDIRECT

\- pfSense alias BLOCK\_REALSERVER

\- Wazuh alert triggering response

\- Redirect test result

\- Block IP test result

\- Email alert result

