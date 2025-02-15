import cv2
import numpy as np
from PIL import Image
from util import get_limits

yellow = [0, 255, 255]

cap = cv2.VideoCapture('ye.mp4')  # Ensure file exists

if not cap.isOpened():
    print("Error: Could not open video file")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Error: Could not read frame (End of video or file not found)")
        break  # Exit the loop

    hsvImg = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_limit, upper_limit = get_limits(color=yellow)
    mask = cv2.inRange(hsvImg, lower_limit, upper_limit)

    mask_ = Image.fromarray(mask)
    box = mask_.getbbox()

    if box is not None:
        x1, y1, x2, y2 = box
        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 255), 4)

    cv2.imshow('Frame', frame)

    if cv2.waitKey(40) & 0xFF == ord('x'):
        break

cap.release()
cv2.destroyAllWindows()
