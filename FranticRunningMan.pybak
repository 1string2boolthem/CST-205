import threading
from random import randint

runningLegs = ["/ \\", " | ", "/| "]
legs = "/ \\"
sky = []

def skyLine(rocks):
  line = ""
  for space in range(25):
    if rocks and randint(1,100) > 95:
      line += "()"
    else:
      line += "  "
  return str(line)

for space in range(10):
  sky.append(skyLine(false))

skyCounter = 0

def moveSkyDown():
  global sky
  global skyCounter
  if skyCounter == 10:
    skyCounter = 0
    sky.pop()
    sky.insert(0, skyLine(true))
  else:
    skyCounter += 1

def moveSkyOver(sky):
  for line in range(len(sky)):
    newLine = sky[line][2:]
    if randint(1,100) > 95:
      newLine += "()"
    else:
      newLine += "  "
    sky[line] = newLine
  return sky
 
def printMan(margin, running):
  global runningLegs
  global legs
  global sky
  if running:
    legs = runningLegs[randint(0,2)]
  else:
    legs = "/ \\"
  man = ""
  for space in range(50):
    man += "\n"
  moveSkyDown()
  if running: sky = moveSkyOver(sky)
  for line in sky:
    man += str(line) + "\n"
  line = ""
  for space in range(margin):
    line += " "
  man += line
  man += " @ \n"
  man += line
  man += "/|\\\n"
  man += line
  man += legs
  printNow(man)

def getInput():
  global direction
  text = raw_input()
  if text == "a":
    direction = 0
  elif text == "s":
    direction = 1
  elif text == "d":
    direction = 2

man = ""
margin = 0
direction = 1

import thread

def inputThread(list):
    raw_input()
    list.append(None)

def circulate():
  global running
  list = []
  thread.start_new_thread(inputThread, (list,))
  while True:
    printMan(25, running)
    if list:
      if running:
        running = false
      else:
        running = true
      break

running = false

while True:
  circulate()
