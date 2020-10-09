import sys
import time
from os import system, name
import players
import cave
import deep_forest

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


def forest():
    slowprint ("The first thing you see as you enter the forest is a rabbit.")
    slowprint ("He's signaling for you to come follow him. Do you want to follow him?")
    forest_cont = input('Y/N\n').upper()
    if forest_cont == 'Y':
        slowprint ("You follow the rabbit and he leads you to a cave. Do you wish to continue?")
        forest_cave = input('Y/N\n').upper()
        if forest_cave == 'Y':
            slowprint ("Good luck!")
            cave.cave()
        elif forest_cave == 'N':
            slowprint ("You kill the rabbit because you don't trust him.")
            cave.cave()
    elif forest_cont == 'N':
        slowprint ("Go in the opposite direction.")
        slowprint ("You happen to stumble upon an old abandoned house. Should you enter?")
        forest_house = input('Y/N\n').upper()
        if forest_house == 'Y':
            slowprint ("You explore the house and come across a crest with gold coins.")
            slowprint ("You ponder if you should take the coins or leave them there. Should you take them?")
            forest_coins = input('Y/N\n').upper()
            if forest_coins == 'Y':
                slowprint ("You pick up the coins and place them in your bag.")
                slowprint ("You continue to explore the house and in the hallway, you see two doors. Do you want to enter door A or door B?")
                house_door = input('A/B\n').upper()
                if house_door == 'A':
                    slowprint ("This leads you outside and you go deeper into the forest")
                    deep_forest.deepForest()
                if house_door == 'B':
                    slowprint ("There is a bear in this room and he kills you.")
            elif forest_coins == 'N':
                slowprint ("You leave them there and exit the house to go deeper into the forest.")
                deep_forest.deepForest()
        elif forest_house == 'N':
            slowprint ("Continue to go deeper into the forest.")
            deep_forest.deepForest()

forest()
