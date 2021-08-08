## -*- coding : UTF-8 -*-
from http.server import SimpleHTTPRequestHandler,HTTPServer

class Server_Up:
    def __init__(self, server_class, handler_class):
        self.server_class = server_class
        self.handler_class = handler_class
    def run(self):
        server_address = ('', 8000)
        self.server_class(server_address, self.handler_class).serve_forever()

      
if __name__ == "__main__":
    server_up = Server_Up(HTTPServer, SimpleHTTPRequestHandler)
    server_up.run()
