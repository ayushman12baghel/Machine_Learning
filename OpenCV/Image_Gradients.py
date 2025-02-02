import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# Load the image
img = cv.imread('lena.png', cv.IMREAD_GRAYSCALE)

# Apply different gradient operators
laplacian = cv.Laplacian(img, cv.CV_64F)  # Laplacian Gradient
sobelx = cv.Sobel(img, cv.CV_64F, 1, 0, ksize=5)  # Sobel X
sobely = cv.Sobel(img, cv.CV_64F, 0, 1, ksize=5)  # Sobel Y
scharrx = cv.Scharr(img, cv.CV_64F, 1, 0)  # Scharr X
scharry = cv.Scharr(img, cv.CV_64F, 0, 1)  # Scharr Y
edges = cv.Canny(img, 50, 150)

# Convert gradients to absolute values (uint8)
laplacian = np.uint8(np.absolute(laplacian))
sobelx = np.uint8(np.absolute(sobelx))
sobely = np.uint8(np.absolute(sobely))
scharrx = np.uint8(np.absolute(scharrx))
scharry = np.uint8(np.absolute(scharry))

# Display results using Matplotlib
titles = ['Original', 'Laplacian', 'Sobel X', 'Sobel Y', 'Scharr X', 'Scharr Y','Canny']
images = [img, laplacian, sobelx, sobely, scharrx, scharry,edges]

plt.figure(figsize=(12, 6))
for i in range(7):
    plt.subplot(2, 4, i+1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.axis('off')

plt.show()
