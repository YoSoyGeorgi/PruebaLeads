import tkinter as tk
from tkinter import filedialog, messagebox
import csv
import webbrowser
import os

with open("aceptados.txt", "r", encoding="utf-8") as file:
    nombres_destacados = [nombre.strip('"') for nombre in file.read().split(", ")]


def guardar_en_archivo(datos):
        # Obtener la ruta del escritorio
            escritorio = "C:/Users/HolaY/OneDrive/Escritorio"

        # Crear o abrir el archivo en modo de escritura
            with open(os.path.join(escritorio, 'datos_guardados.txt'), 'w', encoding='utf-8') as archivo:
                # Escribir los datos en el archivo
                for fila in datos:
                    fila_como_texto = ','.join(fila)  # Convertir la lista de datos de la fila en una cadena separada por comas
                    archivo.write(fila_como_texto + '\n')  # Escribir la fila en el archivo, seguida de un salto de línea

def mostrar_fila(indice_fila, datos, fila_inicio, fila_fin):
    global ventana_datos

    ventana_datos = tk.Toplevel()
    ventana_datos.title("Datos de la Fila")

    nombres_columnas = datos[0]
    datos_fila = datos[indice_fila][1:27]  # Asegurarse de incluir hasta la columna Z

    # Paneles para organizar la UI
    panel_izquierdo = tk.Frame(ventana_datos)
    panel_izquierdo.grid(row=0, column=0, sticky="nsew")

    panel_derecho = tk.Frame(ventana_datos)
    panel_derecho.grid(row=0, column=1, sticky="nsew")

    # Paneles para organizar los checkboxes en dos columnas
    panel_checkboxes = tk.Frame(panel_derecho)
    panel_checkboxes.grid(row=8, column=1, sticky="nsew", padx=10, pady=10)
    
    nombres_checkboxes = [
        "MSM", "TTEN", "SICOM", "BAW", "POLIMATA", "TRESITE", "CMOV",
        "INTEGRA", "BRIYAM", "ITNNOVATION", "ENRED", "MYCASHLESS",
        "VIRMAR", "COVALU", "INTERASTAR", "STRATEGO", "LANZ"
    ]
    
    # Determina el número de nombres para calcular la división en dos listas
    mitad_lista = len(nombres_checkboxes) // 2

    # Crear checkboxes en la primera columna
    for i, nombre in enumerate(nombres_checkboxes[:mitad_lista]):
        var = tk.BooleanVar()
        check = tk.Checkbutton(panel_checkboxes, text=nombre, variable=var)
        check.grid(row=i, column=0, sticky='w')

    # Crear checkboxes en la segunda columna
    for i, nombre in enumerate(nombres_checkboxes[mitad_lista:]):
        var = tk.BooleanVar()
        check = tk.Checkbutton(panel_checkboxes, text=nombre, variable=var)
        check.grid(row=i, column=1, sticky='w')

    # Configuración de los índices de columnas para cada panel
    indices_izquierdos = list(range(0, 12)) + [16]  # Incluir Q después de K y M
    indices_derechos = [13, 14, 15, 17, 21, 22, 23, 24]  # Incluir O antes de P

    # Diccionario para manejar la creación de widgets dinámicamente
    special_widgets = {
        6: "entry1",  # Columna H, índice 7 en los datos
        10: "entry2", # Columna L, índice 11 en los datos
        3: "dropdown" # Columna E, índice 4 en los datos
    }

    # Función para crear los widgets adecuados
    def create_widget(parent, column, value, row, column_idx):
        if column_idx in special_widgets:
            if special_widgets[column_idx] == "entry1":
                entry = tk.Entry(parent, width=50)
                entry.insert(0, value)
                entry.grid(row=row, column=1, padx=5, pady=5)
                if value.strip('"') in nombres_destacados:
                    entry.config(bg='Green')  # Cambiar el fondo a rojo si el nombre está en la lista
                return entry
            if special_widgets[column_idx] == "entry2":
                entry = tk.Entry(parent, width=50)
                entry.insert(0, value)
                entry.grid(row=row, column=1, padx=5, pady=5)
                return entry
            elif special_widgets[column_idx] == "dropdown":
                var = tk.StringVar(parent)
                var.set(value)  # set default value
                dropdown = tk.OptionMenu(parent, var, 
                                        "MSM",
                                        "TTEN",
                                        "SICOM",
                                        "BAW",
                                        "POLIMATA",
                                        "TRESITE",
                                        "CMOV",
                                        "INTEGRA",
                                        "BRIYAM",
                                        "ITNNOVATION",
                                        "ENRED",
                                        "MYCASHLESS",
                                        "VIRMAR",
                                        "COVALU",
                                        "INTERASTAR",
                                        "STRATEGO",
                                        "LANZ")
                dropdown.config(width=48)
                dropdown.grid(row=row, column=1, padx=5, pady=5)
                return var
        else:
            label = tk.Label(parent, text=value, width=50, anchor="w")
            label.grid(row=row, column=1, padx=5, pady=5)

    # Crea widgets para el panel izquierdo
    for i, idx in enumerate(indices_izquierdos):
        tk.Label(panel_izquierdo, text=f"{nombres_columnas[idx + 1]}:", padx=10, pady=5, font=("Arial", 10, "bold")).grid(row=i, column=0, padx=5, pady=5)
        create_widget(panel_izquierdo, idx, datos_fila[idx], i, idx)

    # Crea widgets para el panel derecho
    for i, idx in enumerate(indices_derechos):
        tk.Label(panel_derecho, text=f"{nombres_columnas[idx + 1]}:", padx=10, pady=5, font=("Arial", 10, "bold")).grid(row=i, column=0, padx=5, pady=5)
        create_widget(panel_derecho, idx, datos_fila[idx], i, idx)

    def avanzar_con_guardar():
        global datos
    # Actualizar los datos en la lista de datos con los valores editados en los TextBoxes
    # Asegurarse de incluir las entradas de ambos paneles
        for i, entry in enumerate(textbox_entries_left):
            datos[indice_fila][i + 1] = entry.get()  # Actualizar el valor en la lista de datos para el panel izquierdo
        
        # Indices para los datos del panel derecho, ajustados para las columnas en el CSV
        indices_derechos = [14, 15, 16, 21, 22, 23, 24]  # Indices de las columnas P, Q, R, W, X, Y, Z
        for i, entry in enumerate(textbox_entries_right):
            datos[indice_fila][indices_derechos[i] + 1] = entry.get()  # Sumamos 1 porque los índices del CSV comienzan en 0

        messagebox.showinfo("Datos guardados", "Los datos editados han sido guardados correctamente.")

        guardar_en_archivo(datos)

        # Cerrar la ventana actual
        ventana_datos.destroy()

        # Verificar si estamos en la última fila permitida para evitar un error de índice
        if indice_fila + 1 < len(datos) and indice_fila + 1 <= fila_fin:
            # Pasar a la siguiente fila
            mostrar_fila(indice_fila + 1, datos, fila_inicio, fila_fin)
        else:
            messagebox.showinfo("Fin del archivo", "Has alcanzado el final del rango especificado.")

        


    def avanzar_sin_guardar():
        # Cerrar la ventana actual
        ventana_datos.destroy()

        # Verificar si estamos en la última fila permitida para evitar un error de índice
        if indice_fila + 1 < len(datos) and indice_fila + 1 <= fila_fin:
            # Pasar a la siguiente fila
            mostrar_fila(indice_fila + 1, datos, fila_inicio, fila_fin)
        else:
            messagebox.showinfo("Fin del archivo", "Has alcanzado el final del rango especificado.")

    # Botones
    boton_frame = tk.Frame(ventana_datos)
    boton_frame.grid(row=1, column=0, columnspan=2, pady=10)

    tk.Button(boton_frame, text="Abrir Página web", command=lambda: webbrowser.open_new(datos_fila[11])).grid(row=1, column=2, padx=5, pady=5)
    tk.Button(boton_frame, text="Aceptar", command=lambda: avanzar_con_guardar()).grid(row=1, column=0, padx=10, pady=5)
    tk.Button(boton_frame, text="Rechazar", command=lambda: avanzar_sin_guardar()).grid(row=1, column=1, padx=10, pady=5)

    ventana_datos.mainloop()


