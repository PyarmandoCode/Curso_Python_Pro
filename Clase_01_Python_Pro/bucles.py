"""
Crea un programa que cuente del 1 al 10 utilizando un bucle while.
"""

# numero=1

# while numero <=10:#True
#     print(numero)
#     numero +=1#False


"""
Contar vocales en una cadena de texto:
"""
cadena=input("Ingrese una frase:")
vocales="aeiouAEIOU"
contador=0
for letra in cadena:
    if letra in vocales:
        contador +=1
#FUERA DEL BUCLE        
print(f"El Numero de vocales en la frase {contador}")        
