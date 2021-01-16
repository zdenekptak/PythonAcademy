import random
from datetime import datetime


def guessedNumber():
    """Funkce která vygeneruje náhodné čtyř místné číslo bez opakování číslic a nuly na začátku"""
    # List s nulou na zacatku
    digitsList = [0]
    # Dokud bude nula na zacatku budu generovat novy list
    while digitsList[0] == 0:
        digitsList = random.sample(range(10), 4)
    # Cislo prepsane na string
    digitsListString = ''.join(map(str, digitsList))
    # Vracime list pro dalsi pouziti ve fci
    return digitsList


def splitChar(string):
    """ Funkce ktera rozdeli string na list"""
    return [int(char) for char in string]


def numberBulls(digitsList, myNumberList):
    """ Funkce ktera nam vrati pocet bullu"""
    bulls = 0
    # Smycka pres listy hadaneho cisla a vlozeneho cisla pomoci ktere spocítam pocet bull
    for indexDl, dl in enumerate(digitsList):
        for indexNl, nl in enumerate(myNumberList):
            if indexDl == indexNl and dl == nl:
                bulls += 1
    return bulls


def numberCows(digitsList, myNumberList):
    """ Funkce ktera nam vrati pocet pomocných cows"""
    helpCows = 0
    for n in myNumberList:
        if n in digitsList:
            helpCows += 1
    return helpCows


def myNumber():
    """ Funkce pro vlozeni vlastniho cisla, která zkontroluje zda číslo neobshuje špatné znaky (písmena, znaménka ...)"""
    # Uložíme vstup od uživatele
    myInputStr = input("Enter a number: ")
    # Nastavme podmínku pro opakované zadaní čísla přo špatném znaku
    x = True
    while x:
        # Pokud je vstup číselný vrátíme seznam
        if myInputStr.isdigit():
            myNumberList = splitChar(myInputStr)
            return myNumberList
        # Pokud není vstup číselný vložíme znovu vstup
        else:
            myInputStr = input("There are bad characters in the number. Insert it again: ")

def testSameDigits(seznam):
    """ Kontrola aby nebyly stejne cisla"""
    # uložení delky seznamu do proměnné
    delkaSeznamu = len(seznam)
    x = 0
    # Dokud platí podmínka
    while x < delkaSeznamu:
        # Vezmu prvek se list smažu ho a zároveň porovnám se zbytkem listu
        number = seznam.pop()
        if number in seznam:
            return False
        x += 1
    return True

def main():
    """ Funkce pro spusteni celeho skriptu"""

    print('''
    Hi there!
    I've generated a random 4 digit number for you. Digit must not be repeated.
    Let's play a bulls and cows game.
    ''')

    digitsList = guessedNumber()
    # Radek pro kontrolu funkcnosti programu, aby jsem nemusel cislo dlouho hadat
    # print(digitsList)
    bulls = 0
    count = 0

    # cas zacatku hadani
    start_time = datetime.now()

    # Podminka ktera musi byt splnena pro dokonceni hry
    while bulls < 4:
        myNumberList = myNumber()
        sameDigits = list(myNumberList)
        ed = testSameDigits(sameDigits)
        # Podmínka pro kontrolu prvního čísla - nesmí být 0
        if myNumberList[0] != 0:
            # Kontrola správné délky vstupního čísla
            if len(myNumberList) == 4:
                # kontrola jestli číslo neobsahuje stejné číslice
                if ed == True:
                    bulls = numberBulls(digitsList, myNumberList)
                    helpCows = numberCows(digitsList, myNumberList)
                    cows = helpCows - bulls
                    count += 1
                    print(f"Actual bulls is: {bulls} and cows is: {cows}")
                else:
                    print(f"The number may not contain the same digits. Insert number again.")
            else:
                print(f"The number is the wrong length (max length is 4). Insert number again.")
        else:
            print(f"Number cannot start with zero. Insert number again.")
    # cas konce hadani
    end_time = datetime.now()
    duration = end_time - start_time
    # cas potrebny k uhodnuti cisla
    durationModif = str(duration)[:-5]

    # Vypiseme vysledky
    print()
    print(f"You won, you have {bulls} bulls.")
    print(f"Yours number of attempts was {count} and time was {durationModif}.")
    print()


main()