def abrir_csv():
    global datos, ventana_principal, fila_inicio_entry, fila_fin_entry

    ruta_csv = filedialog.askopenfilename(filetypes=[("Archivos CSV", "*.csv")])

    if ruta_csv:
        with open(ruta_csv, newline='', encoding='utf-8') as csvfile:
            lector_csv = csv.reader(csvfile)
            datos = list(lector_csv)

        fila_inicio = 2
        fila_fin = len(datos)

        # Mostrar los datos de la fila especificada
        mostrar_fila(fila_inicio - 1, datos, fila_inicio, fila_fin)  # Restamos 1 para que coincida con el índice de Python (que comienza desde 0)

ventana_principal = tk.Tk()
ventana_principal.title("Cargar CSV")

ancho_pantalla = ventana_principal.winfo_screenwidth()
alto_pantalla = ventana_principal.winfo_screenheight()

x = int((ancho_pantalla - 640) / 2)
y = int((alto_pantalla - 480) / 2)

ventana_principal.geometry(f"+{x}+{y}")
ventana_principal.geometry("640x480")

# Añadir labels y textboxes para el rango de filas (eliminados por brevedad)

# Botón para abrir el archivo CSV
boton_abrir_csv = tk.Button(ventana_principal, text="Abrir CSV", command=abrir_csv)
boton_abrir_csv.pack(ipadx=20, ipady=20, expand=True)  # Ajusta ipadx e ipady para modificar el tamaño

ventana_principal.mainloop()