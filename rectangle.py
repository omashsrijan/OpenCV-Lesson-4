import cv2
img=cv2.imread("pika.png")

#Start coordinate is 0,0)
start_point=(10,10)

#End coordinate is (400,400)
end_point=(400,400)

#color-BGR format
color=(0,0,255)

#Thickness of rectangle border(negative value indicates filled rectangle)
thickness=2

#Defining rectangle on screen
img=cv2.rectangle(img,start_point,end_point,color,thickness)

cv2.imshow("Rectangle pika", img)
cv2.waitKey(0)
cv2.destroyAllWindows()