import tkinter as tk
from tkinter import filedialog, messagebox
import csv

def abrir_csv():
    # Función para abrir y leer el archivo CSV
    global datos, ventana_principal

    # Diálogo para seleccionar un archivo CSV
    ruta_csv = filedialog.askopenfilename(filetypes=[("Archivos CSV", "*.csv")])

    # Si se selecciona un archivo
    if ruta_csv:
        # Abrir y leer el archivo CSV
        with open(ruta_csv, newline='', encoding='utf-8') as csvfile:
            lector_csv = csv.reader(csvfile)
            datos = list(lector_csv)

        # Cerrar la ventana principal
        ventana_principal.destroy()

        # Mostrar los datos fila por fila en una nueva ventana
        mostrar_fila(1, datos)  # Empezar desde la segunda fila

def mostrar_fila(indice_fila, datos):
    # Función para mostrar los datos de la fila actual del CSV

    global ventana_datos  # Hacer la ventana_datos global para que pueda ser cerrada desde la función avanzar

    # Crear una nueva ventana para mostrar los datos de la fila actual del CSV
    ventana_datos = tk.Tk()
    ventana_datos.title("Datos de la Fila")

    # Obtener los nombres de las columnas de la primera fila
    nombres_columnas = datos[0]

    # Obtener los datos de las columnas B a M de la fila actual
    datos_fila = datos[indice_fila][1:15]

    # Mostrar etiquetas para los nombres de las columnas B a M y los datos correspondientes de la fila actual
    for i, nombre_columna in enumerate(nombres_columnas[1:15]):  # Excluir la primera columna
        etiqueta = tk.Label(ventana_datos, text=f"{nombre_columna}: {datos_fila[i]}", padx=10, pady=5)
        etiqueta.grid(row=i // 4, column=i % 4, padx=5, pady=5)

    # Botón para rechazar
    boton_rechazar = tk.Button(ventana_datos, text="Rechazar", command=lambda: avanzar(indice_fila + 1, datos))
    boton_rechazar.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

    # Botón para aceptar
    boton_aceptar = tk.Button(ventana_datos, text="Aceptar", command=lambda: avanzar(indice_fila + 1, datos))
    boton_aceptar.grid(row=4, column=2, columnspan=2, padx=10, pady=5)

def avanzar(indice_fila, datos):
    global ventana_datos  # Hacer la ventana_datos global para que pueda ser cerrada

    # Si se alcanza el final del archivo CSV
    if indice_fila >= len(datos):
        ventana_datos.destroy()  # Cerrar la ventana actual
        messagebox.showinfo("Fin del archivo", "Se han procesado todos los datos del archivo CSV.")
        return

    # Cerrar la ventana actual
    ventana_datos.destroy()

    # Mostrar la siguiente fila
    mostrar_fila(indice_fila, datos)

# Crear la ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("Cargar CSV")

# Obtener el ancho y alto de la pantalla
ancho_pantalla = ventana_principal.winfo_screenwidth()
alto_pantalla = ventana_principal.winfo_screenheight()

# Calcular la posición central de la ventana
x = int((ancho_pantalla - 640) / 2)
y = int((alto_pantalla - 480) / 2)

# Centrar la ventana
ventana_principal.geometry(f"+{x}+{y}")

# Ajustar el tamaño de la ventana
ventana_principal.geometry("640x480")

# Crear un botón para abrir el archivo CSV
boton_abrir_csv = tk.Button(ventana_principal, text="Abrir CSV", command=abrir_csv)
boton_abrir_csv.pack(pady=20)

# Ejecutar el bucle principal de la ventana principal
ventana_principal.mainloop()
