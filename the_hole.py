import sys
import time
from os import system, name
import players
from pyfiglet import Figlet

def slowprint(str):
  for letter in str + '\n':
    sys.stdout.write(letter)
    sys.stdout.flush()
    time.sleep(1/60)

def slowerprint(str):
  for letter in str + '\n':
    sys.stdout.write(letter)
    sys.stdout.flush()
    time.sleep(1/15)

def clear():
    _ = system('clear')

banner = Figlet(font='roman')

player = players.Player()

clear()

# dev tools
# isRope = input('Did you pack a rope? Y/N: ').upper()
# if isRope == 'N':
#     player.items.pop('Rope', None)
# if isRope == 'Y':
#     player.items.append('Rope')
#
# isTorch = input('And did you pack a torch? Y/N: ').upper()
# if isTorch == 'N':
#     player.items.pop('Torch', None)
#
# print(player.items)

# -----------------------------------------------------------------------------

def the_mineshaft():
    slowprint('\n\n\n')
    slowprint('You follow the stream deeper into the cave. Twisting around corners and bends, you follow it for what seems like forever. Eventually you come upon an old mineshaft.')
    slowprint('\nIt looks as if it hasn\'t been used in ages, maybe even centuries. You stop to observe the entrance, afraid of what might be inside.')
    slowprint('There are markings surrounding the threshold, and and cobwebs full of small spiders covering a small alcove just inside the entrance to the mineshaft.')
    if 'Scroll' in player.items:
        slowprint('\n** You notice the markings are vaguely similar to the scroll you found on the lakeshore. **\n')
    slowprint('You are desperate to find a way out, so you decide to press on into the mineshaft. You stop at the small alcove covered in cobwebs for a moment. Would you like to go inside?')
    player_ipt = input('Y/N: ').upper()
    if player_ipt == 'Y':
        slowprint('You burn away the cobwebs with your torch, revealing what appears to be living quarters.')
        slowprint('There are a few skeletons propped against the walls and laying against a set of chairs.')
        slowprint('Walking into the room, you find a small stone tablet with markings covering it. Alongside those markings are translations to an archaic version of your native tongue.\n')
        player.items.append('Rosetta Stone')
        slowerprint('You\'ve found a Rosetta Stone!')
        print(player.items)
        if 'Scroll' in player.items:
            slowprint('\nYou remember the scroll you found in the lake. Hurriedly, you scramble through your bag to find it and decipher the text and markings within.\n')
            slowerprint("CLARITY CAN BE FOUND WITHIN: READ THIS SCROLL WHEN IN DANGER TO FIND YOUR PATH TO SAFETY")
            player.items.pop('Scroll')
            player.items.append('Scroll of Clarity')
            slowprint('You got the Scroll of Clarity!')
            print(player.items)
        else:
            slowprint('You think the markings on the threshold are similar to the ones on the tablet, but you\'re not quite sure what to use this for. You store it for later.')
    slowprint('You slowly find your way down the mineshaft corridor, when suddenly, your torch burns out')
    player.items.remove('Torch')
    slowprint('You are shrouded in darkness, painfully aware of every bump and creak in the mineshaft supports.')
    slowprint('Behind you, you can hear a faint clicking noise, and what sounds like nails on a chalkboard.')
    slowerprint('What do you do now?')
    player_action = input('run // use item // nothing\n').lower()
    if player_action == 'run':
        slowprint('You flee the creature, running until you have no room left to run. The creature is biting at your heels the entire way, eventually cornering you and killing you.')
        exit()
    if player_action == 'nothing':
        slowprint('Your nihilism and apathy take hold and you choose to surrender your fate to the creature. It doesn\'t exhibit any remorse as it horrendously devours your motionless body.')
        exit()
    if player_action == 'use item':
        print(player.items)
        item_action = input('Which item would you like to use? ')
        item_action.title()
        while item_action not in player.items:
            slowprint('\nYou do not have that item in your bag.')
            print(player.items)
            item_action = input('Which item would you like to use? ')

        if item_action == 'Potion':
            slowprint('\nYou drink a health potion and restore 25 health.')
            slowprint('While drinking the potoin, the creature attacks you, ending your adventure.')
            exit()
        elif item_action == 'Torch':
            slowprint('\nYou light a new torch, revealing the source of the awful noises. It is a man-sized spider which recoils at the bright torch in your hand. You aggressively wave it in the spiders direction, scaring it off. Relieved to have survived the spider encounter, you venture further into the mineshaft...cautiously.')
            slowprint('The mineshaft leads you around corners and bends to a large room with a freight elevator in it.')
            slowprint('You pull the lever at the base of the elevator, rising up into the bright light, to safety.')
            slowerprint('\n . \n . \n . \n . \nAfter what seems like an eternity you surface in a clearing. The dark forest behind you.')
            slowprint('Relieved to have survived the forest, you walk free to continue on with your life, leaving your adventure behind.')

            print('\n')
            print(banner.renderText('Congratulations!'))
            print('\n\n')
            slowprint('Run the file "forest.py" again if you\'d like to go on another adventure.')
            exit()
        elif item_action == 'Rope':
            slowprint('\nYou pull out your rope, creating a lasso like you\'re trying to wrangle the creature threatening you. Because you can\'t see a thing you miss and are slaughtered by the mysterious beast.')
            exit()
        elif item_action == 'Medicine':
            slowprint('\nYou pull out your medicine from the goblin market. It does nothing but calm your nerves. The creature attacks while you are sealing the medicine, killing you.')
            exit()
        elif item_action == 'Pickaxe':
            slowprint('\nYou wield your pickaxe, but still can\'t see what is threatening you. You swing wildly, damaging the beast but miss your follow up strike. The beast uses this opportunity to maul you, ending your adventure.')
            exit()
        elif item_action == 'Rosetta Stone':
            slowprint('\nYou toss the Rosetta Stone at the monster. It does nothing. You are violently murdered.')
            exit()
        elif item_action == 'Scroll of Clarity':
            slowprint('\nYou remember the words inscribed on the Scroll, and hurriedly search your bag for it. You unravel the scroll and immediately the mineshaft is filled with a blinding bright light emanating from the scroll. The creature is revealed to be a massive spider, which recoils at the power of the Scroll. It scurries away to whatever hole it came from.')
            slowprint('Along the mineshaft corridor you can see magical markers lighting your way out. You follow it around the maze-like mineshaft until you are guided to a large frieght elevator. This might be your way out of this hole, out of this forest.')
            slowprint('\n')
            slowprint('You pull the lever at the base of the elevator, rising up into the bright light, to safety.')
            slowerprint('\n . \n . \n . \n . \nAfter what seems like an eternity you surface in a clearing. The dark forest behind you.')
            slowprint('Relieved to have survived the forest, you walk free to continue on with your life, leaving your adventure behind.')

            print('\n')
            print(banner.renderText('Congratulations!'))
            print('\n\n')
            slowprint('Run the file "forest.py" again if you\'d like to go on another adventure.')
            exit()


