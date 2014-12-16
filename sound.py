def getHighestValue(sound):
  highest = 0
  for i in range(0, len(getSamples(sound))):
    if getSampleValueAt(sound, i) > highest:
      highest = getSampleValueAt(sound, i)
  return highest
def isolateSound(sound):
  soundSamples = len(getSamples(sound))
  printNow("Number of Samples: " + str(soundSamples))
  silenceThreshold = int((getHighestValue(sound) * 0.20))
  consecutive = 30
  printNow("Silence Threshold: " + str(silenceThreshold))
  printNow("Number of Samples: " + str(soundSamples))
  #First, find where the sound starts on the left side.
  firstValue = 0
  for i in range(0, soundSamples):
    value = getSampleValueAt(sound, i)
    if abs(value) > silenceThreshold:
      firstValue = i
      break
  #Next, find the last value.
  lastValue = 0
  count = 0
  first = 0
  for i in range(soundSamples-1, 0, -1):
    value = getSampleValueAt(sound, i)
    if abs(value) > silenceThreshold:
      count = count + 1
    if count > consecutive:
      lastValue = i - count
      break
  printNow("First Value: " + str(firstValue))
  printNow("Last Value: " + str(lastValue))
  #Now, make the new isolated sound.
  samplingRate = getSamplingRate(sound)
  printNow("Sampling Rate: " + str(samplingRate))
  newSound = makeEmptySound(lastValue-firstValue, int(getSamplingRate(sound)))
  for i in range(firstValue, lastValue):
    setSampleValueAt(newSound, i-firstValue, getSampleValueAt(sound, i))
  soundSamples = len(getSamples(newSound))
  if(soundSamples > int(getSamplingRate(newSound))):
    samplingRate = int(getSamplingRate(newSound))
    newerSound = makeEmptySound(samplingRate, samplingRate)
    for i in range(0, samplingRate):
      setSampleValueAt(newerSound, i, getSampleValueAt(newSound, i))
    newSound = newerSound
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
  
#makeSong() takes a list of notes and durations, then creates a song by generating square waves.
def makeSong(song):
  import math #Used for rounding the duration up.
  #This is a dictionary of notes. Using trial and error, I found the duration of time
  #needed between changing the value from negative to positive needed to generate
  #each note.
  notes = {'d':38, 'e':33, 'f':30, 'g':28, 'a':25, 'b':22, 'c':21, 'd2':19, 's':1}
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
  value = 100 #The volume, 100 works wel.
  offset = 0 #The current position to write the value in newSound.
  for i in range(0, len(song)-1, 2):
    currentNote = notes[song[i]] #The current note.
    currentLength = song[i+1] #The duration of the note
    value = 100
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
  #Finally, trim the end.
  lastValue = 0
  for i in range(sampleLength-1, 0, -1):
    if getSampleValueAt(newSound, i) == 0:
      lastValue = i
  trimmedSound = makeEmptySound(lastValue, 44100)
  for i in range(0, lastValue):
    setSampleValueAt(trimmedSound, i, getSampleValueAt(newSound, i))
  return newSound
def postScore(name, score):
  import urllib2
  request = urllib2.Request("http://icantfindmy.tk/score.php?a=post&name=" + str(name) + "&score=" + str(score))
  response = urllib2.urlopen(request)
def getScores():
  import urllib2
  try:
    request = urllib2.Request("http://icantfindmy.tk/score.php?a=get")
    response = urllib2.urlopen(request)
    response = response.read()
    scores = response.split('|')
    scores.pop(len(scores)-1)
  except:
    scores = []
  return scores
def makeSoundEffects(sound):
  effects = {}
  sound = isolateSound(sound)
  #The first effect will (hopefully) be a very loud he!
  heStart = 0
  heEnd = int(len(getSamples(sound))/3)
  heSound = makeEmptySound(heEnd-heStart, int(getSamplingRate(sound)))
  for i in range(heStart, heEnd):
    setSampleValueAt(heSound, i-heStart, getSampleValueAt(sound, i)*2)
  effects["he"] = heSound
  oStart = int(len(getSamples(sound))/1.3)
  oEnd = len(getSamples(sound))
  oSound = makeEmptySound(oEnd-oStart, int(getSamplingRate(sound)))
  for i in range(oStart, oEnd):
    setSampleValueAt(oSound, i-oStart, getSampleValueAt(sound, i))
  effects["o"] = oSound
  drawnOutStart = oStart
  drawnOutEnd = oEnd
  lengthMultiplier = 2
  drawnOutSound = makeDrawnOut(sound, drawnOutStart, drawnOutEnd, lengthMultiplier)
  effects["drawn"] = drawnOutSound
  weirdSound = makeDrawnOut(sound, drawnOutStart, drawnOutEnd, 6)
  effects["weird"] = weirdSound
  return effects
sound = makeSound(pickAFile())
sound = isolateSound(sound)
song = ['d', .5, 'e', .5, 'g', .5, 's', .01, 'd',.5, 's', .01, 'd', .5, 'a', .25, 'd', .25, 'g',.5, 'f',.5, 'e',.5, 'd',1]
#effects = makeSoundEffects(sound)