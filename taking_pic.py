

import cv2 
import os
import sys

count = 0
folder = sys.argv[1]
if not os.path.exists('images/' + folder):
    os.makedirs('images/'+folder)

# Load prebuilt model for Frontal Face
cascadePath = "haarcascade_frontalface_default.xml"

# Create classifier from prebuilt model
faceCascade = cv2.CascadeClassifier(cascadePath);

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FPS, 1)

while(cap.isOpened()):
  # get pic from cam
  ret, frame = cap.read()
  
  resized_image = cv2.resize(frame, (800, 450)) 
  
  gray = cv2.cvtColor(resized_image,cv2.COLOR_BGR2GRAY)
  
  faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.15,
    minNeighbors=5,
    minSize=(5,5)
    )
  
  
  for(x,y,w,h) in faces:

  
        file_name = 'images/' + folder + '/' + str(count) + '.jpg'
        cv2.imwrite(file_name,resized_image)
        
        # Create rectangle around the face
        cv2.rectangle(resized_image, (x-20,y-20), (x+w+20,y+h+20), (0,255,0), 4)
        count = count + 1   
        
  
        
  cv2.putText(resized_image, str(count) , (10, 10), cv2.FONT_HERSHEY_SIMPLEX,
  1, (0, 255, 255), 1,  cv2.LINE_AA)      
  # show img
  cv2.imshow('cam', resized_image)
  
  if cv2.waitKey(100) & count == 10:
    break

# release and close cam
cap.release()

cv2.destroyAllWindows()
cv2.waitKey(1)
print('save images successful')

