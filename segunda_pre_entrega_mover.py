
from paquete_entregas_finales.clase_cliente import Client
from paquete_entregas_finales.funcion_select_client import select_client


Client_list =[            
Client("David","david@coder.com","JJpaso 123"),
Client("juan","juan@coder.com","La rioja 124"),
Client("Maria","mar@coder.com", "Av siempreviva 742")
]

client_select = select_client(Client_list)

while True:
    print("----MENU----")
    print("**Elija una opcion**")
    print("1- Agregar producto al carrito")
    print("2- Eliminar un producto del carrito")
    print("3- Mostrar carrito")
    print("4- cambiar de cliente")
    print("5- Salir")        

    option = input("ingrese una opcion: ")

    if option == "1":
        product = input("ingrese el producto para agregar al carrito: ").strip().capitalize()
        if product == "":
            print("**Debe ingrasar un producto!**")
        else:
            client_select.add_to_cart(product)
    elif option == "2":
        product = input("ingrese el producto para eliminar del carrito: ").strip().capitalize()
        if product == "":
            print("**No ingreso ningun producto para eliminar**")
        else:    
            client_select.delet_from_car(product)
    elif option == "3":
        client_select.show_cart()
    elif option == "4":
       client_select = select_client(Client_list)
    elif option == "5":
        print("adiooos, gracias por comprar!")
        break
    else:
        print("**Esa opcion no es correcta**")    

            
#creamos un menu con un while true para invocar las funciones y los atrbutos.















