import http.server
import socketserver
import os

class FriskyWebServer:
    def __init__(self, port=8000):
        self.port = port
        self.handler = http.server.SimpleHTTPRequestHandler
        self.current_dir = os.getcwd()
    
    def start(self):
        os.chdir(self.current_dir)
        with socketserver.TCPServer(("", self.port), self.handler) as httpd:
            print(f"Frisky Web Server running on http://localhost:{self.port}/")
            httpd.serve_forever()

    def generate_html(self, file_path, content):
        with open(file_path, "w") as file:
            file.write(content)

