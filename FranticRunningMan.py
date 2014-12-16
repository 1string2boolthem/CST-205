import thread
from random import randint
from time import sleep

#getHighestValue returns the highest value found in sound.
def getHighestValue(sound):
  highest = 0
  for i in range(0, len(getSamples(sound))):
    if getSampleValueAt(sound, i) > highest:
      highest = getSampleValueAt(sound, i)
  return highest

#isolateSound isolates the sound from any leading or trailing silence.
def isolateSound(sound):
  soundSamples = getSamples(sound)
  silenceThreshold = int((getHighestValue(sound) * 0.20))
  consecutiveSamples = 30 #The number of consecutive samples that need to break the silence threshold.
  #First, find where the sound starts on the left side.
  firstValue = 0
  count = 0
  for i in range(0, len(soundSamples)):
    value = getSampleValueAt(sound, i)
    if abs(value) > silenceThreshold:
      count = count + 1
    if count > consecutiveSamples:
      firstValue = i - count
      break
  #Next, find the last value.
  lastValue = 0
  count = 0
  for i in range(len(soundSamples)-1, 0, -1):
    value = getSampleValueAt(sound, i)
    if abs(value) > silenceThreshold:
      count = count + 1
    if count > consecutiveSamples:
      lastValue = i + count - 1
      break
  #Now, make the new isolated sound.
  samplingRate = getSamplingRate(sound)
  newSound = makeEmptySound(lastValue-firstValue, int(getSamplingRate(sound)))
  for i in range(firstValue, lastValue):
    setSampleValueAt(newSound, i-firstValue, getSampleValueAt(sound, i))
  #Now, make sure that the sound is only a second long.
  numSamples = len(getSamples(newSound))
  if numSamples > int(getSamplingRate(newSound)):
    samplingRate = int(getSamplingRate(newSound))
    shortenedSound = makeEmptySound(samplingRate, samplingRate)
    for i in range(0, samplingRate):
      setSampleValueAt(shortenedSound, i, getSampleValueAt(newSound, i))
    newSound = shortenedSound
    explore(newSound)
  return newSound
def makeDrawnOut(sound, start, end, mult):
  offset = 0
  newSound = makeEmptySound((end-start)*mult, int(getSamplingRate(sound)))
  for i in range(start, end):
    for x in range(offset, offset+mult):
      setSampleValueAt(newSound, offset, getSampleValueAt(sound, i))
      offset += 1
  return newSound
  
#makeSong takes a list of notes and durations, then creates a song by generating square waves.
def makeSong(song):
  import math #Used for rounding the duration up.
  #This is a dictionary of notes. Using trial and error, I found the duration of time
  #needed between changing the value from negative to positive needed to generate
  #each note.
  notes = {'d':38, 'e':33, 'f':30, 'g':28, 'a':25, 'b':22, 'c':21, 'd2':19, 'e2':14, 'f2':11, 'g2':9, 's':1}
  length = 0
  #First, the length of the entire song must be found.
  for i in range(0, len(song)):
    if i % 2 != 0:
      length += song[i]
  length = math.ceil(length) #Round up, there will be silence on the end.
  #Create a new sound with the proper length.
  newSound = makeEmptySoundBySeconds(int(length), 44100)
  sampleLength = len(getSamples(newSound)) #The number of samples in newSound
  switch = true #Whether to use negative or positive values as the sample.
  value = 1000 #The volume, 100 works wel.
  offset = 0 #The current position to write the value in newSound.
  for i in range(0, len(song)-1, 2):
    currentNote = notes[song[i]] #The current note.
    currentLength = song[i+1] #The duration of the note
    value = 1000
    if(currentNote == 1):
      value = 0
    for x in range(offset, int((44100 * currentLength)) + offset):
      #Values switch from positive to negative when the length of the wave has been reached.
      if x % currentNote == 0:
        if switch:
          switch = false
        else:
          switch = true
      if offset < sampleLength:
        if switch:
          setSampleValueAt(newSound, offset, value)
        else:
          setSampleValueAt(newSound, offset, 0-value)
      offset += 1
  return newSound

