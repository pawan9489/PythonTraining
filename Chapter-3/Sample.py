# https://www.hackerrank.com/challenges/the-minion-game/problem?isFullScreen=true

word = "apple"

# list of Substrings
#  -> Group By Vowel Starting Words
#  -> Count the words in 2 groups
#  -> Max is the Winner


def listOfSubstrings(s):
    lst = []
    l = len(s)
    for i in range(1, l + 1):  # Size of SubString
        for j in range(0, l):
            t = s[j : j + i]
            if len(t) == i:
                # print(s[j: j + i])
                lst.append(s[j : j + i])
    return lst


subLists = listOfSubstrings(word)
print("------- SubLists ---------")
print(subLists)


def groupByVowelStart(lst):
    vLst = []  # Vowels
    cLst = []  # Consonants
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    for i in lst:
        if i[0] in vowels:
            vLst.append(i)
        else:
            cLst.append(i)
    return (vLst, cLst)


print("------- Group By ---------")
groupedLists = groupByVowelStart(subLists)
print(groupedLists)


def declareWinner(groupedLists):
    # (VowelsList, ConsonantsList)
    vLen = len(groupedLists[0])
    cLen = len(groupedLists[1])
    if vLen == cLen:
        return 'Draw'
    elif vLen > cLen:
        return 'Kevin {0}'.format(len(groupedLists[0]))
    else:
        return 'Stuart {0}'.format(len(groupedLists[1]))


print("------- Declare Winner ----------")
winner = declareWinner(groupedLists)
print(winner)

def result(s):
    vLen = 0
    cLen = 0
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    l = len(s)
    for i in range(1, l + 1): # Size of SubString
        for j in range(0, l):
            if j + i <= l:
                # t = s[j: j + i]
                if s[j] in vowels:
                    vLen += 1
                else:
                    cLen += 1
    return "Draw" if vLen == cLen else "Kevin {0}".format(vLen) if vLen > cLen else "Stuart {0}".format(cLen) 
print(word)
print(result(word))

def result2(string):
    # Calculate in One Single GO
    # UnNecessary Calculations
    textLen = len(string)
    vLen = 0
    cLen = 0
    for (index, character) in enumerate(string):
        if character in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            vLen += textLen - index
        else:
            cLen += textLen - index
    return "Draw" if vLen == cLen else "Kevin {0}".format(vLen) if vLen > cLen else "Stuart {0}".format(cLen) 
print(word)
print(result2(word))

