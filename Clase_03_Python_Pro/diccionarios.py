mi_diccionario = {}
mi_diccionario = dict()

mi_diccionario = {
    "nombre":"juan",
    "edad":30,
    "ciudad":"New York"
}

#print(mi_diccionario["ciudad"])
mi_diccionario['profesion'] = "Developer"
mi_diccionario['nombre'] = "Oscar"
del mi_diccionario["profesion"]
del mi_diccionario["ciudad"]

claves = mi_diccionario.keys()
valores = mi_diccionario.values()
todos = mi_diccionario.items()

# print(f"imprimiendo las claves {claves}")
# print(f"imprimiendo los valores {valores}")
# print(f"imprimiendo key y val {todos}")

for k , v in mi_diccionario.items():
    print(f" la clave {k} y su valor {v}")