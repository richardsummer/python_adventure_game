import sys
import time
from os import system, name

def slowprint(str):
  for letter in str + '\n':
    sys.stdout.write(letter)
    sys.stdout.flush()
    time.sleep(1./60)
def clear():
    _ = system('clear')

clear()
def cave():
    slowprint('You come across a cave deep in the forest, do you go into the cave?')
    cave_cont = input('Y/N \n')
    if cave_cont == 'Y':
        slowprint('As you descend the cave you hear a loud crash behind you, you look back to see that you are now trapped inside the cave. Do you panic?')
    elif cave_cont == 'N':
        slowprint('You continue deeper into the forrest')
    panic = input('Y/N \n')
    if panic == 'Y':
        slowprint('While you panice you fail to notice that you caused a rockslide. You inevitable end up dying.')
    elif panic == 'N':
        slowprint('You continue down the cave and to your surprise you notice that there is a market inside the cave.')

cave()
