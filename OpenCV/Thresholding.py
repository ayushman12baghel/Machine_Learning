import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
# Simple Thresholding
img=cv.imread('gradient.jpeg',0)
_,th1=cv.threshold(img,127,255,cv.THRESH_BINARY)
_,th2=cv.threshold(img,127,255,cv.THRESH_BINARY_INV)
_,th3=cv.threshold(img,127,255,cv.THRESH_TRUNC)
_,th4=cv.threshold(img,127,255,cv.THRESH_TOZERO)
_,th5=cv.threshold(img,127,255,cv.THRESH_TOZERO_INV)

# cv.imshow('Image',img)
# cv.imshow('th1',th1)
# cv.imshow('th2',th2)
# cv.imshow('th3',th3)
# cv.imshow('th4',th4)
# cv.imshow('th5',th5)


# //Adaptive Thresholding

# img2=cv.imread('sudoku.png')
# _,th1=cv.threshold(img,127,255,cv.THRESH_BINARY)
# th2=cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,2)

# cv.imshow("image",img2)
# cv.imshow("th1",th1)
# cv.imshow("th2",th2)

titles= ['Original Image', 'BINARY', 'BINARY_INV', 'TRUNC' ,'TOZERO', 'TOZERO_INV']
images=[img,th1,th2,th3,th4,th5]

for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])

plt.show()
cv.waitKey(0)
cv.destroyAllWindows()