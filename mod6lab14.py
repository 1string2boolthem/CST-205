import re
def wordCount(wordDict):
  count = 0
  for key in wordDict:
    count += wordDict[key]
  return count
def mostCommonWord(wordDict):
  word = ""
  count = 0
  for key in wordDict:
    if wordDict[key] > count:
      word = key
      count = wordDict[key]
  return word
def printHeadlines():
  file = open(pickAFile(), "rt")
  data = file.read()
  file.close()
  blocks = data.split("rel=\"bookmark\">")
  for i in range(1, len(blocks)):
    block = str(blocks[i].split("</a")[0])
    block = block.strip()
    block = block.replace("&nbsp;", ' ')
    block = block.replace("&#8230;", "...")
    block = block.replace('â', '\'')
    block = block.replace('™', '')
    block = block.replace(chr(128), '')
    printNow(block)
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
printHeadlines()