# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 19:32:00 2017

@author: Administrator
"""
import os

src = os.getcwd()
root = os.path.abspath(os.path.join(src, os.pardir))
model = os.path.join(root, "model")
data = os.path.join(root, "data")
faces = os.path.join(root, "faces")
backup = os.path.join(root, "backup")
face_features_data = os.path.join(data, "data.csv")
dictionary = os.path.join(data, "idname.txt") 
SVM_model = os.path.join(model, "SVMModel.pkl")
face_detection_model = os.path.join(model,"shape_predictor_68_face_landmarks.dat")
face_recognition_model= os.path.join(model,"dlib_face_recognition_resnet_model_v1 (1).dat")
pics_number = 200