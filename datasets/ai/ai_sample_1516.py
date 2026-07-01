from http.server import CGIHTTPRequestHandler, HTTPServer

class MyHTTPServer(CGIHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        file = open('index.html', 'r')
        html = file.read()
        file.close()
        self.wfile.write(html.encode())

server = HTTPServer(('', 8080), MyHTTPServer)
print("Starting server at http://localhost:8080")
server.serve_forever()