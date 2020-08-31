import http.server
from urllib.parse import urlparse, parse_qs
import os

config = { "host": "127.0.0.1", "port": 9797 }

class testHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
  def do_GET(self):
    print("GET {}".format( self.path ) )
    parsedPath = parse_qs( urlparse(self.path).query )
    print( "PATH {}".format(parsedPath) )
    self.send_response(200)
    self.send_header('Content-type','text-html')
    self.end_headers()
    return

  def do_POST(self):
    print("POST {}".format( self.path ) )
    contentLen = int(self.headers.get('Content-Length'))
    postBody = self.rfile.read(contentLen)
    print( "BODY {}".format(postBody) )
    self.send_response(200)
    self.send_header('Content-type','text-html')
    self.end_headers()
    return

def run():
  httpd = http.server.HTTPServer((config["host"], config["port"]), testHTTPRequestHandler)
  print('http server is running...')
  httpd.serve_forever()

if __name__ == '__main__':
  run()
