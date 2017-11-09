# Where it all comes together
from wordCounter import *
from sorters import *

def printDict(dictionary):
    for key in dictionary:
        print(key + " : " + str(dictionary[key]))

def main():
    # print("Hello Words!")
    chString = ""
    # f = open('../test-docs/bbsEthics.txt', 'r')
    f = open('../test-docs/bc1-3.txt', 'r')
    for line in f:
        chString = chString + line
    chString = chString.replace('\n',' ').replace('\r',' ').replace(',','').replace('.', '').replace('\'','').replace('"','').replace('[','').replace(']','')
    chDict = {}
    iterString(chString, chDict)
    #sortDictFreq(globalDict)


    sortedDict = sortDictAlpha(chDict)
    # dictSortedFreq = sortDictFreq(chDict)
    printDict(sortedDict)
    # print("Most frequent word- " + max(sortedDict, key=sortedDict.get) + " : " + str(sortedDict[max(sortedDict, key=sortedDict.get)]))    # print(len(sortedDict.keys()))
    #print(mostCommon + " : " + str(globalDict[mostCommon]) )
    f.close()

main()
