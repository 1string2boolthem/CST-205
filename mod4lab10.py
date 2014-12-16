###################
# CST-205         #
# Module 4 Lab 10 #
# Sevren Gail     #
# Chris Rendall   #
# Nathan Hoover   #
###################

#Draws the hangman that is free from the gallows.
def drawWinningMan():
  printNow(" @    ----------")
  printNow(" /|\\     PHEW!")
  printNow("  |      ----------")
  printNow(" / \\")
#Draw the hangman in his current state, based on the number of false guesses the user has used.
def drawHangman(guess):
  heightLeft = 6
  printNow("--------")
  if guess >= 1:
    printNow("|        |")
    printNow("|       @")
    heightLeft = heightLeft - 2
  if guess == 2:
    printNow("|        |")
    printNow("|        |")
    heightLeft -= 2
  if guess == 3:
    printNow("|      / | ")
    printNow("|        |")
    heightLeft -= 2
  if guess >= 4:
    printNow("|      / | \\")
    printNow("|        |")
    heightLeft -= 2
  if guess == 5:
    printNow("|      /")
    heightLeft -= 1
  if guess >= 6:
    printNow("|      /  \\")
    heightLeft -= 1
  for x in range(0, heightLeft):
    printNow("|")
  printNow("--------")
#This prints the word in its current state. If a letter has not been guessed, a _ will be in its place.
def printWord(word, guesses):
  printedWord = ""
  for x in range(0, len(word)):
    guessed = false
    if guesses.count(word[x]) > 0:
      printedWord += word[x] + " "
    else:
      printedWord += "_ "
  printNow(printedWord)
#This determines if the word has been guessed based on a list of the user's guesses.
#If the user's guesses contain all of the letters, the word is considered guessed.
def wordGuessed(word, guesses):
  guessed = true
  if len(guesses) >= len(word):
    for x in range(0, len(word)):
      if guesses.count(word[x]) == 0:
        guessed = false
  else:
    guessed = false
  return guessed
#This pulls a random word and definition from vocabula.com
def getWordAndDefinition():
  import urllib2
  response = urllib2.urlopen('http://www.vocabula.com/feature/definitions.aspx')
  html = response.read()
  #The actual word and definition must be parsed from the HTML.
  word = html.split('<span id="lblWord" class="Word">')[1].split('<')[0].lower()
  definition = html.split('<span id="lblDefinition" class="Definition">')[1].split('<')[0]
  wordList = []
  wordList.append(word)
  wordList.append(definition)
  return wordList
#The main entry point to the hangman game.
def playHangman():
  wordAndDefinition = getWordAndDefinition() #Retrieve a word and definition.
  word = wordAndDefinition[0] #Change here if you want a specific word.
  definition = wordAndDefinition[1]
  guess = 0
  guesses = []
  #Print the rules
  printNow("Welcome to Hang Man!")
  printNow("A word will be randomly chosen and a definition will be given as a hint.")
  printNow("You can guess the word letter by letter when prompted.")
  printNow("The correct letter will be displayed when you uncover it.")
  printNow("If you guess incorrectly, the hang man will be drawn.")
  printNow("Once he is fully drawn (once you have incorrectly guessed 6 times),")
  printNow("it is game over.")
  printNow("If you guess the word correctly, hang man will live.")
  printNow("Please, help the hang man!")
  #This is the main game loop for the program. It will continue until guesses run out
  #or the word is guessed.
  while guess < 6 and wordGuessed(word, guesses) == false:
    printNow("You have used %s of 6 guesses." % guess)
    printNow("Word Hint: " + definition) #Give the word hint.
    letter = requestString("Guess a letter: ").lower()
    if len(letter) > 1 or letter.isalpha() == false:
      printNow("Letters only please!")
    elif guesses.count(letter) > 0:
      printNow("You already guessed that letter! Pick another!")
    elif word.count(letter) > 0:
      printNow("Correct!")
      guesses.append(letter[0])
    else:
      printNow("Incorrect. =(")
      guesses.append(letter[0])
      guess += 1
    drawHangman(guess) #Draw the hangman in whatever state he is in.
    printWord(word, guesses) #Print the word (with _ for letters that haven't been guessed).
    printNow("Incorrect guesses: ")
    guessString = ""
    #This loop iterates through all of the user's incorrect guesses
    #and displays them.
    for x in range(0, len(guesses)):
      if word.count(guesses[x]) == 0: #If the word does not contain the guess, then don't print the guess.
        guessString += guesses[x] + " "
    printNow(guessString)
  printNow("You have used %s of 6 guesses." % guess)
  #If all of the guesses have been used, then game over!
  if guess == 6:
    printNow("GAME OVER!: Sorry, better luck next time!")
    printNow("The word was " + word)
  else: #Otherwise, if the former while loop is over and you still have guesses, then you've won! Good job!
    printNow("Congratulations! You live for now...")
    drawWinningMan() #Draw the free hang man.
playHangman()