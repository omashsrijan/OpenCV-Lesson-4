import cv2
img=cv2.imread("pika.png")

#Font of the text
font=cv2.FONT_HERSHEY_SIMPLEX

#Origin coordinate of the text box, basically the top-left corner of the textbox
origin=(150,150)

#color-BGR format
color=(255,0,0)

#Size of font
fontscale=1

#Boldness of text
boldness=2

#Defining textbox on screen
img=cv2.putText(img,"Bonjour!",origin,font,fontscale,color,boldness)

cv2.imshow("Talking pika", img)
cv2.waitKey(0)
cv2.destroyAllWindows()