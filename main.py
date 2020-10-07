import sys
import time

def slowprint(str):
  for letter in str + '\n':
    sys.stdout.write(letter)
    sys.stdout.flush()
    time.sleep(1./10)

slowprint("This is a test of slowprint")
