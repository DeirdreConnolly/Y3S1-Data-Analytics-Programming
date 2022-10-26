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


# Function to compare
def compareHolidays(data, holiday):
    subset = data[data[:, 5] == holiday]    # Array indexing
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
print()

# How to normalise temp col
newData = np.copy(data)     # Make a copy of the array

print(newData[:, 9])    # Print the copy

newData[:, 9] *= 9      # Replace the normalised values with real values

print(newData[:, 9])


# =============================================================================
# (iii)
# =============================================================================
result = data[:, 13]>data[:, 14]
print "Percentage of time where causal users > registered ", (len(data[result])*100.0)/len(data)



# =============================================================================
# (iv)
# =============================================================================
def averageNumRentalBikesPerCondition(data):conditions = {1:"Clear", 2:"Misty", 3:"Light Rain", 4:"Heavy Rain"}for key in conditions:subsetData = data[data[:,8]==key]print np.mean(subsetData[:, 15])def main():data = np.genfromtxt(‘bikeSharing.csv', delimiter=',')averageNumRentalBikesPerCondition(data)










