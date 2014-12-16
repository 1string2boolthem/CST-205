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
#greenEggs reads the eggs.txt file input by the user, creates a dictionary with each unique word as a key
#and the key's value as the number of times that word occurs in the text. It also prints various
#information to an html document, as per specifications.
def greenEggs():
  printNow("Provide eggs.txt.")
  file = open(pickAFile(), "rt")
  data =  file.read()
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
  content += "Now, for a visual representation: <br />"
  makePage(content)

#makePage writes content to a user-supplied html page.
def makePage(content):
  printNow("Choose an HTML file to write to.")
  file = pickAFile()
  file = open(file, "wt")
  data = "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.01 Transition//EN" "http://www.w3.org/TR/html4/loose.dtd\"><html><head><title>MiniLab</title></head><body>" + content + "</body></html>"
  file.write(data)
  file.close()