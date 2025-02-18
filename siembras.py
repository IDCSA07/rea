from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector
import textwrap

def siembras(frame):
    for widget in frame.winfo_children():
        widget.destroy()

    frame.config(bg="#1E1E1E")

    Label(
        frame,
        text="🌱 Cultivos Disponibles 🌱",
        bg="#1E1E1E",
        fg="white",
        font=("Arial", 22, "bold")
    ).pack(pady=15)

    Label(
        frame,
        text="Consulta los cultivos disponibles en Puebla.",
        bg="#1E1E1E",
        fg="#A0A0A0",
        font=("Arial", 14)
    ).pack(pady=5)
