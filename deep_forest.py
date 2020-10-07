import sys
import time
from os import system, name
import players
import cave
import market


def slowprint(str):
  for letter in str + '\n':
    sys.stdout.write(letter)
    sys.stdout.flush()
    time.sleep(1./60)
def clear():
    _ = system('clear')

clear()

player = players.Player()

def death(player):
    if player.alive == False:
        slowprint('Game Over')
        exit()

def deepForest():
    slowprint('''It is very dark here and the forest is even more dense.

    To make matters worse, you haven't had water in days.

    Would you like to proceed into the forest?
    ''')
    forest_cont = input('Y/N \n')
    if forest_cont == 'Y':
        slowprint('You come to an old well. Drink out of the well?')
        drink_well = input('Y/N \n')
    elif forest_cont == 'N':
        cave.cave()
    if drink_well == 'Y':
        slowprint('The water was poisoned. You died!')
        player.alive = False
        death(player)
    elif drink_well == 'N':
        slowprint('You are too good for well water. Continue walking?')
    cont_walk = input('Y/N \n')
    if cont_walk == 'Y':
        slowprint('You see a dark silhouette in the distance. Go towards it?')
    elif cont_walk == 'N':
        slowprint('You decide to sit in the middle of a dark forest with no water. You died... and probably deserved to.')
        player.alive = False
        death(player)
    walk_toward = input('Y/N \n')
    if walk_toward == 'Y':
        slowprint('It is a town guard! He helps you out of the dark forest and takes you to the market!')
        market.market()
    elif walk_toward == "N":
        slowprint('You run away from the mysterious figure and find yourself back at the cave!')
        cave.cave()


deepForest()
