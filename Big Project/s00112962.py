#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 11:58:04 2019

@author: farshadtoosi
"""

from pandas import read_csv
import numpy as np
from pandas.plotting import scatter_matrix
from matplotlib import pyplot
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from io import StringIO
from sklearn import linear_model
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
from sklearn.preprocessing import KBinsDiscretizer
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification

# Note: Not all the libararies above are necessarily needed for this project
# and not all the libraries you need for this project are necessarily listed
# above.


"""
Your Name and Your student ID:

Deirdre Connolly
R00112962

"""

df = pd.read_csv("bank-fullReady.csv", encoding = "ISO-8859-1")

###############################################################################

def task1():

    # Aim is to predict y

    # Create dataset
    d1 = df[["age", "job", "poutcome", "balance", "default", "y"]]
    d2 = df[["age", "job", "poutcome", "balance", "default", "loan"]]

    # Fill NaN values using the specified method
    d1 = d1.fillna(d1.mean())
    d2 = d2.fillna(d2.mean())

    print(d1)
    print(d2)

    # Inputs for machine learning alg to learn from
    X1 = (d1[["age", "job", "poutcome", "balance", "default"]])
    X2 = (d2[["age", "job", "poutcome", "balance", "default"]])

    # Fixes output
    X1 = pd.get_dummies(X1)
    X2 = pd.get_dummies(X2)

    # Target (what we want to predict)
    y1 = d1[["y"]]
    y2 = d2[["loan"]]

    print(len(X1),len(y1))
    print(len(X2),len(y2))

    # Model
    tree_clf = DecisionTreeClassifier(max_depth=2, random_state=42)

    # Fit trains the model, score is accuracy
    tree_clf.fit(X1, y1)

    print("Dataset 1",
          "\tAccuracy:", tree_clf.score(X1, y1),
          "\tError:", (1-tree_clf.score(X1, y1)))

    tree_clf.fit(X2, y2)

    print("Dataset 2",
          "\tAccuracy:", tree_clf.score(X2, y2),
          "\tError:", (1-tree_clf.score(X2, y2)))

#task1()

# COMMENT
# Dataset 1 has a higher accuracy (lower error)

###############################################################################

def task2():

    # Create dataset
    d1 = df[["age", "marital"]]

    # Fill NaN values using the specified method
    d1 = d1.fillna(d1.mean())

    d1 = pd.get_dummies(d1)

    x = []
    y = []

    print(len(d1))

    for i in range(8):

        # Unsupervised learning algorithm
        kmeans = KMeans(n_clusters=i+1, random_state=0).fit(d1)

        y.append(kmeans.inertia_) # Error
        x.append(i)
        print(kmeans.inertia_)


    plt.xlabel("Number of Clusters (K)")
    plt.ylabel("Distortion Function")
    plt.title("Using Elbow Method to Determine Optimal Number of Clusters")
    plt.plot(x, y)


#task2()

# COMMENT
# From the graph, a cluster size of 2 would be suitable
# After K = 2, it begins to plateaux

# FIXME: x values (should start at 1)

###############################################################################

def task3():

    # Aim: predict bank_arg1

    # Create dataset
    d1 = df[["y", "loan", "bank_arg1"]]

    # Fill NaN values using the specified method
    d1 = d1.fillna(d1.mean())

    X = (d1[["loan", "y"]])
    X = pd.get_dummies(X)

    # Target
    y = d1[["bank_arg1"]]

    # Supervised learning algorithm
    n_bins = 0

    for i in range (2,9):
        n_bins = i
        est = KBinsDiscretizer(n_bins=i, encode="ordinal", strategy="uniform")
        est.fit(y)
        yt = est.transform(y)

        tree_clf = DecisionTreeClassifier(max_depth=4, random_state=42)
        tree_clf.fit(X, yt)

        print("Accuracy for", n_bins, "bins:", tree_clf.score(X, yt))


#task3()

# COMMENT
# If bins < 2, a ValueError will occur
# An accuracy of 1.0 suggests overheading
# Therefore, nbins = 5 has the best accuracy

###############################################################################

def task4():

    # Create dataset
    d1 = df[["age", "job", "marital", "education", "loan", "y"]]

    # Fill NaN values using the specified method
    d1 = d1.fillna(d1.mean())

    X = (d1[["age", "job", "marital", "education", "loan"]])
    X = pd.get_dummies(X)

    # Target
    y = d1["y"]

    # KNeighborsClassifier
    neigh_clf = KNeighborsClassifier(n_neighbors=3)
    neigh_clf.fit(X, y.values.ravel())
    neigh_scores = cross_val_score(neigh_clf, X, y, cv=4)
    print("KNeighborsClassifier\t", neigh_scores.mean())

    # DecisionTreeClassifier
    tree_clf = DecisionTreeClassifier(max_depth=4, random_state=42)
    tree_clf.fit(X, y.values.ravel())
    tree_scores = cross_val_score(tree_clf, X, y, cv=4)
    print("DecisionTreeClassifier\t", tree_scores.mean())

    # GaussianNB
    gnb_clf = GaussianNB()
    gnb_clf.fit(X, y.values.ravel())
    gnb_scores = cross_val_score(gnb_clf, X, y, cv=4)
    print("GaussianNB\t\t", gnb_scores.mean())

    # SVM (support vector machine)
    svm_clf = svm.SVC(gamma="auto")
    svm_clf.fit(X, y.values.ravel())
    svm_scores = cross_val_score(svm_clf, X, y, cv=4, n_jobs=-1)
    print("SVM\t\t\t", svm_scores.mean())

    # RandomForestClassifier
    forest_clf = RandomForestClassifier(max_depth=2, random_state=0)
    forest_clf.fit(X, y)
    forest_scores = cross_val_score(forest_clf, X, y, cv=4)
    print("RandomForestClassifier\t", forest_scores.mean())


#task4()

# COMMENT
# Decision Tree Classifier is the best as it has the highest mean accuracy score

###############################################################################

def task5():

    # Create dataset
    d1 = df[["bank_arg1", "bank_arg2"]]

    # Fill NaN values using the specified method
    d1 = d1.fillna(d1.mean())

    X = (d1[["bank_arg1", "bank_arg2"]])
    X = pd.get_dummies(X)

    # Target
    y = d1["bank_arg1"]

    x = []
    y = []

    for i in range(8):

        # Unsupervised learning algorithm
        kmeans = KMeans(n_clusters=i+1, random_state=0).fit(d1)

        y.append(kmeans.inertia_) # Error
        x.append(i)
        print(kmeans.inertia_)

    plt.xlabel("Number of Clusters (K)")
    plt.ylabel("Distortion Function")
    plt.title("Using Elbow Method to Determine Optimal Number of Clusters")
    plt.plot(x, y)



#task5()

# COMMENT
# FIXME: ???
# I'm not sure how to do this.

###############################################################################

def task6():

    # Create dataset
    d1 = df[["housing", "balance", "y"]]

    # Fill NaN values using the specified method
    d1 = d1.fillna(d1.mean())

    X = (d1[["housing", "balance"]])
    X = pd.get_dummies(X)

    # Target
    y = d1[["y"]]

    # Split data into training and test sets
    i = 0.5
    X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=i)

    # Without max_depth
    tree_clf = DecisionTreeClassifier(random_state=42)
    tree_clf.fit(X_train, Y_train.values.ravel())

    print("\nMax depth = null")
    print("Training data\t", tree_clf.score(X_train, Y_train))

    # With various max_depth values
    for x in range (1,21):
        max_depth = x

        tree_clf = DecisionTreeClassifier(max_depth=x, random_state=42)
        print("\nMax depth = ", max_depth)
        tree_clf.fit(X_train, Y_train.values.ravel())

        print("Training data\t", tree_clf.score(X_train, Y_train))
        print("Testing data\t", tree_clf.score(X_test, Y_test))


#task6()

# COMMENT
# Overfitting happens when the max_depth has not been specified
# Setting max_depth reduces overfitting

###############################################################################

def task7():

    # Create dataset
    d1 = df[["loan", "balance", "y", "bank_arg1"]]

    # Fill NaN values using the specified method
    d1 = d1.fillna(d1.mean())

    X = (d1[["loan", "balance"]])
    X = pd.get_dummies(X)

    # Target
    y = d1["y"]

    # Split data into training and test sets
    for i in np.arange (0.05, 0.95, 0.05):
        test_size = i
        X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=i)

        # DecisionTreeClassifier
        tree_clf = DecisionTreeClassifier(random_state=42)
        tree_clf.fit(X_train, Y_train.values.ravel())

        # RandomForestClassifier
        forest_clf = RandomForestClassifier(max_depth=2, random_state=0)
        print("\nTest size = ", test_size)
        forest_clf.fit(X_train, Y_train.values.ravel())

        print("DecisionTreeClassifier test set:",
              tree_clf.score(X_test, Y_test))
        print("RandomForestClassifier test set:",
              forest_clf.score(X_test, Y_test))

    plt.xlabel("DecisionTreeClassifier")
    plt.ylabel("RandomForestClassifier")
    plt.title("Decision Tree vs Random Forest Using Test Data")
#    plt.annotate()
    plt.plot(tree_clf.score(X_test, Y_test), forest_clf.score(X_test, Y_test))


task7()

# Note: bankarg1 should be descritized
# COMMENT
# Random Forest Classifier generates a better score using the test data
# FIXME: Graph

###############################################################################

