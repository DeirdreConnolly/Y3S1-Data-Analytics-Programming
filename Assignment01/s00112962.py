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
df.dropna(inplace=True)
df.income = [x.strip('.') for x in df.income]
#df.lstrip()

# --> Need to clean data (lecture notes weeks 4 & 9)
# --> Can submit CSV file with submission
# --> Explain why


# Please write your name and student ID:

# Deirdre Connolly
# R00112962


# =============================================================================
# TASK 1
# =============================================================================
def task1():


    #your implementation for task 1 goes here
    print("\n>>> Q1")

    male = df["sex"] == "Male"
    female = df["sex"] == "Female"
    maleWorkclass = df["workclass"][male].value_counts()
    femaleWorkclass = df["workclass"][female].value_counts()

    labels = ["Private", "Self-emp-inc", "Self-emp-not-inc", "Local-gov",
              "Federal-gov", "State-gov", "Without-pay", "Never-worked", "?"]

    width = 0.4
    index = np.arange(0, 9)
    plt.figure(figsize=(15, 5))

    plt.bar(index-0.2, maleWorkclass, width, color="deepskyblue")
    plt.bar(index+0.2, femaleWorkclass, width, color="deeppink")

    plt.xlabel("Work class")
    plt.ylabel("Number of people")
    plt.title("Distribution of all work classes for different genders")
    plt.legend(["Male", "Female"], loc = 0)
    plt.xticks(index, labels)
    plt.show()


task1()

#comment for task1:
# Ans: The majority of both males and females work in the private sector


# =============================================================================
# TASK 2
# =============================================================================
def task2():


    #your implementation for task 2 goes here
    print("\n>>> Q2")

    female = df[df["sex"] == "Female"]
    education = female.groupby("education")["hours-per-week"].mean()
    print(education)
#    print(np.std(education))

    width = 0.4
    index = np.arange(0, 16)
    plt.figure(figsize=(10, 5))

    plt.bar(index, education, width, color="violet", align="center")

    plt.xlabel("Level of education")
    plt.ylabel("Hours per week")
    plt.title("Relationship between the level of education " +
              "and their hours of work per week\n" +
              "Females only")
    plt.legend(["Female"], loc = 0)
    plt.xticks(index, education.index.tolist(), rotation="90")
    plt.show()


task2()

#comment for task2:
# Ans: Females with a Doctorate degree work the most hours per week
# ??? has the largest varity of working hours


# =============================================================================
# TASK 3
# =============================================================================
def task3():

    #your implementation for task 3 goes here
    print("\n>>> Q3")

    country = (df["native-country"].value_counts().head())
    print(country)

    width = 0.4
    index = np.arange(0, 5)
    plt.figure(figsize=(5, 5))

    plt.barh(index, country, width, color="darkviolet")

    plt.xlabel("Number of entries")
    plt.ylabel("Country")
    plt.yticks(index, country.index.tolist())
    plt.title("Country with maximum entries")
    plt.show()


task3()

#comment for task3:
# Ans: United States


# =============================================================================
# TASK 4
# =============================================================================
def task4():


    #your implementation for task 3 goes here
    print("\n>>> Q4")

    country = (df["native-country"].value_counts()[1:3])
    print(country)

    width = 0.4
    index = np.arange(0, 2)
    plt.figure(figsize=(5, 5))

    plt.barh(index, country, width, color="darkgreen")

    plt.xlabel("Number of entries")
    plt.ylabel("Country")
    plt.yticks(index, country.index.tolist())
    plt.title("Countries with second and third maximum entires")
    plt.show()


task4()

#comment for task4:
# Ans: 2nd = Mexico, 3rd = Unknown (?)


