import tkinter as tk
from tkinter import filedialog, messagebox
from csv_data_viewer import CSVDataViewer
import csv

class CSVReaderApp:
    def __init__(self):
        self.ventana_principal = tk.Tk()
        self.ventana_principal.title("Cargar CSV")
        self.configurar_ventana()

    def configurar_ventana(self):
        ancho_pantalla = self.ventana_principal.winfo_screenwidth()
        alto_pantalla = self.ventana_principal.winfo_screenheight()
        x = int((ancho_pantalla - 640) / 2)
        y = int((alto_pantalla - 480) / 2)
        self.ventana_principal.geometry(f"+{x}+{y}")
        self.ventana_principal.geometry("640x480")

        self.boton_abrir_csv = tk.Button(self.ventana_principal, text="Abrir CSV", command=self.abrir_csv)
        self.boton_abrir_csv.pack(pady=20)

    def abrir_csv(self):
        ruta_csv = filedialog.askopenfilename(filetypes=[("Archivos CSV", "*.csv")])
        if ruta_csv:
            with open(ruta_csv, newline='', encoding='utf-8') as csvfile:
                lector_csv = csv.reader(csvfile)
                datos = list(lector_csv)
            self.ventana_principal.destroy()
            CSVDataViewer(datos)

