#!usr/bin/python2.7
import pyglet
from pyglet import media
from pyglet.media import procedural

player = media.Player()
player.play()

def main():
    print("in")
    source1 = procedural.Sine(0.5)
    source2 = procedural.Sine(0.5)
    player.queue(source1)
    player.queue(source2)

if __name__=="__main__":
    main()
    try:
        pyglet.app.run()
    except KeyboardInterrupt:
        print("exit")
