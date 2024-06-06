from http.server import SimpleHTTPRequestHandler, HTTPServer

host = '0.0.0.0'
port = 9999

server = HTTPServer((host, port), SimpleHTTPRequestHandler)
print(f"Starting server at http://{host}:{port}")
server.serve_forever()