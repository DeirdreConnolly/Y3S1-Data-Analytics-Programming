# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import datetime as DT
import matplotlib.pyplot as plt
from matplotlib.dates import date2num

# =============================================================================
# Q1
# =============================================================================

def Q1():

    plt.plot([0, 10, 20, 30, 40, 50], [0, 20, 40, 60, 80, 100])

    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")

    plt.show()


# =============================================================================
# Q2
# =============================================================================

def Q2():

    #                   X-axis                    Y-axis
    plt.plot([1.0, 1.5, 2.0, 2.5, 3.0], [2.0, 3.0, 4.0, 2.5, 1.0])

    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Sample graph!")

    plt.show()


# =============================================================================
# Q3
# =============================================================================

def Q3():

    df = pd.read_csv("fdata.csv", sep=",", parse_dates=True, index_col=0)

    plt.xlabel("Date")
    plt.ylabel("Data")
    plt.title("Sample Financial Data")

    plt.plot(df)
    plt.legend(["Open", "High", "Low", "Close"], loc="upper left")
    plt.show()


# =============================================================================
# Q4
# =============================================================================

def Q4():

    plt.plot([10, 20, 30], [20, 40, 10], color="purple", linestyle="dotted")
    plt.plot([10, 20, 30], [40, 10, 30], color="red", linestyle="dashed")

    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Plot two or more lines with different styles")

    plt.legend(["Dotted", "Dashed"])
    plt.show()


# =============================================================================
# Q5
# =============================================================================

def Q5():

    t = np.arange(0.0, 5.0, 0.2)

    plt.plot(t, t, "r--", t, t**2, "bs", t, t**3, "g^")
    plt.show()


# =============================================================================
# Q6
# =============================================================================

def Q6():

    data = [(DT.datetime.strptime("2016-10-03", "%Y-%m-%d"), 772.559998),
            (DT.datetime.strptime("2016-10-04", "%Y-%m-%d"), 776.429993),
            (DT.datetime.strptime("2016-10-05", "%Y-%m-%d"), 776.469971),
            (DT.datetime.strptime("2016-10-06", "%Y-%m-%d"), 776.859985),
            (DT.datetime.strptime("2016-10-07", "%Y-%m-%d"), 775.080017 )]

    x = [date2num(date) for (date, value) in data]
    y = [value for (date, value) in data]

    fig = plt.figure()

    graph = fig.add_subplot(111)

    # Plot the data as a red line with round markers
    graph.plot(x,y,"r-o")

    # Set the xtick locations
    graph.set_xticks(x)

    # Set the xtick labels
    graph.set_xticklabels(
            [date.strftime("%Y-%m-%d") for (date, value) in data]
            )
    plt.show()


# =============================================================================
# Q7
#
# =============================================================================

def Q7():

    x = ["Java", "Python", "PHP", "JavaScript", "C#", "C++"]
    y = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

    plt.bar(x, y, color="blue")

    plt.xlabel("Languages")
    plt.ylabel("Popularity")
    plt.title("Popularity of Programming Languages Worldwide" +
              "\nOct 2017 compared to a year ago")


    #plt.xticks(x)

    # Turn on the grid
    plt.minorticks_on()

    # Customise the major grid
    plt.grid(which="major", linestyle="-", linewidth="0.5", color="red")

    # Customize the minor grid
    plt.grid(which="minor", linestyle=":", linewidth="0.5", color="black")

    plt.show()


# =============================================================================
# Main
# =============================================================================

def main():
#    Q1()
#    Q2()
#    Q3()
#    Q4()
#    Q5()
#    Q6()
    Q7()


main()















