\# pfSense Active Response Aliases



\## Overview



This document describes the pfSense aliases or tables used by the active response workflow.



\## Required Aliases / Tables



| Name | Purpose |

|---|---|

| HONEY\_REDIRECT | Stores suspicious IPs that should be redirected to Honeypot |

| BLOCK\_REALSERVER | Stores malicious IPs that should be blocked from accessing Server-real |



\## HONEY\_REDIRECT



The HONEY\_REDIRECT alias/table is used to identify source IP addresses that should be redirected away from the real server and toward Honeypot services.



\## BLOCK\_REALSERVER



The BLOCK\_REALSERVER alias/table is used to prevent malicious IP addresses from reaching the protected Server-real.



\## Automation



The active response daemon updates these aliases or tables remotely over SSH.



\## Security Notes



\- Do not expose pfSense SSH access to untrusted networks.

\- Use SSH key-based authentication.

\- Limit automation account privileges.

\- Keep trusted administrator IPs in a whitelist.

\- Test redirect and block rules in an isolated lab.

