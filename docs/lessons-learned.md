\# Lessons Learned



\## Overview



This project provided hands-on experience in building a proactive SOC monitoring lab using firewall, IDS/IPS, SIEM, Honeypot, active response, and AI-based alert classification.



\## Technical Lessons



\### 1. Multi-layer Detection Is More Effective



Using only one security tool is not enough. The lab combines multiple layers:



\- pfSense for firewall and traffic control

\- Suricata for network-based detection

\- Wazuh for SIEM correlation and alerting

\- Honeypot services for attacker behavior collection

\- Wazuh FIM and auditd for host-based monitoring



This improves visibility across network, host, and application layers.



\### 2. Honeypot Data Is Valuable for SOC Analysis



Honeypot logs provide high-value attacker behavior data because normal users should not interact with Honeypot services.



Cowrie, Heralding, and Snare/Tanner help capture:



\- Source IP addresses

\- Login attempts

\- Usernames and passwords attempted

\- Commands executed by attackers

\- Web payloads

\- Suspicious service interactions



\### 3. SIEM Correlation Improves Investigation



Wazuh helps centralize logs from multiple systems and correlate events into meaningful alerts.



This makes it easier to investigate:



\- Repeated brute-force attempts

\- Web attack patterns

\- Scan activity followed by exploitation attempts

\- File modification after suspicious access

\- High-risk IP behavior across multiple modules



\### 4. Active Response Adds Proactive Defense



The active response workflow allows the system to move beyond detection.



The lab implements:



\- Redirecting suspicious attackers to Honeypot

\- Blocking malicious IP addresses from accessing Server-real

\- Blocking IPs locally on Server-real

\- Sending email alerts



\### 5. File Integrity Monitoring Is Important



Wazuh FIM helps detect suspicious file changes on Server-real.



This is useful for detecting:



\- Web defacement

\- Nginx configuration tampering

\- Unauthorized system file modification

\- Possible post-exploitation behavior



\### 6. AI Can Assist Alert Prioritization



The AI module classifies alerts into medium, high, and critical risk levels.



It helps SOC analysts prioritize investigation, but it should not replace human review.



AI output should be treated as supporting evidence, not the only decision source.



\## Challenges



\- Integrating logs from multiple sources required careful field normalization.

\- Custom Wazuh rules needed tuning to reduce false positives.

\- Active response required whitelist logic to avoid blocking trusted systems.

\- Screenshots and logs needed redaction before publishing to GitHub.

\- AI model quality depends on the quality and balance of the training dataset.



\## Future Improvements



\- Add Splunk integration as a second SIEM comparison.

\- Add FortiGate or another enterprise firewall version of the lab.

\- Add more custom Suricata local rules.

\- Add dashboard screenshots and sample sanitized logs.

\- Add automated deployment scripts.

\- Add Sigma rule mapping.

\- Add more detailed incident timelines.

\- Improve AI model evaluation with larger datasets.

\- Add API-based response instead of SSH-based automation where possible.



\## Conclusion



This lab demonstrates a practical SOC workflow from detection to response:



Attack simulation

\-> log collection

\-> SIEM analysis

\-> alert generation

\-> investigation

\-> active response

\-> reporting



The project provides a strong foundation for SOC Tier 1, Blue Team, detection engineering, and incident response portfolio development.

