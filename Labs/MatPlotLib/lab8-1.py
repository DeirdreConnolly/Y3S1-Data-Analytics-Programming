#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 10:19:58 2019

@author: farshadtoosi
"""

import numpy as np
import datetime as DT
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
from matplotlib.dates import date2num


def Q7(): 
    x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
    popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
    x_pos = [i for i, _ in enumerate(x)]
    plt.bar(x_pos, popularity, color='blue')
    plt.xlabel("Languages")
    plt.ylabel("Popularity")
    plt.title("PopularitY of Programming Language\n" + "Worldwide, Oct 2017 compared to a year ago")
    plt.xticks(x_pos, x)
    # Turn on the grid
    plt.minorticks_on()
    plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
    # Customize the minor grid
    plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
    plt.show()


def Q6():
        
    data = [(DT.datetime.strptime('2016-10-03', "%Y-%m-%d"), 772.559998),
            (DT.datetime.strptime('2016-10-04', "%Y-%m-%d"), 776.429993),
            (DT.datetime.strptime('2016-10-05', "%Y-%m-%d"), 776.469971),
            (DT.datetime.strptime('2016-10-06', "%Y-%m-%d"), 776.859985),
            (DT.datetime.strptime('2016-10-07', "%Y-%m-%d"), 775.080017 )]
    
    x = [date2num(date) for (date, value) in data]
    y = [value for (date, value) in data]
    
    fig = plt.figure()
    
    graph = fig.add_subplot(111)
    
    # Plot the data as a red line with round markers
    graph.plot(x,y,'r-o')
    
    # Set the xtick locations
    graph.set_xticks(x)
    
    # Set the xtick labels
    graph.set_xticklabels(
            [date.strftime("%Y-%m-%d") for (date, value) in data]
            )
    plt.show()

def Q5():

    # Sampled time at 200ms intervals
    t = np.arange(0., 5., 0.2)
    
    # green dashes, blue squares and red triangles
    plt.plot(t, t, 'g--', t, t**2, 'bs', t, t**3, 'r^')
    plt.show()
    
  



def Q4():
    x1 = [10,20,30]
    y1 = [20,40,10]
    # line 2 points
    x2 = [10,20,30]
    y2 = [40,10,30]
    # Set the x axis label of the current axis.
    plt.xlabel('x - axis')
    # Set the y axis label of the current axis.
    plt.ylabel('y - axis')
    # Plot lines and/or markers to the Axes.
    plt.plot(x1,y1, color='blue', linewidth = 3,  label = 'line1-dotted',linestyle='dotted')
    plt.plot(x2,y2, color='red', linewidth = 5,  label = 'line2-dashed', linestyle='dashed')
    # Set a title 
    plt.title("Plot with two or more lines with different styles")
    # show a legend on the plot
    plt.legend()
    # function to show the plot
    plt.show()
    
def Q3():
    df = pd.read_csv('fdata.csv', sep=',', parse_dates=True, index_col=0)
    df.plot()
    plt.show()
    

def Q2():
    # x axis values
    x = [1,2,3]
    # y axis values
    y = [2,4,1]
    # Plot lines and/or markers to the Axes.
    plt.plot(x, y)
    # Set the x axis label of the current axis.
    plt.xlabel('x - axis')
    # Set the y axis label of the current axis.
    plt.ylabel('y - axis')
    # Set a title 
    plt.title('Sample graph!')
    # Display a figure.
    plt.show()
    
def Q1():
    X = range(1, 50)
    Y = [value * 3 for value in X]
    print("Values of X:")
    print(*range(1,50)) 
    print("Values of Y (thrice of X):")
    print(Y)
    # Plot lines and/or markers to the Axes.
    plt.plot(X, Y)
    # Set the x axis label of the current axis.
    plt.xlabel('x - axis')
    # Set the y axis label of the current axis.
    plt.ylabel('y - axis')
    # Set a title 
    plt.title('Draw a line.')
    # Display the figure.
    plt.show()
    
Q7()