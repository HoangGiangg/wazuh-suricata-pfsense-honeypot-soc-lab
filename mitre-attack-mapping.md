\# MITRE ATT\&CK Mapping



\## Overview



This document maps the detection scenarios in this SOC lab to MITRE ATT\&CK techniques.



The goal is to show how each lab scenario relates to real-world attacker behaviors and how the deployed tools support detection and response.



\## Mapping Table



| Use Case | Technique ID | Technique Name | Data Sources | Detection Components |

|---|---|---|---|---|

| Port Scan Detection | T1046 | Network Service Discovery | Suricata, pfSense, Wazuh | Suricata alerts, Wazuh correlation rules |

| Active Scanning | T1595 | Active Scanning | Suricata, pfSense | IDS alerts, firewall traffic logs |

| SSH Brute Force | T1110 | Brute Force | Cowrie, auth.log, Wazuh | Honeypot logs, authentication logs, Wazuh rules |

| SSH Remote Service | T1021.004 | Remote Services: SSH | Cowrie, Server-real auth.log | SSH login attempts, failed authentication |

| FTP Brute Force | T1110 | Brute Force | Heralding, vsftpd.log, Wazuh | Credential attempt logs, Wazuh brute-force rules |

| Mail Service Attack | T1110 | Brute Force | Heralding, mail.log, mail.err | SMTP, POP3, IMAP authentication attempts |

| Web Attack | T1190 | Exploit Public-Facing Application | Snare/Tanner, Nginx, Suricata, Wazuh | Web payload detection, IDS alerts |

| Command Execution | T1059 | Command and Scripting Interpreter | Cowrie, Wazuh | Command execution logs, suspicious command rules |

| Suspicious File Download | T1105 | Ingress Tool Transfer | Cowrie, Suricata, Wazuh | wget/curl patterns, file download behavior |

| Unauthorized File Modification | T1565 | Data Manipulation | Wazuh FIM, auditd | File integrity alerts |

| Web Defacement | T1491 | Defacement | Wazuh FIM, Nginx logs | Web content modification alerts |

| Privilege Abuse / Persistence Indicator | T1547 | Boot or Logon Autostart Execution | Wazuh FIM, auditd, auth.log | Sensitive file change and sudo activity |

| Automated Response | N/A | Defensive Response | Wazuh, pfSense, scripts | Redirect, block IP, email alert |

| AI Alert Prioritization | N/A | Alert Triage Support | Wazuh alerts, AI pipeline | Risk classification, confidence score |



\## Detection Coverage by Tool



| Tool | Detection Role |

|---|---|

| pfSense | Firewall, NAT, traffic segmentation, redirect/block enforcement |

| Suricata | Network IDS/IPS detection |

| Wazuh | SIEM, log collection, rule correlation, alerting |

| Cowrie | SSH attacker behavior collection |

| Heralding | FTP, SMTP, POP3, IMAP credential attack collection |

| Snare/Tanner | Web attack behavior collection |

| auditd | Host activity monitoring |

| Wazuh FIM | File integrity monitoring |

| AI Pipeline | Risk classification and alert prioritization |

| Local Chatbot | Analyst support for AI alert lookup |



\## Notes



Some defensive actions such as redirecting attackers to Honeypot or blocking IP addresses are not mapped directly to ATT\&CK techniques because they represent response mechanisms rather than attacker techniques.



The mapping is intended for educational and SOC portfolio documentation purposes.

