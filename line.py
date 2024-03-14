import cv2
img=cv2.imread("pika.png")

#Start coordinate, here (0,0) represents the top-left corner of img
start_point=(0,0)

#End coordinate, here (425,425) represents the bottom-right corner of img
end_point=(425,425)

#color-BGR format
color=(0,255,0)

#Thickness of line
thickness=9

#Defining line on screen
img=cv2.line(img,start_point,end_point,color,thickness)

cv2.imshow("Lined pika", img)
cv2.waitKey(0)
cv2.destroyAllWindows()