"""
----------------------
Creator : Pluto
Last Edited : 26/2/2020
Usage : Cleans Up Main File, Pretty much just a dump of functions
License : www.gnu.org/licenses/lgpl-3.0.txt
Repository : https://github.com/PlvtoV2/LuckyUnicorn/blob/master/LuckyUnicorn.py
----------------------
"""

import random
import sys


def enter():
    enter = input("Press Enter To Start")
    while enter != "":
        enter = input("Press Enter To Start\n")


def newline():
    print("-----------------------------------")


def randomanimal():
    token = ["zebra", "horse", "donkey", "unicorn"]
    animal = random.choice(token)
    cost = 1
    print("How much money would you like to deposit into the machine?")
    newline()
    startingMoney = int(float(input("")))
    newline()
    while startingMoney > 10:
        print("You Only Have $10")
        startingMoney = int(float(input("")))
        newline()

    if animal == "zebra":
        won = cost - .50
        balance = startingMoney + won
        print("Oh no! you just lost 50c, You rolled a %s, Your Balance is now $%s" % (
            animal, balance))

    elif animal == "horse":
        won = cost - .50
        balance = startingMoney + won
        print("Oh no! you just lost 50c, You rolled a %s, Your Balance is now $%s" % (
            animal, balance))

    elif animal == "donkey":
        won = 0 - cost
        balance = startingMoney + won
        print("Oh no! you just lost $1, You rolled a %s, Your Balance is now $%s" % (
            animal, balance))

    elif animal == "unicorn":
        won = 5
        balance = startingMoney + won
        print("Congratulations You Won $%s, You rolled a %s, Your Balance is now $%s" % (
            won, animal, balance))
    newline()
    print("Would You Like To Continue (yes/no)")
    newline()
    answer = input("").lower()
    yes1 = "yes"
    newline()
    while answer == yes1:
        animal = random.choice(token)
        if animal == "zebra":
            won = cost - .50
            balance = balance + won
            print("Oh no! you just lost 50c, You rolled a %s, Your Balance is now $%s" % (
                animal, balance))

        elif animal == "horse":
            won = cost - .50
            balance = balance + won
            print("Oh no! you just lost 50c, You rolled a %s, Your Balance is now $%s" % (
                animal, balance))

        elif animal == "donkey":
            won = 0 - cost
            balance = balance + won
            print("Oh no! you just lost $1, You rolled a %s, Your Balance is now $%s" % (
                animal, balance))

        elif animal == "unicorn":
            won = 5
            balance = balance + won
            print("Congratulations You Won $%s, You rolled a %s, Your Balance is now $%s" % (
                won, animal, balance))
        newline()
        print("Would You Like To Continue (yes/no)")
        newline()
        answer = input("").lower()
    if answer == "no":
        newline()
        sys.exit()