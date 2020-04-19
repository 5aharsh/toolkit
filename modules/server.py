import http.server
import socketserver

class Server:
    def __init__(self):
        self.handler = http.server.SimpleHTTPRequestHandler

    def run(self, port):
        with socketserver.TCPServer(("", port), self.handler) as httpd:
            print("Starting the server...")
            print("\nReady at:\n http://127.0.0.1:"+str(port))
            print("\nCTRL-C to quit the server")
            httpd.serve_forever()