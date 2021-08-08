## -*- coding : UTF-8 -*-
from http.server import SimpleHTTPRequestHandler, HTTPServer

with open('index.html', 'r')as f:
    index_file = f.read()

class OriginalHTTPRequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        html = index_file.format(
            title = "blog",
            content = "bog"
        )
        self.wfile.write(html.encode('utf-8'))
        return None
