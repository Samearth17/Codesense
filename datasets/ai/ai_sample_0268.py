import http.server
from http.server import SimpleHTTPRequestHandler

class MyHandler(SimpleHTTPRequestHandler):
  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/html')
    self.end_headers()

    html = b"""
        <html>
        <body>
        <h1>Hello, World!</h1>
        </body>
        </html>
    """

    self.wfile.write(html)
 
server = http.server.HTTPServer(('', 8080), MyHandler)
server.serve_forever()