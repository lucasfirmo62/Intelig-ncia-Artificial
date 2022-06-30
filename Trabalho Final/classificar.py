#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
from sklearn import svm
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.metrics import confusion_matrix
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier

tr = np.loadtxt('treino.txt');
ts = np.loadtxt('teste.txt');
y_test = ts[:,-1]
y_train = tr[:,-1]
X_train = tr[:, 1 : -1]
X_test = ts[:, 1 : -1]

# KNN
neigh = KNeighborsClassifier(n_neighbors=3, metric='manhattan')
neigh.fit(X_train, y_train)
print('\n\nKNN\n')
pneigh = neigh.predict(X_test)
print(classification_report(y_test, pneigh))
print(confusion_matrix(y_test, pneigh))
print('\n')
        
# Random Forest Classifier
rfc = RandomForestClassifier(n_estimators=130, max_depth=None, random_state=1)
rfc.fit(X_train, y_train)
print('\n\nRandom Forest\n')
prfc = rfc.predict(X_test)
print(classification_report(y_test, prfc))
print(confusion_matrix(y_test, prfc))
print('\n')

# SVM
svmc = svm.SVC()
svmc.fit(X_train, y_train)
print('\n\nSVM\n')
psvmc = svmc.predict(X_test)
print(classification_report(y_test, psvmc))
print('\n')

# DT - Decision Tree
dtc = tree.DecisionTreeClassifier()
dtc = dtc.fit(X_train, y_train)
print('\n\nDT\n')
pdtc = dtc.predict(X_test)
print(classification_report(y_test, pdtc))
print('\n')