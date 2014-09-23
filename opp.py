from sing import *

voice1 = 'Fred'

voices = [voice1, 'Junior', 'Alfred']

lyrics = load_lyrics('opp')

for n, line in enumerate(lyrics):
    print n % 2
    if n % 2 == 1:
        dup = [line for v in voices]
        say_parallel(dup, voices)
    else:
        say(line)




