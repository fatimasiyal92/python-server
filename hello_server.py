from http.server import BaseHTTPRequestHandler, HTTPServer

class HelloWorldHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"Hello, world!")

if __name__ == '__main__':
    server_address = ('', 8000)  # Serve on all addresses, port 8000
    httpd = HTTPServer(server_address, HelloWorldHandler)
    print("Server started at http://localhost:8000")
    httpd.serve_forever()

