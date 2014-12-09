#Sevren Gail
#Christopher Rendall
#Team 3 - Lab 14

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
#printHeadlines() prints the headlines in The Otter Realm.
def printHeadlines():
  file = open(pickAFile(), "rt")
  data = file.read()
  file.close()
  blocks = data.split("rel=\"bookmark\">")
  printNow("*** Otter Realm Breaking News! ***")
  for i in range(1, len(blocks)):
    block = str(blocks[i].split("</a")[0])
    block = block.strip()
    block = block.replace("&nbsp;", ' ') #Replace html space character.
    block = block.replace("&#8230;", "...") #Replace the encoded ellipsis with an ellipsis
    block = block.replace('â', '\'') #Replace this character with an apostrophe.
    block = block.replace('™', '') #Replace this with nothing.
    block = block.replace(chr(128), '') #Replace this weird space character with nothing.
    printNow(block) #Print the headline.
#greenEggs reads the eggs.txt file input by the user, creates a dictionary with each unique word as a key
#and the key's value as the number of times that word occurs in the text. It also prints various
#information as per specifications.
def greenEggs():
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
  printNow("Word counts per word:")
  for key in wordDict:
    printNow(key + ": " + str(wordDict[key]))
  printNow("Total number of words in this story: " + str(wordCount(wordDict)))
  printNow("Total number of unique words in this story: " + str(len(wordDict)))
  printNow("Most Common Word: " + mostCommonWord(wordDict))
greenEggs()
#printHeadlines()