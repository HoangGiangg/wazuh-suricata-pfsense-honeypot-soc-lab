\# IP Addressing Plan



\## Network Overview



| Machine | IP Address | Role |

|---|---|---|

| Kali Linux | 172.20.10.2 | Attacker machine |

| pfSense WAN | 172.20.10.4 | WAN interface |

| pfSense LAN | 192.168.200.1 | LAN gateway |

| Wazuh Server | 192.168.200.30 | SIEM server |

| Honeypot | 192.168.200.20 | Honeypot server |

| Suricata Collector | 192.168.200.40 | Suricata log collector |

| Server-real | 192.168.200.50 | Protected real server |



\## Network Zones



| Zone | Description |

|---|---|

| Attack Zone | Contains the Kali Linux attacker machine |

| Firewall Zone | pfSense separates attacker traffic from the internal lab network |

| Honeypot Zone | Contains Honeypot services used to collect attacker behavior |

| Monitoring Zone | Contains Wazuh and log collection components |

| Server Zone | Contains the protected server and service simulation systems |



\## Notes



The IP addresses are used only for the lab environment and should be adjusted if the lab is rebuilt in a different network.

