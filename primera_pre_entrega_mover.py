#esta va a ser la funcion para registrar un usuario, utilizamos ".strip() para quitar los espacios de inicio y final"
def registrar_usuario(db):
    nombre_usuario = input("Ingrese nombre de usuario: ").strip()
    contraseña = input("Ingrese su contraseña: ").strip()
    if nombre_usuario == "" or contraseña == "":
        print("El usuario o contraseña no puede estar vacio")
    else:
        db[nombre_usuario] = contraseña
        print("Usuario cargado correctamnte!")
    
#en este diccionario vacio vamos a  guardar los usuarios registrados para despues usarlo como valor o argumento en las funciones.

usuario = {}

#aca vamos a hacer la funcion para mostrar los usuarios. (usamos la funcion ".item" para desempaquetar el conjunto de clave-valor y mostrar las variables separadas)

def mostrar_usuarios(db):
    print("---USUARIOS---")
    if len(db) < 1:
        print("No hay usuarios registrados hasta el momento")
    else:
        for usuario, contraseña in db.items():
            print(f"usuario:  {usuario}, contraseña:  {contraseña}")

#aca vamos a hacer el login.

def login(db):
    nombre_usuario = input("Ingrese nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")
    if nombre_usuario in db and db[nombre_usuario] == contraseña:
        print("Ingresó con exito")
    else:
        print("Usuario o contrasela no coinciden, vuelva a intentar!")
        
#menu

while True: 
    print("\n")
    print("1 - Registrar usuario ")
    print("2 - Mostrar usuarios ")
    print("3 - Login ")
    print("4 - Salir")

    seleccionar_opcion = input("seleccione una opcion: ")

    if seleccionar_opcion == "1":
        registrar_usuario(usuario)
    elif seleccionar_opcion =="2":
        mostrar_usuarios(usuario)
    elif seleccionar_opcion == "3":
        login(usuario)
    elif seleccionar_opcion == "4":
        print(" Chauuuu! ")
        break
    else:
        print("No existe esa opcion!, Intenta de nuevo")
    
