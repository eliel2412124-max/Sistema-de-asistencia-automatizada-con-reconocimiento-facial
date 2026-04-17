import cv2
import os
import numpy as np
import pandas as pd
from datetime import datetime


# Archivos
archivo_csv = "registro.csv"
archivo_excel = "registro.xlsx"

# Crear CSV si no existe
if not os.path.exists(archivo_csv):
    df = pd.DataFrame(columns=["Nombre", "Fecha", "Hora"])
    df.to_csv(archivo_csv, index=False)

# Registrar asistencia
def registrar_asistencia(nombre):
    hoy = datetime.now().strftime("%Y-%m-%d")
    hora = datetime.now().strftime("%H:%M:%S")

    # Leer CSV
    df = pd.read_csv(archivo_csv)

    # Evitar duplicados
    if not ((df['Nombre'] == nombre) & (df['Fecha'] == hoy)).any():
        nuevo = pd.DataFrame([[nombre, hoy, hora]], columns=["Nombre", "Fecha", "Hora"])
        df = pd.concat([df, nuevo], ignore_index=True)

        # Guardar CSV
        df.to_csv(archivo_csv, index=False)

        # Guardar Excel con hoja por día
        if os.path.exists(archivo_excel):
            with pd.ExcelWriter(archivo_excel, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
                df_dia = df[df["Fecha"] == hoy]
                df_dia.to_excel(writer, sheet_name=hoy, index=False)
        else:
            with pd.ExcelWriter(archivo_excel, engine='openpyxl') as writer:
                df_dia = df[df["Fecha"] == hoy]
                df_dia.to_excel(writer, sheet_name=hoy, index=False)

        # BONUS 🔥 mensaje en consola
        print(f"Asistencia registrada: {nombre} a las {hora}")


# Cargar rostros
data_path = 'data/rostros'
people = os.listdir(data_path)

labels = []
faces_data = []
label = 0

for person in people:
    person_path = os.path.join(data_path, person)
    for file in os.listdir(person_path):
        img_path = os.path.join(person_path, file)
        img = cv2.imread(img_path, 0)
        
        if img is not None:
            faces_data.append(img)
            labels.append(label)
    
    label += 1

# Entrenar modelo
face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.train(faces_data, np.array(labels))

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

video = cv2.VideoCapture(0)

# Reconocimiento en tiempo real
while True:
    ret, frame = video.read()
    if not ret:
        break
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    for (x, y, w, h) in faces:
        rostro = gray[y:y+h, x:x+w]
        rostro = cv2.resize(rostro, (150, 150))
        
        result = face_recognizer.predict(rostro)
        
        if result[1] < 70:
            name = people[result[0]]
            
            registrar_asistencia(name)
            
            cv2.putText(frame, name, (x, y-10), 2, 0.8, (0,255,0), 2)
            cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
        else:
            cv2.putText(frame, "Desconocido", (x, y-10), 2, 0.8, (0,0,255), 2)
            cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)

    cv2.putText(frame, "ESC o Q para salir", (10, 30), 2, 0.7, (255,255,255), 2)
    
    cv2.imshow("Reconocimiento Facial", frame)

    if cv2.waitKey(1) & 0xFF in [27, ord('q')]:
        break

video.release()
cv2.destroyAllWindows()