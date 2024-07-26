from http.server import HTTPServer, BaseHTTPRequestHandler
import time

HOST = "localhost"  # IP address
PORT = 8888

class NeauralHTTP(BaseHTTPRequestHandler):
    
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        
        self.wfile.write(bytes("<html><body><h1>TEXT HERE!</h1></body></html>", "utf-8"))
        
    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        response = bytes(f'{{"time": "{date}"}}', "utf-8")
        self.wfile.write(response)

server = HTTPServer((HOST, PORT), NeauralHTTP)

print("Server running")
server.serve_forever()
server.server_close()
print("Server stopped")