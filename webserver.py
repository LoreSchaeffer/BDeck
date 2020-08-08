import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from threading import Thread
from urllib.parse import parse_qs
from buttons import ButtonEncoder

config = None


class RequestHandler(BaseHTTPRequestHandler):

    def send(self, code, message):
        self.send_response(code)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        if message is not None:
            self.wfile.write(bytes(message, "utf8"))

    def do_GET(self):
        args = None
        if "?" in self.path:
            path = self.path.split("?")[0]
            args = parse_qs(self.path.split("?")[1])
        else:
            path = self.path

        if path == "/button":
            if "btn" not in args:
                self.send(401, '{"error": "Invalid request"}')
            else:
                print(args)
                self.send(200, json.dumps(config.get_button(args["btn"][0]), cls=ButtonEncoder))
        else:
            self.send(404, None)

    def do_POST(self):
        self.send(200, '{"post": "POST"}')


class WebServer(Thread):

    def __init__(self, host, port, cfg):
        global config
        Thread.__init__(self)
        self.host = host
        self.port = port
        config = cfg

    def run(self):
        httpd = HTTPServer((self.host, self.port), RequestHandler)
        httpd.serve_forever()
