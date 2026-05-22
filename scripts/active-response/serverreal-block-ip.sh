#!/usr/bin/env bash

set -euo pipefail

IPSET_NAME="serverreal_block"
ACTION="${1:-}"
TARGET_IP="${2:-}"
TIMEOUT="${3:-600}"

usage() {
  echo "Usage:"
  echo "  $0 add <ip> [timeout_seconds]"
  echo "  $0 del <ip>"
  echo "  $0 list"
  exit 1
}

ensure_ipset() {
  if ! ipset list "$IPSET_NAME" >/dev/null 2>&1; then
    ipset create "$IPSET_NAME" hash:ip timeout 0
  fi
}

ensure_iptables_rule() {
  if ! iptables -C INPUT -m set --match-set "$IPSET_NAME" src -j DROP >/dev/null 2>&1; then
    iptables -I INPUT -m set --match-set "$IPSET_NAME" src -j DROP
  fi
}

validate_ip() {
  local ip="$1"
  python3 - <<PY
import ipaddress
ipaddress.ip_address("$ip")
PY
}

case "$ACTION" in
  add)
    if [ -z "$TARGET_IP" ]; then
      usage
    fi
    validate_ip "$TARGET_IP"
    ensure_ipset
    ensure_iptables_rule
    ipset add "$IPSET_NAME" "$TARGET_IP" timeout "$TIMEOUT" -exist
    echo "[OK] Added $TARGET_IP to $IPSET_NAME with timeout ${TIMEOUT}s"
    ;;

  del)
    if [ -z "$TARGET_IP" ]; then
      usage
    fi
    validate_ip "$TARGET_IP"
    ensure_ipset
    ipset del "$IPSET_NAME" "$TARGET_IP" 2>/dev/null || true
    echo "[OK] Removed $TARGET_IP from $IPSET_NAME"
    ;;

  list)
    ensure_ipset
    ipset list "$IPSET_NAME"
    ;;

  *)
    usage
    ;;
esac