from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse

class RequestHandler(BaseHTTPRequestHandler):

  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-Type', 'text/html')
    self.end_headers()
    self.wfile.write(b"<!DOCTYPE html><html><head> <title>Home Page</title> </head><body> <h1> Welcome to my website! </h1> </body></html>")

def run(server_class = HTTPServer, handler_class = RequestHandler):
  server_address = ('', 8000)
  httpd = server_class(server_address, handler_class)
  httpd.serve_forever()

run()