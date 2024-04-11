import tkinter as tk
from tkinter import messagebox

class CSVDataViewer:
    def __init__(self, datos):
        self.datos = datos
        self.indice_fila = 1
        self.mostrar_fila()

    def mostrar_fila(self):
        self.ventana_datos = tk.Tk()
        self.ventana_datos.title("Datos de la Fila")

        nombres_columnas = self.datos[0]
        datos_fila = self.datos[self.indice_fila][1:15]

        for i, nombre_columna in enumerate(nombres_columnas[1:15]):
            etiqueta = tk.Label(self.ventana_datos, text=f"{nombre_columna}: {datos_fila[i]}", padx=10, pady=5)
            etiqueta.grid(row=i // 4, column=i % 4, padx=5, pady=5)

        boton_rechazar = tk.Button(self.ventana_datos, text="Rechazar", command=self.avanzar)
        boton_rechazar.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

        boton_aceptar = tk.Button(self.ventana_datos, text="Aceptar", command=self.avanzar)
        boton_aceptar.grid(row=4, column=2, columnspan=2, padx=10, pady=5)

    def avanzar(self):
        if self.indice_fila >= len(self.datos):
            self.ventana_datos.destroy()
            messagebox.showinfo("Fin del archivo", "Se han procesado todos los datos del archivo CSV.")
            return
        self.ventana_datos.destroy()
        self.indice_fila += 1
        self.mostrar_fila()
