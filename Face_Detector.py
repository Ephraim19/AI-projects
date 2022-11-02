import cv2

#load data
face_data = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# #choose image to be detected
#img = cv2.imread('Ephraim.jpg')
#convert img to blacknwhite

webcam = cv2.VideoCapture(0)

while True:
    succesful_frame, frame = webcam.read()
    blacknwhite = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    #Detect faces
    face_coord = face_data.detectMultiScale(blacknwhite)

    #draw rectangle around the face
    for (x,y,w,h) in face_coord:
        cv2.rectangle(frame,(x,y),(x + w,y + h),(0,255,0),2)

    #show image
    cv2.imshow("This is Ephraim", frame)
    cv2.waitKey(1)






# print("Code completed")