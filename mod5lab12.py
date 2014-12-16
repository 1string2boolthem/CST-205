####################
# CST-205          #
# Module 5 Lab 12  #
# Sevren Gail      #
# Chris Rendall    #
####################

from random import randint

class Object: #These are objects found around the mansion.
  def __init__(self, name, description, permanence): #This constructor estabishes the name, description and permanence.
    self.name = name #This is the name of the object.
    self.description = description #This is the name of the object.
    self.permanence = permanence #This is the permanence of the object (whether an object can be removed from the room).
    self.uses = {} #This is a dictionary with a use (cause) as the key and the fallout (effect) as the value.
    
  def setName(self, name): #This is the mutator for the name.
    self.name = name
  
  def printName(self): #This prints the name.
    printNow(self.name)
  
  def getName(self): #This is the accessor for the name.
    return self.name
  
  def setDescription(self, description): #This is the mutator for the description.
    self.description = description
  
  def printDescription(self): #This prints the description.
    printNow(self.description)
  
  def getDescription(self): #This is the accessor for the description.
    return self.description
  
  def setPermanence(self, permanence): #This is the mutator for the permanence.
    self.permanence = permanence
  
  def getPermanence(self): #This is the accessor for the permanence.
    return self.permanence
  
  def setUse(self, use, fallout): #This is the mutator for the uses. It adds a key if one doesn't exist and sets the value.
    self.uses[use] = fallout

  def removeUse(self, use): #This lets you remove a use from an item.
    del self.uses[use]
  
  def getUses(self): #This is the accessor for the list of uses.
    return self.uses.keys()
  
  def getFallout(self, use): #This is the accessor for a specific use.
    return uses[use]

class Room: #These are rooms around the mansion.
  def __init__(self, name, description): #This constructor estabishes the name and description.
    self.name = name #This is the name of the room.
    self.description = description #This is the description of the room.
    self.directions = {} #This dictionary contains the directions you can go and the Rooms they lead to.
    self.objects = [] #These are the objects in the room.
  
  def setName(self, name): #This is the mutator for the name.
    self.name = name
  
  def printName(self): #This prints the name.
    printNow(self.name)
  
  def getName(self): #This is the accessor for the name.
    return self.name
  
  def setDescription(self, description): #This is the mutator for the description.
    self.description = description
  
  def printDescription(self): #This prints the description.
    printNow(self.description)
  
  def getDescription(self): #This is the accessor for the description.
    return self.description
  
  def getRoom(self, direction): #This returns the room that lies in the direction you want to go.
    return self.directions[direction]
  
  def setDirection(self, direction, room): #This creates a direction if one doesn't exist and sets the room there.
    self.directions[direction] = room
  
  def removeDirection(self, direction): #This removes a direction from the room.
    del self.directions[direction]
  
  def printDirections(self): #This prints the directions you can go.
    for direction in self.directions.keys():
      printNow(direction)

  def getDirections(self): #This returns the list of direction names.
    return self.directions.keys()
  
  def addObject(self, object): #This adds an object to the room.
    self.objects.append(object)
  
  def removeObject(self, object): #This removes an object from the room.
    if object in self.objects:
      self.objects.remove(object)
  
  def printObjects(self): #This prints the names of the objects in the room.
    for object in self.objects:
      object.printName()

  def getObjects(self): #This returns a list of objects in the room.
    return self.objects
  
  def fullyDescribe(self): #This prints a description that also includes the name, directions and objects
    printNow("------------" + self.getName().upper() + "------------")
    self.printDescription()
    printNow("")
    if len(self.objects) == 0:
      printNow("There are no objects in this room.")
    else:
      printNow("Here are the objects in the room:")
      self.printObjects()
    printNow("")
    if len(self.directions) == 0:
      printNow("You can't see a way out. Bummer!")
    else:
      printNow("Here are the directions you can go:")
      self.printDirections()

