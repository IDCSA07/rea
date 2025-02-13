from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk, ImageEnhance
import mysql.connector
import cv2
from utils import cifrar_contraseña, verificar_contraseña
from principal import crear_ventana_menu  # Función para redirigir al menú principal


# Función para conectar a la base de datos
def conectar_bd():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Ccrj1108231407&",
            database="sistema_login"
        )
        return conexion
    except mysql.connector.Error as err:
        messagebox.showerror("Error de conexión", f"No se pudo conectar a la base de datos: {err}")
        return None


# Reproducción del video como fondo
def reproducir_video():
    global fondo_video, cap
    ret, frame = cap.read()
    if ret:
        # Convertir el frame a formato RGB
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        imagen = Image.fromarray(frame)

        # Aplicar un filtro oscuro (oscurece el video)
        enhancer = ImageEnhance.Brightness(imagen)
        imagen = enhancer.enhance(0.2)  # Reduce la luminosidad al 20%

        # Convertir a formato compatible con Tkinter
        imagen_tk = ImageTk.PhotoImage(imagen)
        fondo_video.config(image=imagen_tk)
        fondo_video.image = imagen_tk
        ventana.after(15, reproducir_video)
    else:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        reproducir_video()


# Página de inicio
def mostrar_pagina_inicio():
    limpiar_ventana()

    # Marco central
    marco_central = Frame(ventana, bg="#181818", bd=2, relief="solid")
    marco_central.place(relx=0.5, rely=0.5, anchor=CENTER, width=500, height=400)

    # Título del proyecto
    Label(
        marco_central,
        text="AGTEC",
        bg="#181818",
        fg="#E50914",
        font=("Arial", 36, "bold")
    ).pack(pady=(20, 10))

    Label(
        marco_central,
        text="Bienvenido al sistema de gestión AGTEC",
        bg="#181818",
        fg="white",
        font=("Arial", 16)
    ).pack(pady=10)

    # Botones de acción
    Button(
        marco_central,
        text="Iniciar Sesión",
        bg="#E50914",
        fg="white",
        font=("Arial", 14, "bold"),
        width=15,
        command=mostrar_pagina_login
    ).pack(pady=10)

    Button(
        marco_central,
        text="Registrarse",
        bg="#E50914",
        fg="white",
        font=("Arial", 14, "bold"),
        width=15,
        command=mostrar_pagina_registro
    ).pack(pady=10)


# Página de login
def mostrar_pagina_login():
    limpiar_ventana()

    def verificar_credenciales():
        conexion = conectar_bd()
        if not conexion:
            return

        usuario = usuario_entry.get().strip()
        contraseña = contraseña_entry.get().strip()

        if not usuario or not contraseña:
            messagebox.showwarning("Campos vacíos", "Por favor, ingrese ambos campos.")
            return

        try:
            cursor = conexion.cursor(dictionary=True)
            cursor.execute(
                "SELECT * FROM usuarios WHERE nombre_usuario = %s OR telefono = %s",
                (usuario, usuario)
            )
            resultado = cursor.fetchone()

            if resultado and verificar_contraseña(contraseña, resultado["clave"]):
                messagebox.showinfo("Éxito", "Inicio de sesión exitoso.")
                
                usuario_id = resultado.get("id_usuario", None)  # Usamos "id" como ejemplo, reemplázalo si es diferente
                if usuario_id is not None:
                    redirigir_menu_principal(usuario_id)
                else:
                    messagebox.showerror("Error", "Usuario o contraseña incorrectos.")
            else:
                messagebox.showerror("Error", "Usuario o contraseña incorrectos.")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error en la base de datos: {err}")
        finally:
            conexion.close()

    marco_central = Frame(ventana, bg="#181818", bd=2, relief="solid")
    marco_central.place(relx=0.5, rely=0.5, anchor=CENTER, width=500, height=400)

    Label(
        marco_central,
        text="Iniciar Sesión",
        bg="#181818",
        fg="#E50914",
        font=("Arial", 28, "bold")
    ).pack(pady=(20, 10))

    Label(
        marco_central,
        text="Usuario o Número de Teléfono:",
        bg="#181818",
        fg="white",
        font=("Arial", 14)
    ).pack(pady=5)
    usuario_entry = Entry(marco_central, font=("Arial", 14), bg="#282828", fg="white", insertbackground="white")
    usuario_entry.pack(pady=5)

    Label(
        marco_central,
        text="Contraseña:",
        bg="#181818",
        fg="white",
        font=("Arial", 14)
    ).pack(pady=5)
    contraseña_entry = Entry(marco_central, font=("Arial", 14), show="*", bg="#282828", fg="white", insertbackground="white")
    contraseña_entry.pack(pady=5)

    Button(
        marco_central,
        text="Acceder",
        bg="#E50914",
        fg="white",
        font=("Arial", 14, "bold"),
        width=15,
        command=verificar_credenciales
    ).pack(pady=10)

    Button(
        marco_central,
        text="Volver",
        bg="#282828",
        fg="white",
        font=("Arial", 14),
        width=15,
        command=mostrar_pagina_inicio
    ).pack(pady=5)


