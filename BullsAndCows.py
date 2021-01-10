import random


def splitchar(string):
    return [int(char) for char in string]


digitsList = random.sample(range(10), 4)
print(digitsList)

myNumber = input("Uhodni čtyrmístné číslo: ")
myNumberList = splitChar(myNumber)
print(myNumberList)

bulls = 0
cows = 0

for indexDl, dl in enumerate(digitsList):

    for indexNl, nl in enumerate(myNumberList):
        if indexDl == indexNl and dl == nl:
            bulls += 1
        elif nl != dl and nl in digitsList:
            cows += 1
            print(cows)
print(bulls)
print(cows)
