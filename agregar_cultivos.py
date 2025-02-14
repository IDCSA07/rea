from tkinter import *
from tkinter import ttk, messagebox, simpledialog
import mysql.connector
import textwrap

def conectar_bd():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Ccrj1108231407&",
            database="sistema_login"
        )
        return conexion
    except mysql.connector.Error:
        return None

def editar_campo(id_usuario, cultivo, campo, indice):
    nuevo_valor = simpledialog.askstring("Editar", f"Nuevo valor para {campo}:", initialvalue=cultivo[indice])
    if nuevo_valor:
        conexion = conectar_bd()
        cursor = conexion.cursor()
        cursor.execute(f"UPDATE cult_personalizado SET {campo}=%s WHERE id_usuario=%s AND nombre_cult=%s", 
                       (nuevo_valor, id_usuario, cultivo[0]))
        conexion.commit()
        conexion.close()
        messagebox.showinfo("Éxito", f"{campo} actualizado correctamente.")
        agregar_cultivos(frame_global, id_usuario)

def editar_todo(id_usuario, cultivo):
    campos = ["nombre_cult", "tipo_cult", "precio_estimado", "ubicacion", "descripcion"]
    nuevos_valores = []
    for i, campo in enumerate(campos):
        valor = simpledialog.askstring("Editar", f"Nuevo valor para {campo}:", initialvalue=cultivo[i])
        if valor is None:
            return  # Si cancela, no se actualiza nada
        nuevos_valores.append(valor)
    
    conexion = conectar_bd()
    cursor = conexion.cursor()
    cursor.execute("""
        UPDATE cult_personalizado 
        SET nombre_cult=%s, tipo_cult=%s, precio_estimado=%s, ubicacion=%s, descripcion=%s
        WHERE id_usuario=%s AND nombre_cult=%s
    """, (*nuevos_valores, id_usuario, cultivo[0]))
    conexion.commit()
    conexion.close()
    messagebox.showinfo("Éxito", "Cultivo actualizado correctamente.")
    agregar_cultivos(frame_global, id_usuario)

def borrar_cultivo(id_usuario, cultivo):
    confirmacion = messagebox.askyesno("Eliminar Cultivo", f"¿Seguro que quieres eliminar {cultivo[0]}?")
    if confirmacion:
        conexion = conectar_bd()
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM cult_personalizado WHERE id_usuario=%s AND nombre_cult=%s", (id_usuario, cultivo[0]))
        conexion.commit()
        conexion.close()
        messagebox.showinfo("Éxito", "Cultivo eliminado correctamente.")
        agregar_cultivos(frame_global, id_usuario)

def menu_contextual(event, id_usuario):
    item = tabla.identify_row(event.y)
    if item:
        cultivo = tabla.item(item, "values")
        menu = Menu(frame_global, tearoff=0)
        
        columnas = ["nombre_cult", "tipo_cult", "precio_estimado", "ubicacion", "descripcion"]
        for i, columna in enumerate(columnas):
            menu.add_command(label=f"Editar {columna}", command=lambda i=i: editar_campo(id_usuario, cultivo, columnas[i], i))
        
        menu.add_separator()
        menu.add_command(label="Editar Todo", command=lambda: editar_todo(id_usuario, cultivo))
        menu.add_command(label="Eliminar", command=lambda: borrar_cultivo(id_usuario, cultivo))
        menu.post(event.x_root, event.y_root)

def agregar_cultivos(frame, id_usuario):
    global frame_global, tabla
    frame_global = frame
    
    for widget in frame.winfo_children():
        widget.destroy()
    
    frame.config(bg="#1E1E1E")
    Label(frame, text="🌱 Cultivos Disponibles 🌱", bg="#1E1E1E", fg="white", font=("Arial", 22, "bold")).pack(pady=15)
    Label(frame, text="Consulta los cultivos disponibles en Puebla.", bg="#1E1E1E", fg="#A0A0A0", font=("Arial", 14)).pack(pady=5)
    
    tabla_frame = Frame(frame, bg="#1E1E1E")
    tabla_frame.pack(pady=10, padx=20, fill=BOTH, expand=True)
    
    columnas = ("Nombre", "Tipo", "Precio (MXN/kg)", "Ubicación", "Descripción")
    tabla = ttk.Treeview(tabla_frame, columns=columnas, show="headings")
    
    for col in columnas:
        tabla.heading(col, text=col)
    
    tabla.column("Nombre", width=150)
    tabla.column("Tipo", width=120)
    tabla.column("Precio (MXN/kg)", width=130)
    tabla.column("Ubicación", width=180)
    tabla.column("Descripción", width=300)
    
    tabla.pack(fill=BOTH, expand=True)
    tabla.bind("<Button-3>", lambda event: menu_contextual(event, id_usuario))
    
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
    
    boton_agregar = Button(frame, text="Agregar Cultivo", bg="#008CBA", fg="white", font=("Arial", 14, "bold"), command=lambda: messagebox.showinfo("Agregar", "Función en desarrollo."))
    boton_agregar.pack(pady=10)
