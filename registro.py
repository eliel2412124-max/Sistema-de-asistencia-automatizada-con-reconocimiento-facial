import cv2
import os
import sys

nombre = sys.argv[1]

ruta = f"data/rostros/{nombre}"
os.makedirs(ruta, exist_ok=True)

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

video = cv2.VideoCapture(0)

contador = 0

while True:
    ret, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    for (x, y, w, h) in faces:
        rostro = frame[y:y+h, x:x+w]
        rostro = cv2.resize(rostro, (150, 150))
        
        cv2.imwrite(f"{ruta}/{contador}.jpg", rostro)
        contador += 1
        
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)
    
    cv2.imshow("Registro de rostro", frame)
    
    if contador >= 50:
        break
    
    if cv2.waitKey(1) & 0xFF in [27, ord('q')]:
        break

video.release()
cv2.destroyAllWindows()