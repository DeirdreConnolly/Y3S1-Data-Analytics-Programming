# -*- coding: utf-8 -*-

# =============================================================================
# HOW TO: ARRAY SLICING
# a[start:stop]  # items start through stop-1
# a[start:]      # items start through the rest of the array
# a[:stop]       # items from the beginning through stop-1
# a[:]           # a copy of the whole array
# a[start:stop:step] # start through not past stop, by step
# =============================================================================

import numpy as np

np.set_printoptions(suppress=True)

file = np.genfromtxt("bikeSharing.csv", dtype=float, delimiter=",")

data = np.array(file)

# =============================================================================
# (i)
# =============================================================================
print("\n(i)")

# Function to compare
def compareHolidays(data, holiday):
    subset = data[data[:, 5] == holiday]    # Array indexing, keeping all the holiday ones only
    print("Number of entries: ", len(subset))
    print("Mean for total users: ", np.mean(subset[:, 15]))
    print("Mean for casual users: ", np.mean(subset[:, 13]))


print("\n- Not on holidays - ")
compareHolidays(file, 0)    # Not on holidays

print("\n- On holidays - ")
compareHolidays(file, 1)    # On holidays


# =============================================================================
# (ii)
# =============================================================================
print("\n(ii)")

# How to normalise temp col
newData = np.copy(data)     # Make a copy of the array

print(newData[:, 9])    # Select col 10

newData[:, 9] *= 41      # Replace the normalised values with real values

print(newData[:, 9])


# =============================================================================
# (iii)
# =============================================================================
print("\n(iii)")

result = data[:, 13] > data[:, 14]    # 13 -> casual users, 14-> registered users, using relational operator

print("Percentage of time where causal users > registered: ", (len(data[result])*100.0)/len(data))  # Find the percentage


# =============================================================================
# (iv)
# =============================================================================
print("\n(iv)")

def averageNumRentalBikesPerCondition(data):

    # Using array indexing
    conditions = {1:"Clear", 2:"Misty", 3:"Light Rain", 4:"Heavy Rain"}

    for key in conditions:
        subsetData = data[data[:,8]==key]
        print(np.mean(subsetData[:, 15]))

    def main():
        data = np.genfromtxt("bikeSharing.csv", delimiter=",")
        averageNumRentalBikesPerCondition(data)

averageNumRentalBikesPerCondition(data)


# =============================================================================
# (v)
# =============================================================================
print("\n(v)")


def main():

    for temp in range(1, 40, 5):    # Start at 1, stop at 40, step of 5
        analyseTemp(data, temp, temp+4)


def analyseTemp(data, minValue, maxValue):

    # the temperature values stored in the array are multiplied by 41
    higherTempCondition = (data[:,9]*41)>=minValue
    lowerTempCondition = (data[:,9]*41)<=maxValue

    subset2 = data[higherTempCondition & lowerTempCondition]

    meanValue = np.mean(subset2[:, 15])

    print("For temp in range ", minValue, "to", maxValue, "the mean number of casual users was ", meanValue)




main()




