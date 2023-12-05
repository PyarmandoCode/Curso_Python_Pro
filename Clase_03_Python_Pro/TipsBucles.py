nombres = ["Ana","Carlos", "Eva"]
edades = [30,25,28]
cursos = ["PYTHON","FLASK","DJANGO"]

# for items in edades:
#     print(items)

"""
zip () permite iterar simultanemanete sobre multiples listas
y combinar sus elementos
"""

for nombre,edad,curso in zip(nombres,edades,cursos):
    print(f"{nombre} tiene {edad} años y le gusta el curso de {curso}")
    

"""
sorted() itera sobre una secuencia y ordena la lista de valores
"""    
numeros = [5,2,7,1,9]
for numero in sorted(numeros):
    print(numero)


"""
Comprension de Listas
Imprimir los cuadrados que existen hasta el numero 6
"""

#ejemplo01
#manera clasica
for i in range(1,6):
     print ( i **2 )

#manera comprension de listas

cuadrados = [i**2 for i in range (1,6)]    
print(cuadrados)

#ejemplo02
numeros = [1,2,3,4,5,6,7,8,9,10]
#manera clasica
for x in numeros:
     if x % 2 == 0:
         print(x)

#manera comprension de listas
pares = [x for x in numeros if x % 2 == 0]
print(pares)

#ejemplo03
frutas = ['manzana','banana','naranja','platano']
# for fruta in frutas:
#     print(fruta.upper())

mayusculas = [fruta.upper() for fruta in frutas]    
print(mayusculas)
