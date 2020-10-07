import sys
import time
from os import system, name

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

#response = ""
#while response not in yes_no:
#    response = input("Would you like to enter the forest?\nyes/no\n")
#    if response == "yes":
#        slowprint ("Cool. Let the adventure begin")
#    elif response == "no":
#        slowprint ("I figured you would be scared. Goodbye")
#        quit()
#    else:
#        slowprint ("I don't understand your answer")

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

forest()

#response = ""
#while response not in yes_no:
    #response = input("Should you follow him?\nyes/no\n")
    #if response =="yes":
        #slowprint ("You follow the rabbit and he leads you to a cave.")
        #response = ""
        #while response not in yes_no:
            #response = input("Do you want to enter the cave?\nyes/no\n ")
            #if response == "yes":
            #    slowprint ("I hope you know what you're getting into.")

                #Brian's code

#            elif response == "no":
#                slowprint ("Well go in the other direction")
#            else:
#                slowprint ("I don't understand your answer")
#    elif response == "no":
#        slowprint ("You go in the opposite direction.")
#        slowprint ("You happen to stumble upon an old abandoned house.")

#        response = ""
#        while response not in yes_no:
#            response = input("Would you like to enter?\nyes/no\n")
#            if response == "yes":
#                slowprint ("Alright. Let's go")
#                response = ""
#                while response not in yes_no:
#                    response = input("While exploring the house, you come across a chest with some gold coins. Should you take them?\nyes/no\n")
#                    if response == "yes":
#                        slowprint ("You touch them, but they are laced with poison and you drop dead.")
#                    elif response == "no":
#                        slowprint ("You walk out the house and continue deeper into the forest. ")
#            elif response == "no":
#                slowprint ("Well let's continue deeper into the forest")
        #Richard's code
#            else:
#                slowprint ("I don't understand your answer")
