import http.server

class myHandler(http.server.BaseHTTPRequestHandler):
	def do_GET(self):
		if self.path == '/page1':
			self.send_response(200)
			self.end_headers()
			self.wfile.write(b"This is page 1")
		elif self.path == '/page2':
			self.send_response(200)
			self.end_headers()
			self.wfile.write(b"This is page 2")
		else:
			self.send_error(404)

httpd = http.server.HTTPServer(('0.0.0.0',8080), myHandler)
httpd.serve_forever()