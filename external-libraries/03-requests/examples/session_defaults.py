from __future__ import annotations

import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from threading import Thread

import requests


class SessionHandler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        payload = {
            "client": self.headers.get("X-Client"),
            "authorization": self.headers.get("Authorization"),
        }
        body = json.dumps(payload).encode("utf-8")

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format: str, *args: object) -> None:
        return


server = ThreadingHTTPServer(("127.0.0.1", 0), SessionHandler)
thread = Thread(target=server.serve_forever, daemon=True)
thread.start()

try:
    host, port = server.server_address
    with requests.Session() as session:
        session.headers.update(
            {
                "X-Client": "python-study-guide",
                "Authorization": "Bearer example-token",
            }
        )
        response = session.get(f"http://{host}:{port}/profile", timeout=(1, 2))
        response.raise_for_status()
        data = response.json()

    print(f"client: {data['client']}")
    print(f"auth-scheme: {data['authorization'].split()[0]}")
finally:
    server.shutdown()
    server.server_close()
    thread.join()
