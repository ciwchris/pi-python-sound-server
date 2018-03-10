Play sound
----------

In a text editor enter the following Python script and save the file as `simple-sound.py`:

```
import sounddevice as sd
import soundfile as sf
import time

data, samplerate = sf.read('./E_major_piano.ogg.ogx')
sd.play(data, samplerate)

time.sleep(8)
```

Download sound file and save it in the same directory as `simple-sound.py`:
[E_major_piano.ogg](https://upload.wikimedia.org/wikipedia/commons/6/6f/E_major_piano.ogg)

In a terminal run the python program: `python simple-sound.py`

Web server
----------

In a text editor enter the following text and save the file as `index.html`:

```
Hello from Pi
```

In a terminal run a simple developer web server:

```
python -m SimpleHTTPServer
```

Navigate to [http://localhost:8000](http://localhost:8000)

To stop the server type: `Ctrl+c`

Web server with content
-----------------------

In a text editor enter the following Python script and save the file as `server.py`:

```
import SimpleHTTPServer
import SocketServer

class Server(SimpleHTTPServer.SimpleHTTPRequestHandler):
        def do_GET(self):
                self.protocol_version='HTTP/1.1'
                self.send_response(200, 'OK')
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write("Hello from PI")


def serve_forever(port):
        SocketServer.TCPServer(('', port), Server).serve_forever()

if __name__ == "__main__":
    SocketServer.TCPServer.allow_reuse_address = True
    serve_forever(8080)
```

In a terminal start the web server by running the script: `python server.py`


Navigate to [http://localhost:8080](http://localhost:8080)

The text we told the script to write out will be displayed: "Hello from PI"

To stop the server type: `Ctrl+c`

Play sound in web server
------------------------

Instead of playing a sound file the web server will be updated to play a tone. An equation based on
a sin wave will be used to play the tone. In a text editor update `server.py` to include:

```
import SimpleHTTPServer
import SocketServer
import sounddevice as sd
import numpy as np

class Server(SimpleHTTPServer.SimpleHTTPRequestHandler):
        def do_GET(self):
                volume = 1.0          # range [0.0, 1.0]
                duration = 1.0        # in seconds, may be float
                f = 189.0             # sin frequency, Hz, may be float
                fs = 44100            # sampling rate, Hz, must be integer

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
    SocketServer.TCPServer(('', port), Server).serve_forever()

if __name__ == "__main__":
    SocketServer.TCPServer.allow_reuse_address = True
    serve_forever(8080)
```

In a terminal start the web server by running the script: `python server.py`

To play the sound navigate to [http://localhost:8080](http://localhost:8080)

To stop the server type: `Ctrl+c`

Play sound from web page
------------------------


In a text editor update `index.html` to include:

```
<!DOCTYPE html>
<html>
    <body>
        <button onclick="play()">Play</button>
        <script>
            function play() {
                fetch('http://localhost:8080');
            }
        </script>
    </body>
</html>
```

In a terminal run the developer web server for the `index.html` page:

```
python -m SimpleHTTPServer
```

In another terminal start the web server to play sounds by running the script: `python server.py`

Navigate to [http://localhost:8000](http://localhost:8000)

Click the button to play the sound

To stop the servers in each terminal type: `Ctrl+c`

Complete application
--------------------

In a text editor update `index.html` to include the [content from
here](https://raw.githubusercontent.com/ciwchris/pi-python-sound-server/master/index.html)

In a text editor update `server.py` to include the [content from
here](https://raw.githubusercontent.com/ciwchris/pi-python-sound-server/master/server.py)

In a terminal run a simple developer web server for the index.html page:

```
python -m SimpleHTTPServer
```

In another terminal start the web server to play sounds by running the script: `python server.py`

Navigate to [http://localhost:8000](http://localhost:8000)

Click the buttons to play the sounds

To stop the servers in each terminal type: `Ctrl+c`
