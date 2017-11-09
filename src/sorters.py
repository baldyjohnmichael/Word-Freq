def sortDictAlpha(dictionary):
    alphaSortedDict = {}
    keylist = dictionary.keys()
    keylist.sort()
    for key in keylist:
        alphaSortedDict[key] = dictionary[key]
        print(key + " : " + str(alphaSortedDict[key]))
    return alphaSortedDict

def sortDictFreq(dictionary):
    freqSortedDict = {}
    copyDict = dictionary
    while len(copyDict.keys()) > 0:
        nextBiggest = max(copyDict, key=copyDict.get)

        freqSortedDict[nextBiggest] = copyDict[nextBiggest]
        del copyDict[nextBiggest]
        print(nextBiggest + " : " + str(freqSortedDict[nextBiggest]))
    return freqSortedDict
