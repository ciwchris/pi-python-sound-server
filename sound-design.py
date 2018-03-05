import sounddevice as sd
import soundfile as sf
import time

data, samplerate = sf.read('./E_major_piano.ogg.ogx')
sd.play(data)

time.sleep(8)
