#/usr/bin/python2.7
import SimpleHTTPServer
import SocketServer
import sounddevice as sd
import numpy as np
from urlparse import urlparse, parse_qs
import socket
            
keys = {'a':439.0, 'b':389.0, 'c': 339.0, 'd': 289.0, 'e': 239.0, 'f': 189.0}
                
def getQuerystringValue(qs, key, defaultValue):
        return qs[key][0] if qs.has_key(key) else defaultValue
                
class Server(SimpleHTTPServer.SimpleHTTPRequestHandler):
        def do_GET(self):
                qs = parse_qs(urlparse(self.path).query)
                volume = float(getQuerystringValue(qs, "volume", 1.0))          # range [0.0, 1.0]
                duration = float(getQuerystringValue(qs, "length", 1.0))        # in seconds, may be float
                f = keys[getQuerystringValue(qs, "key", 'a')]                   # sin frequency, Hz, may be float
                fs = 44100                                                      # sampling rate, Hz, must be integer

                sample = (np.sin(2*np.pi*np.arange(fs*duration)*f/fs)).astype(np.float32)
                sd.play(volume*sample, fs)

                self.protocol_version='HTTP/1.1'
                self.send_response(200, 'OK')
                self.send_header('Content-type', 'text/html')
                self.send_header('Cache-Control', 'no-cache')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write("Played")


def serve_forever(port):
    try:
        print("Send requests to http://" + id_address() + ":" + str(port))
        SocketServer.TCPServer(('', port), Server).serve_forever()
    except KeyboardInterrupt:
        print("exit")

def id_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip

if __name__ == "__main__":
    SocketServer.TCPServer.allow_reuse_address = True
    serve_forever(8080)