# =============================================================================
# TASK 5
# =============================================================================
#def task5():
#
#
#    #your implementation for task 5 goes here
#    print("\n>>> Q5")
#
#    age = df["age"]
##    workingHours = df["hours-per-week"]
#
#    xindex = np.arange(16, 100, step=2)
#    yindex = np.arange(16, 50, step=4)
#
#    ages = age.value_counts().sort_index().index.tolist()
#
#    dictionary = {}
#
#    for i in range(len(ages)):
#        agePos = df["age"] == ages[i]
#        hoursAge = df["hours-per-week"][agePos]
#        dictionary[ages[i]] = np.mean(hoursAge)
#
#    maxAge = max(dictionary, key=dictionary.get)
#
#    plt.plot([list(dictionary.keys())], [list(dictionary.values())])
#
#    plt.xticks(xindex)
#    plt.yticks(yindex)
#
#    plt.annotate("Max hour",
#                 xy=(maxAge, dictionary[maxAge]),
#                 xytext="offset points",
#                 arrowprops=dict(arrowstyle="->"))
#
#    plt.xlabel("Age")
#    plt.ylabel("Hours worked per week")
#    plt.show()
#
#    width = 0.4
#    plt.figure(figsize=(20, 10))
#
#    hoursPerAge = df["hours-per-week"][age].value_counts()
#    hoursPerAge.plot(kind="bar")
#    plt.bar(hoursPerAge, width, color="green")
#
#    plt.xlabel("Age")
#    plt.ylabel("Hours worked per week")
#    plt.title("Relationship between age and hours worked per week")
#    plt.show()
#    #plt.clf()
#
#
#task5()

#comment for task5:
# FIXME -- commented as it causes errors


## =============================================================================
## TASK 6
## =============================================================================
def task6():


    #your implementation for task 6 goes here
    print("\n>>> Q6")

    education = pd.DataFrame(df["education-num"])

    plt.figure(figsize=(10, 5))

    plt.ylabel("Education level by number")
    plt.title("Education levels")

    education.boxplot()

task6()

#comment for task6:
# Ans: Levels 1, 2, 3, 4 are outliers


# =============================================================================
# TASK 7
# =============================================================================
def task7():


    #your implementation for task 7 goes here
    print("\n>>> Q7")

    male = df["sex"] == "Male"
    female = df["sex"] == "Female"
    maleIncome = df["income"][male].value_counts()
    femaleIncome = df["income"][female].value_counts()

    print("--- Male income ---")
    print(maleIncome)
    print("--- Female income ---")
    print(femaleIncome)

    labels = [">50k", "<50k"]

    width = 0.4
    index = np.arange(0, 2)
    plt.figure(figsize=(5, 5))

    plt.bar(index-0.2, maleIncome, width, color="deepskyblue")
    plt.bar(index+0.2, femaleIncome, width, color="deeppink")

    plt.xlabel("Income")
    plt.ylabel("Number of occurrences")
    plt.title("Analysis of income classes for different genders")
    plt.legend(["Male", "Female"], loc = 0)
    plt.xticks(index, labels)
    plt.show()


task7()

#comment for task7:
# Males earn more than females
# More of both genders earn >50k
# More males have an income compared to females


# =============================================================================
# TASK 8
# =============================================================================
def task8():


    #your implementation for task 8 goes here
    print("\n>>> Q8")

    maritalStatus = df["marital-status"]
    education = df["education"]

    plt.figure(figsize=(10, 10))

    plt.scatter(maritalStatus, education, color="blue", marker="D")

    plt.xlabel("Martial status")
    plt.ylabel("Education level")
    plt.title("Relationship between education and martial status")
    plt.xticks(rotation="90")
    plt.grid(True)
    plt.show()


task8()

#comment for task8:
# Ans: Married-AF-spouse has the least variance of education types


# =============================================================================
# TASK 9
# =============================================================================
def task9():


    #your implementation for task 9 goes here
    print("\n>>> Q9")

    maritalStatus = df["marital-status"]
    occupation = df["occupation"]

    plt.figure(figsize=(10, 10))

    plt.scatter(maritalStatus, occupation, color="blue", marker="D")

    plt.xlabel("Martial status")
    plt.ylabel("Occupation")
    plt.title("Relationship between occupation and martial status")
    plt.xticks(rotation="90")
    plt.grid(True)
    plt.show()


