# -*- coding: utf-8 -*-
__author__ = "Kounosu Yuto <mail@example.com>"
__status__ = "production"
__version__ = "0.0.1"
__date__    = "22 Janualy 2022"
__prodactname__ = "HttpServerConnect"

from http.server import HTTPServer, SimpleHTTPRequestHandler

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()
    
with open('index.html', 'r') as f:
    index_file = f.read()

class OriginalHTTPRequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):

        self.send_response(200)
        self.end_headers()

        html = index_file.format(
            title = 'Login',
            content = 'Form'
        )
        self.wfile.write(html.encode('utf-8'))
        return None

if __name__ == '__main__':
    run()