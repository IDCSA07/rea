from tkinter import *

def mostrar_perfil(frame):
    Label(
        frame,
        text="Mi Perfil",
        bg="#121212",
        fg="white",
        font=("Arial", 20, "bold")
    ).pack(pady=20)

    Label(
        frame,
        text="Nombre: Usuario Prueba\nCorreo: usuario@ejemplo.com\nPublicaciones: - Sin publicaciones -",
        bg="#121212",
        fg="#B3B3B3",
        font=("Arial", 14)
    ).pack(pady=10)
