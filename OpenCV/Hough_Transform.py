import cv2
import numpy as np

# Load image
image = cv2.imread('road.jpeg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect edges using Canny
edges = cv2.Canny(gray, 50, 150)

# Apply Hough Transform
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength=50, maxLineGap=10)

# Draw detected line segments
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

# Show result
cv2.imshow("Hough Lines", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
