import serial
import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
serialcomm = serial.Serial('COM3', 9600)
serialcomm.timeout = 1
cap=cv2.VideoCapture(1) 
detector = HandDetector(detectionCon=0.5, maxHands=1)
while True:
    success,img =cap.read()
    img=cv2.resize(img,(500, 350))
    img=detector.findHands(img)
    l,box = detector.findPosition(img,draw=False)
    if l:
        f=detector.fingersUp()        
        s=(list(map(int,f)))
        w=0
        e='\n'
        for q in s:
            w +=q      
        serialcomm.write(e.encode())
        serialcomm.write(str(w).encode())         
    cv2.imshow('Image',img)  
    if cv2.waitKey(20) & 0xFF == 27:
        break                
cv2.destroyAllWindows()