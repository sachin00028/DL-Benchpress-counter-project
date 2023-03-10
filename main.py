import cv2
import poseModule as pm
import numpy as np

cap = cv2.VideoCapture('/home/sachin/Videos/computer_vision/opencv/Projects/Benchpress_counter/bench.mp4')

detector = pm.poseDetector()

dir=0
count=0

while True:

#1. image preprocessing

    success,image = cap.read()
    image = cv2.resize(image,(1280,720))

#2. find body

    image = detector.findPose(image,draw=False)
    # print(image)
    lmlist = detector.findPosition(image,draw=False)
    # print(lmlist)




#3. find angles of specific landmark

    if len(lmlist)!=0:

        angle = detector.findAngle(image,12,14,16)
        print(angle)

#4. counting

    per = np.interp(angle,(199,320),(0,100))
    # print(angle,'---->',per)

    if per == 100:
        if dir == 0:
            count += 0.5
            dir = 1

    if per == 0:
        if dir == 1:
            count += 0.5
            dir = 0
    print(count)

    cv2.rectangle(image,(0,0),(150,150),(0,0,0),cv2.FILLED)
    cv2.putText(image,str(int(count)),(50,100),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),5)









    cv2.imshow('Benchpress Counter',image)
    if cv2.waitKey(1) & 0xFF ==27:
        break