#!/usr/bin/env python3
import sys
import json
import requests
import socket

if len(sys.argv) != 2:
    print("Usage: printsol <filename>")
    sys.exit(1)

filename = sys.argv[1]

# ดึงข้อมูลเครื่องและ IP
hostname = socket.gethostname()
try:
    ip_address = socket.gethostbyname(hostname)
except:
    ip_address = "Unknown"

payload = {
    "command": "print",
    "file": filename,
    "client_hostname": hostname,
    "client_ip": ip_address
}

res = requests.post(
    "http://192.168.17.111:9000/",
    data=json.dumps(payload),
    headers={"Content-Type": "application/json"}
)

print(res.json())