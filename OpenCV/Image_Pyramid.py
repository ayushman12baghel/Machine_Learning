import cv2 as cv
import matplotlib.pyplot as plt

# Load the image
img = cv.imread('lena.png')

# Generate Gaussian Pyramid
lower_res1 = cv.pyrDown(img)  # First level downsample
lower_res2 = cv.pyrDown(lower_res1)  # Second level downsample
higher_res = cv.pyrUp(lower_res2)  # Upsampling the second level

# Display images
titles = ['Original Image', 'Level 1 Down', 'Level 2 Down', 'Upsampled Image']
images = [img, lower_res1, lower_res2, higher_res]

plt.figure(figsize=(10, 5))
for i in range(4):
    plt.subplot(2, 2, i+1)
    plt.imshow(cv.cvtColor(images[i], cv.COLOR_BGR2RGB))
    plt.title(titles[i])
    plt.axis('off')

plt.show()
