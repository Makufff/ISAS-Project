from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import subprocess

class RPCHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)

        data = json.loads(body)
        command = data.get("command")
        filename = data.get("file")
        content = data.get("content", "")
        client_hostname = data.get("client_hostname", "Unknown")
        client_ip = data.get("client_ip", "Unknown")

        if command == "print":
            # แสดงข้อมูลการ print
            print("\n" + "="*60)
            print(f"🖨️  PRINT JOB RECEIVED")
            print("="*60)
            print(f"📄 File: {filename}")
            print(f"👤 From: {client_hostname}")
            print(f"🌐 IP: {client_ip}")
            print("-"*60)
            print("📝 Content:")
            print("-"*60)
            print(content)
            print("="*60 + "\n")

            response = {
                "status": "ok",
                "message": f"Print job received from {client_hostname} ({client_ip})",
                "file": filename,
                "client_info": {
                    "hostname": client_hostname,
                    "ip": client_ip
                }
            }
        else:
            response = {
                "status": "error",
                "message": "Unknown command"
            }

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(response).encode())

def run():
    server = HTTPServer(("0.0.0.0", 9000), RPCHandler)
    print("🖨 Worker RPC running on port 9000")
    server.serve_forever()

if name == "main":
    run()