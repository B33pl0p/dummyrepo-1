import cv2
import numpy as np


capture = cv2.VideoCapture(0)

while True:
    ret, frame = capture.read()

    width = int(capture.get(3))
    height = int(capture.get(4))

    img = cv2.line(frame, (0, 0), (width, height), (0, 0, 255), 2 )
    img = cv2.line(frame, (width, 0), (0, height), (0, 0, 255), 2)
    img = cv2.rectangle(frame, (50, 50), ((width - 50), (height - 50)), (200, 255, 100), 4)
    img = cv2.circle(frame, (width//2, height//2), 50, (100, 250, 250), 3)
    font = cv2.FONT_HERSHEY_SIMPLEX
    img = cv2.putText(img, 'halo frands chaye peelo', (120, (height - 20)), font, 1,  (200, 200, 200), 3, cv2.LINE_AA)

    cv2.imshow('frame', img)
    print(frame)

    if cv2.waitKey(1) == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
