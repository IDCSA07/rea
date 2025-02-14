from tkinter import *
from tkinter import messagebox
from fpdf import FPDF
import mysql.connector
import os
from datetime import datetime

# Conexión a MySQL
def conectar_bd():
    return mysql.connector.connect(
        host="localhost",
        user="root",  # Cambia según tu configuración
        password="Ccrj1108231407&",  # Si tienes contraseña, agrégala aquí
        database="sistema_login"
    )

CARPETA_REPORTES = "reportes_generados"
os.makedirs(CARPETA_REPORTES, exist_ok=True)

# Función para generar y guardar el PDF en MySQL con fecha
def generar_pdf(titulo, descripcion, id_usuario):
    if not titulo.strip() or not descripcion.strip():
        messagebox.showerror("Error", "El título y la descripción no pueden estar vacíos.")
        return
    
    fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Formato DATETIME de MySQL

    # Crear el PDF en memoria
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", style="B", size=16)
    pdf.cell(0, 10, "Reporte", ln=True, align='C')

    pdf.ln(5)
    pdf.set_font("Arial", style="B", size=12)
    pdf.cell(0, 10, titulo, ln=True, align='L')
    pdf.set_font("Arial", size=10)
    pdf.cell(0, 10, f"Fecha: {datetime.now().strftime('%d/%m/%Y')}", ln=True, align='R')

    pdf.ln(10)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 7, descripcion)

    # Guardar temporalmente el PDF
    pdf_path = os.path.join(CARPETA_REPORTES, f"{titulo.replace(' ', '_')}.pdf")
    pdf.output(pdf_path)

    # Leer el PDF como binario
    with open(pdf_path, "rb") as archivo_pdf:
        binario_pdf = archivo_pdf.read()

    # Guardar en MySQL con la fecha de subida
    conexion = conectar_bd()
    cursor = conexion.cursor()

    sql = "INSERT INTO documentos (id_usuario, nombre, archivo, fecha_subida) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (id_usuario, titulo, binario_pdf, fecha_actual))

    conexion.commit()
    cursor.close()
    conexion.close()

    os.remove(pdf_path)  # Eliminar el PDF temporal
    messagebox.showinfo("Éxito", "Reporte guardado en la base de datos con fecha de subida.")
    actualizar_lista_reportes(id_usuario)

# Función para actualizar la lista de reportes desde MySQL
def actualizar_lista_reportes(id_usuario):
    for widget in frame_lista_reportes.winfo_children():
        widget.destroy()

    conexion = conectar_bd()
    cursor = conexion.cursor()
    cursor.execute("SELECT id, nombre, fecha_subida FROM documentos WHERE id_usuario = %s", (id_usuario,))
    reportes = cursor.fetchall()
    conexion.close()

    if not reportes:
        Label(frame_lista_reportes, text="No hay reportes disponibles.", bg="#121212", fg="#B3B3B3", font=("Arial", 14)).pack(pady=10)
    else:
        for reporte in reportes:
            reporte_id, nombre, fecha_subida = reporte
            frame_reporte = Frame(frame_lista_reportes, bg="#282828", pady=2)
            frame_reporte.pack(fill=X, padx=5, pady=5)

            Label(frame_reporte, text=f"{nombre} - {fecha_subida}", bg="#282828", fg="white", font=("Arial", 10), anchor="w", padx=5).pack(side=LEFT, fill=X, expand=True)

            Button(frame_reporte, text="Abrir", bg="#E50914", fg="white", font=("Arial", 10), command=lambda r=reporte_id: abrir_pdf(r)).pack(side=RIGHT, padx=5)

# Función para abrir un PDF desde MySQL
def abrir_pdf(reporte_id):
    conexion = conectar_bd()
    cursor = conexion.cursor()
    cursor.execute("SELECT nombre, archivo FROM documentos WHERE id = %s", (reporte_id,))
    reporte = cursor.fetchone()
    conexion.close()

    if reporte:
        nombre, archivo_binario = reporte
        ruta_pdf = os.path.join(CARPETA_REPORTES, f"{nombre.replace(' ', '_')}.pdf")

        with open(ruta_pdf, "wb") as pdf:
            pdf.write(archivo_binario)

        os.system(f"start {ruta_pdf}")  # Abre el archivo en Windows
    else:
        messagebox.showerror("Error", "No se encontró el archivo en la base de datos.")

# Función para mostrar la página de reportes
def mostrar_reportes(frame, id_usuario):
    for widget in frame.winfo_children():
        widget.destroy()

    Label(frame, text="Reportes", bg="#121212", fg="white", font=("Arial", 20, "bold")).pack(pady=20)

    Label(frame, text="Título del reporte:", bg="#121212", fg="white", font=("Arial", 14)).pack(anchor=W, padx=20)
    titulo_entry = Entry(frame, font=("Arial", 12), bg="#282828", fg="white")
    titulo_entry.pack(fill=X, padx=20, pady=5)

    Label(frame, text="Descripción del reporte:", bg="#121212", fg="white", font=("Arial", 14)).pack(anchor=W, padx=20)
    descripcion_text = Text(frame, font=("Arial", 12), bg="#282828", fg="white", height=6)
    descripcion_text.pack(fill=X, padx=20, pady=5)

    Button(frame, text="Generar PDF", bg="#E50914", fg="white", font=("Arial", 14, "bold"),
           command=lambda: generar_pdf(titulo_entry.get(), descripcion_text.get("1.0", END).strip(), id_usuario)).pack(pady=10)

    Label(frame, text="Reportes Generados:", bg="#121212", fg="white", font=("Arial", 14)).pack(anchor=W, padx=20, pady=10)

    global frame_lista_reportes
    frame_lista_reportes = Frame(frame, bg="#121212")
    frame_lista_reportes.pack(fill=BOTH, expand=True, padx=20, pady=10)

    actualizar_lista_reportes(id_usuario)
