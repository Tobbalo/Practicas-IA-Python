#Cerezo
import cv2
import numpy as np

lowerBound1=np.array([0,100,100])
upperBound1=np.array([30,255,255])

lowerBound2=np.array([150,100,100])
upperBound2=np.array([180,255,255])

#cam= cv2.VideoCapture(0)
kernelOpen=np.ones((5,5))
kernelClose=np.ones((20,20))

font = cv2.FONT_HERSHEY_SIMPLEX

while True:
    img=cv2.imread('c4.jpg')
    #img=cv2.resize(img,(340,220))

    #convert BGR to HSV
    imgHSV= cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    # create the Mask
    mask1=cv2.inRange(imgHSV,lowerBound1,upperBound1)
    mask2=cv2.inRange(imgHSV,lowerBound2,upperBound2)

    mask = cv2.bitwise_or(mask1, mask2)

    #morphology
    maskOpen=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernelOpen)
    maskClose=cv2.morphologyEx(maskOpen,cv2.MORPH_CLOSE,kernelClose)

    maskFinal=maskClose
    conts, _ = cv2.findContours(maskFinal.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    
    cv2.drawContours(img,conts,-1,(255,0,0),3)
    for i in range(len(conts)):
        x,y,w,h=cv2.boundingRect(conts[i])
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255), 2)
        cv2.putText(img, str(i+1),(x,y+h),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,255,255))
        
    cv2.imshow("maskClose",maskClose)
    cv2.imshow("cam",img)
    if cv2.waitKey(10) &0xFF ==ord('q'):
                cap.release()
                cv2.destroyAllWindows()
                break
