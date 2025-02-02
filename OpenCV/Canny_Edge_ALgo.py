import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# Load the image
img = cv.imread('lena.png', cv.IMREAD_GRAYSCALE)

# Apply Gaussian Blur to reduce noise
blurred = cv.GaussianBlur(img, (5, 5), 0)

# Apply Canny Edge Detection
edges = cv.Canny(blurred, 50, 150)  # Lower & upper threshold values

# Display results using Matplotlib
titles = ['Original Image', 'Blurred Image', 'Canny Edges']
images = [img, blurred, edges]

plt.figure(figsize=(12, 4))
for i in range(3):
    plt.subplot(1, 3, i+1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.axis('off')

plt.show()
