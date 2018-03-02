PI Python Sound Server
======================

Play sounds on a PI by receiving requests through a web server running on the PI.

Installation
------------

- Runs under Python 2.7
- `pip install cffi`
- `apt-get install` (required by sounddesign)
    - libportaudio2 (PortAudio)
- `pip install`
    - numpy
    - sounddesign (requires 


Run
---

- Determine IP address: ` ifconfig wlan0 | grep "inet addr:"`
- Update `index.html` to use IP address found above
- Start web server to process sound requests (will use port 8080): `python server.py`
- Start web server to server file requests (will use port 8000): `python -m SimpleHTTPServer`
- Point your favorite browser at the IP of the web server serving file requests


