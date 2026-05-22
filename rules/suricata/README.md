\# Suricata Rules



\## Overview



This lab uses Suricata on pfSense for network-based intrusion detection.



The primary Suricata ruleset used in the lab is Emerging Threats Open. Suricata generates IDS alerts, and those alerts are forwarded to Wazuh for correlation and analysis.



\## Current Status



No custom Suricata `.rules` file is included in this repository at this stage.



The file `pfsense\_suricata\_rules.xml` from the original lab is a Wazuh XML rules file for parsing and correlating Suricata events. It is stored under:



rules/wazuh/suricata\_correlation\_rules.xml



\## Detection Coverage



Suricata is used to detect:



\- ICMP probing

\- Port scanning

\- Reconnaissance

\- Suspicious HTTP traffic

\- Web attack signatures

\- High severity IDS alerts

\- Blocked or dropped traffic



\## Future Improvements



Possible future additions:



\- Custom Suricata local.rules

\- Lab-specific detection signatures

\- C2 traffic simulation rules

\- Malware download indicator rules

\- Custom HTTP payload detection rules



\## Security Notes



\- Do not upload raw Suricata `eve.json` logs if they contain sensitive traffic data.

\- Redact IP addresses, domains, hostnames, and payloads before publishing evidence.

