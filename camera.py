
#import OpenCV module
import cv2
import pickle

# Load prebuilt model for Frontal Face
cascadePath = "haarcascade_frontalface_default.xml"

# Create classifier from prebuilt model
faceCascade = cv2.CascadeClassifier(cascadePath);


recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("face-trainner.yml")


labels = {"person_name": 1}
with open("pickles/face-labels.pickle", 'rb') as f:
	og_labels = pickle.load(f)
	labels = {v:k for k,v in og_labels.items()}
    
    
# Set the font style
font = cv2.FONT_HERSHEY_SIMPLEX

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
      roi_gray = gray[y:y+h, x:x+w] #(ycord_start, ycord_end)
      id_, conf = recognizer.predict(roi_gray)
      if conf>=0 and conf <= 85:
          font = cv2.FONT_HERSHEY_SIMPLEX
          name = labels[id_]
          color = (0, 255, 0)
          stroke = 2
          cv2.putText(resized_image, name, (x,y), font, 1, color, stroke, cv2.LINE_AA)
          # Create rectangle around the face
          cv2.rectangle(resized_image, (x-20,y-20), (x+w+20,y+h+20), (0,255,0), 4)
      else:
          font = cv2.FONT_HERSHEY_SIMPLEX
          name = 'unknown'
          color = (0, 255, 0)
          stroke = 2
          cv2.putText(resized_image, name, (x,y), font, 1, color, stroke, cv2.LINE_AA)
          # Create rectangle around the face
          cv2.rectangle(resized_image, (x-20,y-20), (x+w+20,y+h+20), (0,255,0), 4)
            
            
  # show img
  cv2.imshow('cam', resized_image)

  # press q for leave
  if cv2.waitKey(200) & 0xFF == ord('q'):
    break

# release and close cam
cap.release()

cv2.destroyAllWindows()
cv2.waitKey(1)