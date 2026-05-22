\# pfSense Firewall Setup



\## Purpose



pfSense is used as the main firewall and routing device in this SOC lab. It separates the attacker network from the internal lab network and controls access to Honeypot services, the protected real server, and monitoring components.



\## pfSense Roles



\- Network gateway

\- Firewall policy enforcement

\- NAT and port forwarding

\- Traffic segmentation

\- Redirect suspicious attackers to Honeypot

\- Block malicious IP addresses from accessing the real server



\## Interface Design



| Interface | IP Address | Role |

|---|---|---|

| WAN | 172.20.10.4 | Connected to attacker network |

| LAN | 192.168.200.1 | Connected to internal lab network |



\## Internal Hosts



| Host | IP Address | Role |

|---|---|---|

| Wazuh Server | 192.168.200.30 | SIEM |

| Honeypot | 192.168.200.20 | Cowrie, Heralding, Snare/Tanner |

| Suricata Collector | 192.168.200.40 | Receives Suricata logs |

| Server-real | 192.168.200.50 | Protected real server |



\## Firewall Policy Goals



| Direction | Action | Purpose |

|---|---|---|

| WAN to pfSense | Allow selected traffic | Lab testing and management |

| WAN to Honeypot | Allow and NAT | Expose Honeypot services |

| WAN to Server-real | Allow selected web traffic | Simulate public web access |

| WAN to LAN | Deny by default | Protect internal network |

| Wazuh to pfSense | Allow SSH where needed | Active response automation |

| Internal hosts to Wazuh | Allow | Log forwarding and monitoring |



\## NAT and Port Forwarding



The lab uses NAT and port forwarding to expose selected services.



| Public Service | Destination Host | Purpose |

|---|---|---|

| SSH Honeypot | Honeypot / Cowrie | Capture SSH brute-force and commands |

| FTP, SMTP, POP3, IMAP Honeypot | Honeypot / Heralding | Capture credential attacks |

| Web Honeypot | Honeypot / Snare-Tanner | Capture web attack payloads |

| Web Server | Server-real | Simulate protected production service |



\## pfSense Alias Design



| Alias | Purpose |

|---|---|

| HONEY\_REDIRECT | Stores suspicious IPs redirected to Honeypot |

| BLOCK\_REALSERVER | Stores malicious IPs blocked from Server-real |

| ADMIN\_WHITELIST | Stores trusted administrator IPs |



\## Security Notes



\- Do not expose the pfSense management interface to untrusted networks in production.

\- Do not upload real pfSense backup files such as config.xml to GitHub.

\- Screenshots should hide usernames, passwords, public IP addresses, serial numbers, and tokens.

\- This configuration is for isolated lab use only.



\## Evidence



Recommended screenshots should be placed in:



evidence/pfsense/



Recommended evidence:



\- pfSense dashboard

\- WAN and LAN interface configuration

\- Firewall rules

\- NAT port forwarding rules

\- Alias list

\- Block and redirect rules

