import cv2
import numpy as np
import matplotlib.pyplot as plt


def region_of_interset(img, vertices):
    mask = np.zeros_like(img)
    match_mask_color = 255
    cv2.fillPoly(mask, vertices, match_mask_color)
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image


def draw_the_lines(img, lines):
    img = np.copy(img)
    blank_image = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)

    if lines is not None:  # Ensure lines are found before drawing
        for line in lines:
            for x1, y1, x2, y2 in line:
                cv2.line(blank_image, (x1, y1), (x2, y2), (0, 255, 0), thickness=3)

    img = cv2.addWeighted(img, 0.8, blank_image, 1, 0.0)
    return img


def process(image):
    height, width = image.shape[:2]

    region_of_interset_vertices = [
        (0, height),
        (int(width / 2), int(height / 2)),
        (width, height)
    ]

    gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    canny_image = cv2.Canny(gray_image, 100, 120)
    cropped_Image = region_of_interset(canny_image, np.array([region_of_interset_vertices], np.int32))

    lines = cv2.HoughLinesP(cropped_Image, rho=2, theta=np.pi/60, threshold=50,
                            minLineLength=40, maxLineGap=100)

    image_with_lines = draw_the_lines(image, lines) if lines is not None else image
    return image_with_lines


cap = cv2.VideoCapture('road_video.mp4')

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break  # Exit loop if video ends or frame cannot be read
    frame = cv2.resize(frame, (720, 480))
    frame = process(frame)
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
