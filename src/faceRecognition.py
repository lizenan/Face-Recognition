## -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 13:38:17 2017

@author: Administrator
"""

import dlib
import cv2
import numpy as np
from sklearn.externals import joblib
import os
import pathAttributes
#ap = argparse.ArgumentParser()
#ap.add_argument("-p", "--shape-predictor", metavar="D:\\用户目录\\下载\\shape_predictor_68_face_landmarks.dat\\shape_predictor_68_face_landmarks.dat", required=True,
#	help="path to facial landmark predictor")
#ap.add_argument("-r", "--picamera", type=int, default=-1,
	#help="whether or not the Raspberry Pi camera should be used")
#args = vars(ap.parse_args())
def faceRecognition():
    
    f = open(pathAttributes.dictionary, 'r')                  
    result = {}
    for line in f.readlines():
        line = line.strip()
        print(line)
        if not len(line):
            continue
        result[line.split(':')[0]] = line.split(':')[1]
    f.close()
    #face_detection_model = "C:\\Users\\Administrator\\shape_predictor_68_face_landmarks.dat"
    #print(result)
    print("[INFO] loading facial landmark predictor...")
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor(pathAttributes.face_detection_model)
    face_encoder = dlib.face_recognition_model_v1(pathAttributes.face_recognition_model)
    
    print("[INFO] camera sensor warming up...")
    #vs = VideoStream().start()
    video_capture = cv2.VideoCapture(0) #open camra by calling opencv's function
    #time.sleep(2.0)
    """
    chris_image = cv2.imread('E:\\49.png')
    #chris_image_gray = cv2.cvtColor(chris_image, cv2.COLOR_GRAY2RGB)
    chris = detector(chris_image, 1)
    chris_shape = predictor(chris_image, chris[0])
    chris_face_encoding = face_encoder.compute_face_descriptor(chris_image, chris_shape, 1)
    print("Chris:"+str(chris_face_encoding))
    julie_image = cv2.imread('E:\\1.png')
    #julie_image_gray = cv2.cvtColor(julie_image, cv2.COLOR_GRAY2RGB)
    julie = detector(julie_image, 1)
    julie_shape = predictor(julie_image, julie[0])
    julie_face_encoding = face_encoder.compute_face_descriptor(julie_image, julie_shape, 1)
    print("JULIE:"+str(julie_face_encoding))
    """
    face_locations = []
    face_encodings = []
    face_names = []
    raw_list = []
    while True:
        raw_list = []
        face_names = []
    	# grab the frame from the threaded video stream, resize it to
    	# have a maximum width of 400 pixels, and convert it to
    	# grayscale
        #frame = vs.read()
        #frame = imutils.resize(frame, width=400)
        ret, frame = video_capture.read()
        #dim = (int(frame.shape[1] * 0.25), int(frame.shape[0] * 0.25))
        dim = (int(frame.shape[1] * 0.2), int(frame.shape[0] * 0.2))
        small_frame = cv2.resize(frame, dim)
        gray_one_channel = cv2.cvtColor(small_frame, cv2.COLOR_BGR2GRAY)
        #face_locations = face_recognition.face_locations(small_frame)
        gray = cv2.cvtColor(gray_one_channel, cv2.COLOR_GRAY2RGB)
    	# detect faces in the grayscale frame
        rects = detector(gray, 1)
        #print("rects:"+str(rects))
        for rect in rects:
            #print("rect:"+str(rect))
            css = [rect.top(), rect.right(), rect.bottom(), rect.left()]
            location = max(css[0], 0), min(css[1], gray.shape[1]), min(css[2], gray.shape[0]), max(css[3], 0)
            face_location = dlib.rectangle(location[3], location[0], location[1], location[2])
            face_locations.append(face_location)
            raw_list.append(css)
            shape = predictor(gray, face_location)
            
            face_encoding = face_encoder.compute_face_descriptor(gray, shape, 1)
            #print("random:"+str(face_encoding))
            """
            match_chris = []
            match_julie = []
            chris_norm = 0
            julie_norm = 0
            if len([chris_face_encoding]) == 0:
                match_chris = list(0<=0.6)
            else:
                chris_norm = np.linalg.norm(np.array([chris_face_encoding]) - np.array([face_encoding]), axis=1)
                match_chris = list(chris_norm<= 0.6)
                print("chris:"+str(chris_norm))
            name = "Unknown"
            if len([julie_face_encoding]) == 0:
                match_julie = list(0<=0.6)
            else:
                julie_norm = np.linalg.norm(np.array([julie_face_encoding]) - np.array([face_encoding]), axis=1)
                match_julie = list(julie_norm <= 0.6)
                print("julie:"+str(julie_norm))
            if match_chris[0]!=0 and match_julie[0]!=0:
                if julie_norm>chris_norm:
                    name = "Chris"
                else:
                    name = "Julie"
            elif match_julie[0] == 0 and match_chris[0] !=0:
                name = "Chris"
            elif match_julie[0] != 0 and match_chris[0] ==0:
                name = "Julie"
            else:
                name = "Unknown"
                """
            threshold = -0.05 #-0.1 for C=0.1 4-8 6 for 0.3 
            proba = 0.72
            clf = joblib.load(pathAttributes.SVM_model)
            feeaturesArray = np.array(face_encoding)
            ID = clf.predict(feeaturesArray.reshape(1,-1))[0]
            name = result[str(ID)]
            #scores = clf.decision_function(feeaturesArray.reshape(1,-1))
            scores = clf.predict_proba(feeaturesArray.reshape(1,-1))
            """
            scores_sorted = np.sort(scores)
            second_biggest = scores_sorted[0][-2]
            minimum = scores_sorted[0][0]
            biggest_score = np.max(scores)
            gap = biggest_score - minimum
            gap_2 = biggest_score - second_biggest
            print(gap_2)
            percentage = gap_2/gap *100
            print(percentage)
            if percentage < 30:
                name = "unknown"
            """    """
            biggest_score = np.max(scores)
            if biggest_score < threshold:
                name = "unknown"
                """
            biggest_score = np.max(scores)
            if biggest_score < proba:
                name="unknown"
            #scores = scores - np.min(scores)
            #scores = scores/np.max(scores)
            print(scores,name)
            face_names.append(name)
            #print(face_names)
        for (top, right, bottom, left), name in zip(raw_list, face_names):
                # Scale back up face locations since the frame we detected in was scaled to 1/4 size
                top *= 5
                right *= 5
                bottom *= 5
                left *= 5
        
                # Draw a box around the faceq
                cv2.rectangle(frame, (left-10, top-10), (right+10, bottom+10), (0, 0, 255), 2)
        
                # Draw a label with a name below the face
                cv2.rectangle(frame, (left-10, bottom+10), (right+10, bottom+45), (0, 0, 255), cv2.FILLED)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(frame, name, (left, bottom + 30), font, 1.0, (255, 255, 255), 1)
        
        cv2.imshow('Video', frame)    #display the camra
    
        # Hit 'q' on the keyboard to quit!
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    video_capture.release()
    cv2.destroyAllWindows()
    
faceRecognition()
