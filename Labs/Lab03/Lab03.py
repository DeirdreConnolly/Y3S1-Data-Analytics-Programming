# -*- coding: utf-8 -*-


import math


"""
Created on Mon Sep 30 12:14:31 2019

@author: Deirdre
"""


# =============================================================================
# Q1
# =============================================================================

def main():
    powerV1()
    powerV2()


def powerV1():
    baseNumber = int(input("Enter base number: "))
    powerNumber = int(input("Enter power number: "))
    ans = pow(baseNumber, powerNumber)

    print("The value", str(baseNumber), "raised to the power of", str(powerNumber), "is:", str(ans))


def powerV2():
    # A = B^C
    valueA = int(input("Enter value of A: "))
    valueB = int(input("Enter value of B: "))
    valueC = math.log(valueA, valueB)

    print("The logarithm of", int(valueA), "with base", int(valueB), "is:", int(valueC))


main()


# =============================================================================
# Q2
# =============================================================================

from random import randrange


def main():
    rand = generateRandomNumber()
    guess = askUser()
    checkGuess(rand, guess)


def generateRandomNumber():
    rand = randrange(100)
    print("Program has generated a random number: ", int(rand))

    return rand


def askUser():
    guess = int(input("Please enter your guess: "))

    return guess


def checkGuess(rand, guess):

    count = 1

    while True:

        if count > 1:
            guess = askUser()

        # Too high
        if (guess > rand):
            print("Too high!")
            count += 1

        # Too low
        elif (guess < rand):
            print("Too low!")
            count += 1

        # Correct
        elif (guess == rand):
            print("Correct. You made a total of", count, "guesses.")
            break


main()
