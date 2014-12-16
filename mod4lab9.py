####################
# CST-205          #
# Module 4 Lab 9   #
# Sevren Gail      #
# Chris Rendall    #
# Nathan Hoover    #
####################

from random import randint

def maxSample(sound): # Returns the value of the largest sample in sound
  max = 0
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    if max < value:
      max = value
  return max

def maxVolume(sound): # Sets each value to the maximum value based on the largest value in sound
  factor = 32767/maxSample(sound)
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    setSampleValue(sample, value * factor)

def clip(source, start, end): # Creates a sound clip from source
  sound = makeEmptySound(end - start, int(getSamplingRate(source)))
  index = start
  while index < end:
    setSampleValueAt(sound, index - start, getSampleValueAt(source, index))
    index += 1
  maxVolume(sound)
  return sound

def copy(source, target, start): # Places a source sound into target at start
  index = start
  targetLength = getLength(target)
  for sample in getSamples(source):
    if index < targetLength:
      setSampleValueAt(target, index, getSampleValue(sample))
    index += 1

def combine(sound1, sound2): # Returns a new sound combining sound1 with sound2
  samplingRate = (getSamplingRate(sound1) + getSamplingRate(sound2)) / 2
  combined = makeEmptySound(getLength(sound1) + getLength(sound2), int(samplingRate))
  copy(sound1, combined, 0)
  copy(sound2, combined, getLength(sound1))
  return combined

def randomClip(sound): # Returns a random clip from sound
  clip = makeEmptySound(randint(500, getLength(sound) / 5), int(getSamplingRate(sound)))
  start = randint(0, getLength(sound) - getLength(clip))
  counter = 0
  while counter < getLength(clip):
    setSampleValueAt(clip, counter, getSampleValueAt(sound, counter + start))
    counter += 1
  return clip

def makeCollage(count): # makes collage of random clips from count sounds 
  counter = 0
  collage = randomClip(makeSound(pickAFile()))
  while counter < (count - 1):
    collage = combine(collage, randomClip(makeSound(pickAFile())))
    counter += 1
  maxVolume(collage)
  return collage

collage = makeCollage(5)

writeSoundTo(collage, "/Users/sgail/Desktop/sound.wav")

explore(collage)