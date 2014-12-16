#Module 7 Lab 16
#Team 3
#Christopher Rendall
#Sevren Gail

import re #For regular expressions, to replace an undetermined number of spaces in eggs.txt.
#wordCount counts the number of total words in wordDict and returns the result.
def wordCount(wordDict):
  count = 0
  for key in wordDict:
    count += wordDict[key]
  return count
#mostCommonWord finds the word that occurs the most in dictionary wordDict.
def mostCommonWord(wordDict):
  word = ""
  count = 0
  for key in wordDict:
    if wordDict[key] > count:
      word = key
      count = wordDict[key]
  return word
  
def getModifier(frequency): #returns the modifying html based on the frequency of a word
  size = 7 + int(frequency/10)
  modifier = "<span style=\"font-size:" + str(size) + "pt "
  if frequency == 1:
    modifier += "color:LightGreen"
  elif frequency < 10:
    modifier += "color:green>"
  elif frequency < 30:
    modifier += "color:purple>"
  elif frequency < 50:
    modifier += "color:blue>"
  elif frequency < 70:
    modifier += "color:orange; font-weight:bold>"
  elif frequency == 84:
    modifier += "color:DarkRed; font-weight:bold>"
  else:
    modifier += "color:red; font-weight:bold>"
  return modifier
#greenEggs reads the eggs.txt file input by the user, creates a dictionary with each unique word as a key
#and the key's value as the number of times that word occurs in the text. It also prints various
#information to an html document, as per specifications.
def greenEggs():
  printNow("Provide eggs.txt.")
  file = open(pickAFile(), "rt")
  data =  file.read()
  fileData = data
  file.close()
  data = data.replace('\n', ' ')
  data = data.replace('-', ' ')
  data = re.sub(' +', ' ', data)
  wordList = data.split(' ')
  wordDict = {}
  for word in wordList:
    if wordDict.has_key(word.lower()):
      wordDict[word.lower()] += 1
    else:
      wordDict[word.lower()] = 1
  for key in wordDict:
    printNow(key + ": " + str(wordDict[key]))
  content = "<h1>Green Eggs & Ham!</h1>"
  content += "Number of words in \"Green Eggs & Ham\": " + str(wordCount(wordDict)) + "<br />"
  content += "Number of unique words in \"Green Eggs & Ham\": " + str(len(wordDict)) + "<br />"
  content += "The most common word in \"Green Eggs & Ham\": " + mostCommonWord(wordDict) + "<br />"
  content += "Now, for a visual representation: <br /><br />"
  data = fileData
  data = data.replace('\n', "<br>")
  data = data.replace('-', ' ')
  data = re.sub(' +', ' ', data)
  words = data.replace("<br>", " <br> ")
  words = words.split(' ')
  wordList = []
  data = ""
  for word in range(len(words)):
    if words[word] != "<br>" and words[word] != '':
      frequency = wordDict[words[word].lower()]
      modifier = getModifier(frequency)
      data += modifier + words[word] + "</span> "
    else:
      data += "<br>"
  content += data
  makePage(content)

#makePage writes content to a user-supplied html page.
def makePage(content):
  printNow("Choose an HTML file to write to.")
  file = pickAFile()
  file = open(file, "wt")
  data = "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.01 Transition//EN" "http://www.w3.org/TR/html4/loose.dtd\"><html><head><title>MiniLab</title></head><body>" + content + "</body></html>"
  file.write(data)
  file.close()