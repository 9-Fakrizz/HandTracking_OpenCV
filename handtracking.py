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
TipsID = [8, 12, 16, 20]
Pip = [6, 10, 14, 18]
constfinger = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    
    cv2.putText(img, "Finger : ", (20, 450), cv2.FONT_HERSHEY_PLAIN, 2, (218, 224, 159), 2)
    cv2.putText(img, f"Finger Count: ", (20, 410), cv2.FONT_HERSHEY_PLAIN, 2, (218, 224, 159), 3)
   
   
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark): #get id and position
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                pos[id] = [cx, cy]
            
            #print(pos[0][0], pos[0][1])
            thdx = mt.pow(pos[4, 0]-pos[5, 0],2)
            thdy = mt.pow(pos[4, 1]-pos[5, 1],2)
            Lthumb = int(mt.sqrt(abs(thdy + thdx))) #thumb distancing
            
            long1= numpy.zeros((4, 1))
            long0= numpy.zeros((4, 1))
            for i in range(0, 4):
                dx1 = mt.pow(pos[TipsID[i], 0]-pos[0, 0],2)
                dy1 = mt.pow(pos[TipsID[i], 1]-pos[0, 1],2)
                long1[i] = int(mt.sqrt(abs(dy1 + dx1))) 

                dx0 = mt.pow(pos[Pip[i], 0]-pos[0, 0],2)
                dy0 = mt.pow(pos[Pip[i], 1]-pos[0, 1],2)
                long0[i] = int(mt.sqrt(abs(dy0 + dx0)))
            
            finger=[]
            if (Lthumb > (long0[0]/2)):
                finger.append(constfinger[0])
            for i in range(0, 4):
                if (long1[i] > long0[i]):
                    finger.append(constfinger[i+1])
            
            #print(finger, len(finger))
            
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
            if(len(finger)!=0):
                cv2.putText(img,str(finger), (180,445), cv2.FONT_HERSHEY_PLAIN, 1, (20, 80, 155), 2)
                cv2.putText(img,str(len(finger)), (260,410), cv2.FONT_HERSHEY_PLAIN, 2, (20, 80, 155), 2)
            else:
                cv2.putText(img,"NONE", (180,445), cv2.FONT_HERSHEY_PLAIN, 1, (20, 80, 155), 2)
                cv2.putText(img,str(len(finger)), (260,410), cv2.FONT_HERSHEY_PLAIN, 2, (20, 80, 155), 2)  
    
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img,str(int(fps)), (10,60), cv2.FONT_HERSHEY_PLAIN, 2, (20, 80, 155), 2)
    
    
    cv2.imshow("Image", img)
    cv2.waitKey(1)
