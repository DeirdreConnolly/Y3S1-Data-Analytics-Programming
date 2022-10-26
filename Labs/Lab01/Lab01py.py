# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 13:05:06 2019

@author: Deirdre
"""


# =============================================================================
# Q2
# =============================================================================
name = "Mary"
age = 17

print("Hello 'Python'")
print('Hello "Python"')

print("\nName:", name, "\nAge:", age,)


# =============================================================================
# Q3
# =============================================================================
distance = float(input("Enter distance (km): "))
miles = (distance * 0.6214)

print("The distance is", miles, "miles.")


# =============================================================================
# Q4
# =============================================================================
fName = input("Enter your first name: ")
sName = input("Enter your surname: ")
grade1 = int(input("Enter your grade: #1 "))
grade2 = int(input("Enter your grade: #2 "))
grade3 = int(input("Enter your grade: #3 "))

print("Name: ", fName, sName, "\tGrades: ", grade1, grade2, grade3)


# =============================================================================
# Q5
# =============================================================================
weight = int(input("Enter weight (lbs): "))
height = int(input("Enter height (inches): "))
BMI = ((weight / height) * 703)

print("Your BMI is: ", BMI)


# =============================================================================
# Q6
# =============================================================================
classA = 25
classB = 20
classC = 30

classA_sold = int(input("Number of Class A tickets sold: "))
classB_sold = int(input("Number of Class B tickets sold: "))
classC_sold = int(input("Number of Class C tickets sold: "))

classA_income = (classA * classA_sold)
classB_income = (classB * classB_sold)
classC_income = (classC * classC_sold)
totalIncome = (classA_income, classB_income, classC_income)

print("Total income: €", sum(totalIncome))


# =============================================================================
# Q7
# =============================================================================
name = input("Enter your name: ")
age = int(input("Enter your age: "))
months = (age * 12)
days = (age * 365)

print()
print(name, "is", months, "months old.",
      name, "is", days, "days old.")


# =============================================================================
# Q8
# =============================================================================
radius = float(input("Enter radius of circle: "))
area = (3.14 * (radius * radius))

print("Area:", area, "\tType:", type(area))
