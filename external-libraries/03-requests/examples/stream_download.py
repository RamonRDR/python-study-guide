from __future__ import annotations

from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from threading import Thread

import requests


PAYLOAD = b"chunked-data"


class StreamHandler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        self.send_response(200)
        self.send_header("Content-Type", "application/octet-stream")
        self.send_header("Content-Length", str(len(PAYLOAD)))
        self.end_headers()
        self.wfile.write(PAYLOAD[:6])
        self.wfile.flush()
        self.wfile.write(PAYLOAD[6:])

    def log_message(self, format: str, *args: object) -> None:
        return


server = ThreadingHTTPServer(("127.0.0.1", 0), StreamHandler)
thread = Thread(target=server.serve_forever, daemon=True)
thread.start()

try:
    host, port = server.server_address
    with requests.get(
        f"http://{host}:{port}/download",
        stream=True,
        timeout=(1, 2),
    ) as response:
        response.raise_for_status()
        chunks = list(response.iter_content(chunk_size=4))
        content = b"".join(chunks)

    print(f"bytes: {len(content)}")
    print(f"content: {content.decode('utf-8')}")
finally:
    server.shutdown()
    server.server_close()
    thread.join()
