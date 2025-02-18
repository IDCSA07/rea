from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector
from datetime import date

def conectar_bd():
    try:
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="Ccrj1108231407&",
            database="sistema_login"
        )
    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"No se pudo conectar a la base de datos: {e}")
        return None

def guardar_finanza(id_usuario, tipo, monto, fecha, detalle, tabla):
    conexion = conectar_bd()
    if conexion:
        try:
            cursor = conexion.cursor()
            consulta = """
                INSERT INTO finanzas (id_usuario, tipo, monto, fecha, detalle)
                VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(consulta, (id_usuario, tipo, monto, fecha, detalle))
            conexion.commit()
            messagebox.showinfo("Éxito", "Registro guardado correctamente")
            cargar_datos(tabla, id_usuario)
        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"No se pudo guardar el registro: {e}")
        finally:
            cursor.close()
            conexion.close()

def cargar_datos(tabla, id_usuario):
    conexion = conectar_bd()
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT tipo, monto, fecha, detalle FROM finanzas WHERE id_usuario = %s", (id_usuario,))
            registros = cursor.fetchall()
            tabla.delete(*tabla.get_children())
            for registro in registros:
                tabla.insert("", "end", values=registro)
        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"No se pudo cargar los registros: {e}")
        finally:
            cursor.close()
            conexion.close()

def finanzas(frame, id_usuario):
    for widget in frame.winfo_children():
        widget.destroy()
    
    finanzas_frame = Frame(frame, bg="#1E1E1E", padx=20, pady=20)
    finanzas_frame.pack(pady=20, padx=20, fill="both", expand=True)

    Label(finanzas_frame, text="Registro de Finanzas", bg="#1E1E1E", fg="white", font=("Arial", 20, "bold")).pack(pady=10)
    ttk.Separator(finanzas_frame, orient="horizontal").pack(fill="x", pady=10)

    form_frame = Frame(finanzas_frame, bg="#1E1E1E")
    form_frame.pack(pady=10, fill="x")

    Label(form_frame, text="Tipo (i = Ingreso, g = Gasto):", bg="#1E1E1E", fg="#AAAAAA", font=("Arial", 12, "bold")).grid(row=0, column=0, padx=5, pady=5, sticky="w")
    tipo_entry = ttk.Entry(form_frame)
    tipo_entry.grid(row=0, column=1, padx=5, pady=5)

    Label(form_frame, text="Monto:", bg="#1E1E1E", fg="#AAAAAA", font=("Arial", 12, "bold")).grid(row=0, column=2, padx=5, pady=5, sticky="w")
    monto_entry = ttk.Entry(form_frame)
    monto_entry.grid(row=0, column=3, padx=5, pady=5)

    Label(form_frame, text="Detalle:", bg="#1E1E1E", fg="#AAAAAA", font=("Arial", 12, "bold")).grid(row=0, column=4, padx=5, pady=5, sticky="w")
    detalle_entry = ttk.Entry(form_frame, width=30)
    detalle_entry.grid(row=0, column=5, padx=5, pady=5)

    def guardar():
        tipo = tipo_entry.get().strip().lower()
        if tipo == "i":
            tipo = "Ingreso"
        elif tipo == "g":
            tipo = "Gasto"
        else:
            messagebox.showerror("Error", "Tipo inválido. Ingresa 'i' para Ingreso o 'g' para Gasto.")
            return

        try:
            monto = float(monto_entry.get())
            fecha_actual = date.today().strftime('%Y-%m-%d')
            detalle = detalle_entry.get()
            guardar_finanza(id_usuario, tipo, monto, fecha_actual, detalle, tabla)
        except ValueError:
            messagebox.showerror("Error", "Monto inválido. Debe ser un número.")
    
    ttk.Button(form_frame, text="Guardar Registro", command=guardar).grid(row=0, column=6, padx=10, pady=5)

    tabla_frame = Frame(finanzas_frame)
    tabla_frame.pack(pady=10, padx=10, fill=BOTH, expand=True)

    columnas = ("Tipo", "Monto", "Fecha", "Detalle")
    tabla = ttk.Treeview(tabla_frame, columns=columnas, show="headings")

    for col in columnas:
        tabla.heading(col, text=col)
        tabla.column(col, anchor="center")

    tabla.pack(fill=BOTH, expand=True)
    cargar_datos(tabla, id_usuario)
