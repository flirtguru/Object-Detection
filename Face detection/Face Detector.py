import cv2
import numpy as np

classifier=cv2.CascadeClassifier("Projects/Modules/haarcascade_frontalface_default.xml")

image=cv2.imread("aunty.jpg")

gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

det=classifier.detectMultiScale(gray,1.2,3)

if det is():
    print("NO FACES FOUND!!")

for (t1,t2,b1,b2) in det :
    
    cv2.rectangle(image,(t1,t2),(t1+b1,t2+b2),(69,69,69),2)
    
    cv2.imshow("Detected ",image)
    
    cv2.waitKey(0)
    
cv2.destroyAllWindows()    
    
