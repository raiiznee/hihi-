import sys
from time import sleep
import time

def print_lyrics():
    lines = [
        ("Dumd conversation", 0.1, False),
        ("we lose track of time", 0.1, False),
        ("have i told you lately I'm grateful you're mine", 0.1, False),
        ("we'll watch The Notebook for the 17th time", 0.11, False),
        ("I'll say it's stupid", 0.11, False),
        ("Then you'll catch me crying", 0.07, False),
        
        ("We're not making out", 0.1, False),
        ("on a boat in the rain", 0.1, False),
        ("Or in a house I've painted blue", 0.08, False),
        ("but there's nothing", 0.11, True),
        ("like doing nothing", 0.13, False),
        ("With you", 0.13, True)
    ]

    delays = [0.8, 0.5, 0.5, 0.5, 0.7, 0.5, 0.5, 0.8, 
              0.8, 0.8, 1, 0.8, 0.8, 0.8, 5]

    for i, (line, char_delay, is_colored) in enumerate(lines):
        if is_colored:
            print("\033[91m", end='')  

        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)

        if is_colored:
            print("\033[0m", end='')  

        time.sleep(delays[i])
        print('')

print_lyrics()