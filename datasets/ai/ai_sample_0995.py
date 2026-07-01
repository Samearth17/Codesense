import http.server
import datetime

port = 8888

class MyHandler(http.server.BaseHTTPRequestHandler):
 def do_GET(self):
 self.send_response(200)
 self.send_header('Content-type', 'text/html')
 self.end_headers()
 self.wfile.write(("""
<html>
 <head>
 <title>Static page</title>
 </head>
 <body>
 <p>The time is: {}</p>
 </body>
</html>
""".format(datetime.datetime.now())).encode())

try:
 server = http.server.HTTPServer(('', port), MyHandler)
 print('Server running at localhost:{}'.format(port))
 server.serve_forever()
except KeyboardInterrupt:
 print('\nServer stopped')
 server.socket.close()