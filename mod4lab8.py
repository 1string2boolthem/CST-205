####################
# CST-205          #
# Module 4 Lab 8   #
# Sevren Gail      #
# Chris Rendall    #
# Nathan Hoover    #
####################

sound = makeSound(pickAFile())

explore(sound)

def increaseVolume(sound): # Doubles the volume of sound
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    setSampleValue(sample, value * 2)

def decreaseVolume(sound): # Halves the volume of sound
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    setSampleValue(sample, value / 2)

def changeVolume(sound, degree, up): # Changes the volume of sound to degree based on up (or down)
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    if up:
      setSampleValue(sample, value * degree)
    else:
      setSampleValue(sample, value / degree)

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

def goToEleven(sound): # Sets all positive samples to maximum and negative samples to minimum
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    if value > 0:
      setSampleValue(sample, 32767)
    elif value < 0:
      setSampleValue(sample, -32768)

goToEleven(sound)

explore(sound)