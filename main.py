import sys
import time
from os import system, name
<<<<<<< HEAD
import players
=======
>>>>>>> c6e8be6493c54ec6d50f9992f1ffcf7cac3e34c6

def slowprint(str):
  for letter in str + '\n':
    sys.stdout.write(letter)
    sys.stdout.flush()
<<<<<<< HEAD
    time.sleep(2/60)
=======
    time.sleep(1./60)
>>>>>>> c6e8be6493c54ec6d50f9992f1ffcf7cac3e34c6
def clear():
    _ = system('clear')


player = players.Player()

clear()
slowprint("'Hey you, you’re finally awake. You were trying to cross the border right? Walked right into that Imperial ambush same as us and that thief over there. \n ........ \n ........ \n ........\n ........ \n'What's your name anyway?'")

player.name = input('')
slowprint(f"'{player.name} is it? Well you better get comfy, were in for a long ride to our deaths. Dont suppose I'll remember your name, the Imperials will have our heads soon.' \n\n")
