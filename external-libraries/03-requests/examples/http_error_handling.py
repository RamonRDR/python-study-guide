from __future__ import annotations

from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from threading import Thread

import requests


class NotFoundHandler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        self.send_response(404)
        self.send_header("Content-Length", "0")
        self.end_headers()

    def log_message(self, format: str, *args: object) -> None:
        return


server = ThreadingHTTPServer(("127.0.0.1", 0), NotFoundHandler)
thread = Thread(target=server.serve_forever, daemon=True)
thread.start()

try:
    host, port = server.server_address
    try:
        response = requests.get(f"http://{host}:{port}/missing", timeout=(1, 2))
        response.raise_for_status()
    except requests.HTTPError as exc:
        print(f"caught: {exc.__class__.__name__}")
        print(f"status: {exc.response.status_code}")
finally:
    server.shutdown()
    server.server_close()
    thread.join()