def the_lake():
    slowprint('\n\n\n')
    slowprint('Remembering your rope, you pass it through the hole in the wall. You just barely squeeze through and are greeted with a vast underground lake, mutliple stories below you.')
    slowprint('Scaling down the rock wall you just passed through, you eventually reach the surface of the lake. It\'s shallower than you expected, and you are able to stand, the water barely covering your shins.')
    slowprint('On the lake shore is a bright, shining object, and you are immediately drawn to it.')
    slowprint('You wade through the water and eventually reach the shore, discovering an open chest, glowing with potential.\n')
    slowerprint('Inside the chest is a plain, nondescript scroll. Unraveling the scroll reveals it is written in some ancient language, full of markings and symbols. You decide to store the scroll for later, although you\'re not sure what to use it for.')
    player.items.append('Scroll')
    slowerprint('You\'ve obtained a Scroll!')
    print(player.items)
    slowprint('\n\n')
    slowprint('You return to the rope and slowly climb back up it, unsure of where to go next.')
    player_move = input('Which way do you go now? ')
    if player_move == 'left':
        while player_move == 'left':
            slowprint('Why would you go that way? You just came from there')
            player_move = input('Which way do you go now? ')
    if player_move == 'right':
        the_mineshaft()

def the_hole():
    player_move = ''
    slowprint('\nYou slowly come to, not sure of where or when you are.\n\nSitting up, you are disoriented by the ringing in your head, most likely from the fall. It seems that you should be more careful next time you go spelunking.')
    slowprint('\nStill foggy-headed, you realize you can\'t see a thing.')
    if 'Torch' in player.items:
        slowprint('\nYou light a torch, illuminating the small room. You see damp rock walls, covered in moss and mildew, and to your right, a small stream ahead of you leading further into the cave. Looking to your left, you see a crack in the rocks, just barely big enough for a person to fit through...\nMaybe.\nJust behind where you landed is a bottomless pit.\nWhich way do you go?')
        player_move = input('').lower()
        if player_move == 'left':
            slowprint('\nYou pass on going deeper into the cave, contemplating still whether a person could fit through the hole in the rock wall. You skipped a few meals this morning, so if you suck in your stomach and position just the right way, you think you could do it.\nYou\'re unsure what\'s on the other side of the wall. Do you investigate further?')
            player_ipt = input('Y/N: ').upper()
            if player_ipt == 'Y':
                slowprint('The torch barely illuminates through the crack in the rock wall; you can make out the sound of running water, and what sounds like an item in a video game that would help you out. Unfortunately you can\'t see anything through the crack, as if there were just emptiness on the other side. Do you continue anyways?')
                player_ipt = input('Y/N: ').upper()
                if player_ipt =='Y':
                    if 'Rope' in player.items:
                        the_lake()
                    else:
                        slowprint('You squeeze through the crack in the wall, heeding slightly more caution. You lose your balance as theres no solid ground on the other side and you fall multiple stories into a shallow lake and break all the bones in your body. The promise of treasure and items curses you to death.')
                        exit()
                elif player_ipt =='N':
                    player_move = input('Which way do you go now? ')
                    while player_move == 'left':
                        slowprint('Why would you go that way? You just came from there')
                        player_move = input('Which way do you go now? ')
            elif player_ipt == 'N':
                slowprint('How dangerous could a hole in the wall be anyways? Do you attempt to fit through?')
                player_ipt = input('Y/N ').upper()
                if player_ipt == 'Y':
                    if 'Rope' in player.items:
                        the_lake()
                    else:
                        slowprint('You squeeze through the crack in the wall, confident you\'ve made the right choice. You lose your balance as theres no solid ground on the other side and you fall multiple stories into a shallow lake and horribly die from the impact. Ignorance spells your demise.')
                        exit()
                elif player_ipt == 'N':
                    player_move = input('Which way do you go now? ')
                    while player_move == 'left':
                        slowprint('Why would you go that way? You just came from there')
                        player_move = input('Which way do you go now? ')
        if player_move == 'right':
            the_mineshaft()

    if player_move == 'backwards' or player_move == 'behind' or 'Torch' not in player.items:
        if 'Torch' in player.items:
            slowprint('For some ungodly reason, you decide to go into the bottomless pit behind you. Way to go stupid. You fall forever and are stuck in a Lovecraftian horror of never dying but never living at all.')
            exit()
        slowprint('You fumble around in your bag, searching for a torch. You can\'t find one and resort to feeling your way around in the dark.')
        slowprint('\n\n')
        slowerprint('While stumbling around, you find yet another hole and fall down a bottomless pit to your death.')
        exit()



#the_mineshaft()