def help(): #This prints the intro and directions.
  #The intro is the introductory statement that explains the premise of the game.
  intro = "Your millionaire father has passed away. You have now realized that if you do not find his will, your "
  intro += "young stepmother will fabricate one and take everything. Right now your stepmother is working to acquire "
  intro += "an eviction notice to remove you from this house. You remember your father telling you that he hid it in "
  intro += "the library of his mansion. If you do not find the will soon, there is no hope."
  #These instructions tell how to play the game.
  instructions = "You can move around the house by indicating a direction to move (ex: Move North). "
  instructions += "Feel free to abbreviate the commands (ex: Move n). "
  instructions += "You can also look at objects around the house (ex: Look At Table) and pick up some of them (ex: Pick Up Sandwich). "
  instructions += "Type inventory to see what you're holding. Try other commands too, like pull, push, open, use, etc... "
  instructions += "Type help at any time to see these directions again."
  printNow(intro)
  printNow("")
  printNow(instructions)

def move(direction): #This moves the user to the room in the indicated direction if the direction is valid.
  global room
  validDirections = ["north", "south", "east", "west", "up", "down", "n", "s", "e", "w", "u", "d"]
  if direction == "n":
    direction = "north"
  if direction == "s":
    direction = "south"
  if direction == "e":
    direction = "east"
  if direction == "w":
    direction = "west"
  if direction == "u":
    direction = "up"
  if direction == "d":
    direction = "down"
  roomDirections = room.getDirections()
  for i in range(0, len(roomDirections)):
    roomDirections[i] = roomDirections[i].lower()
  if direction == " ":
    printNow("Move where?")
  elif validDirections.count(direction) == 0:
    printNow("That's not a direction...")
  elif roomDirections.count(direction) == 0:
    printNow("You cannot move that direction in this room.")
  else:
    room = room.getRoom(direction.capitalize())

def useCrowbar(): #This allows a user who has the crowbar in the library to move the bookshelf.
   global room
   global inventory
   global bookshelfMoved
   if room.getName() != "Library":
     printNow("You cannot use the crowbar here.")
   else:
     for object in room.getObjects():
       if object.getName() == "Bookshelf":
         printNow("You use the crowbar to move the bookshelf, revealing a safe that was hidden behind it.")
         printNow("The crowbar breaks just as the shelf moves aside.")
         bookshelfMoved = true
         room.setDescription(getLibraryDescription())
         room.removeObject(object)
         room.addObject(Object("Safe", "A sturdy looking standard dial safe. The words, \"kitchen, bathroom, bedroom\" are scrawled on it.", true))
         removeInventory("Crowbar")
         
def removeInventory(item): #This removes object with name item from the inventory.
  global inventory
  for o in inventory:
    if o.getName() == item:
      inventory.remove(o)

def use(modifiers): #This calls useCrowbar when the user types use crowbar.
  global inventory
  if modifiers[0] == "crowbar":
    for object in inventory:
      if object.getName() == "Crowbar":
        useCrowbar()
      
def displayInventory(): #This prints the inventory objects.
  global inventory
  if len(inventory) == 0:
    printNow("You have nothing in you inventory. How sad...")
  else:
    printNow("You have the following in your inventory:")
    for object in inventory:
      printNow(object.getName())

def open(modifiers): #Open the safe if the user is in the library and the bookshelf is moved and the safe is closed.
  global kitchenNumber
  global bathroomNumber
  global bedroomNumber
  global room
  global bookshelfMoved
  global safeOpen
  safeFound = false
  if modifiers[0].lower() == "safe":
    for o in room.getObjects():
      if o.getName() == "Safe":
        safeFound = true
        if safeOpen:
          printNow("The safe is already open...")
        else:
          number1 = requestInteger("Enter the first number of the combination:")
          number2 = requestInteger("Enter the second number of the combination:")
          number3 = requestInteger("Enter the third number of the combination:")
          if number1 == kitchenNumber and number2 == bathroomNumber and number3 == bedroomNumber:
            printNow("As you open up the safe you see a big red button inside.")
            room.setDescription(getLibraryDescription())
            room.addObject(Object("Button", "An invitingly bright red button.", true))
          else:
            printNow("That... didn't work. Did you just make those numbers up?")
    if not safeFound:
      printNow("There is no safe here...")
  else:
    printNow("You cannot open that...")

