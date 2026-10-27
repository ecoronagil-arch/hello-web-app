import os, socket, datetime
from http.server import BaseHTTPRequestHandler, HTTPServer

VERSION = os.environ.get("APP_VERSION", "dev")

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = f"""<html><body style="font-family:sans-serif;text-align:center;padding-top:80px">
<h1>Hello v5 - shipped by a git push!</h1>
<p>Git push &rarr; Cloud Build &rarr; GitOps repo &rarr; Config Sync &rarr; GKE</p>
<p>Build: {VERSION}<br>Time: {datetime.datetime.utcnow():%Y-%m-%d %H:%M:%S} UTC</p>
</body></html>"""
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(body.encode())

HTTPServer(("", int(os.environ.get("PORT", 8080))), Handler).serve_forever()
