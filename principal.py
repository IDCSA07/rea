import mysql.connector
from tkinter import *
from datetime import datetime
from tkinter import messagebox
from mapa import mostrar_mapa
from cultivos import mostrar_cultivos
from reportes import mostrar_reportes
from agregar_cultivos import agregar_cultivos
from perfil_usuario import mostrar_perfil
from finanzas import finanzas
from almacen import Almacen
from aplicacion_insumos import Aplicaciones_Insumos
from insumos import insumos
from parcelas import parcelas
from siembras import siembras
from cosechas import cosechas

# Función para conectarse a la base de datos y obtener el nombre del usuario
def obtener_nombre_usuario(id_usuario):
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Ccrj1108231407&",
            database="sistema_login"
        )
        cursor = conexion.cursor()
        cursor.execute("SELECT nombre_usuario FROM usuarios WHERE id_usuario = %s", (id_usuario,))
        resultado = cursor.fetchone()
        conexion.close()
        return resultado[0] if resultado else "Usuario desconocido"
    except mysql.connector.Error as e:
        print("Error al conectar a la base de datos:", e)
        return "Error"

# Función para actualizar la hora de acceso en la base de datos
def actualizar_hora_acceso(id_usuario):
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Ccrj1108231407&",
            database="sistema_login"
        )
        cursor = conexion.cursor()
        hora_actual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute("UPDATE usuarios SET ultimo_acceso = %s WHERE id_usuario = %s", (hora_actual, id_usuario))
        conexion.commit()
        conexion.close()
        return hora_actual
    except mysql.connector.Error as e:
        print("Error al actualizar la hora de acceso:", e)
        return "Error"

# Función para manejar navegación
def cambiar_pagina(funcion, *args):
    for widget in cuerpo_principal.winfo_children():
        widget.destroy()
    funcion(cuerpo_principal, *args)

# Configuración del menú y páginas
def crear_ventana_menu(id_usuario):
    global ventana, cuerpo_principal

    nombre_usuario = obtener_nombre_usuario(id_usuario)
    hora_acceso = actualizar_hora_acceso(id_usuario)

    ventana = Tk()
    ventana.title("AgriTech - Sistema de Gestión")
    ventana.geometry("1000x600")
    ventana.configure(bg="#121212")
    ventana.resizable(True, True)

    barra_superior = Frame(ventana, bg="#181818", height=50)
    barra_superior.pack(side=TOP, fill=X)

    Label(
        barra_superior,
        text=f"Bienvenido, {nombre_usuario}",
        bg="#181818",
        fg="white",
        font=("Arial", 14, "bold"),
        padx=10
    ).pack(side=RIGHT, padx=20)

    Label(
        barra_superior,
        text="AgriTech",
        bg="#181818",
        fg="#E50914",
        font=("Arial", 24, "bold"),
        padx=10
    ).pack(side=LEFT, padx=20)

    menu_bar = Menu(ventana)
    
    menu_inicio = Menu(menu_bar, tearoff=0, bg="#181818", fg="white", activebackground="#E50914")
    menu_inicio.add_command(label="Inicio", command=lambda: cambiar_pagina(mostrar_inicio, nombre_usuario, hora_acceso))
    menu_bar.add_cascade(label="Inicio", menu=menu_inicio)

    menu_cultivos = Menu(menu_bar, tearoff=0, bg="#181818", fg="white", activebackground="#E50914")
    menu_cultivos.add_command(label="Mapa", command=lambda: cambiar_pagina(mostrar_mapa))
    menu_cultivos.add_command(label="Cultivos", command=lambda: cambiar_pagina(mostrar_cultivos))
    menu_cultivos.add_command(label="Agregar Cultivos", command=lambda: cambiar_pagina(agregar_cultivos, id_usuario))
    menu_bar.add_cascade(label="Cultivos", menu=menu_cultivos)

    menu_reportes = Menu(menu_bar, tearoff=0, bg="#181818", fg="white", activebackground="#E50914")
    menu_reportes.add_command(label="Reportes", command=lambda: cambiar_pagina(mostrar_reportes, id_usuario))
    menu_reportes.add_command(label="Finanzas", command=lambda: cambiar_pagina(finanzas, id_usuario))
    menu_bar.add_cascade(label="Reportes", menu=menu_reportes)

    menu_operaciones = Menu(menu_bar, tearoff=0, bg="#181818", fg="white", activebackground="#E50914")
    menu_operaciones.add_command(label="Almacen", command=lambda: cambiar_pagina(Almacen))
    menu_operaciones.add_command(label="Insumos", command=lambda: cambiar_pagina(Aplicaciones_Insumos))
    menu_bar.add_cascade(label="Operaciones", menu=menu_operaciones)


    menu_produccion = Menu(menu_bar, tearoff=0, bg="#181818", fg="white", activebackground="#E50914")
    menu_produccion.add_command(label="Insumos", command=lambda: cambiar_pagina(insumos, id_usuario))
    menu_produccion.add_command(label="Parcelas", command=lambda: cambiar_pagina(parcelas, id_usuario))
    menu_produccion.add_command(label="Siembras", command=lambda: cambiar_pagina(siembras))
    menu_produccion.add_command(label="Cosechas", command=lambda: cambiar_pagina(cosechas))
    menu_bar.add_cascade(label="Operaciones", menu=menu_produccion)

    menu_perfil = Menu(menu_bar, tearoff=0, bg="#181818", fg="white", activebackground="#E50914")
    menu_perfil.add_command(label="Ver Mi Perfil", command=lambda: cambiar_pagina(mostrar_perfil, id_usuario))
    menu_bar.add_cascade(label="Perfil", menu=menu_perfil)

    ventana.config(menu=menu_bar)

    cuerpo_principal = Frame(ventana, bg="#121212")
    cuerpo_principal.pack(expand=True, fill=BOTH)

    mostrar_inicio(cuerpo_principal, nombre_usuario, hora_acceso)
    ventana.mainloop()

# Página inicial
def mostrar_inicio(frame, nombre_usuario, hora_acceso):
    Label(
        frame,
        text=f"Bienvenido, {nombre_usuario} al sistema de gestión AGTEC",
        bg="#121212",
        fg="white",
        font=("Arial", 20, "bold")
    ).pack(pady=20)

    Label(
        frame,
        text=f"Tu última hora de acceso fue: {hora_acceso}",
        bg="#121212",
        fg="#B3B3B3",
        font=("Arial", 14)
    ).pack(pady=10)

if __name__ == "__main__":
    id_usuario = None  # Sustituye con el ID real del usuario logueado
    crear_ventana_menu(id_usuario)

