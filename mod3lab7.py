####################
# CST-205          #
# Module 3 Lab 7   #
# Sevren Gail      #   Sevren's Thanksgiving Card
# Chris Rendall    #
# Nathan Hoover    #
####################

def snowMan(pic): #paint a snowman onto a selected photo
  w = makeColor(255, 255, 255)
  o = makeColor(255, 204, 102)
  addOvalFilled(pic, 150, 175, 110, 110, w) #bottom body
  addOvalFilled(pic, 165, 110, 80, 80, w) #middle body
  addOvalFilled(pic, 180, 65, 50, 50, w) #head
  addOvalFilled(pic, 190, 75, 15, 15) #left eye
  addOvalFilled(pic, 210, 75, 15, 15) #right eye
  addOvalFilled(pic, 202, 90, 10, 10, o) #nose
  addOvalFilled(pic, 202, 130, 10, 10) #first button
  addOvalFilled(pic, 202, 160, 10, 10) #second button
  addOvalFilled(pic, 202, 190, 10, 10) #third button
  addLine(pic, 195, 105, 218, 105) #mouth
  addLine(pic, 183, 80, 227, 80) #sunglasses
  addRectFilled(pic, 126, 143, 40, 5)
  addRectFilled(pic, 245, 143, 40, 5)
  repaint(pic)

def sepia(thePicture): #creates a B&W of the picture by averaging the color values
  pixels = getPixels(thePicture)
  for pixel in pixels:
    r = getRed(pixel)
    g = getGreen(pixel)
    b = getBlue(pixel)
    average = (r * .299) + (g * .587) + (b * .114)
    setGreen(pixel, average)
    if average < 63:
      setRed(pixel, average * 1.1)
      setBlue(pixel, average * 0.9)
    elif average < 192 and average > 62:
      setRed(pixel, average * 1.15)
      setBlue(pixel, average * 0.85)
    else:
      setRed(pixel, average * 1.08)
      setBlue(pixel, average * 0.93)
  #repaint(thePicture)

def murderfy(thePicture):  #gives the picture a gruesome aspect
  pixels = getPixels(thePicture)
  for pixel in pixels:
    redOrGray(pixel)
  #repaint(thePicture)

def redOrGray(pixel): #makes redish pixels more red and makes all others b&w
    if getRed(pixel) > getGreen(pixel) + getBlue(pixel):
      if (getRed(pixel) * 2) > 255:
        setRed(pixel, 255)
      else:
        setRed(pixel, getRed(pixel) * 2)
      setGreen(pixel, getGreen(pixel) / 2)
      setBlue(pixel, getBlue(pixel) / 2)
    else:
      average = (getRed(pixel) * .299) + (getGreen(pixel) * .587) + (getBlue(pixel) * .114)
      setRed(pixel, average)
      setGreen(pixel, average)
      setBlue(pixel, average)

def artify(thePicture): #creates a color art effect
  pixels = getPixels(thePicture)
  for pixel in pixels:
    r = getRed(pixel)
    g = getGreen(pixel)
    b = getBlue(pixel)
    setGreen(pixel, colorChange(g))
    setRed(pixel, colorChange(r))
    setBlue(pixel, colorChange(b))
  #repaint(thePicture)

def colorChange(theColor): #splits a color into one of three choices based on its value
  if theColor < 64:
    return 31
  elif theColor > 63 and theColor < 128:
    return 95
  elif theColor > 127 and theColor < 192:
    return 159
  else:
    return 223

def makeCollage(): #Makes a collage of 3 pictures, applying a filter to each
  collage = makeEmptyPicture(612, 792)
  familyPicture = getSizedPicture(400, 250) #submit a picture of your family here
  sepia(familyPicture)
  turkeyPicture = getSizedPicture(400, 250) #submit a picture of a turkey here
  murderfy(turkeyPicture)
  campingPicture = getSizedPicture(400, 250) #submit a picture of black friday campers here
  artify(campingPicture)
  addPicture(familyPicture, collage, 10, 145 - (getHeight(familyPicture) / 2))
  addPicture(turkeyPicture, collage, 602 - getWidth(turkeyPicture), 395 - (getHeight(turkeyPicture) / 2))
  addPicture(campingPicture, collage, 10, 645 - (getHeight(campingPicture) / 2))
  addText(collage, 175, 20, "The fowl history of Thanksgiving revealed")
  addText(collage, 420, 70, "Thanksgiving is a time")
  addText(collage, 420, 90, "honored tradition from times")
  addText(collage, 420, 110, "of old. Many Thanksgiving")
  addText(collage, 420, 130, "activities have been handed")
  addText(collage, 420, 150, "down through generations.")
  addText(collage, 420, 170, "These include saying Thank")
  addText(collage, 420, 190, "You, seeing family and, of")
  addText(collage, 420, 210, "course, eating turkey.")
  addText(collage, 10, 330, "This is where the history")
  addText(collage, 10, 350, "turns dark. In a fight for")
  addText(collage, 10, 370, "self preservation, the")
  addText(collage, 10, 390, "turkeys began fighting back.")
  addText(collage, 10, 410, "Turkeysfrom around the world")
  addText(collage, 10, 430, "have conspired to change our")
  addText(collage, 10, 450, "traditions.")
  addText(collage, 420, 600, "Turkeys now celebrate the")
  addText(collage, 420, 620, "success of their endeavors.")
  addText(collage, 420, 640, "Humans are now mysteriously")
  addText(collage, 420, 660, "compelled to camp outside")
  addText(collage, 420, 680, "on Thanksgiving. Now a days,")
  addText(collage, 420, 700, "turkeys everywhere laugh")
  addText(collage, 420, 720, "inwardly at our discomfort.")
  addText(collage, 190, 782, "Happy Thanksgiving to you and yours!")
  show(collage)

#Copies source to targetX and targetY on target image.
def addPicture(source, target, x, y):
  pixels = getPixels(source)
  for pixel in pixels:
    if x + getX(pixel) < getWidth(target) and y + getY(pixel) < getHeight(target):
      setColor(getPixel(target, x + getX(pixel), y + getY(pixel)), getColor(pixel))

def getSizedPicture(width, height): #sizes picture smaller than the given dimensions
  thePicture = makePicture(pickAFile())
  while getWidth(thePicture) > width or getHeight(thePicture) > height:
    thePicture = shrink(thePicture)
  return thePicture

def shrink(thePicture): #returns a duplicate of thePicture at half size
  thePixels = getPixels(thePicture)
  theCopy = makeEmptyPicture(getWidth(thePicture)/2, getHeight(thePicture)/2)
  copyPixels = getPixels(theCopy)
  counter = 0
  for pixel in copyPixels:
    setColor(pixel, getColor(getPixel(thePicture, getX(pixel) * 2, getY(pixel) * 2)))
  return theCopy

makeCollage()