import csv

def cargar_datos_desde_csv(ruta_csv):
    with open(ruta_csv, newline='', encoding='utf-8') as csvfile:
        lector_csv = csv.reader(csvfile)
        datos = list(lector_csv)
    return datos
