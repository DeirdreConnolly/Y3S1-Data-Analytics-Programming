#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 09:07:04 2019

@author: farshad.toosi
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
df = pd.read_csv("mdata.csv",encoding = "ISO-8859-1")

def workclassMenWoman(df):
   
    sctmtx = df[['degree','price']]
    sctmtx = sctmtx.dropna()
    sctmtx['degree'] = sctmtx['degree'].str.strip('.').str.strip('=')
    sctmtx['price'] = sctmtx['price'].str.strip('.').str.strip('=')
   
    dict1 = {}
    k = 1
    for i in pd.unique(sctmtx['degree']):
        print(i)
        if i == i:
            dict1[i] = k
            k = k +1
    sctmtx['degree'] = sctmtx['degree'].map(dict1)
    index1 = np.asarray(list(dict1.values()))
    
    dict2 = {}
    k = 1
    for i in pd.unique(sctmtx['price']):
        print(i)
        if i == i:
            dict2[i] = k
            k = k +1
    sctmtx['price'] = sctmtx['price'].map(dict2)
    index2 = np.asarray(list(dict2.values()))
    
    leb1 = list(np.asarray(list(dict1.keys())))
    
    leb2 = list(np.asarray(list(dict2.keys())))
    
    plt.scatter(sctmtx['degree'], sctmtx['price'])
    plt.xticks(index1, leb1)
    plt.yticks(index2, leb2)
    plt.show()
#workclassMenWoman(df)
    
def PriceGoodBad(df):
   
    sctmtx = df[['price','degree','quality']]
    sctmtx = sctmtx.dropna()
    sctmtx['price'] = sctmtx['price'].str.strip('.').str.strip('=')
    sctmtx['degree'] = sctmtx['degree'].str.strip('.').str.strip('=')
    sctmtx['quality'] = sctmtx['quality'].str.strip('.').str.strip('=')
    l1 = sctmtx['quality']=='good'
    sctmtx1 = sctmtx[l1]
    
    l2 = sctmtx['quality']=='bad'
    sctmtx2 = sctmtx[l2]
    
    index = np.arange(1,4)
    
    plt.bar(index+0.35, sctmtx1['price'].value_counts(), 0.35)
    plt.bar(index, sctmtx2['price'].value_counts(), 0.35)
    print(pd.unique(sctmtx['price']))
    plt.xticks(index, pd.unique(sctmtx['price']))
    plt.legend(['bad', 'good'])
    plt.show()
    
#PriceGoodBad(df) 

def boxplotOutlier(df):
    sctmtx = df[['Test']]
    sctmtx.boxplot()
    #plt.show()
boxplotOutlier(df)