def push(modifiers): #Push the button if user is in the Library and the safe is open.
  global room
  global safeOpen
  global trapDoorOpen
  buttonFound = false
  if modifiers[0].lower() == "button":
    for o in room.getObjects():
      if o.getName() == "Button":
        buttonFound = true
        if trapDoorOpen:
          printNow("You press the button, but nothing happens.")
        else:
          printNow("As you push the button, a cleverly hidden trap door pops open in the middle of the floor.")
          trapDoorOpen = true
          room.setDescription(getLibraryDescription())
          basement = Room("Basement", "The basement is a small dark room with a writing table. On it lies your father's will.")
          basement.setDirection("Up", room)
          basement.addObject(Object("Father's Will", "", false))
          room.setDirection("Down", basement)
    if not buttonFound:
      printNow("There is no button here...")
  else:
    printNow("Pushing that does nothing...")

def performAction(action, modifiers): #This takes parsed actions and modifiers and performs the appropriate task.
  if len(modifiers) == 0:
    modifiers.append(" ")
  moveActions = ["move", "go", "travel", "walk"]
  helpActions = ["help", "?"]
  directionActions = ["north", "south", "east", "west", "up", "down", "n", "e", "s", "w", "u", "d"]
  lookActions = ["look", "l", "examine", "look"]
  dropActions = ["drop"]
  pickupActions = ["pickup", "get"]
  inventoryActions = ["inventory", "i", "inv", "equipment", "backpack"]
  pullActions = ["pull"]
  useActions = ["use"]
  openActions = ["open"]
  pushActions = ["push", "press"]
  if moveActions.count(action.lower()) > 0:
    move(modifiers[0])
  elif directionActions.count(action.lower()) > 0:
    move(action)
  elif helpActions.count(action) > 0:
    help()
  elif lookActions.count(action) > 0:
    look(modifiers)
  elif useActions.count(action) > 0:
    use(modifiers)
  elif openActions.count(action) > 0:
    open(modifiers)
  elif pushActions.count(action) > 0:
    push(modifiers)
  elif pickupActions.count(action) > 0:
    pickup(modifiers)
  elif inventoryActions.count(action) > 0:
    displayInventory()
  elif pullActions.count(action) > 0:
    pull(modifiers)
  else: 
    printNow("You can't do that...")

def pull(modifiers): #Pull the latch if the user is in the library and the latch is unpulled.
  global latchPulled
  global room
  if modifiers[0] == " ":
    printNow("Pull what?")
  elif modifiers[0] == "latch" and room.getName() == "Library" and latchPulled == false:
    printNow("You pull the latch and a trap door opens leading upward and a ladder extends down to the floor.")
    attic = Room("Attic", "A dark and dusty room with a small amount of light coming in through a window at the top of the room.")
    attic.setDirection("Down", room)
    attic.addObject(Object("Crowbar", "A rusty steel crowbar that's seen better days.", false))
    room.setDirection("Up", attic)
    for o in room.getObjects():
      if o.getName() == "Latch":
        room.removeObject(o)
    latchPulled = true
    room.setDescription(getLibraryDescription())
  else:
    printNow("There is no " + modifiers[0] + " here.")
    
def look(modifiers): #Print the description of modifier if it exists.
  global room
  object = modifiers[0]
  objects = room.getObjects()
  objectFound = false
  for i in range(0, len(objects)):
    if objects[i].getName().lower() == object:
      printNow(objects[i].getDescription())
      objectFound = true
  if(not objectFound):
    printNow("There is no object by that name here...")

def pickup(modifier): #Add the item to inventory and remove from room if it exists and is not permanent.
  global room
  global inventory
  objectFound = false
  for object in room.getObjects():
    if object.getName().lower() == modifier[0]:
      if object.getPermanence() == false:
        inventory.append(object)
        printNow("You pick up the " + object.getName())
        objectFound = true
        room.removeObject(object)
      else:
        printNow(object.getName() + " will not fit in your inventory...")
        objectFound = true
  if not objectFound and modifier[0] != " ":
    printNow("There is no " + modifier[0] + " here.")
  elif not objectFound and modifier[0] == " ":
    printNow("Pick up what?")

def parseCommand(commandList): #This parses the command.
  verb = commandList[0]
  modifiers = commandList
  modifiers.pop(0)
  performAction(verb, modifiers)

def fixCommand(command): #This cleans up the command to make it easier to parse.
  command = command.replace("pick up", "pickup")
  command = command.replace("look at", "look")
  command = command.replace("the ", "")
  return command