#makeEffects makes various sound effects out of the sound file provided by the user.
def makeEffects(sound):
  sound = isolateSound(sound)
  effects = {}
  #The first effect will (hopefully) be a "he" sound. This will be used when the player starts running.
  heStart = 0
  heEnd = int(len(getSamples(sound))/3)
  heSound = makeEmptySound(heEnd-heStart, int(getSamplingRate(sound)))
  for i in range(heStart, heEnd):
    setSampleValueAt(heSound, i-heStart, getSampleValueAt(sound, i))
  effects["he"] = heSound
  #The second effect will be an o sound used when the player stops running.
  oStart = int(len(getSamples(sound))/1.3)
  oEnd = len(getSamples(sound))
  oSound = makeEmptySound(oEnd-oStart, int(getSamplingRate(sound)))
  for i in range(oStart, oEnd):
    setSampleValueAt(oSound, i-oStart, getSampleValueAt(sound, i))
  effects["o"] = oSound
  #The third effect will be a drawn out o. This will be played when the player dies.
  drawnOutStart = oStart
  drawnOutEnd = oEnd
  lengthMultiplier = 2
  drawnOutSound = makeDrawnOut(sound, drawnOutStart, drawnOutEnd, lengthMultiplier)
  effects["drawn"] = drawnOutSound
  screech = smashSound(sound)
  effects["screech"] = screech
  return effects

#smashSound condenses a sound into 1/4th of its normal time.
def smashSound(sound):
  numSamples = len(getSamples(sound))
  screech = makeEmptySound(numSamples/4, int(getSamplingRate(sound)))
  offset = 0
  for i in range(0, numSamples):
    if i % 4 == 0:
      if(offset < len(getSamples(screech))):
        setSampleValueAt(screech, offset, getSampleValueAt(sound, i))
        offset += 1
  return screech

def printRequestSound(): # prints a request for a sound file from the user.
  request = ""
  for space in range(50):
    request += "\n"
  for space in range(76):
    request += "*"
  request += "\n\n                            F R A N T I C    R U N N I N G    M A N\n\n\n"
  request += "To run this game, a sound bit of you saying hello is needed. Please\n"
  request += "select a sound file when prompted.\n\n\n"
  request += "                                       Please enjoy the game!\n\n"
  for space in range(76):
    request += "*"
  try:
    printNow(request)
  except:
    print request

def printInitializeSound(): # prints a request for the user to wait while sounds initialize.
  initialize = ""
  for space in range(50):
    initialize += "\n"
  for space in range(76):
    initialize += "*"
  initialize += "\n\n                            F R A N T I C    R U N N I N G    M A N\n\n\n\n\n\n\n"
  initialize += "                                 Initializing sound, please wait...\n\n"
  for space in range(76):
    initialize += "*"
  try:
    printNow(initialize)
  except:
    print initialize

def initializeSounds(): #initializes the various sounds used in this program.
  global effects
  global beginLevelSong
  global endLevelSong
  global endGameSong
  printRequestSound()
  sound = makeSound(pickAFile())
  printInitializeSound()
  beginLevelNotes = ['d', .37, 'e', .37, 'g', .37, 'd', .37, 'a', .20, 'd', .20, 'g',.37, 'f',.37, 'e',.37, 'd',.37, 'g', .75]
  endLevelNotes = ['s', .01, 'g', .2, 'b', .37, 'c', .37, 'd2', .75]
  endGameNotes = beginLevelNotes + endLevelNotes
  beginLevelSong = makeSong(beginLevelNotes)
  endLevelSong = makeSong(endLevelNotes)
  endGameSong = makeSong(endGameNotes)
  effects = makeEffects(sound)

