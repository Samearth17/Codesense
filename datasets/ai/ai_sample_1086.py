"""
from http.server import HTTPServer, BaseHTTPRequestHandler

class MyServer(HTTPServer):
    def __init__(self, server_address, handler_class):
        super().__init__(server_address, handler_class)

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response_only(200)
        self.end_headers()
        self.wfile.write("Hello, world!".encode("utf-8"))

if __name__=="__main__":
    HOST, PORT = "localhost", 8002

    server = MyServer((HOST, PORT), MyHandler)
    print("Start server at http://{}:{}".format(HOST, PORT))
    server.serve_forever()
"""