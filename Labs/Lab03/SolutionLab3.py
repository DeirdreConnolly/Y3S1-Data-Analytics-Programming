# -*- coding: utf-8 -*-
"""

"""

import numpy as np


data  = np.genfromtxt("bikeSharing.csv", delimiter = ',', dtype=None)
print (data[0])



subsetData = data[data[:, 5] == 0]
print ("SubsetData ", np.mean(subsetData[:, 15]))


# Solution to Q1 (i)

def compareHolidays(data, holiday):
    subset = data[data[:, 5] == holiday]
    print ("\nHoliday value is ", holiday)
    print ("Total number of users ", len(subset))
    print ("Mean number of userrs ", np.mean(subset[:, 15]))



    
# Solution to Q1 (ii)


def normalization(bikeData):
    
    copyBikeData = np.copy(bikeData)
    
    copyBikeData[:, 9] *= 41.0
    
    print (copyBikeData[:, 9])
    
    

# Solution to Q1 (iii)

def percentageCausal(bikeData):
    
    result = bikeData[:, 13]>bikeData[:, 14]
    print ('Percentage of time where causal users > registered ', (len(bikeData[result])*100.0)/len(bikeData)) 





# Solution to Q1 (iv)

def averageNumRentalBikesPerCondition(data):
    
    conditions = {1:"Clear", 2:"Misty", 3:"Light Rain", 4:"Heavy Rain"}
    
    for key in conditions:
        subsetData = data[data[:,8]==key]
        print ("Mean users for weather = ", conditions[key], ": ", np.mean(subsetData[:, 15]))



# solution to Q1 (v)

def analyseTemp(data, minValue, maxValue):
    # the temperature values stored in the array are multiplied by 41 
    
    higherTempCondition = (data[:,9]*41)>=minValue    
    lowerTempCondition = (data[:,9]*41)<=maxValue
    
    subset = data[higherTempCondition & lowerTempCondition]

    meanValue = np.mean(subset[:, 15])
    print ("For temp in range ", minValue, "to", maxValue, "the mean number of casual users was ", meanValue)




def main():
    
    bikeData = np.genfromtxt("bikeSharing.csv", delimiter = ',')
    
    
    
    # Q1 (i)
    compareHolidays(bikeData, 0)
    compareHolidays(bikeData, 1)
    
    # Q1 (ii)
    normalization(bikeData)
    
    # Q1 (iii)
    percentageCausal(bikeData)
    
    # Q1 (iv)
    averageNumRentalBikesPerCondition(bikeData)
    
    # Q1 (v)
    for temp in range(1, 40, 5):
        analyseTemp(bikeData, temp, temp+4)
    
    
    
    
main()