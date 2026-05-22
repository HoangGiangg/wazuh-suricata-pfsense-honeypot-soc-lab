\# Lab Environment



\## Virtual Machines



| VM | Operating System | Role | Suggested Resources |

|---|---|---|---|

| Kali Linux | Kali Linux | Attacker machine | 2 vCPU, 2-4 GB RAM |

| pfSense + Suricata | pfSense CE | Firewall, NAT, IDS/IPS | 2 vCPU, 2-4 GB RAM |

| Wazuh Server | Ubuntu Server 22.04 | SIEM platform | 4 vCPU, 8 GB RAM |

| Honeypot | Ubuntu Server 22.04 | Cowrie, Heralding, Snare/Tanner | 2 vCPU, 2-4 GB RAM |

| Suricata Collector | Ubuntu Server 22.04 | Collects Suricata logs | 2 vCPU, 2-4 GB RAM |

| Server-real | Ubuntu Server 22.04 | Protected real server | 2 vCPU, 2-4 GB RAM |

| Mail-FTP Server | Ubuntu Server 22.04 | Mail and FTP services | 2 vCPU, 2-4 GB RAM |



\## Tools Used



\- pfSense CE

\- Suricata

\- Wazuh

\- Cowrie

\- Heralding

\- Snare/Tanner

\- Nginx

\- Postfix

\- Dovecot

\- vsftpd

\- Kali Linux tools

\- Python scripts for active response and AI alert classification



\## Lab Purpose



The purpose of this lab is to simulate common attack behaviors and demonstrate how multiple security layers can detect, monitor, analyze, and respond to suspicious activities.

