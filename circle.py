import cv2
img=cv2.imread("pika.png")

#color-BGR format
color=(255,0,0)

#circle center coordinates
center=(120,50)

#radius length of circle
radius=20

#Thickness of circle border(negative value indicates filled circle)
thickness=2

#Defining circle on screen
img=cv2.circle(img,center,radius,color,thickness)

cv2.imshow("Circle", img)
cv2.waitKey(0)
cv2.destroyAllWindows()



