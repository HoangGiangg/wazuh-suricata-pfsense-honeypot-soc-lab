#!/usr/bin/env python3
import json
import os
import time
import subprocess
import ipaddress

ALERT_FILE = "/var/ossec/logs/alerts/alerts.json"

PFSENSE_HOST = "admin@192.168.200.1"
PFSENSE_KEY = "/root/.ssh/pfsense_honey"
REDIRECT_ALIAS = "HONEY_REDIRECT"
BLOCK_ALIAS = "BLOCK_REALSERVER"

SERVER_REAL_HOST = "adminops@192.168.200.50"
SERVER_REAL_KEY = "/root/.ssh/server_real_honey"
SERVER_REAL_BLOCK_CMD = "/usr/local/sbin/serverreal-block-ip.sh"

REDIRECT_TTL = 600
TRIGGER_RULE_IDS = {"100510", "100511", "100512"}

WHITELIST = {
    "127.0.0.1",
    "192.168.200.1",
    "192.168.200.20",
    "192.168.200.30",
    "192.168.200.40",
    "192.168.200.50",
}

tracked = {}

def valid_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except Exception:
        return False

def ssh_run(host, key, cmd):
    full_cmd = [
        "ssh",
        "-i", key,
        "-o", "StrictHostKeyChecking=no",
        host,
        cmd
    ]
    return subprocess.run(full_cmd, capture_output=True, text=True)

def add_pf(ip):
    cmd = (
        f"pfctl -t {REDIRECT_ALIAS} -T add {ip}; "
        f"pfctl -t {BLOCK_ALIAS} -T add {ip}; "
        f"pfctl -k {ip}"
    )
    return ssh_run(PFSENSE_HOST, PFSENSE_KEY, cmd)

def del_pf(ip):
    cmd = (
        f"pfctl -t {REDIRECT_ALIAS} -T delete {ip}; "
        f"pfctl -t {BLOCK_ALIAS} -T delete {ip}; "
        f"pfctl -k {ip}"
    )
    return ssh_run(PFSENSE_HOST, PFSENSE_KEY, cmd)

def add_server_real(ip):
    cmd = f"sudo {SERVER_REAL_BLOCK_CMD} add {ip} {REDIRECT_TTL}"
    return ssh_run(SERVER_REAL_HOST, SERVER_REAL_KEY, cmd)

def del_server_real(ip):
    cmd = f"sudo {SERVER_REAL_BLOCK_CMD} del {ip}"
    return ssh_run(SERVER_REAL_HOST, SERVER_REAL_KEY, cmd)

def extract_src_ip(alert):
    if "src_ip" in alert:
        return alert["src_ip"]
    data = alert.get("data", {})
    if isinstance(data, dict):
        if "src_ip" in data:
            return data["src_ip"]
        if "srcip" in data:
            return data["srcip"]
    return None

def extract_rule_id(alert):
    rule = alert.get("rule", {})
    rid = rule.get("id")
    return str(rid) if rid is not None else None

def follow(path):
    with open(path, "r") as f:
        f.seek(0, os.SEEK_END)
        while True:
            line = f.readline()
            if not line:
                time.sleep(0.5)
                continue
            yield line

def add_everywhere(ip):
    pf_res = add_pf(ip)
    print(f"[PF ADD] {ip} rc={pf_res.returncode} out={pf_res.stdout.strip()} err={pf_res.stderr.strip()}")

    sr_res = add_server_real(ip)
    print(f"[SR ADD] {ip} rc={sr_res.returncode} out={sr_res.stdout.strip()} err={sr_res.stderr.strip()}")

def del_everywhere(ip):
    pf_res = del_pf(ip)
    print(f"[PF DEL] {ip} rc={pf_res.returncode} out={pf_res.stdout.strip()} err={pf_res.stderr.strip()}")

    sr_res = del_server_real(ip)
    print(f"[SR DEL] {ip} rc={sr_res.returncode} out={sr_res.stdout.strip()} err={sr_res.stderr.strip()}")

def cleanup_expired():
    now = time.time()
    expired = [ip for ip, ts in tracked.items() if now - ts > REDIRECT_TTL]
    for ip in expired:
        del_everywhere(ip)
        del tracked[ip]

def main():
    print("[*] Honey redirect daemon started")
    for line in follow(ALERT_FILE):
        cleanup_expired()

        try:
            alert = json.loads(line)
        except Exception:
            continue

        rule_id = extract_rule_id(alert)
        if rule_id not in TRIGGER_RULE_IDS:
            continue

        src_ip = extract_src_ip(alert)
        if not src_ip or not valid_ip(src_ip):
            continue

        if src_ip in WHITELIST:
            print(f"[SKIP] {src_ip} is whitelisted")
            continue

        if src_ip not in tracked:
            add_everywhere(src_ip)
            tracked[src_ip] = time.time()

if __name__ == "__main__":
    main()
