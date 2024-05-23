
#enumeramos los clientes  
def select_client(Client_list):    
    print("**Clientes disponibles**")
    for i, client_position in enumerate(Client_list , start=1):
        print(f"{i}- {client_position}")
    #seleccionamos un cliente
    cliente_num_select = int(input("Seleccione un cliente para iniciar la compra: ")) 
    client_select = Client_list[cliente_num_select -1]
    print(f"Ha seleccionado a {client_select} \r")
    print("Hola",client_select, "Bienvenido!")
    
    return client_select

#creamos una funcion para seleccionar un cliente de la lista:
#Un for para iterar la lista y le decimos q guarde cada cliente en una variable client_position. enumeramos la lista de clientes, le indicamos con "start=1" que comience enumerando desde el 1 en [0] , 2 [1]... y que imprima esa posicion con el nombre del cliente en esa posicion.
#con un int((input()) hacemos que el usuario seleccione el numero de un cliente y lo guardamos en client_num_select.
#creamos la variable client_select y le decimos que busque la posicion ingresada dentro de la lista de clientes (client_list) y le restamos 1 para que seleccione el cliente en la posicion [0].