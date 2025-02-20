from tkinter import *
from tkinter import ttk, messagebox, simpledialog
import mysql.connector
import textwrap

def conectar_bd():
    try:
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="Ccrj1108231407&",
            database="sistema_login"
        )
    except mysql.connector.Error:
        return None

def actualizar_cultivo(id_usuario, columna, nuevo_valor, nombre_cult):
    conexion = conectar_bd()
    if conexion:
        cursor = conexion.cursor()
        try:
            consulta = f"UPDATE cult_personalizado SET {columna} = %s WHERE id_usuario = %s AND nombre_cult = %s"
            cursor.execute(consulta, (nuevo_valor, id_usuario, nombre_cult))
            conexion.commit()
            messagebox.showinfo("Éxito", "Cultivo actualizado correctamente.")
        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"No se pudo actualizar el cultivo: {e}")
        finally:
            conexion.close()
        agregar_cultivos(frame_global, id_usuario)

def eliminar_cultivo(id_usuario, nombre_cult):
    if messagebox.askyesno("Eliminar", f"¿Seguro que deseas eliminar el cultivo '{nombre_cult}'?"):
        conexion = conectar_bd()
        if conexion:
            cursor = conexion.cursor()
            try:
                cursor.execute("DELETE FROM cult_personalizado WHERE id_usuario = %s AND nombre_cult = %s", (id_usuario, nombre_cult))
                conexion.commit()
                messagebox.showinfo("Éxito", "Cultivo eliminado correctamente.")
            except mysql.connector.Error as e:
                messagebox.showerror("Error", f"No se pudo eliminar el cultivo: {e}")
            finally:
                conexion.close()
            agregar_cultivos(frame_global, id_usuario)

def editar_celda(event, id_usuario):
    item = tabla.identify_row(event.y)
    column_id = tabla.identify_column(event.x)
    
    if item:
        col_index = int(column_id[1:]) - 1
        columnas = ["nombre_cult", "tipo_cult", "precio_estimado", "ubicacion", "descripcion"]
        
        if col_index < len(columnas):
            columna = columnas[col_index]
            valores = tabla.item(item, "values")
            nombre_cult = valores[0]
            valor_actual = valores[col_index]
            
            nuevo_valor = simpledialog.askstring("Editar", f"Nuevo valor para {columna}:", initialvalue=valor_actual)
            if nuevo_valor is not None:
                actualizar_cultivo(id_usuario, columna, nuevo_valor, nombre_cult)

def mostrar_menu(event, id_usuario):
    item = tabla.identify_row(event.y)
    if item:
        global evento_guardado
        evento_guardado = event
        menu_contextual.post(event.x_root, event.y_root)

def agregar_cultivo(id_usuario):
    campos = ["nombre_cult", "tipo_cult", "precio_estimado", "ubicacion", "descripcion"]
    valores = []
    for campo in campos:
        valor = simpledialog.askstring("Agregar Cultivo", f"Ingrese {campo}:")
        if valor is None:
            return
        valores.append(valor)
    
    conexion = conectar_bd()
    if conexion:
        cursor = conexion.cursor()
        try:
            cursor.execute("""
                INSERT INTO cult_personalizado (id_usuario, nombre_cult, tipo_cult, precio_estimado, ubicacion, descripcion)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (id_usuario, *valores))
            conexion.commit()
            messagebox.showinfo("Éxito", "Cultivo agregado correctamente.")
        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"No se pudo agregar el cultivo: {e}")
        finally:
            conexion.close()
        agregar_cultivos(frame_global, id_usuario)

def agregar_cultivos(frame, id_usuario):
    global frame_global, tabla, menu_contextual
    frame_global = frame
    
    for widget in frame.winfo_children():
        widget.destroy()
    
    Label(frame, text="🌱 Cultivos Agregados 🌱", font=("Arial", 22, "bold"), bg="#1E1E1E", fg="white").pack(pady=15)
    Label(frame, text="Agrega tus cultivos personalizados.", font=("Arial", 14), bg="#1E1E1E", fg="#AAAAAA").pack(pady=5)
    
    tabla_frame = Frame(frame, bg="#1E1E1E")
    tabla_frame.pack(pady=10, padx=20, fill=BOTH, expand=True)
    
    columnas = ("Nombre", "Tipo", "Precio (MXN/kg)", "Ubicación", "Descripción")
    tabla = ttk.Treeview(tabla_frame, columns=columnas, show="headings")
    
    for col in columnas:
        tabla.heading(col, text=col)
        tabla.column(col, anchor="center")
    
    tabla.pack(fill=BOTH, expand=True)
    
    try:
        conexion = conectar_bd()
        cursor = conexion.cursor()
        cursor.execute("SELECT nombre_cult, tipo_cult, precio_estimado, ubicacion, descripcion FROM cult_personalizado WHERE id_usuario = %s", (id_usuario,))
        for row in cursor.fetchall():
            nombre, tipo, precio, ubicacion, descripcion = row
            descripcion_formateada = "\n".join(textwrap.wrap(descripcion, width=40))
            tabla.insert("", "end", values=(nombre, tipo, precio, ubicacion, descripcion_formateada))
        conexion.close()
    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"No se pudieron cargar los cultivos: {e}")
    
    menu_contextual = Menu(tabla, tearoff=0)
    menu_contextual.add_command(label="Editar", command=lambda: editar_celda(evento_guardado, id_usuario))
    menu_contextual.add_command(label="Eliminar", command=lambda: eliminar_cultivo(id_usuario, tabla.item(tabla.selection())['values'][0]))
    
    tabla.bind("<Button-3>", lambda event: mostrar_menu(event, id_usuario))
    
    Button(frame, text="Agregar Cultivo", command=lambda: agregar_cultivo(id_usuario), bg="#007BFF", fg="white", font=("Arial", 12, "bold"), padx=10, pady=5).pack(pady=10)
