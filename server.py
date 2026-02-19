#!/usr/bin/env python3
"""Simple HTTP server for Fitness Timer PWA."""

import http.server
import socket
import os

PORT = 8080
DIR = os.path.dirname(os.path.abspath(__file__))


def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "localhost"


os.chdir(DIR)
handler = http.server.SimpleHTTPRequestHandler
server = http.server.HTTPServer(("0.0.0.0", PORT), handler)
ip = get_local_ip()

print(f"\n  Fitness Timer Web")
print(f"  ─────────────────────────────")
print(f"  Local:   http://localhost:{PORT}")
print(f"  iPhone:  http://{ip}:{PORT}")
print(f"\n  En tu iPhone:")
print(f"  1. Abre Safari y ve a http://{ip}:{PORT}")
print(f"  2. Toca Compartir > Agregar a pantalla de inicio")
print(f"  3. Listo! Funciona como app nativa\n")

try:
    server.serve_forever()
except KeyboardInterrupt:
    print("\nServidor detenido.")