def initializeRooms(): #This sets up the rooms initially.
  global kitchenNumber
  global bathroomNumber
  global bedroomNumber
  library = Room("Library", getLibraryDescription())
  kitchen = Room("Kitchen", "You are in the kitchen. There is a large stainless steel refrigerator.")
  bedroom = Room("Bedroom", "You are in your father's bedroom. There is a large bed in the corner.")
  entryway = Room("Entryway", "You are in the entryway to your father's mansion. There is a large door to the south.")
  bathroom = Room("Bathroom", "You are in the bathroom. There is a large bathtub. The toilet is spotless.")
  outside = Room("Outside", "You are outside. Your stepmother is there with the eviction notice. She locks you outside. How cold!")
  library.setDirection("West", kitchen)
  library.setDirection("East", bathroom)
  library.setDirection("North", bedroom)
  library.setDirection("South", entryway)
  library.addObject(Object("Table", "A table made of old oak covered in a film of dust.", true))
  library.addObject(Object("Bookshelf", "A bookshelf that seems slightly offset.", true))
  library.addObject(Object("Latch", "A latch extending down from the ceiling.", true))
  kitchen.setDirection("East", library)
  kitchen.addObject(Object("Refrigerator", "A large stainless steel refrigerator with fridge magnet showing the number " + str(kitchenNumber), true))
  bedroom.setDirection("South", library)
  bedroom.addObject(Object("Bed", "A large bed covered by a plush comforter carefully embroidered with the number " + str(bedroomNumber), true))
  bathroom.setDirection("West", library)
  bathroom.addObject(Object("Bathtub", "A sizeable bath tub with a state of the art faucet.", true))
  bathroom.addObject(Object("Toilet", "A spotless toilet. While it looks clean, it clearly stinks like the number " + str(bathroomNumber), true))
  entryway.setDirection("North", library)
  entryway.setDirection("South", outside)
  return library
  
def getLibraryDescription(): #This returns the current description of the library.
  global bookshelfMoved
  global latchPulled
  global trapDoorOpen
  description = "You find yourself in a room surrounded by bookshelves."
  if bookshelfMoved:
    description += " There is a large sturdy dial safe in the wall."
  else:
    description += " There is a bookshelf that is slightly offset."
  if latchPulled:
    description += " There is a ladder leading upward."
  else:
    description += " In the ceiling there is a latch that looks just within reach."
  if trapDoorOpen:
    description += " A trap door gapes invitingly in the center of the floor."
  return description

def playGame(): #This is the main loop.
  global room
  continuePlaying = true
  inventory = []
  while(continuePlaying):
    printNow("")
    room.fullyDescribe()
    printNow("")
    if room.getName() == "Basement":
      printNow("You have found your father's will! Congratulations!")
      if randint(1,10) > 5:
        printNow("It says that you inherit everything! Score!")
      else:
        printNow("It says... that your step mom inherits everything... Let's just forget we found this, eh?")
      continuePlaying = false
    elif room.getName() == "Outside":
      printNow("You facepalm your shortsightedness in coming outside. Oh, well. You probably wouldn't appreciate that fortune anyways.")
      continuePlaying = false
    else:
      try:
        command = requestString("Enter a command:").lower()
        if(command != "exit"):
          command = fixCommand(command)
          parseCommand(command.split(' '))
        else:
          printNow("You gave up? I guess a multi-million dollar estate is overrated, right?")
          continuePlaying = false
      except:
        printNow("You gave up? I guess a multi-million dollar estate is overrated, right?")
        continuePlaying = false

kitchenNumber = randint(1,99) #This is the number found in the kitchen.
bathroomNumber = randint(1,99) #This is the number found in the bathroom.
bedroomNumber = randint(1,99) #This is the number found in the bedroom.
bookshelfMoved = false #This turns true when the user moves the bookshelf in the library.
latchPulled = false #This turns true when the user pulls the latch in the library.
trapDoorOpen = false #This turns true when the user opens the trap door in the library.
safeOpen = false #This turns true when the user opens the safe in the library.
room = initializeRooms() #This is the current room that the user is in.
inventory = [] #This is a list containing the objects carried by the user.
help()
playGame()