import cv2 as cv
import matplotlib.pyplot as plt
img =cv.imread('lena.png',-1)

cv.imshow("image",img)

img=cv.cvtColor(img,cv.COLOR_BGR2RGB)
plt.imshow(img)
plt.show()
cv.waitKey(0)
cv.destroyAllWindows()