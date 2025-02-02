import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# Load the image
img = cv.imread('lena.png')

# Apply different blurring techniques
average = cv.blur(img, (5,5))  # Averaging
gaussian = cv.GaussianBlur(img, (5,5), 0)  # Gaussian Blur
median = cv.medianBlur(img, 5)  # Median Blur
bilateral = cv.bilateralFilter(img, 9, 75, 75)  # Bilateral Filter

# Display results using Matplotlib
titles = ['Original', 'Averaging', 'Gaussian Blur', 'Median Blur', 'Bilateral Filter']
images = [img, average, gaussian, median, bilateral]

plt.figure(figsize=(12, 6))
for i in range(5):
    plt.subplot(2, 3, i+1)
    plt.imshow(cv.cvtColor(images[i], cv.COLOR_BGR2RGB))
    plt.title(titles[i])
    plt.axis('off')

plt.show()
