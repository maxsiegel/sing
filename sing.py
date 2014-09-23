from IPython.parallel import Client
from IPython.parallel import interactive
import subprocess as sp
rc = Client()
engines = rc[:]

voice1 = 'Fred'

def load_lyrics(song):
    with open(song) as f:
        lyrics = f.readlines()
        lyrics = [l.strip('\n') for l in lyrics]
        lyrics = [l for l in lyrics if l]
        
    return lyrics

def do_song(song):
    lyrics = load_lyrics(song)
    for line in lyrics:
        say(line + '.')

def say(t):
    sp.call(['say', '-v', voice1, t])


# parallel part for choruses
@interactive
def isay(t, voice=voice1):
    import subprocess as sp
    sp.call(['say', '-v', voice, t])

def say_parallel(lines, voices=voice1):
    assert isinstance(lines, list)

    if len(voices) == 1:
        engines['voice1'] = voice1
    elif len(voices) == len(lines):
        engines.map_sync(isay, lines, voices)
