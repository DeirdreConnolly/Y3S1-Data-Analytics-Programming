# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 13:08:27 2019

@author: Deirdre
"""


# =============================================================================
# Q1
# =============================================================================
length1 = int(input("Enter length of rectangle 1: "))
width1 = int(input("Enter width of rectangle 1: "))
length2 = int(input("Enter length of rectangle 2: "))
width2 = int(input("Enter width of rectangle 2: "))

area1 = (length1 * width1)
area2 = (length2 * width2)

if (area1 > area2):
    print("\nRectangle 1 is bigger than rectangle 2")

elif (area1 < area2):
    print("\nRectangle 2 is bigger than rectangle 1")

else:
    print("\nRectangle 1 and rectangle 2 are the same size")


# =============================================================================
# Q2
# =============================================================================
commercialSoftDevExperience = int(input("How many years of commercial software development experience do you have? "))
MicrosoftCertification = input("Do you hold a Microsoft certification? (y/n) ")
firstClassHonoursUndergradComputingDegree = input("Do you have a First Class Honours in an Undergraduate Computing Degree? (y/n) ")

# Nested if statement method
if (commercialSoftDevExperience >= 4):

    if (MicrosoftCertification == "y"):

        if (firstClassHonoursUndergradComputingDegree == "y"):
            print("\nYou are eligible.")

        else:
            print("\nYou are not eligible, you need a First Class Honours in an Undergrad Computing Degree.")

    else:
        print("\nYou are not eligible, you need a Microsoft certification.")

else:
    print("\nYou are not eligible, you need more than 4 years of commercial software development experience.")


# Single if statement method
if ((commercialSoftDevExperience >= 4) and (MicrosoftCertification == "y") and (firstClassHonoursUndergradComputingDegree == "y")):
    print("\nYou are eligible.")
else:
    print("\nYou are not eligible.")


# =============================================================================
# Q3
# =============================================================================
quantity = int(input("Packages purchased: "))
price = 99
discount = 0
total = (price * quantity)

# Quantity    Discount
# 1 – 9       0%
# 10 – 19     20%
# 20 – 49     30%
# 50 – 99     40%
# 100+        50%

if (1 <= quantity <= 9):
    total = (total)
    print("Discount: €" + str(discount))
    print("Total: €" + str(total))

elif (10 <= quantity <= 19):
    discount = (.2 * total)
    total = ((quantity * price) - discount)
    print("Discount: €" + str(discount))
    print("Total: €" + str(total))

elif (20 <= quantity <= 49):
    discount = (.3 * total)
    total = ((quantity * price) - discount)
    print("Discount: €" + str(discount))
    print("Total: €" + str(total))

elif (50 <= quantity <= 99):
    discount = (.4 * total)
    total = ((quantity * price) - discount)
    print("Discount: €" + str(discount))
    print("Total: €" + str(total))

elif (quantity >= 100):
    discount = (.5 * total)
    total = ((quantity * price) - discount)
    print("Discount: €" + str(discount))
    print("Total: €" + str(total))

else:
    print("Please enter a valid number.")


# =============================================================================
# Q4
# =============================================================================
#num = int(input("Number: "))
#limit = int(input("Stop at: "))
#print()
#
#
#def multiply(num, limit):
#
#    for i in range(0, limit + 1):
#        print(num, "x", i, "=", (num * i))
#
#
#multiply(num, limit)


# Desired output:
# 1
# 22
# 333
# 4444
# 55555


triangleSize = int(input("Enter size of triangle: "))


def printNumTriangle():

    for num in range(triangleSize + 1):
        for i in range(num):
            print(num, end=" ")
        print("\n")


printNumTriangle()


# =============================================================================
# Q5
# =============================================================================
import statistics

numOfMonths = int(input("How many months of data do you wish to enter: "))

for i in range(numOfMonths):
    rainfall = input("Rainfall for month %i: ")

average = int(sum(rainfall) / int(len(rainfall)))
print("Average rainfall recorded:", average)
print("Lowest rainfall recorded:", min(rainfall))
print("Highest rainfall recorded:", max(rainfall))

print(statistics.mean(rainfall))







