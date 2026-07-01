from http.server import HTTPServer, BaseHTTPRequestHandler

# Create the server
server = HTTPServer(('localhost', 8080), BaseHTTPRequestHandler)

# Request handler for both GET and POST requests
class RequestHandler(BaseHTTPRequestHandler):

    # Handle GET requests
    def do_GET(self):
        # Send response status code
        self.send_response(200)

        # Send headers
        self.send_header('Content-type','text/html')
        self.end_headers()

        # Send response in html
        self.wfile.write("<html><body>This is a GET request</body></html>")

    # Handle POST requests
    def do_POST(self):
        # Send response status code
        self.send_response(200)

        # Send response headers
        self.send_header('Content-type','text/html')
        self.end_headers()

        # Send response in html
        self.wfile.write("<html><body>This is a POST request</body></html>")

# Run the server
server.serve_forever()