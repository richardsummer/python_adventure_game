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
        print('Which item would you like to use? Type in either 0 or 1', player.items)
        selected_item = int(input(''))
        if selected_item == 0:
            player.hp += 10
            player.items.pop(0)
            slowprint(f"Your health has been regained! You are now at {player.hp} health")
            print('Items left: ', player.items)
        elif selected_item == 1:
            slowprint("It does nothing to help you... \n You have wasted a torch")
            player.items.pop(1)
            print('Items left: ', player.items)
        # elif selected_item == 'Gold':
        #     slowprint('You take out your Coin purse to inspect it. You fumble the coin purse and drop all of your gold...\n way to go loser')
        #     player.items.pop('Gold')
        #     print('Items left: ', player.items)

def market():
    slowprint('Goblins! You freak out but notice that they aren\'t attacking you.')
    slowprint('One of the goblin townsfolk approaches you and says "Welcome Traveler! Would you like to shop at our fine establishment? I noticed that bite mark on your hand, I have some medicine that could treat that."')
    slowprint('Would you like to shop?')
    shop = input('Y/N \n').upper()
    if shop == 'Y':
        shop_items = {'Torch': 25, 'Medicine': 50, 'Rope': 25, 'Pickaxe': 25}
        print('What would you like to buy?', shop_items)
        print('Your gold: ', player.gold)
        isShopping = True

        while isShopping is True or player.gold > 0:

            buy = input('Type in name of item you want to buy: ').title()
            if buy == 'Medicine' and player.gold >= 50:
                player.gold -= shop_items['Medicine']
                player.items.append('Medicine')
                print(player.gold)
                continueShopping = input('Do you want to continue shopping? Y or N: \n').upper()
                if continueShopping == 'N' or player.gold > 0:
                    slowprint('You better have spent all your money..')
                    isShopping = False
                    break
            elif buy == 'Torch' and player.gold >= 25:
                player.gold -= shop_items['Torch']
                player.items.append('Torch')
                print(player.gold)
                continueShopping = input('Do you want to continue shopping? Y or N: \n').upper()
                if continueShopping == 'N' or player.gold > 0:
                    slowprint('You better have spent all your money..')
                    isShopping = False
                    break
            elif buy == 'Rope':
                player.gold -= shop_items['Rope']
                player.items.append('Rope')
                print(player.gold)
                continueShopping = input('Do you want to continue shopping? Y or N: \n').upper()
                if continueShopping == 'N' or player.gold > 0:
                    slowprint('You better have spent all your money..')
                    isShopping = False
                    break
            elif buy == 'Pickaxe':
                player.gold -= shop_items['Pickaxe']
                player.items.append('Pickaxe')
                print(player.gold)
                continueShopping = input('Do you want to continue shopping? Y or N: \n').upper()
                if continueShopping == 'N' or player.gold > 0:
                    slowprint('You better have spent all your money..')
                    isShopping = False
                    break
            else:
                slowprint('You do not have enough gold for that.')
                print(player.items)
                break

def cave_path_1():
    slowprint('You igore all the signs to stay away from this path and march straight forward..')
    slowprint('The cave suddenly gets colder as you continue down this path and in the short distance you see a bear laying motionless on the cold cave floor.\n You aren\'t sure if it\'s alive or dead. \n There is a stick on the ground you could use. Do you check to see if it is alive?')
    check_bear_status = input('Y/N \n').upper()
    if check_bear_status == 'Y':
        slowprint('You grab a stick off the floor and proceed to poke the bear.. That wasn\'t a very good idea.. the bear now angry from being woken up from its slumber lunges at you..')
        player.alive = False
        death(player)
    if check_bear_status == 'N':
        slowprint('Smart choice! You decide to turn back but in the process you step on the stick *CRACK*. The stick breaks and the sound echoes throughout the cave inevitablely waking the bear up.')
        slowprint('Do you run?')
        run = input('Y/N \n').upper()
        if run == 'Y':
            slowprint('You run as fast as you can but you forget that bears can run up to 35 miles an hour so it quickly catches up to you.')
            player.alive = False
            death(player)
        if run == 'N':
            slowprint('You accept your fate.')
            player.alive = False
            death(player)


def cave_path_2():
    slowprint('You choose the middle path. To your surprise in the distance you see a market! But before you can continue foward a stray corgi approaches you. Do you stop to pet it?')
    pet_the_dog = input('Y/N \n').upper()
    if pet_the_dog == 'Y':
        player.hp -= 50
        slowprint(f"You approach the corgi, it seems friendly at first but as you reach out to pet it, it lashes out and bites you. Despite its small and innocent looks its bite packs a punch and you lose half your hp. You are now at {player.hp} health. The corgi runs away and you are left with a bite mark on your hand.")
        use_item()
        slowprint('You walk towards the market and notice the people there aren\'t human..')
        market()
        if 'Medicine' in player.items:
            slowprint('You drink the medicine that cures your rabies. You evade death.')
        else:
            player.alive = False
            slowprint('You forgot to buy the medicine! You slowly begin to lose consciousness.')
            death(player)
        if 'Pickaxe' in player.items:
            slowprint('You continue your adventure when you suddenly feel a small breeze. It is coming from a tiny crack in the wall.\n You remember your trusty pickaxe and you begin to excavate your way out.')
            #Richard/deep_forest
        else:
            slowprint('You continue your adventure when suddenly the ground beneath you starts to crumble. You fall into the abyss...')
            #Noelle/the_hole
    elif pet_the_dog == 'N':
        slowprint('The corgi wimpers and begs for attention but you pay it no mind. As you walk way the dog runs up and bites your hand! .. You shake it off and walk towards the market and notice the people there aren\'t human..')
        market()
        if 'Medicine' in player.items:
            slowprint('You drink the medicine that cures your rabies. You evade death.')
        else:
            player.alive = False
            slowprint('You forgot to buy the medicine! You slowly begin to lose consciousness.')
            death(player)
        if 'Pickaxe' in player.items:
            slowprint('You continue your adventure when you suddenly feel a small breeze. It is coming from a tiny crack in the wall.\n You remember your trusty pickaxe and you begin to excavate your way out.')
            #Richard/deep_forest
        else:
            slowprint('You continue your adventure when suddenly the ground beneath you starts to crumble. You fall into the abyss...')
            #Noelle/the_hole

def cave_path_3():
    slowprint('You choose the far right option. As you take one step forward the ground beneath you starts to crumble. You fall into the abyss..')
    #Noelle/the_hole


def death(player):
    if player.alive == False:
        slowprint('Oh? Looks like you died')
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
        slowprint('You continue down the cave until you come to a stopping point where the path divides into 3.')
        slowprint('Hint: Your spidey senses are tinglying telling you to stay AWAY from the left path')
        slowprint('Which path do you choose? The left, middle, or right?')
    path = input('').lower()
    if path == 'left':
        cave_path_1()
    elif path == 'middle':
        cave_path_2()
    elif path == 'right':
        cave_path_3()

# cave()
