import sys
import time
from os import system, name
import players


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


player = players.Player()

clear()

# dev tools
isRope = input('Did you pack a rope? Y/N: ').upper()
if isRope == 'N':
    player.items.pop('Rope', None)
if isRope == 'Y':
    player.items.append('Rope')

isTorch = input('And did you pack a torch? Y/N: ').upper()
if isTorch == 'N':
    player.items.pop('Torch', None)

print(player.items)

# -----------------------------------------------------------------------------

def the_lake():
    slowprint('\n\n\n')
    slowprint('Remembering your rope, you pass it through the hole in the wall. You just barely squeeze through and are greeted with a vast underground lake, mutliple stories below you.')
    slowprint('Scaling down the rock wall you just passed through, you eventually reach the surface of the lake. It\'s shallower than you expected, and you are able to stand, the water barely covering your shins.')
    slowprint('On the lake shore is a bright, shining object, and you are immediately drawn to it.')
    slowprint('You wade through the water and eventually reach the shore, discovering an open chest, glowing with potential.\n')
    slowerprint('Inside the chest is a plain, nondescript scroll. Unraveling it reveals it is written in some foreign text. You decide to store the scroll for later.')
    player.items.append('Scroll')
    slowerprint('\nYou\'ve obtained a Scroll!')
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
    slowprint('You slowly come to, not sure where or when you are.\nSitting up, you are disoriented by the ringing in your head, most likely from the fall. It seems that you should be more careful next time you go spelunking.\nStill foggy-headed, you realize you can\'t see a thing.')
    if 'Torch' in player.items:
        slowprint('You light a torch, illuminating the small room. You see damp rock walls, covered in moss and mildew, and to your right, a small stream ahead of you leading further into the cave. Looking to your left, you see a crack in the rocks, just barely big enough for a person to fit through...\nMaybe.\nJust behind where you landed is a bottomless pit.\nWhich way do you go?')
        player_move = input('').lower()
        if player_move == 'left':
            slowprint('You pass on going deeper into the cave, contemplating still whether a person could fit through the hole in the rock wall. You skipped a few meals this morning, so if you suck in your stomach and position just the right way, you think you could do it.\nYou\'re unsure what\'s on the other side of the wall. Do you investigate further?')
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
                    player_move = 'right'
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
                    player_move = 'right'
        if player_move == 'right':
            the_mineshaft()

    if player_move == 'backwards' or player_move == 'behind' or 'Torch' not in player.items:
        if 'Torch' in player.items:
            slowprint('For some ungodly reason, you decide to go into the bottomless pit behind you. Way to go stupid. You fall forever and are stuck in a Lovecraftian horror of never dying but never living at all.')
            exit()
        slowprint('You fumble around in your bag, searching for a torch. You can\'t find one and resort to feeling your way around in the dark.')
        slowprint('........')
        slowprint('While stumbling around, you find yet another hole and fall down a bottomless pit to your death.')
        exit()



# the_hole()
