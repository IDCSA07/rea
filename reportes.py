from tkinter import *
from tkinter import messagebox
from fpdf import FPDF
import os

# Función para generar un PDF
def generar_pdf(titulo, descripcion):
    carpeta_reportes = "reportes_generados"
    if not os.path.exists(carpeta_reportes):
        os.makedirs(carpeta_reportes)

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.set_text_color(0, 0, 0)

    pdf.set_fill_color(240, 240, 240)
    pdf.set_draw_color(0, 0, 0)

    pdf.cell(190, 10, txt="Reporte", ln=True, align='C', fill=True)

    pdf.ln(10)  # Salto de línea
    pdf.multi_cell(30, 10, txt=f"{titulo}\n\n{descripcion}")
    pdf_name = f"{carpeta_reportes}/{titulo.replace(' ', '_')}.pdf"
    pdf.output(pdf_name)

    messagebox.showinfo("Éxito", f"Reporte guardado como: {pdf_name}")
    actualizar_lista_reportes()


# Función para mostrar la lista de reportes en el frame
def actualizar_lista_reportes():
    for widget in frame_lista_reportes.winfo_children():
        widget.destroy()

    carpeta_reportes = "reportes_generados"
    if not os.path.exists(carpeta_reportes):
        os.makedirs(carpeta_reportes)

    reportes = os.listdir(carpeta_reportes)
    if not reportes:
        Label(
            frame_lista_reportes,
            text="No hay reportes disponibles.",
            bg="#121212",
            fg="#B3B3B3",
            font=("Arial", 14)
        ).pack(pady=10)
    else:
        for reporte in reportes:
            frame_reporte = Frame(frame_lista_reportes, bg="#282828", pady=2)
            frame_reporte.pack(fill=X, padx=5, pady=5)

            Label(
                frame_reporte,
                text=reporte,
                bg="#282828",
                fg="white",
                font=("Arial", 10),
                anchor="w",
                padx=5
            ).pack(side=LEFT, fill=X, expand=True)

            Button(
                frame_reporte,
                text="Abrir",
                bg="#E50914",
                fg="white",
                font=("Arial", 10),
                command=lambda r=reporte: abrir_pdf(r)
            ).pack(side=RIGHT, padx=5)


# Función para abrir un PDF
def abrir_pdf(nombre_pdf):
    ruta_pdf = os.path.join("reportes_generados", nombre_pdf)
    if os.path.exists(ruta_pdf):
        os.system(f"start {ruta_pdf}")
    else:
        messagebox.showerror("Error", f"No se encontró el archivo: {ruta_pdf}")


# Función para mostrar la página de reportes en el frame principal
def mostrar_reportes(frame):
    # Limpiar el frame
    for widget in frame.winfo_children():
        widget.destroy()

    Label(
        frame,
        text="Reportes",
        bg="#121212",
        fg="white",
        font=("Arial", 20, "bold")
    ).pack(pady=20)


    # Formulario para crear reportes
    Label(
        frame,
        text="Título del reporte:",
        bg="#121212",
        fg="white",
        font=("Arial", 14)
    ).pack(anchor=W, padx=20)
    titulo_entry = Entry(frame, font=("Arial", 12), bg="#282828", fg="white")
    titulo_entry.pack(fill=X, padx=20, pady=5)

    Label(
        frame,
        text="Descripción del reporte:",
        bg="#121212",
        fg="white",
        font=("Arial", 14)
    ).pack(anchor=W, padx=20)
    descripcion_text = Text(frame, font=("Arial", 12), bg="#282828", fg="white", height=6)
    descripcion_text.pack(fill=X, padx=20, pady=5)

    Button(
        frame,
        text="Generar PDF",
        bg="#E50914",
        fg="white",
        font=("Arial", 14, "bold"),
        command=lambda: generar_pdf(titulo_entry.get(), descripcion_text.get("1.0", END).strip())
    ).pack(pady=10)

    # Sección de reportes guardados
    Label(
        frame,
        text="Reportes Generados:",
        bg="#121212",
        fg="white",
        font=("Arial", 14)
    ).pack(anchor=W, padx=20, pady=10)

    # Canvas para el scroll
    canvas = Canvas(frame, bg="#121212", highlightthickness=0)
    canvas.pack(side=LEFT, fill=BOTH, expand=True, padx=20, pady=10)

    scrollbar = Scrollbar(frame, orient=VERTICAL, command=canvas.yview)
    scrollbar.pack(side=RIGHT, fill=Y)

    global frame_lista_reportes
    frame_lista_reportes = Frame(canvas, bg="#121212")

    # Configurar el canvas para usar el scrollbar
    frame_lista_reportes.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )
    canvas.create_window((0, 0), window=frame_lista_reportes, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    actualizar_lista_reportes()
