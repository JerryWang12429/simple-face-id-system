# simple-face-id-system
a symple face id system with python 3.6 and openCV


Envirenment :   
-  python 3.6  
-  openCV 3.4.1  
-  Tkinter 8.6.7  
                      
` execute main program named "gui_Test" `

Click `camera` button to start the recognizer.

You can register your face with `register` button if the name is unknown.

The program will take 10 pic. and they will be saved.(picture will be take only if your face in front of the camera)

Then press `training` button,it will train the feature of the face picture with LBPH algorithm and save the feature with names and IDs into DB.

Finally,restart the camera program by click the `camera` button,program will recognize the face and show id beside.
