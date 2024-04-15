import tkinter as tk
from tkinter import filedialog, messagebox
import csv
import webbrowser
import os

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

    

    ventana_datos = tk.Toplevel()  # Uso de Toplevel para evitar problemas con la destrucción de ventanas
    ventana_datos.title("Datos de la Fila")

    nombres_columnas = datos[0]
    datos_fila = datos[indice_fila][1:27]  # Asegurarse de incluir hasta la columna Z

    # Verificar si la fila debe ser omitida
    if float(datos_fila[14]) < 11 and datos_fila[3] not in ["TRESITE", "MYCASHLESS"]:
        messagebox.showinfo("Fila omitida", "La fila ha sido omitida debido a que el valor en la columna P es menor a 11 y la columna E no es TRESITE ni MYCASHLESS.")
        avanzar_sin_guardar()
        return

    # Paneles para organizar la UI
    panel_izquierdo = tk.Frame(ventana_datos)
    panel_izquierdo.grid(row=0, column=0, sticky="nsew")

    panel_derecho = tk.Frame(ventana_datos)
    panel_derecho.grid(row=0, column=1, sticky="nsew")

    # Lista para almacenar las referencias a los TextBoxes editables en el panel izquierdo
    textbox_entries_left = []
    for i, nombre_columna in enumerate(nombres_columnas[1:15]):
        tk.Label(panel_izquierdo, text=f"{nombre_columna}:", padx=10, pady=5, font=("Arial", 10, "bold")).grid(row=i, column=0, padx=5, pady=5)
        entry = tk.Entry(panel_izquierdo, width=50)
        entry.insert(0, datos_fila[i])
        entry.grid(row=i, column=1, padx=5, pady=5)
        textbox_entries_left.append(entry)

    # Lista para almacenar las referencias a los TextBoxes editables en el panel derecho
    textbox_entries_right = []
    indices_derechos = [14, 15, 16, 21, 22, 23, 24]  # Indices de las columnas P, Q, R, W, X, Y, Z
    for i, idx in enumerate(indices_derechos):
        nombre_columna = nombres_columnas[idx +1]
        tk.Label(panel_derecho, text=f"{nombre_columna}:", padx=10, pady=5, font=("Arial", 10, "bold")).grid(row=i, column=0, padx=5, pady=5)
        entry = tk.Entry(panel_derecho, width=50)
        entry.insert(0, datos_fila[idx])
        entry.grid(row=i, column=1, padx=5, pady=5)
        textbox_entries_right.append(entry)

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

        # Pasar a la siguiente fila sin guardar los cambios
        mostrar_fila(indice_fila + 1, datos, fila_inicio, fila_fin)

    # Botones
    boton_frame = tk.Frame(ventana_datos)
    boton_frame.grid(row=1, column=0, columnspan=2, pady=10)

    tk.Button(boton_frame, text="Abrir Perfil Personal", command=lambda: webbrowser.open_new(datos_fila[8])).grid(row=0, column=0, padx=5, pady=5)
    tk.Button(boton_frame, text="Abrir Página web", command=lambda: webbrowser.open_new(datos_fila[11])).grid(row=0, column=1, padx=5, pady=5)
    tk.Button(boton_frame, text="Abrir Perfil de la empresa", command=lambda: webbrowser.open_new(datos_fila[13])).grid(row=0, column=2, padx=5, pady=5)
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

        fila_inicio = int(fila_inicio_entry.get())
        fila_fin = int(fila_fin_entry.get())

        # Mostrar los datos de la fila especificada
        mostrar_fila(fila_inicio - 3, datos, fila_inicio, fila_fin)  # Restamos 1 para que coincida con el índice de Python (que comienza desde 0)


ventana_principal = tk.Tk()
ventana_principal.title("Cargar CSV")

ancho_pantalla = ventana_principal.winfo_screenwidth()
alto_pantalla = ventana_principal.winfo_screenheight()

x = int((ancho_pantalla - 640) / 2)
y = int((alto_pantalla - 480) / 2)

ventana_principal.geometry(f"+{x}+{y}")
ventana_principal.geometry("640x480")

# Añadir labels y textboxes para el rango de filas
fila_inicio_label = tk.Label(ventana_principal, text="Fila de inicio:")
fila_inicio_label.pack()

fila_inicio_entry = tk.Entry(ventana_principal)
fila_inicio_entry.pack()

fila_fin_label = tk.Label(ventana_principal, text="Fila final:")
fila_fin_label.pack()

fila_fin_entry = tk.Entry(ventana_principal)
fila_fin_entry.pack()

boton_abrir_csv = tk.Button(ventana_principal, text="Abrir CSV", command=abrir_csv)
boton_abrir_csv.pack(pady=20)

ventana_principal.mainloop()
