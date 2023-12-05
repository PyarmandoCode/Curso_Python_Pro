import openpyxl

#Cargando el Libro de Trabajo
archivo_xlsx=openpyxl.load_workbook('stock_4_12_2013.xlsx')

#Selecciona la hoja de trabajo por su nombre
hoja_trabajo= archivo_xlsx['nuevo_stock']

#Obtener los valores de las celdas
for fila in hoja_trabajo.iter_rows(values_only=True):
    print(fila)