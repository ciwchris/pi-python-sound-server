#/usr/bin/python2.7
import Queue
import SimpleHTTPServer
import SocketServer
import sounddevice as sd
import numpy as np
import time
from threading import Thread
from urlparse import urlparse, parse_qs

q = Queue.Queue()
keys = {'a':439.0, 'b':389.0, 'c': 339.0, 'd': 289.0, 'e': 239.0, 'f': 189.0}

def getQuerystringValue(qs, key, defaultValue):
        return qs[key][0] if qs.has_key(key) else defaultValue

def worker():
    while True:
        qs = q.get()
        volume = float(getQuerystringValue(qs, "volume", 1.0))          # range [0.0, 1.0]
        duration = float(getQuerystringValue(qs, "length", 1.0))        # in seconds, may be float
#/usr/bin/python2.7
import Queue
import SimpleHTTPServer
import SocketServer
import sounddevice as sd
import numpy as np
import time
from threading import Thread
from urlparse import urlparse, parse_qs

q = Queue.Queue()
keys = {'a':439.0, 'b':389.0, 'c': 339.0, 'd': 289.0, 'e': 239.0, 'f': 189.0}

def getQuerystringValue(qs, key, defaultValue):
        return qs[key][0] if qs.has_key(key) else defaultValue

def worker():
    while True:
        qs = q.get()
        volume = float(getQuerystringValue(qs, "volume", 1.0))          # range [0.0, 1.0]
        duration = float(getQuerystringValue(qs, "length", 1.0))        # in seconds, may be float
        f = keys[getQuerystringValue(qs, "key", 'a')]                   # sine frequency, Hz, may be float
        fs = 44100                                                      # sampling rate, Hz, must be integer

        sample = (np.sin(2*np.pi*np.arange(fs*duration)*f/fs)).astype(np.float32)
        sd.play(volume*sample, fs)
        q.task_done()

class Server(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        qs = parse_qs(urlparse(self.path).query)
        q.put(qs)
        self.protocol_version='HTTP/1.1'
        self.send_response(200, 'OK')
        self.send_header('Content-type', 'text/html')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(bytes("Played"))


def serve_forever(port):
    try:
        SocketServer.TCPServer(('', port), Server).serve_forever()
    except KeyboardInterrupt:
        print("exit")

if __name__ == "__main__":
    t = Thread(target=worker)
    t.daemon = True
    t.start()
    SocketServer.TCPServer.allow_reuse_address = True
    serve_forever(8000)

