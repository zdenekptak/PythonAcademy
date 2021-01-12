import random
from datetime import datetime

def splitChar(string):
    return [int(char) for char in string]

def numberBulls(digitsList, myNumberList):
    bulls = 0
    for indexDl, dl in enumerate(digitsList):
        for indexNl, nl in enumerate(myNumberList):
            if indexDl == indexNl and dl == nl:
                bulls += 1
    return bulls

def numberCows(digitsList, myNumberList):
    cows = 0
    for n in myNumberList:
        if n in digitsList:
            cows += 1
    return cows

def myNumber():
    myNumber = input("Enter a number: ")
    myNumberList = splitChar(myNumber)
    return myNumberList


print('''
Hi there!
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
''')

digitsList = random.sample(range(10), 4)
print(digitsList)

bulls = 0
count = 0
start_time = datetime.now()

while bulls < 4:
    myNumberList = myNumber()
    bulls = numberBulls(digitsList, myNumberList)
    cows = numberCows(digitsList, myNumberList)
    actualCows = cows - bulls
    count += 1
    print(f"Actual bulls is: {bulls} and cows is: {actualCows}")

end_time = datetime.now()
duration = end_time - start_time
durationModif = str(duration)[:-5]

print(f"You won, you have {bulls} bulls. You number of attempts is {count}")
print(f"Yours number of attempts was {count} and time was {durationModif}")