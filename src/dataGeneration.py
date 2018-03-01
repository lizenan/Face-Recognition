# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 18:22:42 2017

@author: Administrator
"""

import dlib
import cv2
import numpy as np
from sklearn import preprocessing, cross_validation, neighbors, svm
import os
import csv
import pathAttributes
import shutil as su
import time
import glob
#ap = argparse.ArgumentParser()
#ap.add_argument("-p", "--shape-predictor", metavar="D:\\用户目录\\下载\\shape_predictor_68_face_landmarks.dat\\shape_predictor_68_face_landmarks.dat", required=True,
#	help="path to facial landmark predictor")
#ap.add_argument("-r", "--picamera", type=int, default=-1,
	#help="whether or not the Raspberry Pi camera should be used")
#args = vars(ap.parse_args())
def dataGeneration():
    

    print("[INFO] loading facial landmark predictor...")
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor(pathAttributes.face_detection_model)
    face_encoder = dlib.face_recognition_model_v1(pathAttributes.face_recognition_model)
    
    print("[INFO] camera sensor warming up...")
    #vs = VideoStream().start()
    #video_capture = cv2.VideoCapture(0)
    #time.sleep(2.0)
    names = []
    s = os.listdir(pathAttributes.faces)
    
    for i in s:
        name_w_time = os.path.basename(i)
        name_only = name_w_time.split("_",1)
        names.append(name_only)
    people = []
    IDs = []
    for i in s:
        name_w_time = os.path.basename(i)
        time_only = name_w_time.split("_",1)[0]
        IDs.append(time_only)
    #count = 1
    
    for i in s:
        for ID in IDs:
            if str(i).find(ID)>-1:
                document = os.path.join(pathAttributes.faces,i)
                #name_w_time = os.path.basename(document)
                #name_only = name_w_time.split("_",1)
                file_path_data = os.path.join(document, "*.png")
                pics = glob.glob(file_path_data)
                for index in pics:
                    pic = os.path.join(document,index)
                    print(pic)
                    image = cv2.imread(pic)
                    try:
                        faceDetect = detector(image, 1)
                        shape = predictor(image, faceDetect[0])
                        face_encoding = face_encoder.compute_face_descriptor(image, shape, 1)
                        features = list(face_encoding)
                        features.insert(0,ID)
                        #features.insert(1,name_only)
                        people.append(features)
                        print(features)
                    except:
                        pass
    #online mode
    newest_data_name = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))+".csv"
    newest_data = os.path.join(pathAttributes.data, newest_data_name)
    csvfile = open(newest_data,"w",newline='')
    #csvfile = open(pathAttributes.face_features_data,"w",newline='')  batch mode
    writer = csv.writer(csvfile)
    writer.writerows(people)
    csvfile.close()
    return False
    #online mode
    """
    for i in s:
        used_face = os.path.join(pathAttributes.faces, i)
        su.move(used_face,pathAttributes.backup)
"""        
"""measurement = open("E:\\data.txt", 'w')
for person in people:
    measurement.writelines(str(person)+'\n')
measurement.flush()
measurement.close()
"""
"""
    chris_image = cv2.imread('E:\\TiffanyFace-preprocessed\\tiffany_lin_5.png')
#chris_image_gray = cv2.cvtColor(chris_image, cv2.COLOR_GRAY2RGB)
chris = detector(chris_image, 1)
chris_shape = predictor(chris_image, chris[0])
chris_face_encoding = face_encoder.compute_face_descriptor(chris_image, chris_shape, 1)
hey = list(chris_face_encoding)
f = open('E:\\blogCblog.txt', 'w')
print(hey)
chris_image = cv2.imread('E:\\49.png')
#chris_image_gray = cv2.cvtColor(chris_image, cv2.COLOR_GRAY2RGB)
chris = detector(chris_image, 1)
chris_shape = predictor(chris_image, chris[0])
chris_face_encoding = face_encoder.compute_face_descriptor(chris_image, chris_shape, 1)
print("chrisli:"+str(chris_face_encoding))
"""

#dataGeneration()
