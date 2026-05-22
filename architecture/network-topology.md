\# Network Topology



\## Logical Topology



```text

&#x20;               Attack Zone

&#x20;             +-------------+

&#x20;             | Kali Linux  |

&#x20;             | 172.20.10.2 |

&#x20;             +------+------+

&#x20;                    |

&#x20;                    |

&#x20;             +------+------+

&#x20;             |   pfSense   |

&#x20;             | Firewall    |

&#x20;             | WAN: 172.20.10.4

&#x20;             | LAN: 192.168.200.1

&#x20;             +------+------+

&#x20;                    |

&#x20;            Internal Lab Network

&#x20;             192.168.200.0/24

&#x20;                    |

&#x20;  ------------------------------------------------

&#x20;  |                 |              |              |

+--+-----------+ +---+--------+ +---+---------+ +--+-----------+

| Honeypot    | | Wazuh      | | Suricata    | | Server-real  |

| 192.168.200.20 | 192.168.200.30 | Collector | | 192.168.200.50 |

| Cowrie      | | SIEM       | | 192.168.200.40 | Nginx/Web |

| Heralding   | | Dashboard  | |             | | Protected  |

| Snare/Tanner| | Alerts     | |             | | Server     |

+-------------+ +------------+ +-------------+ +--------------+

