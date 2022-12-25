import cv2
import mediapipe as mp
import numpy 
import time
import math as mt

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0
pos = numpy.zeros((21, 2))
side = "none"
TipsID = [4, 8, 12, 16, 20]
Pip = [3, 6, 10, 14, 18]

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark): #get id and position
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                pos[id] = [cx, cy]
            
            #print(pos[0][0], pos[0][1])
            long1= numpy.zeros((5, 1))
            long0= numpy.zeros((5, 1))
            for i in range(0, 5):
                dx1 = mt.pow(pos[TipsID[i], 0]-pos[TipsID[i]-3, 0],2)
                dy1 = mt.pow(pos[TipsID[i], 1]-pos[TipsID[i]-3, 1],2)
                long1[i] = int(mt.sqrt(abs(dy1 + dx1)))

                dx0 = mt.pow(pos[Pip[i], 0]-pos[Pip[i]-1, 0],2)
                dy0 = mt.pow(pos[Pip[i], 1]-pos[Pip[i]-1, 1],2)
                long0[i] = int(mt.sqrt(abs(dy0 + dx0)))
            
            print(long1[1], long0[1])
            
                

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
    
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img,str(int(fps)), (10,60), cv2.FONT_HERSHEY_PLAIN, 2, (20, 80, 155), 2)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
