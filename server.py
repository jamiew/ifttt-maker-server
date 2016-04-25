from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer
import simplejson
import random

class IFTTT(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        f = open("index.html", "r")
        self.wfile.write(f.read())

    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        self._set_headers()
        data_string = self.rfile.read(int(self.headers['Content-Length']))

        self.send_response(200)
        self.end_headers()

        data = simplejson.loads(data_string)
        print simplejson.dumps(data)

        # TODO save to individual files, or god forbid, a database
        with open("last-post.json", "w") as outfile:
            simplejson.dump(data, outfile)

        # f = open("for_presen.py")
        # self.wfile.write(f.read())
        return


def run(port=9090):
    server_address = ('', port)
    httpd = HTTPServer(server_address, IFTTT)
    print 'Starting httpd on port ' + str(port) + '...'
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

if len(argv) == 2:
    run(port=int(argv[1]))
else:
    run()
