from tkinter import *
from tkinter import messagebox
from mapa import mostrar_mapa
from cultivos import mostrar_cultivos
from reportes import mostrar_reportes
from agregar_cultivos import agregar_cultivos
from perfil_usuario import mostrar_perfil

# Función para manejar navegación
def cambiar_pagina(funcion, *args):
    for widget in cuerpo_principal.winfo_children():
        widget.destroy()  # Limpia la sección principal
    funcion(cuerpo_principal, *args)  # Pasa los argumentos adicionales
 # Limpia la sección principal

# Configuración del menú y páginas
def crear_ventana_menu(id_usuario):
    global ventana, cuerpo_principal

    # Configuración de la ventana principal
    ventana = Tk()
    ventana.title("AgriTech - Sistema de Gestión")
    ventana.geometry("1000x600")
    ventana.configure(bg="#121212")
    ventana.resizable(True, True)

    # Barra superior con el título y el menú
    barra_superior = Frame(ventana, bg="#181818", height=50)
    barra_superior.pack(side=TOP, fill=X)

    # Menú en la barra superior
    Label(
        barra_superior,
        text="AgriTech",
        bg="#181818",
        fg="#E50914",
        font=("Arial", 24, "bold"),
        padx=10
    ).pack(side=LEFT, padx=20)

    # Opciones del menú
    menu_bar = Menu(ventana)
    
    menu_inicio = Menu(menu_bar, tearoff=0, bg="#181818", fg="white", activebackground="#E50914")
    menu_inicio.add_command(label="Inicio", command=lambda: cambiar_pagina(mostrar_inicio))
    menu_bar.add_cascade(label="Inicio", menu=menu_inicio)

    menu_cultivos = Menu(menu_bar, tearoff=0, bg="#181818", fg="white", activebackground="#E50914")
    menu_cultivos.add_command(label="Mapa", command=lambda: cambiar_pagina(mostrar_mapa))
    menu_cultivos.add_command(label="Cultivos", command=lambda: cambiar_pagina(mostrar_cultivos))
    menu_cultivos.add_command(label="Agregar Cultivos", command=lambda: cambiar_pagina(agregar_cultivos,id_usuario))
    menu_bar.add_cascade(label="Cultivos", menu=menu_cultivos)

    menu_reportes = Menu(menu_bar, tearoff=0, bg="#181818", fg="white", activebackground="#E50914")
    menu_reportes.add_command(label="Reportes", command=lambda: cambiar_pagina(mostrar_reportes, id_usuario))
    menu_bar.add_cascade(label="Reportes", menu=menu_reportes)

    menu_perfil = Menu(menu_bar, tearoff=0, bg="#181818", fg="white", activebackground="#E50914")
    menu_perfil.add_command(label="Ver Mi Perfil", command=lambda: cambiar_pagina(mostrar_perfil, id_usuario))
    menu_bar.add_cascade(label="Perfil", menu=menu_perfil)



    ventana.config(menu=menu_bar)

    # Cuerpo principal
    cuerpo_principal = Frame(ventana, bg="#121212")
    cuerpo_principal.pack(expand=True, fill=BOTH)

    # Mostrar la página de inicio por defecto
    mostrar_inicio(cuerpo_principal)

    ventana.mainloop()

# Página inicial
def mostrar_inicio(frame):
    Label(
        frame,
        text="Bienvenido al sistema de gestión AGTEC",
        bg="#121212",
        fg="white",
        font=("Arial", 20, "bold")
    ).pack(pady=20)

    Label(
        frame,
        text="Seleccione una opción del menú para comenzar.",
        bg="#121212",
        fg="#B3B3B3",
        font=("Arial", 14)
    ).pack(pady=10)

if __name__ == "__main__":
    crear_ventana_menu()
