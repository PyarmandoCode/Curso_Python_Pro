"""
LECTURA DE UN ARCHIVO CSV
1.-LOCALIZAR ARCHIVO ABRIRLO ES UN BUFFER
2.-LEER ARCHIVO
3.-RECORRER EL ARCHIVO
"""
import csv as MI_CSV

datos_nuevos = []

with open('stock_4_12_2013.csv',newline='') as archivo_csv:
    lector_csv=MI_CSV.reader(archivo_csv)
    #iterar sobre las filas del archivos
    for row in lector_csv:
        columna_a = row[0]
        datos_nuevos.append(columna_a)
        
print(datos_nuevos)
