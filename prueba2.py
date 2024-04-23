import tkinter as tk
from tkinter import filedialog, messagebox
import csv
import webbrowser
import json
from google.auth.credentials import Credentials
from google.oauth2 import service_account
import gspread



with open("aceptados.txt", "r", encoding="utf-8") as file:
    nombres_destacados = [nombre.strip('"') for nombre in file.read().split(", ")]


'''def guardar_en_archivo(filas):
    escritorio = "C:/Users/HolaY/OneDrive/Escritorio"
    with open(os.path.join(escritorio, 'datos_guardados.txt'), 'a', encoding='utf-8') as archivo:
        for fila in filas:
            fila_como_texto = ','.join(fila)  # Asegúrate de que fila es una lista de strings
            archivo.write(fila_como_texto + '\n')  # Escribe la fila en el archivo
'''

def guardar_en_archivo(filas):
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    
    try:
        # Crear credenciales desde el archivo JSON
        credentials = service_account.Credentials.from_service_account_file(r'JsonFileFromGoogle.json', scopes=scope)
        
        # Autorizar la conexión
        gc = gspread.authorize(credentials)
        
        # Clave de la hoja de cálculo
        spreadsheet_key1 = '1kSBKZ873WvsnFzT90-WY1fTEQIe3vp2npEiEw_h5iC8'
        
        # Abrir la hoja de cálculo
        worksheet = gc.open_by_key(spreadsheet_key1).worksheet('TEST')
        
        # Obtener la cantidad de filas en la hoja de cálculo
        last_row = worksheet.row_count
        
        '''
        # Rango para borrar antes de agregar nuevas filas
        range_to_clear = f'A6:V{last_row}'
        
        # Borrar el rango especificado
        worksheet.batch_clear([range_to_clear])
        '''
        
        # Convertir los datos en la lista a cadenas y llenar los valores NaN con una cadena vacía
        rows_to_add = [[str(value) if value != 'nan' else '' for value in row] for row in filas]
        
        # Definir el rango de celdas donde se escribirán los datos
        start_row = len(worksheet.col_values(1)) + 1
        #start_row = 1
        end_row = start_row + len(rows_to_add) - 1
        start_col = 'A'
        end_col = 'AZ'
        range_to_write = f'{start_col}{start_row}:{end_col}{start_row}'
        
        # Actualizar la hoja de cálculo con los nuevos datos
        worksheet.update(range_to_write, rows_to_add)
        print("Exito")
        
        print('Check google sheets')
    except Exception as e:
        print(f'Error al cargar en Google Sheets: {str(e)}')

    



def mostrar_fila(indice_fila, datos, fila_inicio, fila_fin):
    global ventana_datos

    entry_widgets = []
    dropdown_widgets = []

    ventana_datos = tk.Toplevel()
    ventana_datos.title("Datos de la Fila")

    textbox_entries_left = []
    textbox_entries_right = []

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
        check = tk.Checkbutton(panel_checkboxes, text=nombre, variable=var, font=("Roboto", 9))
        check.grid(row=i, column=0, sticky='w')

    # Crear checkboxes en la segunda columna
    for i, nombre in enumerate(nombres_checkboxes[mitad_lista:]):
        var = tk.BooleanVar()
        check = tk.Checkbutton(panel_checkboxes, text=nombre, variable=var, font=("Roboto", 9))
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
                    entry.config(bg="#65E320")  # Cambiar el fondo a verde si el nombre está en la lista
                entry_widgets.append(entry)
                return entry
            if special_widgets[column_idx] == "entry2":
                entry = tk.Entry(parent, width=50)
                entry.insert(0, value)
                entry.grid(row=row, column=1, padx=5, pady=5)
                entry_widgets.append(entry)
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
                dropdown_widgets.append(var)
                return var
        else:
            label = tk.Label(parent, text=value, width=50, anchor="center", justify="center", font=("Roboto", 10))
            label.grid(row=row, column=1, padx=5, pady=5)

    # Crea widgets para el panel izquierdo
    for i, idx in enumerate(indices_izquierdos):
        tk.Label(panel_izquierdo, text=f"{nombres_columnas[idx + 1]}:", padx=10, pady=5, font=("Roboto", 12, "bold")).grid(row=i, column=0, padx=5, pady=5)
        create_widget(panel_izquierdo, idx, datos_fila[idx], i, idx)

    # Crea widgets para el panel derecho
    for i, idx in enumerate(indices_derechos):
        tk.Label(panel_derecho, text=f"{nombres_columnas[idx + 1]}:", padx=10, pady=5, font=("Roboto", 12, "bold")).grid(row=i, column=0, padx=5, pady=5)
        create_widget(panel_derecho, idx, datos_fila[idx], i, idx)

    def get_widget_values():
        entry_values = [entry.get() for entry in entry_widgets]
        dropdown_values = [dropdown.get() for dropdown in dropdown_widgets]
        return entry_values, dropdown_values

    def avanzar_con_guardar():
        global datos
        fila_actualizada = datos[indice_fila]

        for i, entry in enumerate(textbox_entries_left + textbox_entries_right):
            fila_actualizada[i + 1] = entry.get()  # +1 para omitir el ID en el índice 0

        # Obtener los valores de los entry y dropdown
        entry_values, dropdown_values = get_widget_values()

        
        # Insertar los valores en la fila actualizada
        fila_actualizada[7] = entry_values[0]  # Insertar el valor del entry1 en la posición 6
        fila_actualizada[11] = entry_values[1]  # Insertar el valor del entry2 en la posición 10
        fila_actualizada[4] = dropdown_values[0]  # Insertar el valor del dropdown en la posición 3


        guardar_en_archivo([fila_actualizada])  # Pasa la fila actualizada como una lista de una fila
        
        print([fila_actualizada])
        
        messagebox.showinfo("Datos guardados", "Los datos editados han sido guardados correctamente.")

        # Cerrar la ventana actual
        ventana_datos.destroy()

        # Verificar si estamos en la última fila permitida para evitar un error de índice
        if indice_fila + 1 > len(datos):
            messagebox.showinfo("Fin del archivo", "Has alcanzado el final del rango especificado.")
            ventana_datos.destroy()
        else:
            # Pasar a la siguiente fila
            mostrar_fila(indice_fila + 1, datos, fila_inicio, fila_fin)

        


    def avanzar_sin_guardar():
        # Cerrar la ventana actual
        ventana_datos.destroy()

        # Verificar si estamos en la última fila permitida para evitar un error de índice
        if indice_fila + 1 > len(datos):
            messagebox.showinfo("Fin del archivo", "Has alcanzado el final del rango especificado.")
            ventana_datos.destroy()
        else:
            # Pasar a la siguiente fila
            mostrar_fila(indice_fila + 1, datos, fila_inicio, fila_fin)

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
boton_abrir_csv = tk.Button(ventana_principal, text="Abrir CSV", font=("Roboto", 12, "bold"), border= "5px",command=abrir_csv)
boton_abrir_csv.pack(ipadx=20, ipady=20, expand=True)  # Ajusta ipadx e ipady para modificar el tamaño

ventana_principal.mainloop()
