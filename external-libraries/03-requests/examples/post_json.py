from __future__ import annotations

import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from threading import Thread

import requests


class JsonHandler(BaseHTTPRequestHandler):
    def do_POST(self) -> None:
        length = int(self.headers["Content-Length"])
        incoming = json.loads(self.rfile.read(length))
        payload = {"created": incoming, "content_type": self.headers["Content-Type"]}
        body = json.dumps(payload).encode("utf-8")

        self.send_response(201)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format: str, *args: object) -> None:
        return


server = ThreadingHTTPServer(("127.0.0.1", 0), JsonHandler)
thread = Thread(target=server.serve_forever, daemon=True)
thread.start()

try:
    host, port = server.server_address
    response = requests.post(
        f"http://{host}:{port}/items",
        json={"name": "Nova", "active": True},
        timeout=(1, 2),
    )
    response.raise_for_status()
    data = response.json()

    print(f"status: {response.status_code}")
    print(f"created: {data['created']}")
    print(f"content-type: {data['content_type']}")
finally:
    server.shutdown()
    server.server_close()
    thread.join()
