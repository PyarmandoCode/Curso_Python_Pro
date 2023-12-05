
try:
    #codigo que podria generar la excepcion
    numero = int(input("Ingrese el Numero:"))
    divisor = int(input("Ingrese el Divisor:"))
    resultado = numero / divisor
except ZeroDivisionError as error:
    #se producira si existe algun error en nuestro codigo
    print("Ha Ocurrido un Error")    
else:
    #se ejecutara si no hay excepciones en el bloque TRY
    print("La Division se realizo correctamente")  
finally:
    #se ejecutara siempre haya excepcion o no
    print("Finalizando el Proceso")      






