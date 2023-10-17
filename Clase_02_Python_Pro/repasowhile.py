for x in range(1,11):
    print(f"{x} Hola DESDE LA SEGUNDA CLASE")
numero = int(input("Ingrese un numero para ver su tabla de multiplicar:"))
i=1
while i <=12:
    resultado= numero * i
    print(f"{numero} x {i} = {resultado}")
    i +=1#contador

"""
Crea un juego en el que la computadora elija un número aleatorio entre 1 y 100, y el jugador tenga que adivinarlo utilizando un bucle while. La computadora debe proporcionar pistas sobre si el número a adivinar es mayor o menor que el número ingresado por el jugador.
"""
import random
intentos=0
numero_secreto=random.randint(1,100) # Numero que genero la computadora
while True:
    intentos +=1
    numero= int(input("Adivina el numero(entre 1 y 100):")) #Jugador Ingreso
    if numero == numero_secreto:
        print(f"Correcto! Has Adivinado el numero en {intentos}")
        break#Interrumpir bucle ==false
    elif numero < numero_secreto: #Dando las pistas
        print(f"El Numero secreto es mayor {numero_secreto}")
    else:
        print(f"El Numero secreto es menor {numero_secreto}")    

"""
Crea un contador regresivo desde un número dado hasta cero con un efecto visual, como la cuenta regresiva de una película. Utiliza el módulo time.sleep() para crear un efecto de pausa entre los números.
"""    
import time
numero = int(input("ingrese un numero para comenzar la cuenta regresiva:"))

while numero>=0:
    print(numero)
    time.sleep(1) #Pausa de 1 Segundo
    numero -=1
print("Ya Iniciamos La Pelicula")    







