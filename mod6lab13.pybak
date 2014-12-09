####################
# CST-205          #
# Module 6 Lab 13  #
# Sevren Gail      #
# Chris Rendall    #
####################

story = "A Mysterious Giant Legoman Has Appeared On A Japanese Beach\n\nSometime Wednesday, an unusual sight washed up on the shores of Yuigahama beach in the Japanese city of Kamakura. The giant Lego figurine came with a few clues reportedly noted by Tatsuya Hirata, the surfer who happened on the robot man. At more than eight feet, it was dressed in blue pants and a red shirt that proclaimed, \"No Real Than You Are,\" on its front. On the back, it bore the name \"Ego Leonard.\"\n\nYou can almost hear the UFO conspiracists ascending their soap boxes. Sadly though, there's an all too corporeal explanation, as any fan of street art knows. Every practitioner has his thing: Invader sprinkles Pacman faces on the biggest buildings in the world, Banksy turns unremarkable walls into attractions with his signature stencils. And at least since 2007, the anonymous Dutch guerrilla artist Ego Leonard has dispatched Legomen, sending them emblazoned with his motto into great water bodies.\n\nSightings of Leonard's big yellow men mostly occur in the Western hemisphere, specifically, off a sea in the Netherlands, at Brighton Beach in the United Kingdom, and on a Florida beach. There's seemingly been no rhyme or reason to these landings. Of course, onlookers haven't shied away from offering theories to local news stations -- including, naturally, ones about \"UFO people.\""

def replaceWord(word, newWord, text):
  text = text.replace(word, newWord)
  text = text.replace(word.lower(), newWord.lower())
  text = text.replace(word.upper(), newWord.upper())
  text = text.replace(word.capitalize(), newWord.capitalize())
  return text

def getReplacements(words, text):
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
  return text

words = {}

words["unusual"] = 2
words["clue"] = 0
words["eight"] = 0
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
words["ego"] = 1
words["guerrilla"] = 0

story = getReplacements(words, story)

printNow("")
printNow(story)
