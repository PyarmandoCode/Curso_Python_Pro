"""
Un CRUD (Create, Read, Update, Delete) es un conjunto de operaciones básicas para gestionar datos en una aplicación. Puedes implementar un CRUD en Python utilizando listas para almacenar los datos. A continuación, te mostraré un ejemplo simple de cómo crear un CRUD para gestionar una lista de elementos (por ejemplo, una lista de tareas) en Python
"""

from misfunciones import crear_tarea,listar_tareas,eliminar_tarea, actualizar_tarea

while True:
    print("\nOpciones")    
    print("1.-Crear Tarea")
    print("2.-Listar Tareas")
    print("3.-Eliminar Tareas")
    print("4.-Actualizar Tarea")
    print("5.-Salir")

    opcion=input("Seleccione la Opcion:")
    if opcion=="1":
        titulo=input("Ingrese el Titulo de la Tarea:")
        descripcion=input("Ingrese la descripcion de la Tarea:")
        crear_tarea(titulo,descripcion)
    elif opcion=="2":
        listar_tareas()   
    elif opcion=="3":
        listar_tareas()  
        indice=int(input("Ingrese el numero de la tarea a eliminar:"))     
        eliminar_tarea(indice)
    elif opcion=="4":
        listar_tareas()  
        indice=int(input("Ingrese el Numero de la Tarea a actualizar:"))  
        nuevo_titulo=input("Ingrese el Nuevo Titulo:")
        nueva_descripcion=input("Ingrese la Nueva descripcion:")
        actualizar_tarea(indice,nuevo_titulo,nueva_descripcion)
    elif opcion=="5":
        break 
    else:
        print("No Existe la Opcion")   
