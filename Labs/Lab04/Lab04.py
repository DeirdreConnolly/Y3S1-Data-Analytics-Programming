# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 10:10:10 2019

@author: Deirdre
"""

# =============================================================================
# Q1
# =============================================================================
#file = open("studentDetails.txt", "r")  # open file
#
#studentDetails = {}   # create empty dictionary
#
#print("Student", "Grades")
#
#for userline in file:
#    data = userline.split()
#    data[1] = int(data[1])  # convert grade1 string to int
#    data[2] = int(data[2])  # convert grade2 string to int
#    data[3] = int(data[3])  # convert grade3 string to int
#
#    average = int((data[1] + data[2] + data[3]) / 3)
#
##    print(data[0], average)
#    studentDetails[data[0]] = average
#
#print(studentDetails.items())
#
#
#check = input("Do you want to check another student's average? ")
#
#while True:
#    studentName = input("Enter name of student: ")
#    if (studentName in studentDetails):
#        print(studentDetails.get(studentName))
#
#    elif(studentName == "n"):
#        break
#
#file.close()


# =============================================================================
# Q2
# =============================================================================
file = open("AirPassengers.csv", "r")

for userline in file:
    data = userline.split()

    average = (() / 12)




file.close()




