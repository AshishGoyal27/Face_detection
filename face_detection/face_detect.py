import cv2
#load the pre-trained face detection model
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
#choose an image on which we want to test our code
img = cv2.imread('image2.jpg')
#detect faces in an image
faces = face_cascade.detectMultiScale(img, 1.1, 4)
#draw rectangles around the detected faces
for (x, y, w, h) in faces: 
  cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
cv2.imwrite("face_detected2.png", img) 
print('Successfully saved')
