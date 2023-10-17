tareas=[]
#Funcion para crear una nueva tara
def crear_tarea(titulo,descripcion):
    tarea={"titulo":titulo,"descripcion":descripcion}
    tareas.append(tarea)
    print("Tarea Creada con exito")

def listar_tareas():
    if not tareas:
        print("No Hay Tareas que Mostrar")
    else:
        for i,tarea in enumerate(tareas):
            print(f"Tarea {i+1}:")
            print(f"Titulo {tarea['titulo']}")
            print(f"Descripcion {tarea['descripcion']}")
            print()

def eliminar_tarea(indice):
    if 0<= indice <len(tareas):
        tarea_eliminada=tareas.pop(indice)
        print("Tarea Eliminada con exito")
        print(f"Titulo: {tarea_eliminada['titulo']}")
        print(f"Descripcion: {tarea_eliminada['descripcion']}")
    else:
        print("Indice esta fuera de rango")   

def actualizar_tarea(indice,nuevo_titulo,nueva_descripcion):
    if 0<= indice <len(tareas):
        tareas[indice]["titulo"]=nuevo_titulo
        tareas[indice]["descripcion"]=nueva_descripcion
        print("Tarea Actualizada con exito") 
    else:
        print("Indice esta fuera de rango")               

