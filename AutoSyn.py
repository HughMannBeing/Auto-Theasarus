import requests
from bs4 import BeautifulSoup
from sys import argv
import re
import random

#Approved by #5

script, phrase = argv
words = phrase.split()

def cleanhtml(rawHtml):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', rawHtml)
  return cleantext

def getSynonym(word):
    cleanSynonyms = []
    page = requests.get("http://www.thesaurus.com/browse/" + word)
    c = page.content
    soup = BeautifulSoup(c, "lxml")
    synonyms = soup.find_all("span", "text")
    for i in synonyms:
        cleanSynonyms.append(cleanhtml(str(i)))
    return cleanSynonyms[0:(int)(len(cleanSynonyms) / 3)]

def createFalse():
    finalSentence = ""
    for word in words:
        possibleWords = getSynonym(str(word))
        if (len(possibleWords) > 0):
            finalSentence += random.choice(possibleWords)
            finalSentence += " "
        else:
            finalSentence += "detergent"
            finalSentence += " "
    return finalSentence
print (createFalse())
