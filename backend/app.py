from http.server import HTTPServer, BaseHTTPRequestHandler

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Hello from Effective Mobile!")
        else:
            self.send_response(404)
            self.end_headers()

server = HTTPServer(('', 8080), MyHandler)
print("Starting server on port 8080...")
server.serve_forever()

