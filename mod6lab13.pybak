<<<<<<< HEAD
####################
# CST-205          #
# Module 6 Lab 13  #
# Sevren Gail      #
# Chris Rendall    #
####################

#Here's the news story from : http://www.huffingtonpost.com/2014/12/05/giant-legoman-japan_n_6269082.html?ir=Travel?ncid=edlinkushpmg00000072
story = "A Mysterious Giant Legoman Has Appeared On A Japanese Beach\n\nSometime Wednesday, an unusual sight washed up on the shores of Yuigahama beach in the Japanese city of Kamakura. The giant Lego figurine came with a few clues reportedly noted by Tatsuya Hirata, the surfer who happened on the robot man. At more than eight feet, it was dressed in blue pants and a red shirt that proclaimed, \"No Real Than You Are,\" on its front. On the back, it bore the name \"Ego Leonard.\"\n\nYou can almost hear the UFO conspiracists ascending their soap boxes. Sadly though, there's an all too corporeal explanation, as any fan of street art knows. Every practitioner has his thing: Invader sprinkles Pacman faces on the biggest buildings in the world, Banksy turns unremarkable walls into attractions with his signature stencils. And at least since 2007, the anonymous Dutch guerrilla artist Ego Leonard has dispatched Legomen, sending them emblazoned with his motto into great water bodies.\n\nSightings of Leonard's big yellow men mostly occur in the Western hemisphere, specifically, off a sea in the Netherlands, at Brighton Beach in the United Kingdom, and on a Florida beach. There's seemingly been no rhyme or reason to these landings. Of course, onlookers haven't shied away from offering theories to local news stations -- including, naturally, ones about \"UFO people.\""

def replaceWord(word, newWord, text): #replaces word with newWord, considering case and replacing a with an & vice versa
  vowels = ["a","e","i","o","u", "A", "E", "I", "O", "U"]
  if newWord[0] in vowels:
    text = text.replace(" a " + word, " an " + newWord)
  else:
    text = text.replace(" an " + word, " a " + newWord)
  text = text.replace(word, newWord)
  text = text.replace(word.lower(), newWord.lower())
  text = text.replace(word.upper(), newWord.upper())
  text = text.replace(word.capitalize(), newWord.capitalize())
  return text

def getReplacements(words, text): # checks the type and prompts user for replacement word as appropriate
  for word in words:
    if words[word] == 0:
      text = replaceWord(word, raw_input("Enter a noun: "), text)
    elif words[word] == 1:
      text = replaceWord(word, raw_input("Enter a name: "), text)
    elif words[word] == 2:
      text = replaceWord(word, raw_input("Enter a adjective: "), text)
    elif words[word] == 3:
      text = replaceWord(word, raw_input("Enter a year (ex:1987): "), text)
    elif words[word] == 4:
      text = replaceWord(word, raw_input("Enter a place: "), text)
    elif words[word] == 5:
      text = replaceWord(word, raw_input("Enter an acronym (ex:ABC): "), text)
    elif words[word] == 6:
      text = replaceWord(word, raw_input("Enter a number: "), text)
  return text

words = {} #collection of words to be replaced

words["unusual"] = 2
words["clue"] = 0
words["eight"] = 6
words["street"] = 0
words["pacman"] = 1
words["unremarkable"] = 2
words["stencil"] = 0
words["2007"] = 3
words["leonard"] = 1
words["motto"] = 0
words["western"] = 2
words["florida"] = 4
words["netherlands"] = 4
words["ufo"] = 5
words["kamakura"] = 4
words["lego"] = 1
words["guerrilla"] = 0

story = getReplacements(words, story) # replace the words

printNow("")
printNow(story) # print the new story
=======
 story = ÒA Mysterious Giant Legoman Has Appeared On A Japanese Beach\n\nSometime Wednesday, an unusual sight washed up on the shores of Yuigahama beach in the Japanese city of Kamakura. The giant Lego figurine came with a few clues reportedly noted by Tatsuya Hirata, the surfer who happened on the robot man. At more than eight feet, it was dressed in blue pants and a red shirt that proclaimed, \"No Real Than You Are,\" on its front. On the back, it bore the name \"Ego Leonard.\"\n\nYou can almost hear the UFO conspiracists ascending their soap boxes. Sadly though, there's an all too corporeal explanation, as any fan of street art knows. Every practitioner has his thing: Invader sprinkles Pac-man faces on the biggest buildings in the world, Banksy turns unremarkable walls into attractions with his signature stencils. And at least since 2007, the anonymous Dutch guerrilla artist Ego Leonard has dispatched Legomen, sending them emblazoned with his motto into great water bodies.\n\nSightings of Leonard's big yellow men mostly occur in the Western hemisphere, specifically, off a sea in the Netherlands, at Brighton Beach in the United Kingdom, and on a Florida beach. There's seemingly been no rhyme or reason to these landings. Of course, onlookers haven't shied away from offering theories to local news stations -- including, naturally, ones about \"UFO people.\"\n\nLeonard himself seems to be egging that line of reasoning on, with a provocative bio on his website. Translated, it reads as if written by an extraterrestrial, or, more precisely, a figment of the Internet:\n\nMy name is Ego Leonard and according to you I come from the virtual world. A world that for me represents happiness, solidarity, all green and blossoming, with no rules or limitations. Lately however, my world has been flooded with fortune-hunters and people drunk with power. And many new encounters in the virtual world have triggered my curiosity about your way of life.\nWe've reached out to the artist for confirmation. In the meantime, check your giant Lego cars for any missing occupants.Ó
>>>>>>> FETCH_HEAD
