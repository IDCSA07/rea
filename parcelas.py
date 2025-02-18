from tkinter import *
from tkinter import ttk, messagebox, simpledialog
import mysql.connector

def conectar_bd():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Ccrj1108231407&",
        database="sistema_login"
    )

def actualizar_tabla(tabla, id_usuario):
    for row in tabla.get_children():
        tabla.delete(row)
    conexion = conectar_bd()
    cursor = conexion.cursor()
    
    cursor.execute("SELECT nombre, ubicacion, tamano, fertilidad_suelo FROM parcelas WHERE id_usuario = %s", (id_usuario,))
    
    for row in cursor.fetchall():
        tabla.insert("", END, values=row)
    
    cursor.close()
    conexion.close()

def agregar_parcela(nombre, ubicacion, tamano, fertilidad, id_usuario, tabla):
    if not nombre or not ubicacion or not tamano or not fertilidad:
        messagebox.showwarning("Advertencia", "Todos los campos son obligatorios")
        return
    
    try:
        tamano = float(tamano)
    except ValueError:
        messagebox.showerror("Error", "El tamaño debe ser un número válido.")
        return
    
    conexion = conectar_bd()
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO parcelas (nombre, ubicacion, tamano, fertilidad_suelo, id_usuario) VALUES (%s, %s, %s, %s, %s)", 
                   (nombre, ubicacion, tamano, fertilidad, id_usuario))
    conexion.commit()
    cursor.close()
    conexion.close()
    actualizar_tabla(tabla, id_usuario)

def parcelas(frame, id_usuario):
    for widget in frame.winfo_children():
        widget.destroy()

    parcelas_frame = Frame(frame, bg="#1E1E1E", padx=20, pady=20)
    parcelas_frame.pack(pady=20, padx=20, fill="both", expand=True)

    Label(parcelas_frame, text="🌱 Cultivos Disponibles 🌱", bg="#1E1E1E", fg="white", font=("Arial", 22, "bold")).pack(pady=10)
    ttk.Separator(parcelas_frame, orient="horizontal").pack(fill="x", pady=10)

    form_frame = Frame(parcelas_frame, bg="#1E1E1E")
    form_frame.pack(pady=10, fill="x")
    
    Label(form_frame, text="Nombre:", bg="#1E1E1E", fg="#AAAAAA", font=("Arial", 12, "bold")).grid(row=0, column=0, padx=5, pady=5, sticky="w")
    nombre_entry = ttk.Entry(form_frame)
    nombre_entry.grid(row=0, column=1, padx=5, pady=5)
    
    Label(form_frame, text="Ubicación:", bg="#1E1E1E", fg="#AAAAAA", font=("Arial", 12, "bold")).grid(row=0, column=2, padx=5, pady=5, sticky="w")
    ubicacion_entry = ttk.Entry(form_frame)
    ubicacion_entry.grid(row=0, column=3, padx=5, pady=5)
    
    Label(form_frame, text="Tamaño:", bg="#1E1E1E", fg="#AAAAAA", font=("Arial", 12, "bold")).grid(row=0, column=4, padx=5, pady=5, sticky="w")
    tamano_entry = ttk.Entry(form_frame)
    tamano_entry.grid(row=0, column=5, padx=5, pady=5)
    
    Label(form_frame, text="Fertilidad:", bg="#1E1E1E", fg="#AAAAAA", font=("Arial", 12, "bold")).grid(row=0, column=6, padx=5, pady=5, sticky="w")
    fertilidad_entry = ttk.Entry(form_frame)
    fertilidad_entry.grid(row=0, column=7, padx=5, pady=5)
    
    ttk.Button(form_frame, text="Agregar Parcela", command=lambda: agregar_parcela(
        nombre_entry.get(), ubicacion_entry.get(), tamano_entry.get(), fertilidad_entry.get(), id_usuario, tabla)).grid(row=0, column=8, padx=10, pady=5)
    
    tabla_frame = Frame(parcelas_frame)
    tabla_frame.pack(pady=10, padx=10, fill=BOTH, expand=True)
    
    columnas = ("Nombre", "Ubicación", "Tamaño(m²)", "Fertilidad")
    tabla = ttk.Treeview(tabla_frame, columns=columnas, show="headings")
    
    for col in columnas:
        tabla.heading(col, text=col)
        tabla.column(col, anchor="center")
    
    tabla.pack(fill=BOTH, expand=True)
    actualizar_tabla(tabla, id_usuario)


