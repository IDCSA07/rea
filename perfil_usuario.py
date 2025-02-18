from tkinter import *
from tkinter import ttk, messagebox, simpledialog
import mysql.connector
from utils import verificar_contraseña

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

def obtener_datos_usuario(id_usuario):
    conexion = conectar_bd()
    if conexion is None:
        return "Error", "No hay conexión", "", "", "", 0
    
    cursor = conexion.cursor()
    cursor.execute("SELECT nombre_usuario, telefono, direccion, fecha_nacimiento, biografia, notificaciones FROM usuarios WHERE id_usuario = %s", (id_usuario,))
    usuario = cursor.fetchone()
    conexion.close()
    
    return usuario if usuario else ("Usuario no encontrado", "No disponible", "", "", "", 0)

def actualizar_usuario(id_usuario):
    conexion = conectar_bd()
    if conexion:
        try:
            cursor = conexion.cursor()

            # Pedir nuevos valores
            nombre = simpledialog.askstring("Editar Perfil", "Nuevo nombre:")
            telefono = simpledialog.askstring("Editar Perfil", "Nuevo teléfono:")
            direccion = simpledialog.askstring("Editar Perfil", "Nueva dirección:")
            fecha_nacimiento = simpledialog.askstring("Editar Perfil", "Nueva fecha de nacimiento:")
            biografia = simpledialog.askstring("Editar Perfil", "Nueva biografía:")
            notificaciones = simpledialog.askstring("Editar Perfil", "Recibir notificaciones (Sí/No):")
            notificaciones = 1 if notificaciones and notificaciones.lower() == "sí" else 0

            # Confirmar contraseña
            password = simpledialog.askstring("Confirmación", "Ingrese su contraseña para confirmar:", show='*')
            if not password:
                messagebox.showerror("Error", "Debe ingresar la contraseña")
                return

            cursor.execute("SELECT clave FROM usuarios WHERE id_usuario=%s", (id_usuario,))
            contraseña_cifrada = cursor.fetchone()

            if contraseña_cifrada and verificar_contraseña(password, contraseña_cifrada[0]):
                consulta = """
                    UPDATE usuarios SET nombre_usuario=%s, telefono=%s, direccion=%s, fecha_nacimiento=%s, biografia=%s, notificaciones=%s WHERE id_usuario=%s
                """
                cursor.execute(consulta, (nombre, telefono, direccion, fecha_nacimiento, biografia, notificaciones, id_usuario))
                conexion.commit()
                messagebox.showinfo("Éxito", "Perfil actualizado correctamente")
            else:
                messagebox.showerror("Error", "Contraseña incorrecta")
        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"No se pudo actualizar el usuario: {e}")
        finally:
            cursor.close()
            conexion.close()

def cambiar_estado_cuenta(id_usuario, estado):
    password = simpledialog.askstring("Confirmación", "Ingrese su contraseña para continuar:", show='*')
    if not password:
        messagebox.showerror("Error", "Debe ingresar la contraseña")
        return

    conexion = conectar_bd()
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT clave FROM usuarios WHERE id_usuario=%s", (id_usuario,))
            contraseña_cifrada = cursor.fetchone()

            if contraseña_cifrada and verificar_contraseña(password, contraseña_cifrada[0]):
                cursor.execute("UPDATE usuarios SET estado_cuenta=%s WHERE id_usuario=%s", (estado, id_usuario))
                conexion.commit()
                messagebox.showinfo("Éxito", "Estado de cuenta actualizado correctamente")
            else:
                messagebox.showerror("Error", "Contraseña incorrecta")
        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"No se pudo actualizar el estado de la cuenta: {e}")
        finally:
            cursor.close()
            conexion.close()

def mostrar_perfil(frame, id_usuario):
    for widget in frame.winfo_children():
        widget.destroy()

    nombre, telefono, direccion, fecha_nacimiento, biografia, notificaciones = obtener_datos_usuario(id_usuario)

    main_frame = Frame(frame, bg="#1E1E1E", padx=20, pady=20)
    main_frame.pack(fill=BOTH, expand=True)
    
    Label(main_frame, text=nombre, bg="#1E1E1E", fg="white", font=("Arial", 22, "bold")).pack(pady=10)
    ttk.Separator(main_frame, orient="horizontal").pack(fill="x", pady=10)
    
    info = [
        ("Teléfono:", telefono),
        ("Dirección:", direccion),
        ("Fecha de Nacimiento:", fecha_nacimiento),
        ("Biografía:", biografia),
        ("Notificaciones:", "Sí" if notificaciones else "No")
    ]

    for label, value in info:
        Label(main_frame, text=label, bg="#1E1E1E", fg="#AAAAAA", font=("Arial", 12, "bold"), anchor="w").pack(fill="x", pady=2)
        Label(main_frame, text=value, bg="#1E1E1E", fg="white", font=("Arial", 14)).pack(fill="x", pady=2)
    
    button_frame = Frame(main_frame, bg="#1E1E1E")
    button_frame.pack(pady=10)

    style = ttk.Style()
    style.configure("Retro.TButton", font=("Arial", 12), padding=6, background="#FFD700", foreground="black")

    ttk.Button(button_frame, text="Editar Perfil", style="Retro.TButton", command=lambda: actualizar_usuario(id_usuario)).grid(row=0, column=0, padx=10)
    ttk.Button(button_frame, text="Suspender Cuenta", style="Retro.TButton", command=lambda: cambiar_estado_cuenta(id_usuario, "suspendido")).grid(row=0, column=1, padx=10)
    ttk.Button(button_frame, text="Eliminar Cuenta", style="Retro.TButton", command=lambda: cambiar_estado_cuenta(id_usuario, "eliminado")).grid(row=0, column=2, padx=10)

