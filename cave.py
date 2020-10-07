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

player_items = ['Potion', 'Torch']

def use_item():
    slowprint('Do you want to use an item?')
    item_select = input('Y/N \n')
    if item_select == 'Y':
        print('Which item would you like to use?', player_items)
        selected_item = input('')
        if selected_item == 'Potion':
            player.hp += 10
            player_items.pop(0)
            slowprint(f"Your health has been regained! You are now at {player.hp} health")
            print(player_items)
    # elif item_select == 'N':
    #     pass

def death(player):
    if player.alive == False:
        slowprint('Game Over')

def cave():
    slowprint('You come across a cave deep in the forest, do you go into the cave?')
    cave_cont = input('Y/N \n')
    if cave_cont == 'Y':
        slowprint('As you descend the cave you hear a loud crash behind you, you look back to see that you are now trapped inside the cave. Do you panic?')
    elif cave_cont == 'N':
        slowprint('You continue deeper into the forrest')
    panic = input('Y/N \n')
    if panic == 'Y':
        player.alive = False
        slowprint('While you panice you fail to notice that you caused a rockslide. You inevitable end up dying.')
        death(player)
    elif panic == 'N':
        slowprint('You continue down the cave. Surpisingly the inside of the cave is well lit up. You come accross a stray dog. Do you stop to pet it?')
        pet_the_dog = input('Y/N \n')
        if pet_the_dog == 'Y':
            player.hp -= 5
            slowprint(f"You approach the dog, the dog seems friendly at first but as you reach out to pet the dog, it lashes out and bites you. You take some damage, you are now at {player.hp} health. The dog runs away and you are left with a bite mark on your hand but you don\'t think it\'s a big deal.")
            use_item()
            slowprint('You continue onward and you are bewildered as you notice that there is a market inside the cave.')
        elif pet_the_dog == 'N':
            slowprint('The dog wimpers and begs for attention but you pay it no mind. You continue onward and you are bewildered as you notice that there is a market inside the cave.')

cave()
