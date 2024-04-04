import cv2
import numpy as np

img = 255 * np.ones((400, 600, 3), dtype=np.uint8)

cv2.rectangle(img, (200, 250), (250, 400), (255, 0, 0), -1)
cv2.circle(img, (240, 325), 5, (0, 255, 0), -1)
cv2.rectangle(img, (100, 200), (400, 400), (0, 0, 255), -1)  
cv2.rectangle(img, (150, 100), (350, 200), (0, 0, 255), -1)  
cv2.line(img, (250, 100), (150, 200), (0, 255, 0), 3)  
cv2.line(img, (250, 100), (350, 200), (0, 255, 0), 3)  
cv2.circle(img, (500, 100), 50, (0, 255, 255), -1)

cv2.imshow("My Hut", img)
cv2.waitKey(0)
cv2.destroyAllWindows()