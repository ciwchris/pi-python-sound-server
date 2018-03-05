#/usr/bin/python2.7
import SimpleHTTPServer
import SocketServer
import sounddevice as sd
import numpy as np

class Server(SimpleHTTPServer.SimpleHTTPRequestHandler):
        def do_GET(self):
                volume = 1.0          # range [0.0, 1.0]
                duration = 1.0        # in seconds, may be float
                f = 189.0             # sine frequency, Hz, may be float
                fs = 44100            # sampling rate, Hz, must be integer

                sample = (np.sin(2*np.pi*np.arange(fs*duration)*f/fs)).astype(np.float32)
                sd.play(volume*sample, fs)

                self.protocol_version='HTTP/1.1'
                self.send_response(200, 'OK')
                self.send_header('Content-type', 'text/html')
                self.send_header('Cache-Control', 'no-cache')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(bytes("Played"))


def serve_forever(port):
    SocketServer.TCPServer(('', port), Server).serve_forever()

if __name__ == "__main__":
    SocketServer.TCPServer.allow_reuse_address = True
    serve_forever(8080)

