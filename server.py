import http.server
import logging
import socketserver

PORT = 8000

logging.basicConfig(level=logging.DEBUG)

class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write('Python is running...'.encode("utf-8"))

with socketserver.TCPServer(('', PORT), Handler) as httpd:
    logging.info('Serving at port %s', PORT)
    httpd.serve_forever()
