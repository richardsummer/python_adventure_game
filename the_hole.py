import sys
import time
from os import system, name
import players

def slowprint(str):
  for letter in str + '\n':
    sys.stdout.write(letter)
    sys.stdout.flush()
    time.sleep(2/60)
def clear():
    _ = system('clear')

# def fall_in_hole:
clear()
slowprint('You slowly come to, not sure where or when you are.\nSitting up, you are disoriented by the ringing in your head, most likely from the fall. It seems that you should be more careful next time you go spelunking.\nStill foggy-headed, you realize you can\'t see a thing.')
slowprint('You light a torch, illuminating the small room. You see damp rock walls, covered in moss and mildew, and to your right, a small stream ahead of you leading further into the cave. Looking to your left, you see a crack in the rocks, just barely big enough for a person to fit through. Maybe.\nWhich way do you go?')

player_move = input('').lower()
while player_move == 'left' or player_move == 'right':
    if player_move == 'left':
        slowprint('You pass on going deeper into the cave, contemplating still whether a person could fit through the hole in the rock wall. You skipped a few meals this morning, so if you suck in your stomach and position just the right way, you think you could do it.\nYou\'re unsure what\'s on the other side of the wall. Do you investigate further?')
        player_ipt = input('Y/N: ').upper()
        if player_ipt == 'Y':
            slowprint('The torch barely illuminates the crack in the rock wall, but you can make out the sound of running water, and what sounds like an item in a video game that would help you out. Unfortunately you cant see anything through the crack, the torch light just isnt strong enough to see through. Do you continue anyways?')
            player_ipt = input('Y/N: ').upper()
            if player_ipt =='Y':
                slowprint('You squeeze through the crack in the wall, heeding slightly more caution. You lose your balance as theres no solid ground on the other side and you fall multiple stories into a deep lake and drown. The promise of treasure and items curses you to death.')
                break
            elif player_ipt =='N':
                player_move = input('Go left/right ').lower()
        elif player_ipt == 'N':
            slowprint('How dangerous could a hole in the wall be anyways? Do you attempt to fit through?\n')
            player_ipt = input('Y/N ').upper()
            if player_ipt == 'Y':
                slowprint('You squeeze through the crack in the wall, confident you\'ve made the right choice. You lose your balance as theres no solid ground on the other side and you fall multiple stories into a deep lake and drown. Ignorance spells your demise')
            elif player_ipt == 'N':
                player_move = input('left/right')
