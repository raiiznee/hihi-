import sys
from time import sleep
import time

def print_lyrics():
    lines = [
        ("And if a double decker bus", 0.1, False),
        ("crashes into us", 0.13, False),
        ("to die by yourside", 0.1, False),
        ("is such a heavenly way to die", 0.13, False),
        ("And if ten ton truck kills the both of us", 0.07, False),
        
        ("to die by your side ", 0.1, False),
        ("well, the pleasure, the privilege is mine", 0.1, False),
  ]

    delays = [0.8, 1, 0.5, 0.13, 2.7, 0.5, 1.5, 0.8, 
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