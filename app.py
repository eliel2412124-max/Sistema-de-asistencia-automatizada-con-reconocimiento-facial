import tkinter as tk
from tkinter import simpledialog, messagebox
import subprocess
import os

# Funciones

def registrar():
    nombre = simpledialog.askstring("Registro", "Ingresa el nombre de la persona:")
    
    if nombre:
        os.system(f'python registro.py "{nombre}"')


def reconocer():
    subprocess.run(["python", "reconocimiento.py"])

# Ventana principal
ventana = tk.Tk()
ventana.title("Sistema de Asistencia Facial")
ventana.geometry("400x300")
ventana.resizable(False, False)

ventana.configure(bg="#1e1e2f")

titulo = tk.Label(
    ventana, 
    text="Sistema de Asistencia", 
    font=("Arial", 18),
    bg="#1e1e2f",
    fg="white"
)
titulo.pack(pady=20)

# Botón registrar
btn_registrar = tk.Button(
    ventana,
    text="Registrar Persona",
    width=20,
    height=2,
    command=registrar
)
btn_registrar.pack(pady=10)

# Botón reconocimiento
btn_reconocer = tk.Button(
    ventana,
    text="Iniciar Reconocimiento",
    width=20,
    height=2,
    command=reconocer
)
btn_reconocer.pack(pady=10)

# Botón salir
btn_salir = tk.Button(
    ventana,
    text="Salir",
    width=20,
    height=2,
    command=ventana.quit
)
btn_salir.pack(pady=20)

ventana.mainloop()