# Página de registro
def mostrar_pagina_registro():
    limpiar_ventana()

    def registrar_usuario():
        conexion = conectar_bd()
        if not conexion:
            return

        usuario = usuario_entry.get().strip()
        telefono = telefono_entry.get().strip()
        contraseña = contraseña_entry.get().strip()

        if not usuario or not telefono or not contraseña:
            messagebox.showwarning("Campos vacíos", "Por favor, complete todos los campos.")
            return

        contraseña_cifrada = cifrar_contraseña(contraseña)

        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM usuarios WHERE telefono = %s", (telefono,))
            if cursor.fetchone():
                messagebox.showwarning("Error", "El número de teléfono ya está registrado.")
                return

            cursor.execute(
                "INSERT INTO usuarios (nombre_usuario, telefono, clave) VALUES (%s, %s, %s)",
                (usuario, telefono, contraseña_cifrada)
            )
            conexion.commit()
            messagebox.showinfo("Éxito", "Usuario registrado exitosamente.")
            mostrar_pagina_inicio()
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error al registrar usuario: {err}")
        finally:
            conexion.close()

    marco_central = Frame(ventana, bg="#181818", bd=2, relief="solid")
    marco_central.place(relx=0.5, rely=0.5, anchor=CENTER, width=500, height=400)

    Label(
        marco_central,
        text="Registro de Usuario",
        bg="#181818",
        fg="#E50914",
        font=("Arial", 28, "bold")
    ).pack(pady=(20, 10))

    Label(
        marco_central,
        text="Correo electrónico o Usuario:",
        bg="#181818",
        fg="white",
        font=("Arial", 14)
    ).pack(pady=5)
    usuario_entry = Entry(marco_central, font=("Arial", 14), bg="#282828", fg="white", insertbackground="white")
    usuario_entry.pack(pady=5)

    Label(
        marco_central,
        text="Teléfono:",
        bg="#181818",
        fg="white",
        font=("Arial", 14)
    ).pack(pady=5)
    telefono_entry = Entry(marco_central, font=("Arial", 14), bg="#282828", fg="white", insertbackground="white")
    telefono_entry.pack(pady=5)

    Label(
        marco_central,
        text="Contraseña:",
        bg="#181818",
        fg="white",
        font=("Arial", 14)
    ).pack(pady=5)
    contraseña_entry = Entry(marco_central, font=("Arial", 14), show="*", bg="#282828", fg="white", insertbackground="white")
    contraseña_entry.pack(pady=5)

    Button(
        marco_central,
        text="Registrar",
        bg="#E50914",
        fg="white",
        font=("Arial", 14, "bold"),
        width=15,
        command=registrar_usuario
    ).pack(pady=10)

    Button(
        marco_central,
        text="Volver",
        bg="#282828",
        fg="white",
        font=("Arial", 14),
        width=15,
        command=mostrar_pagina_inicio
    ).pack(pady=5)


# Función para redirigir al menú principal tras el login
def redirigir_menu_principal(id_usuario):
    ventana.withdraw()
    crear_ventana_menu(id_usuario)


# Limpiar la ventana
def limpiar_ventana():
    for widget in ventana.winfo_children():
        if widget != fondo_video:  # Mantener el fondo del video
            widget.destroy()


# Configuración principal de la ventana
def crear_ventana_principal():
    global ventana, fondo_video, cap
    ventana = Tk()
    ventana.title("AGTEC - Bienvenido")
    ventana.geometry("1000x600")
    ventana.configure(bg="#121212")
    ventana.resizable(False, False)  # Desactivar maximizar al inicio

    # Cargar el video
    cap = cv2.VideoCapture("Cultivating the Future.video.mp4")
    if not cap.isOpened():
        messagebox.showerror("Error", "No se pudo cargar el video de fondo.")
        ventana.destroy()
        return

    # Configurar el video como fondo
    fondo_video = Label(ventana, bg="black")
    fondo_video.place(relwidth=1, relheight=1)
    reproducir_video()

    # Mostrar la página inicial
    mostrar_pagina_inicio()

    # Ejecutar la ventana principal
    ventana.mainloop()


# Iniciar la aplicación
if __name__ == "__main__":
    crear_ventana_principal()
