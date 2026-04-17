# Proyecto 6: Computer Vision

Este proyecto se basa en el reconocimiento facial, puede ser util para tomar asistencia, aprobar entrada a algun residencial, autorizar la entrada a una escuela sin necesidad de credencial, tomar asistencia en un Gimnasio etc..

Requisitos Obligatorios:
Python 3.8 o superior
Cámara web
Sistema operativo: macOS / Windows / Linux

Instalación:

1._Clonar repositorio:
 git clone <https://github.com/eliel2412124-max/Sistema-de-asistencia-automatizada-con-reconocimiento-facial> aqui va el url del repositorio dentro de TU perfil. En lugar de venir eliel2412124-max debe venir el nombre de tu usuario Github.
 2._
 cd <NOMBRE_DEL_PROYECTO>

 3._Crear etorno virtual:
 python -m venv venv
 si no funciona, prueba:
 python3 -m venv venv

 4._Activar entorno virtual:
 MAC OS/LINUX:
 source venv/bin/activate

WINDOWS:
venv\Scripts\activate

5._Instalar dependencias:
pip install -r requirements.txt

6._Ya dentro, ejecuta el archivo app.py:
python app.py


USO DE LA APLICACIÔN:
Al ejecutar la aplicación se despliega un menú:
1._Registrar
2._Reconocimiento
3._Salir

REGISTRO:
1._Haz click en registrar persona.
2._Ingresa el nombre de la persona que quieres registrar.
3._Observa la camara y mueve la cabeza en varias direcciones.

RECONOCIMIENTO:
1._Haz click en Iniciar Reconocimiento.
2._El sistema por si solo detectara el rostro en caso de que ya este registrado.
3._Para salir de esta opción puede dar click en la tecla ESC o Q.(En la parte superior verás la instrucción)

SALIR:
Dar click en la opción SALIR

El sistema genera automáticamente:
	attendance.csv → Registro general
	attendance.xlsx → Registro en Excel
	Cada día se guarda en una hoja diferente

OSERVACIONES IMPORTANTES:
1.-Asegúrate de tener buena iluminación y mueve la cabeza en diferentes direcciones para mejorar el reconocimiento.
2.-No uses nombres duplicados al registrar personas.

Si cv2.face falla, instala:
pip install opencv-contrib-python