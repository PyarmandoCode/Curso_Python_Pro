usuario_valido= "admin"
contraseña_valida="123456"

intentos = 3

while intentos >0:
    usuario = input("Ingrese usuario:")
    contraseña= input("Ingrese Contraseña:")
    if usuario ==usuario_valido and contraseña == contraseña_valida:
        print("Inicio de Session Exitoso ,Bienvenido")
        break #todo salir del bucle
    else:
        intentos -= 1
        print(f"usuario o contraseña incorrectos Intententos restantes {intentos}")
    if intentos ==0:
        print("Has Agotado todos los intentos CUENTA BLOQUEADA")