task9()

#comment for task9:
# Ans: Armed-Forces has the least variance of martial types


# =============================================================================
# TASK 10
# =============================================================================
#def task10():
#
#
#    #your implementation for task 10 goes here
#    print("\n>>> Q10")
#
#    bachelors = df["education"] == "Bachelors"
#    masters = df["education"] == "Master"
#    bachelorsOccupation = df["occupation"][bachelors].value_counts()
#    mastersOccupation = df["occupation"][masters].value_counts()
#
#    labels =  ["Tech-support", "Craft-repair", "Other-service", "Sales",
#               "Exec-managerial", "Prof-specialty", "Handlers-cleaners",
#               "Machine-op-inspct", "Adm-clerical", "Farming-fishing",
#               "Transport-moving", "Priv-house-serv", "Protective-serv",
#               "Armed-Forces"]
#
#    width = 0.4
#    index = np.arange(0, 14)
#    plt.figure(figsize=(15, 5))
#
#    plt.bar(index-0.2, bachelorsOccupation, width, color="coral")
#    plt.bar(index+0.2, mastersOccupation, width, color="turquiose")
#
#    plt.xlabel("Occupation")
#    plt.ylabel("Number of occurrences")
#    plt.title("Analysis of income classes for different genders")
#    plt.legend(["Bachelors", "Masters"], loc = 0)
#    plt.xticks(index, labels)
#    plt.show()
#
#
#task10()
#
##comment for task10:
# FIXME -- commented as it causes errors


# =============================================================================
# TASK 11
# =============================================================================
def task11():


    #your implementation for task 11 goes here
    print("\n>>> Q11")



task11()

#comment for task11:
# TODO


# =============================================================================
# TASK 12
# =============================================================================
def task12():


    #your implementation for task 12 goes here
    print("\n>>> Q12")

#    maritalStatus = pd.DataFrame(df["marital-status"])
#
#    maritalStatus = df["marital-status"]
#    status = maritalStatus.value_counts().sort_index().index.tolist()
#    print(status)
#
#    plt.figure(figsize=(10, 5))
#
#    plt.ylabel("Marital status")
#    plt.title("Marital status")
#    plt.xticks(status)
#
#    maritalStatus.boxplot()



    maritalStatus = df["marital-status"].value_counts()
    print(maritalStatus)

    value1 = df["marital-status"] == "Married-civ-spouse"
    value2 = df["marital-status"] == "Divorced"
    value3 = df["marital-status"] == "Never-married"
    value4 = df["marital-status"] == "Separated"
    value5 = df["marital-status"] == "Widowed"
    value6 = df["marital-status"] == "Married-spouse-absent"
    value7 = df["marital-status"] == "Married-AF-spouse"

    value_1 = df["marital-status"][value1].value_counts()
    value_2 = df["marital-status"][value2].value_counts()
    value_3 = df["marital-status"][value3].value_counts()
    value_4 = df["marital-status"][value4].value_counts()
    value_5 = df["marital-status"][value5].value_counts()
    value_6 = df["marital-status"][value6].value_counts()
    value_7 = df["marital-status"][value7].value_counts()

    labels = ["Married-civ-spouse", "Divorced", "Never-married", "Separated",
              "Widowed", "Married-spouse-absent", "Married-AF-spouse"]

    colors = ["cyan", "lightblue", "lightgreen", "tan", "violet", "yellow", "pink"]

    #boxPlotData = [value1, value2, value3, value4, value5, value6, value7]
    boxPlotData = [value_1, value_2, value_3, value_4, value_5, value_6, value_7]

    box = plt.boxplot(boxPlotData, vert=0, patch_artist=True, labels=labels)

    for patch, color in zip(box["boxes"], colors):
        patch.set_facecolor(color)

    plt.xlabel("Number of occurrences")
    plt.ylabel("Marital status")
    plt.title("Marital status")

    plt.show()


task12()

#comment for task12:
# FIXME