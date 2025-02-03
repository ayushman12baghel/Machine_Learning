import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread('lena.png')
# hist=cv2.calcHist([img],[0],None,[256],[0,256])

cv2.imshow('image',img)
# plt.hist(img.ravel(),256,[0,256])
b,g,r=cv2.split(img)
cv2.imshow('blue',b)
cv2.imshow('green',g)
cv2.imshow('red',r)
plt.hist(b.ravel(),256,[0,256])
plt.hist(g.ravel(),256,[0,256])
plt.hist(r.ravel(),256,[0,256])

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()