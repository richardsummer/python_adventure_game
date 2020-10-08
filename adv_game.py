import sys
import time
from os import system, name
import deep_forest
import cave

def slowprint(str):
  for letter in str + '\n':
    sys.stdout.write(letter)
    sys.stdout.flush()
    time.sleep(1./60)
def clear():
    _ = system('clear')

yes_no = ["yes", "no"]


slowprint ("Greetings. You seem like the adventurous type.")
slowprint ("Let's go on an adveture through the forest.")

#after entering forest
def forest():
    slowprint ("The first thing you see as you enter the forest is a rabbit.")
    slowprint ("He's signaling for you to come follow him. Do you want to follow him?")
    forest_cont = input ('Y/N\n')
    if forest_cont == 'Y':
        slowprint ("You follow the rabbit and he leads you to a cave. Do you want to enter?")
        forest_cave = input ('Y/N\n')
        if forest_cave == 'Y':
            slowprint ("Good luck!")
        elif forest_cave == 'N':
            slowprint ("Go in the opposite direction.")

    elif forest_cont == 'N':
        slowprint ("Go in the opposite direction.")
        slowprint ("You happen to stumble upon an old abandoned house. Should you enter?")
        forest_house = input ('Y/N\n')
        if forest_house == 'Y':
            slowprint ("You explore the house and come across a crest with gold coins.")
            slowprint ("You ponder if you should take the coins or leave them there. Should you take them?")
            forest_coins = input ('Y/N\n')
            if forest_coins == 'Y':
                slowprint ("You pick up the coins, but their laced with a poisonous material and you die.")
            elif forest_coins == 'N':
                slowprint ("You leave them there and exit the house to go deeper into the forest.")
        elif forest_house == 'N':
            slowprint ("Continue to go deeper into the forest.")
            deep_forest.deepForest()

forest()
