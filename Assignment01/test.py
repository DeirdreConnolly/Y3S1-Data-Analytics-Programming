#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Second Assessment - Programming for df Analytics
"""

# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Data
df = pd.read_csv("fery.csv", encoding = "ISO-8859-1")
# --> Need to clean data (weeks 4 & 9)
# --> Can submit CSV file with submission
# --> Explain why


# Please write your name and student ID:

# Deirdre Connolly
# R00112962

#
## =============================================================================
## TASK 1
## =============================================================================
#def task1():
#
#
#    #your implementation for task 1 goes here
#    print("\n>>> Q1")
#
#    male = df["sex"] == "Male"
#    female = df["sex"] == "Female"
#    maleWorkclass = df["workclass"][male].value_counts()
#    femaleWorkclass = df["workclass"][female].value_counts()
#
#    labels = ["Private", "Self-emp-inc", "Self-emp-not-inc", "Local-gov",
#              "Federal-gov", "State-gov", "Without-pay", "Never-worked", "?"]
#
#    width = 0.4
#    index = np.arange(0, 9)
#    plt.figure(figsize=(15, 5))
#
#    plt.bar(index-0.2, maleWorkclass, width, color="blue", align="center")
#    plt.bar(index+0.2, femaleWorkclass, width, color="orange")
#
#    plt.xlabel("Work class")
#    plt.ylabel("Number of people")
#    plt.title("Distribution of all work classes for different genders")
#    plt.legend(["Male", "Female"], loc = 0)
#    plt.xticks(index, labels)
#    plt.show()
#
#
#task1()
#
##comment for task1:
## Ans: The majority of both males and females work in the private sector
#
#
## =============================================================================
## TASK 2
## =============================================================================
#def task2():
#
#
#    #your implementation for task 2 goes here
#    print("\n>>> Q2")
#
#    female = df[df["sex"] == "Female"]
#    education = female.groupby("education")["hours-per-week"].mean()
#    print(education)
##    print(np.std(education))
#
#    width = 0.4
#    index = np.arange(0, 16)
#    plt.figure(figsize=(10, 5))
#
#    plt.bar(index, education, width, color="violet", align="center")
#
#    plt.xlabel("Level of education")
#    plt.ylabel("Hours per week")
#    plt.title("Relationship between the level of education " +
#              "and their hours of work per week\n" +
#              "Females only")
#    plt.legend(["Female"], loc = 0)
#    plt.xticks(index, education.index.tolist(), rotation="90")
#    plt.show()
#
#
#task2()
#
##comment for task2:
## Ans: Females with a Doctorate degree work the most hours per week
## ??? has the largest varity of working hours
#
#
## =============================================================================
## TASK 3
## =============================================================================
#def task3():
#
#    #your implementation for task 3 goes here
#    print("\n>>> Q3")
#
#    country = (df["native-country"].value_counts().head())
#    print(country)
#
#    width = 0.4
#    index = np.arange(0, 5)
#    plt.figure(figsize=(5, 5))
#
#    plt.barh(index, country, width, color="red")
#
#    plt.xlabel("Number of entries")
#    plt.ylabel("Country")
#    plt.yticks(index, country.index.tolist())
#    plt.title("Country with maximum entries")
#    plt.show()
#
#
#task3()
#
##comment for task3:
## Ans: United States
#
#
## =============================================================================
## TASK 4
## =============================================================================
#def task4():
#
#
#    #your implementation for task 3 goes here
#    print("\n>>> Q3")
#
#    country = (df["native-country"].value_counts()[1:3])
#    print(country)
#
#    width = 0.4
#    index = np.arange(0, 2)
#    plt.figure(figsize=(5, 5))
#
#    plt.barh(index, country, width, color="red")
#
#    plt.xlabel("Number of entries")
#    plt.ylabel("Country")
#    plt.yticks(index, country.index.tolist())
#    plt.title("Countries with second and third maximum entires")
#    plt.show()
#
#
#task4()
#
##comment for task4:
## Ans: Second = Mexico, third = Unknown (?)
#
#
# =============================================================================
# TASK 5
# =============================================================================
def task5():


    #your implementation for task 5 goes here
    print("\n>>> Q5")

    age = df["age"].value_counts()
    workingHours = df["hours-per-week"].value_counts()

    labels = ["age"]

    width = 0.4
    index = np.arange(0, 9)

    plt.figure(figsize=(10, 5))

    plt.bar(labels, workingHours, width, color="blue")
#    plt.bar(labels, age, workingHours, width, color="green")
#    plt.bar(index, age, width, color="green")

    plt.xlabel("Age")
    plt.ylabel("Hours worked per week")
    plt.xticks(index, age.index.tolist())
#    plt.axis([0, 99, 0, 20000])
    plt.title("Relationship between age and hours worked per week")
    plt.show()


task5()

#comment for task5:


## =============================================================================
## TASK 6
## =============================================================================
##def task6():
#
#
#    #your implementation for task 6 goes here
#
#
##task6()
#
##comment for task6:
#
#
## =============================================================================
## TASK 7
## =============================================================================
##def task7():
#
#
#    #your implementation for task 7 goes here
#
#
##task7()
#
##comment for task7:
#
#
## =============================================================================
## TASK 8
## =============================================================================
##def task8():
#
#
#    #your implementation for task 8 goes here
#
#
##task8()
#
##comment for task8:
#
#
## =============================================================================
## TASK 9
## =============================================================================
##def task9():
#
#
#    #your implementation for task 9 goes here
#
#
##task9()
#
##comment for task9:
#
#
## =============================================================================
## TASK 10
## =============================================================================
##def task10():
#
#
#    #your implementation for task 10 goes here
#
#
##task10()
#
##comment for task10:
#
#
## =============================================================================
## TASK 11
## =============================================================================
##def task11():
#
#
#    #your implementation for task 11 goes here
#
#
##task11()
#
##comment for task11:
#
#
## =============================================================================
## TASK 12
## =============================================================================
##def task12():
#
#
#    #your implementation for task 12 goes here
#
#
##task12()
#
##comment for task12: