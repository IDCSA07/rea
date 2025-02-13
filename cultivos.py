from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector
import textwrap

def mostrar_cultivos(frame):
    for widget in frame.winfo_children():
        widget.destroy()

    frame.config(bg="#1E1E1E")

    Label(
        frame,
        text="🌱 Cultivos Disponibles 🌱",
        bg="#1E1E1E",
        fg="white",
        font=("Arial", 22, "bold")
    ).pack(pady=15)

    Label(
        frame,
        text="Consulta los cultivos disponibles en Puebla.",
        bg="#1E1E1E",
        fg="#A0A0A0",
        font=("Arial", 14)
    ).pack(pady=5)

    # Contenedor de la tabla con grid para que se expanda
    tabla_frame = Frame(frame, bg="#1E1E1E")
    tabla_frame.pack(pady=10, padx=20, fill=BOTH, expand=True)
    tabla_frame.grid_columnconfigure(0, weight=1)
    tabla_frame.grid_rowconfigure(0, weight=1)

    # Estilos de la tabla
    style = ttk.Style()
    style.configure("Treeview", background="#252526", foreground="white", fieldbackground="#252526", 
                    font=("Arial", 12), rowheight=80, borderwidth=0, relief="flat")
    style.configure("Treeview.Heading", font=("Arial", 14, "bold"), background="#444", foreground="cyan")
    style.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})])

    # Alternar colores en las filas
    style.map("Treeview", background=[("alternate", "#2E2E2E")])

    # Definir columnas
    columnas = ("Nombre", "Tipo", "Precio (MXN/kg)", "Ubicación", "Descripción")
    tabla = ttk.Treeview(tabla_frame, columns=columnas, show="headings", style="Treeview")

    for col in columnas:
        tabla.heading(col, text=col)
        tabla.column(col, anchor=W, minwidth=100, width=180)

    # Ajustar el ancho de la columna "Descripción"
    tabla.column("Descripción", width=300, minwidth=250)

    tabla.grid(row=0, column=0, sticky="nsew")

    # Scrollbar vertical sutil
    scrollbar_y = ttk.Scrollbar(tabla_frame, orient="vertical", command=tabla.yview, style="Custom.Vertical.TScrollbar")
    scrollbar_y.grid(row=0, column=1, sticky="ns", padx=2)
    tabla.configure(yscrollcommand=scrollbar_y.set)

    # Estilo sutil para el scrollbar
    style.configure("Custom.Vertical.TScrollbar",
                    background="#2E2E2E",
                    troughcolor="#1E1E1E",
                    bordercolor="#1E1E1E",
                    arrowcolor="#444",
                    gripcount=0)

    # Configurar expansión de la tabla con grid
    tabla_frame.grid_columnconfigure(0, weight=1)
    tabla_frame.grid_rowconfigure(0, weight=1)

    # Conectar con la base de datos y cargar los datos
    try:
        conexion = mysql.connector.connect(
            host="localhost", user="root", password="Ccrj1108231407&", database="sistema_login"
        )
        cursor = conexion.cursor()
        cursor.execute("SELECT nombre, tipo, precio_estimado, ubicacion, descripcion FROM cultivos")

        for i, row in enumerate(cursor.fetchall()):
            nombre, tipo, precio, ubicacion, descripcion = row

            # Ajustar la descripción en varias líneas (máx 40 caracteres por línea)
            descripcion_formateada = "\n".join(textwrap.wrap(descripcion, width=40))

            # Alternar colores en las filas
            bg_color = "#2E2E2E" if i % 2 == 0 else "#252526"

            tabla.insert("", "end", values=(nombre, tipo, precio, ubicacion, descripcion_formateada), tags=(bg_color,))

        # Aplicar colores a las filas
        tabla.tag_configure("#2E2E2E", background="#2E2E2E")
        tabla.tag_configure("#252526", background="#252526")

        conexion.close()
    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"No se pudieron cargar los cultivos: {e}")
