import thread
from random import randint
from time import sleep

courseLength = 0 # initialize values for globals
paces = 0
initialTime = 0
gravityInterval = 0
level = 0
running = False
pause = False
alive = True
skyCounter = 0
delay = .1
sky = []

def skyLine(rocks): # returns a line to add to the sky, adding rocks if needed
  line = ""
  for space in range(25):
    if rocks and randint(1,100) > 95:
      line += "()"
    else:
      line += "  "
  return str(line)

def fallingRoof(sky): # changes roof characters in given sky to simulate falling rubble
  roofLine = ['\\', '_', '|', '/', '-']
  newSky = []
  for line in range(len(sky)):
    newLine = ""
    for character in range(len(sky[line])):
      if sky[line][character] in roofLine:
        newLine += roofLine[randint(0, len(roofLine) - 1)]
      else:
        newLine += sky[line][character]        
    newSky.append(newLine)
  return newSky

def clearSky(sky): # removes the rocks from given sky
  newSky = []
  for line in sky:
    newLine = line.replace("(", " ")
    newLine = newLine.replace(")", " ")
    newSky.append(newLine)
  return newSky

def initializeSky(): # creates the initial sky with the roof on the left
  global sky
  sky = []
  roof = ""
  for space in range(8):
    roof += "__"
  roof += "/ "
  for space in range(14):
    roof += "  "
  sky.append(roof)
  line = " |"
  for space in range(24):
    line += "  "
  for space in range(8):
    sky.append(line)

def moveSkyDown(): # removes the bottom line, adds top line, tests alive status
  global sky
  global paces
  global skyCounter
  global courseLength
  global gravityInterval
  global initialTime
  global alive
  if paces <= courseLength - 20 or initialTime > 0: # don't move sky down if safety is in sight
    if skyCounter >= gravityInterval:
      skyCounter = 0
      for character in sky[len(sky) - 1][26:30]:
        if not character == " ":
          alive = False
      sky.pop()
      sky.insert(0, skyLine(True))
      if paces < 20:
        sky = fallingRoof(sky)
    else:
      skyCounter += 1

def moveSkyOver(sky): # moves the sky over to simulate running, clears sky if structure appears
  global paces
  global courseLength
  for line in range(len(sky)):
    newLine = sky[line][2:]
    if paces > courseLength - 20: # clear sky and build roof if safety is in sight
      sky = clearSky(sky)
      if line == 0:
        if "\\" in sky[0]:
          newLine += "__"
        else:
          newLine += "\\_"
      else:
        newLine += "  "
    else: # otherwise, remove left spaces and add right spaces with random rocks
      if randint(1,100) > 95:
        newLine += "()"
      else:
        newLine += "  "
    sky[line] = newLine
  return sky

def printMan(margin, running): # prints man and sky, dropping rocks & moving the sky if running
  global sky
  global paces
  global initialTime
  runningLegs = ["/ \\", " | ", "/| "]
  legs = "/ \\"
  moveSkyDown()
  if running:
    initialTime = 0
    legs = runningLegs[randint(0,2)]
    sky = moveSkyOver(sky)
    paces += 1
  else:
    initialTime -= 1
    legs = "/ \\"
  man = ""
  for space in range(50):
    man += "\n"
  for line in sky:
    man += str(line) + "\n"
  line = ""
  for space in range(margin):
    line += " "
  head = " @ "
  body = "/|\\"
  for character in sky[len(sky) - 1][26:30]:
    if not character == " ":
      head = "\\!/"
      body = " | "
  man += line + head + "\n"
  man += line + body + "\n"
  man += line + legs + "\n"
  try:
    printNow(man)
  except:
    print man

def printLevel(number): # prints the level screen
  level = ""
  for space in range(50):
    level += "\n"
  for space in range(76):
    level += "*"
  level += "\n\n\n\n"
  for space in range(47):
    level += " "
  level += "L E V E L   " + str(number) + "\n\n\n"
  level += "                                         Press Return to start.\n\n\n\n"
  for space in range(76):
    level += "*"
  try:
    printNow(level)
  except:
    print level

def printTitle(): # prints the title screen
  title = ""
  for space in range(50):
    title += "\n"
  for space in range(75):
    title += "*"
  title += "\n                            F R A N T I C    R U N N I N G    M A N\n\n"
  title += "Welcome to Frantic Running Man, the real time console game made for JES.\n"
  title += "The evil villain Crendall has doomed us all! He's created a device that causes\n"
  title += "rocks to fall from the sky! You're our only hope. Although you're an average\n"
  title += "Joe, you've been voluntold to run through the falling rocks from one collapsing\n"
  title += "structure to the next until you reach the device in the building at level 10.\n"
  title += "Press Return to run or stop and watch your head! Good luck, unwilling runner!\n\n"
  title += "                                         Press Return to start.\n"
  for space in range(75):
    title += "*"
  try:
    printNow(title)
  except:
    print title

def printSuccess(): # prints the success screen
  success = ""
  for space in range(50):
    success += "\n"
  for space in range(76):
    success += "*"
  success += "\n\n                            F R A N T I C    R U N N I N G    M A N\n\n"
  success += "You arrive just in the nick of time and save us all! You're not an average Joe.\n"
  success += "From now on, you'll be known by everyone as a slightly-better than average Joe!\n"
  success += "Thanks to you, we can walk freely again! However, we're now all homeless and\n"
  success += "nightfall is fast approaching. What we need now is a Frantic Building Man. . .\n\n"
  success += "                                       Thank you for playing!\n\n"
  for space in range(76):
    success += "*"
  try:
    printNow(success)
  except:
    print success

def printFailure(): # prints the failure screen
  global level
  failure = ""
  for space in range(50):
    failure += "\n"
  for space in range(76):
    failure += "*"
  failure += "\n\n                            F R A N T I C    R U N N I N G    M A N\n\n"
  failure += "Your failure is now complete. You had one job. ONE JOB! Now we'll have to find\n"
  failure += "some other average Joe to save us. Do you have any idea how hard it is to find\n"
  failure += "someone stupid enough-er, uh brave enough to go out there through the rocks?\n"
  failure += "Then again, YOU made it all the way to level " + str(level) + ". Maybe you should try again. . .\n\n"
  failure += "                                       Thank you for playing!\n\n"
  for space in range(76):
    failure += "*"
  try:
    printNow(failure)
  except:
    print failure

def inputThread(list): # gets user input and appends it to list
  raw_input()
  list.append(None)

def pauseScreen(): # creates a thread to wait for user input to continue
  global pause
  pause = True
  list = []
  thread.start_new_thread(inputThread, (list,))
  while pause:
    if list:
      pause = False
    sleep(.1)

def circulate(): # creates a thread to display game; alternates the man's running status
  global running
  global initialTime
  global paces
  global alive
  global delay
  list = []
  thread.start_new_thread(inputThread, (list,))
  while paces < courseLength and alive:
    if list:
      printMan(25, running)
      if running:
        running = False
      else:
        running = True
      break
    else:
      printMan(25, running)
      sleep(delay)

printTitle()
pauseScreen()

while alive: # runs the game while user is alive
  if paces < courseLength:
    printMan(25, running)
    circulate()
  else:
    initializeSky()
    level += 1
    if level > 10:
      printSuccess()
      break
    courseLength = 100 + (level * 15)
    gravityInterval = 22 - (level * 2)
    paces = 0
    running = False
    initialTime = 10
    printLevel(level)
    pauseScreen()

if not alive: # prints failure screen when user is hit by a rock
  printFailure()