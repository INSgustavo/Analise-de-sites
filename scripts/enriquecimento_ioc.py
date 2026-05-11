#!/usr/bin/env python3
"""Enriquecimento básico de IOC (WHOIS/DNS/IP) para apoio de triagem.

Uso:
  python scripts/enriquecimento_ioc.py exemplo.com
"""
from __future__ import annotations
import json
import socket
import subprocess
import sys


def run(cmd: list[str]) -> str:
    try:
        return subprocess.check_output(cmd, text=True, stderr=subprocess.STDOUT, timeout=10).strip()
    except Exception as exc:
        return f"erro: {exc}"


def enrich(domain: str) -> dict:
    data = {"domain": domain}
    try:
        data["ip"] = socket.gethostbyname(domain)
    except Exception as exc:
        data["ip"] = f"erro: {exc}"

    data["whois"] = run(["whois", domain])
    data["nslookup"] = run(["nslookup", domain])
    return data


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("uso: python scripts/enriquecimento_ioc.py <dominio>")
        sys.exit(1)
    print(json.dumps(enrich(sys.argv[1]), ensure_ascii=False, indent=2))
