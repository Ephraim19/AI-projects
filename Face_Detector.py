import cv2

#load data
face_data = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

#choose image to be detected
img = cv2.imread('Ephraim.jpg')
#convert img to blacknwhite
blacknwhite = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#Detect faces
face_coord = face_data.detectMultiScale(blacknwhite)
print(face_coord)
#draw rectangle around the face
for (x,y,w,h) in face_coord:
    cv2.rectangle(img,(x,y),(x + w,y + h),(0,255,0),2)
#show image
cv2.imshow("This is Ephraim", img)
cv2.waitKey()

print("Code completed")