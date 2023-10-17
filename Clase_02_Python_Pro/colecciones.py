"""
Listas
"""
maravillas=list()

maravillas=["Piramides","El Faro de Alejandria","Cristor Redentor","La Estatua de Zeus","La Estatua de Zeus","La Estatua de Zeus"]
#Mostrando Datos
"""
print(maravillas)
for maravilla in maravillas:
    print(maravilla)
print(maravillas[0])
"""
#Añadir Elementos
maravillas.append("El Coloso de Rodas") #Agrega al Final de la lista
maravillas.insert(1,"Los Jardines Colgantes") #Agrega en cualquier Posicion
#Eliminar Elementos
maravillas.pop(1)#Elimina por indice o por posicion
maravillas.remove("El Faro de Alejandria")#Elimina por el valor
#Modificar Elemento
maravillas[3]="El Mauseoleo de Halicarnso"
#Ordenar los Elementos
maravillas.sort()
maravillas.reverse()
#Buscar un Elemento
#if 'La Estatua de Zeus' in maravillas:
#    print("Se encontro la maravilla")
#else:
#    print("No Se encontro")    
#Longitud de la Lista
size=len(maravillas)
#print(size)
#Cantidad de Duplicados
repetidos=maravillas.count("La Estatua de Zeus")
print(repetidos)
#Guardar Elementos de otro tipo
empleados = [
    {"nombre":"juan","apellido":"gomez","salario":"1700"},
    {"nombre":"oscar","apellido":"gomez","salario":"1700"},
    {"nombre":"manuel","apellido":"gomez","salario":"1700"},
    {"nombre":"richard","apellido":"gomez","salario":"1700"},
    {"nombre":"sonia","apellido":"gomez","salario":"1700"},
    {"nombre":"pedro","apellido":"gomez","salario":"1700"},
    {"nombre":"juan","apellido":"gomez","salario":"1700"},
]
print(empleados[6]["salario"])