beginLevelSong = 0 # initialize values for globals
endLevelSong = 0
endGameSong = 0
effects = 0
courseLength = 0
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
playAgain = True
lives = 3
freakOut = False

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
  global effects
  if paces <= courseLength - 20 or initialTime > 0: # don't move sky down if safety is in sight
    if skyCounter >= gravityInterval:
      skyCounter = 0
      for character in sky[len(sky) - 1][26:30]:
        if not character == " ":
          alive = False
          play(effects["drawn"])
      sky.pop()
      sky.insert(0, skyLine(True))
      if paces < 20:
        sky = fallingRoof(sky)
    else:
      skyCounter += 1

def moveSkyOver(sky): # moves the sky over to simulate running, clears sky if structure appears
  global paces
  global courseLength
  global endLevelSong
  for line in range(len(sky)):
    newLine = sky[line][2:]
    if paces > courseLength - 20: # clear sky and build roof if safety is in sight
      sky = clearSky(sky)
      if line == 0:
        if "\\" in sky[0]:
          newLine += "__"
        else:
          newLine += "\\_"
          play(endLevelSong)
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
  global effects
  global freakOut
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
  rock = False
  for character in sky[len(sky) - 1][26:30]:
    if not character == " ":
      rock = True
  if rock:
    if not freakOut:
      freakOut = True
      play(effects["screech"])
    head = "\\!/"
    body = " | "
  else:
    if freakOut:
      freakOut = False
    head = " @ "
    body = "/|\\"
  man += line + head + "\n"
  man += line + body + "\n"
  man += line + legs + "\n"
  try:
    printNow(man)
  except:
    print man

def printLevel(number, sound): # prints the level screen
  global lives
  global beginLevelSong
  level = ""
  for space in range(50):
    level += "\n"
  for space in range(76):
    level += "*"
  level += "\n\n\n"
  for space in range(47):
    level += " "
  level += "L E V E L   " + str(number) + "\n\n"
  for space in range(50):
    level += " "
  level += "Lives: " + str(lives) + "\n\n"
  level += "                                         Press Return to start.\n\n\n\n"
  for space in range(76):
    level += "*"
  if sound:
    play(beginLevelSong)
  try:
    printNow(level)
  except:
    print level

def printTitle(): # prints the title screen
  title = ""
  for space in range(50):
    title += "\n"
  for space in range(76):
    title += "*"
  title += "\n                            F R A N T I C    R U N N I N G    M A N\n\n"
  title += "Welcome to Frantic Running Man, the real time console game made for JES.\n"
  title += "The evil villain Crendall has doomed us all! He's created a device that causes\n"
  title += "rocks to fall from the sky! You're our only hope. Although you're an average\n"
  title += "Joe, you've been voluntold to run through the falling rocks from one collapsing\n"
  title += "structure to the next until you reach the device in the building at level 10.\n"
  title += "Press Return to run or stop and watch your head! Good luck, unwilling runner!\n\n"
  title += "                                         Press Return to start.\n"
  for space in range(76):
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
  global effects
  global courseLength
  list = []
  thread.start_new_thread(inputThread, (list,))
  while paces < courseLength and alive:
    if list:
      if paces > courseLength - 21:
        printMan(25, True)
      else:
        printMan(25, running)
        if running:
          running = False
          play(effects["o"])
        else:
          running = True
          play(effects["he"])
        break
    else:
      printMan(25, running)
      sleep(delay)

initializeSounds() # starts the game

while playAgain: # loops the game until user decides not to play again
  printTitle()
  pauseScreen()
  lives = 3
  alive = True
  level = 0
  paces = 0
  courseLength = 0
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
      printLevel(level, True)
      pauseScreen()
    if not alive: # prints failure screen when user is hit by a rock
      blockingPlay(effects["drawn"])
      if lives <= 1:
        printFailure()
      else:
        lives -= 1
        alive = True
        running = False
        printLevel(level, False)
        pauseScreen()
        sky = clearSky(sky)
  response = ""
  while not "y" in response and not "n" in response:
    response = str(raw_input("Play again (yes or no)? ")).lower()
  if not "y" in response:
    playAgain = False
