""" Python program to extract 1 frame per second from input video and store it to the folder specified by path.
    Just press run. Then go and check the location you specified for saving the images. """

import math
import os
import cv2

# "C:\Users\Anjishnu\Desktop\Face_Recognition" should be the location of haarcascade_frontalface_default.xml file.
# "C:\Users\Anjishnu\Desktop\Face_Recognition\Videos\Anjishnu.mp4" specifies video loaction.
# "C:\Users\Anjishnu\Desktop\Face_Recognition\Faces\Anjishnu" specifies location where images are saved.

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')# load xml file.
cap = cv2.VideoCapture(r"C:\Users\Anjishnu\Desktop\Face_Recognition\Videos\Anjishnu.mp4")# video is stored at this location.
frameRate = cap.get(5) # frame rate of input video
path = r"C:\Users\Anjishnu\Desktop\Face_Recognition\Faces\Anjishnu"# images wwill be saved at this location.
count = 1 # required for naming images uniquely while saving them.

while ( cap.isOpened() ):

    frameId = cap.get(1) # current frame number
    ret,frame = cap.read()
    if (ret != True):
        break
        
    if (frameId % math.floor(frameRate) == 0): # this ensures that only one frame per second is saved to the folder.
        
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray,1.1,8)

        # extract region of face and save it to location specified.
        for (x,y,w,h) in faces:
            face = gray[y:y+h, x:x+w]
            face = cv2.resize(face, (28,28), interpolation = cv2.INTER_AREA)# resizes the face region to size 28*28 pixels.
            cv2.imwrite(os.path.join(path ,'Anjishnu.%d.jpg'%count),face)# cv2.imwrite('Cropped%d.png'%count,roi)
            count = count+1
            
        # press q to stop the program.
        key = cv2.waitKey(1) & 0xff
        if key == ord('q'):
            break
        
cap.release()
cv2.destroyAllWindows()