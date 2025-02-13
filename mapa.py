from tkinter import *
from tkinter import messagebox
import folium
import webview
import os

# Generar el mapa interactivo con Folium
def generar_mapa():
    # Crear un mapa centrado en Puebla
    mapa = folium.Map(location=[19.0414, -98.2063], zoom_start=8, tiles="CartoDB positron")

    # Lista completa de municipios de Puebla
    municipios = [
        {"nombre": "Teziutlán", "coordenadas": [19.8249, -97.3656], "region": "Sierra Norte", "clima": "Templado húmedo", "temperatura_promedio": "16°C"},
        {"nombre": "Cholula", "coordenadas": [19.0594, -98.2988], "region": "Angelópolis", "clima": "Templado subhúmedo", "temperatura_promedio": "18°C"},
        {"nombre": "Puebla", "coordenadas": [19.0414, -98.2063], "region": "Angelópolis", "clima": "Templado subhúmedo", "temperatura_promedio": "17°C"},
        {"nombre": "Atlixco", "coordenadas": [18.9141, -98.4293], "region": "Valle de Atlixco", "clima": "Templado subhúmedo", "temperatura_promedio": "20°C"},
        {"nombre": "Huauchinango", "coordenadas": [20.1779, -97.6738], "region": "Sierra Norte", "clima": "Húmedo semicálido", "temperatura_promedio": "15°C"},
        {"nombre": "Izúcar de Matamoros", "coordenadas": [18.6011, -98.4677], "region": "Mixteca", "clima": "Cálido seco", "temperatura_promedio": "25°C"},
        {"nombre": "San Martín Texmelucan", "coordenadas": [19.2815, -98.4388], "region": "Valle de Serdán", "clima": "Templado subhúmedo", "temperatura_promedio": "17°C"},
        {"nombre": "San Andrés Cholula", "coordenadas": [19.0436, -98.2972], "region": "Angelópolis", "clima": "Templado subhúmedo", "temperatura_promedio": "18°C"},
        {"nombre": "Amozoc", "coordenadas": [19.0378, -98.0381], "region": "Angelópolis", "clima": "Templado subhúmedo", "temperatura_promedio": "17°C"},
        {"nombre": "Cuetzalan del Progreso", "coordenadas": [20.0175, -97.5181], "region": "Sierra Norte", "clima": "Húmedo semicálido", "temperatura_promedio": "18°C"},
    ]

    for municipio in municipios:
        popup_info = f"""
        <b>Municipio:</b> {municipio['nombre']}<br>
        <b>Región:</b> {municipio['region']}<br>
        <b>Clima:</b> {municipio['clima']}<br>
        <b>Temperatura promedio:</b> {municipio['temperatura_promedio']}
        """
        tooltip_info = f"{municipio['nombre']} ({municipio['clima']}, {municipio['temperatura_promedio']})"

        folium.Marker(
            location=municipio["coordenadas"],
            popup=popup_info,
            tooltip=tooltip_info,
            icon=folium.Icon(color="blue", icon="info-sign"),
        ).add_to(mapa)

    # Guardar el mapa en un archivo HTML
    mapa.save("mapa_puebla.html")

# Mostrar el mapa generado
def mostrar_mapa(callback_reabrir_menu):
    # Crear el mapa interactivo
    generar_mapa()

    # Abrir el mapa en el navegador
    if os.path.exists("mapa_puebla.html"):
        webview.create_window("Mapa Interactivo de Puebla", "mapa_puebla.html")
        webview.start()

        # Reabrir la ventana principal al cerrar el mapa
        callback_reabrir_menu()
    else:
        messagebox.showerror("Error", "No se pudo cargar el mapa.")

