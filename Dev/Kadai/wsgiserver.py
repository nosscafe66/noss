from wsgiref.simple_server import make_server

def app(environ, start_response):
    status = '200 OK'
    headers = [('Content-type', 'text/html; charset=utf-8')]
    path = "index.html"
    start_response(status, headers)
    return path.encode('utf-8')

httpd = make_server('', 8000, app)
print("Serving on port 8000...")

# Serve until process is killed
httpd.serve_forever()