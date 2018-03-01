# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 12:37:39 2017

@author: Administrator
"""

import numpy as np
from sklearn import preprocessing, cross_validation, neighbors, svm
from sklearn.linear_model import SGDClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_val_predict
from sklearn.ensemble import VotingClassifier
import pandas as pd
from sklearn.externals import joblib
import os
import pathAttributes
from sklearn.metrics import confusion_matrix
from sklearn.ensemble import RandomForestClassifier
import shutil as su
import glob
from sklearn.model_selection import RandomizedSearchCV, GridSearchCV
from scipy.stats import randint
from sklearn.neighbors import KNeighborsClassifier
        
def SVM():
    #s = os.listdir(pathAttributes.data)
    file_path_data = os.path.join(pathAttributes.data, "*.csv")
    list_of_file = glob.glob(file_path_data)
    latest_data = max(list_of_file, key=os.path.getctime) #-1 is idname.txt because number always bigger than charact
    print(latest_data)
    file_path = os.path.join(pathAttributes.data, latest_data)
    df = pd.read_csv(file_path, header=None)
    df.replace('?',-99999, inplace=True)
    X = np.array(df[df.columns[1:129]])
    X.reshape(-1,1)
    y = np.array(df[df.columns[0]])
    
    #print(X)
    #scaler = StandardScaler()
    #X = scaler.fit_transform(X.astype(np.float64))
    """
    to-do-list
    1.scaled inputs
    2.cross_validation
    3.grid search
    """
    X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2, random_state=42)
    try:
        clt = joblib.load(pathAttributes.SVM_model)
        #backup the current correct model
        su.copy(pathAttributes.SVM_model, pathAttributes.backup)
    except:
        #clt = SGDClassifier(loss="hinge",penalty="l2", random_state=42, warm_start=True)
        rnd_clt = RandomForestClassifier(n_estimators=867, max_leaf_nodes=6)
        svc_clt = svm.SVC(kernel="linear", C=1.6, probability=True)
        knn_clt = KNeighborsClassifier()
        clt = VotingClassifier(
                estimators=[('rc', rnd_clt),('kc', knn_clt),('sc', svc_clt)],
                voting='soft'
                )
        #clt = svm.LinearSVC(penalty='l2', loss="hinge", C=1.6)
        
        #randomizedsearchCV for randomforestclassifier and knn
    """    
    param = {
            'n_estimators':randint(low=1,high=1000),
            'max_leaf_nodes':[6,None],
             }
    rnd_search = RandomizedSearchCV(clt, param_distributions=param, cv=3, scoring='accuracy')
    rnd_search.fit(X_train,y_train)
    print(rnd_search.best_params_,rnd_search.best_score_)
    print(rnd_search.cv_results_)
    """
    """
    param = [
            {'n_neighbors':[1,3,5,7,9]},
             ]
    rnd_search = GridSearchCV(clt, param, cv=3, scoring='accuracy')
    rnd_search.fit(X_train,y_train)
    print(rnd_search.best_params_,rnd_search.best_score_)
    print(rnd_search.cv_results_)
    """
    
    a = cross_val_predict(clt, X_train, y_train, cv=3)
    b = cross_val_score(clt, X_train, y_train, cv=3)
    print(confusion_matrix(y_train, a), b)
    total = len(df.index)
    print(total)
    chunk_size = 1000
    epochs = 1000
    
    """
    classes = []
    for i in clt.classes_:
        classes.append(i)
        
    for i in np.unique(y):
        flag = False
        for j in classes:
            if j == i:
                flag = True
        if not flag:
            classes.append(i)
    chunks = int(total/chunk_size)+1
    for epoch in range(epochs):
        for chunk in range(chunks):
            starter = chunk * chunk_size
            if starter+chunk_size > total:
                
                clt.partial_fit(X_train[starter:total+1],y_train[starter:total+1],classes=classes)
                #clt.fit(X_train[starter:total+1],y_train[starter:total+1])
            else:
                clt.partial_fit(X.train[starter:starter+chunk_size],y_train[starter:starter+chunk_size],classes=np.unique(y))
                #clt.fit(X_train[starter:total+1],y_train[starter:chunk_size])
"""

    clt.fit(X_train,y_train)
    indecs = np.random.permutation(int(total/3))
    X_validation = X_train[indecs]
    y_predict = clt.predict(X_test)
    print(confusion_matrix(y_test,y_predict))
    
    if clt.score(X_test,y_test)>0.96:
        joblib.dump(clt, pathAttributes.SVM_model) 
          
#SVM()
