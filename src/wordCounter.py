# Where parsed strings go to have their frequencies counted.
# Keep track of words and their frequencies via a dict
# dict = {word, int, ... }
# Where word is a word from the string being observed and int is that words frequency
from sorters import *
globalDict = {}
def addToDict(word, dictionary):
    dictionary[word] = 1
    return globalDict


def wordInDict(word, dictionary):
    if dictionary.has_key(word):
        return True
    else:
        return False

def increaseCount(word, dictionary):
    newCount = dictionary[word]
    newCount = newCount + 1
#    globalDict[word] = {newCount}

    dictionary[word] = newCount


# iterates through string
# returns with an unsorted dictionary
# with the keys being the words
# and the values being the number of times
# they appear in the words string
def iterString(words, dictionary):
    wordList = words.split(' ')
    for word in wordList:
        if not dictionary.has_key(word):
            addToDict(word, dictionary)
        else:
            increaseCount(word, dictionary)
    if '' in dictionary:
        del dictionary['']

# def sortDictAlpha(dictionary):
#     alphaSortedDict = {}
#     keylist = dictionary.keys()
#     keylist.sort()
#     for key in keylist:
#         alphaSortedDict[key] = dictionary[key]
#         print(key + " : " + str(alphaSortedDict[key]))
#     return alphaSortedDict

# def sortDictFreq(dictionary):
#     keylist = dictionary.keys()
#     keylist.sort()
#     for key in keylist:
#         print(key, dictionary[key])

def prettyPrint(dictionary):
    for key in dictionary:
        print(key + " : " + str(dictionary[key]))

def main():
    chString = ""
    f = open('../test-docs/bc1-3.txt', 'r')
    for line in f:
        chString = chString + line
    chString = chString.replace('\n',' ').replace('\r',' ').replace(',','').replace('.', '')
    chDict = {}
    iterString(chString, chDict)
    #sortDictFreq(globalDict)


    sortDictAlpha(chDict)
    mostCommon = max(chDict, key=globalDict.get)
    #print(mostCommon + " : " + str(globalDict[mostCommon]) )
    f.close()
