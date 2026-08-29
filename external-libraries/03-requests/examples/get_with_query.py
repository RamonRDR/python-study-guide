from __future__ import annotations

import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from threading import Thread
from urllib.parse import parse_qs, urlparse

import requests


class QueryHandler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        parsed = urlparse(self.path)
        payload = {"path": parsed.path, "query": parse_qs(parsed.query)}
        body = json.dumps(payload).encode("utf-8")

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format: str, *args: object) -> None:
        return


server = ThreadingHTTPServer(("127.0.0.1", 0), QueryHandler)
thread = Thread(target=server.serve_forever, daemon=True)
thread.start()

try:
    host, port = server.server_address
    response = requests.get(
        f"http://{host}:{port}/items",
        params={"status": "open", "limit": 2},
        timeout=(1, 2),
    )
    response.raise_for_status()
    data = response.json()

    print(f"status: {response.status_code}")
    print(f"path: {data['path']}")
    print(f"query: {data['query']}")
finally:
    server.shutdown()
    server.server_close()
    thread.join()
