import cv2

img=cv2.imread('C:/Users/HP/Desktop/Python WH class/c118 Face detection/boy.jpg')

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

face_cascade=cv2.CascadeClassifier('C:/Users/HP/Desktop/Python WH class/c118 Face detection/haarcascade_frontalface_default.xml')

faces=face_cascade.detectMultiScale(gray,1.1,5)

print(len(faces))
 
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_color=img[y:y+h,x:x+w]
    cv2.imwrite("Face.jpg",roi_color)

cv2.imshow("face",img)
cv2.waitKey(0)

