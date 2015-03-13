""" Experiment with face detection and image filtering using OpenCV """

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier('/home/emily/Documents/SoftDesSp15/toolbox/image_processing/haarcascade_frontalface_alt.xml')
kernel = np.ones((21,21),'uint8')

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    faces = face_cascade.detectMultiScale(frame, scaleFactor=1.2, minSize=(20,20)) #detects the face
    for (x,y,w,h) in faces:
    	frame[y:y+h,x:x+w,:] = cv2.dilate(frame[y:y+h,x:x+w,:], kernel)
    	cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255))

    	cv2.circle(frame, (x+w/4+15, y+h/4+40), 15, (255,255,255), -1, 8, 0)
    	cv2.circle(frame, (x+3*w/4-15, y+h/4+40), 15, (255,255,255), -1, 8, 0)

    	cv2.circle(frame, (x+w/4+15, y+h/4+48), 7, (0,0,0), -1, 8, 0)
    	cv2.circle(frame, (x+3*w/4-15, y+h/4+48), 7, (0,0,0), -1, 8, 0)

    	cv2.ellipse(frame, (x+w/2, y+3*h/4+20), (35,20), 180, 360, 180, (0, 0,255), -1)

    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()