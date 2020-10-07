import sys
import time
from os import system, name
import players

def slowprint(str):
  for letter in str + '\n':
    sys.stdout.write(letter)
    sys.stdout.flush()
    time.sleep(1./60)
def clear():
    _ = system('clear')

clear()
player = players.Player()

def use_item():
    slowprint('Do you want to use an item?')
    item_select = input('Y/N \n').upper()
    if item_select == 'Y':
        print('Which item would you like to use?', player.items)
        selected_item = int(input(''))
        if selected_item == 1:
            player.hp += 10
            player.items.pop(1)
            slowprint(f"Your health has been regained! You are now at {player.hp} health")
            # print(player.items)
        elif selected_item == 2:
            slowprint("It does nothing to help you... \n You have wasted a torch")
            player.items.pop(2)
        elif selected_item == 3:
            slowprint('You take out your Coin purse to inspect it. You fumble the coin purse and drop all of your gold...\n way to go loser')
            player.items.pop(3)
    # elif item_select == 'N':
    #     pass

def death(player):
    if player.alive == False:
        slowprint('Game Over')
        exit()

def cave():
    slowprint('You come across a cave deep in the forest, do you go into the cave?')
    cave_cont = input('Y/N \n').upper()
    if cave_cont == 'Y':
        slowprint('As you descend the cave you hear a loud crash behind you, you look back to see that you are now trapped inside the cave. Do you panic?')
    elif cave_cont == 'N':
        slowprint('You continue deeper into the forrest')
    panic = input('Y/N \n').upper()
    if panic == 'Y':
        player.alive = False
        slowprint('While you panick you fail to notice that you caused a rockslide. You inevitable end up dying.')
        death(player)
    elif panic == 'N':
        slowprint('You continue down the cave. Surpisingly the inside of the cave is well lit up. You come accross a stray dog. Do you stop to pet it?')
        pet_the_dog = input('Y/N \n').upper()
        if pet_the_dog == 'Y':
            player.hp -= 5
            slowprint(f"You approach the dog, the dog seems friendly at first but as you reach out to pet the dog, it lashes out and bites you. You take some damage, you are now at {player.hp} health. The dog runs away and you are left with a bite mark on your hand but you don\'t think it\'s a big deal.")
            use_item()
            if player.items == {1: 'Potion', 2: 'Torch'}:
                slowprint('You begrudgingly continue downward. As you walk the ground beneath you begins to crumble and you fall into the abyss')
            else:
                slowprint('You continue onward and as you walk the ground beneath you begins to crumble and you fall into the abyss')
        elif pet_the_dog == 'N':
            slowprint('The dog wimpers and begs for attention but you pay it no mind. You continue onward and as you walk the ground beneath you begins to crumble and you fall into the abyss')

cave()
