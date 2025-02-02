import cv2
import numpy as np

# img=cv2.imread('lena.png',1)
img=np.zeros([512,512,3])
img=cv2.line(img,(0,0),(255,255),(0,0,255),5)
img=cv2.arrowedLine(img,(0,510),(255,255),(0,0,255),5)
img=cv2.rectangle(img,(384,0),(510,128),(0,0,255),5)
img=cv2.circle(img,(447,255),63,(0,255,0),10)
img=cv2.putText(img,'OpenCV',(10,500),cv2.FONT_HERSHEY_SIMPLEX,4,(255,255,255),10)

cv2.imshow('image',img)



cv2.waitKey(0)
cv2.destroyAllWindows()