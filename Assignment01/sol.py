#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 20:09:51 2019

@author: farshad.toosi
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
df = pd.read_csv("titanic.csv",encoding = "ISO-8859-1")


def Q1(df):
    ndf = df[['Survived', 'Sex']]
    ndf1 = ndf['Survived'] == 1
    ndf2 = ndf['Survived'] == 0

    ndf11 = ndf[ndf1]

    ndf22 = ndf[ndf2]

    index = np.arange(1,3)

    plt.bar(index, ndf11['Sex'].value_counts(),0.2)

    plt.bar(index+0.2, ndf22['Sex'].value_counts(),0.2)


    plt.xticks(index,['Male', 'Female'])
    plt.legend(['Survived','died'])
    plt.show()

Q1(df)

def Q2(df):
    ndf = df[['Age','Sex']]
    l1 = ndf['Age'] <40
    l2 = ndf['Age'] >20
    ndf = ndf[l1]
    ndf = ndf[l2]
    print(ndf)

    index = np.arange(1,3)

    plt.bar(index, ndf['Sex'].value_counts(),0.2)

Q2(df)

def Q3(df):
    criteria = df['Survived']==0
    fatalities = df[criteria]
    pclassGroup= fatalities.groupby("Pclass")

    classSurived= pclassGroup['Survived'].count()
    print (classSurived)
    classSurived.plot()
    plt.show()

Q3(df)

def Q4(df):
    ndf = df[['Pclass','Fare']]
    pclassGroup= ndf.groupby("Pclass").mean()

    print(pclassGroup)
    index = [1,2,3]

    plt.bar(index, pclassGroup['Fare'])

Q4(df)

def Q5(df):
    clss = df['Pclass']
    plt.pie(clss.value_counts())

Q5(df)