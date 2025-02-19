from tkinter import *
from tkinter import ttk, messagebox
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
    
    cursor.execute("SELECT nombre, tipo, cantidad_disponible, unidad_medida, fecha_caducidad FROM insumos WHERE id_usuario = %s", (id_usuario,))
    
    for row in cursor.fetchall():
        tabla.insert("", END, values=row)
    
    cursor.close()
    conexion.close()

def agregar_insumo(nombre, tipo, cantidad_disponible, unidad_medida, fecha_caducidad, id_usuario, tabla):
    if not nombre or not tipo or not cantidad_disponible or not unidad_medida or not fecha_caducidad:
        messagebox.showwarning("Advertencia", "Todos los campos son obligatorios")
        return
    
    try:
        cantidad_disponible = float(cantidad_disponible)  # Asegurar que es un número válido
    except ValueError:
        messagebox.showerror("Error", "La cantidad disponible debe ser un número válido.")
        return
    
    # Validación del formato de fecha
    if not fecha_caducidad.count("-") == 2 or len(fecha_caducidad) != 10:
        messagebox.showerror("Error", "La fecha de caducidad debe estar en formato YYYY-MM-DD.")
        return
    
    conexion = conectar_bd()
    cursor = conexion.cursor()
    cursor.execute(
        "INSERT INTO insumos (nombre, tipo, cantidad_disponible, unidad_medida, fecha_caducidad, id_usuario) VALUES (%s, %s, %s, %s, %s, %s)", 
        (nombre, tipo, cantidad_disponible, unidad_medida, fecha_caducidad, id_usuario)
    )
    conexion.commit()
    cursor.close()
    conexion.close()
    actualizar_tabla(tabla, id_usuario)

def insumos(frame, id_usuario):
    for widget in frame.winfo_children():
        widget.destroy()

    insumos_frame = Frame(frame, bg="#1E1E1E", padx=20, pady=20)
    insumos_frame.pack(pady=20, padx=20, fill="both", expand=True)

    Label(insumos_frame, text="📦 Insumos Disponibles 📦", bg="#1E1E1E", fg="white", font=("Arial", 18, "bold")).pack(pady=10)
    ttk.Separator(insumos_frame, orient="horizontal").pack(fill="x", pady=10)

    form_frame = Frame(insumos_frame, bg="#1E1E1E")
    form_frame.pack(pady=10, fill="x")
    
    Label(form_frame, text="Nombre:", bg="#1E1E1E", fg="#AAAAAA", font=("Arial", 10, "bold")).grid(row=0, column=0, padx=3, pady=3, sticky="w")
    nombre_entry = ttk.Entry(form_frame, width=15)
    nombre_entry.grid(row=0, column=1, padx=3, pady=3)
    
    Label(form_frame, text="Tipo:", bg="#1E1E1E", fg="#AAAAAA", font=("Arial", 10, "bold")).grid(row=0, column=2, padx=3, pady=3, sticky="w")
    tipo_entry = ttk.Entry(form_frame, width=15)
    tipo_entry.grid(row=0, column=3, padx=3, pady=3)
    
    Label(form_frame, text="Cantidad:", bg="#1E1E1E", fg="#AAAAAA", font=("Arial", 10, "bold")).grid(row=0, column=4, padx=3, pady=3, sticky="w")
    cantidad_entry = ttk.Entry(form_frame, width=10)
    cantidad_entry.grid(row=0, column=5, padx=3, pady=3)
    
    Label(form_frame, text="Unidad:", bg="#1E1E1E", fg="#AAAAAA", font=("Arial", 10, "bold")).grid(row=0, column=6, padx=3, pady=3, sticky="w")
    unidad_entry = ttk.Entry(form_frame, width=10)
    unidad_entry.grid(row=0, column=7, padx=3, pady=3)
    
    Label(form_frame, text="Fecha (YYYY-MM-DD):", bg="#1E1E1E", fg="#AAAAAA", font=("Arial", 10, "bold")).grid(row=0, column=8, padx=3, pady=3, sticky="w")
    fecha_entry = ttk.Entry(form_frame, width=12)
    fecha_entry.grid(row=0, column=9, padx=3, pady=3)
    
    ttk.Button(form_frame, text="Agregar", command=lambda: agregar_insumo(
        nombre_entry.get(), tipo_entry.get(), cantidad_entry.get(), unidad_entry.get(), fecha_entry.get(), id_usuario, tabla)).grid(row=0, column=10, padx=5, pady=3)
    
    tabla_frame = Frame(insumos_frame)
    tabla_frame.pack(pady=10, padx=10, fill=BOTH, expand=True)
    
    columnas = ("Nombre", "Tipo", "Cantidad", "Unidad", "Fecha de Caducidad")
    tabla = ttk.Treeview(tabla_frame, columns=columnas, show="headings")
    
    for col in columnas:
        tabla.heading(col, text=col)
        tabla.column(col, anchor="center")
    
    tabla.pack(fill=BOTH, expand=True)
    actualizar_tabla(tabla, id_usuario)
