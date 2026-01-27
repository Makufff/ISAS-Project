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
        client_hostname = data.get("client_hostname", "Unknown")
        client_ip = data.get("client_ip", "Unknown")

        if command == "print":
            # จำลองการ print (แทน lpd)
            print_message = f"[PRINT JOB] {filename} | From: {client_hostname} ({client_ip})"
            result = subprocess.run(
                ["echo", print_message],
                capture_output=True,
                text=True
            )

            response = {
                "status": "ok",
                "output": result.stdout.strip(),
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