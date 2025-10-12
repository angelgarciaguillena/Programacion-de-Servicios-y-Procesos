#Creamos un diccionario que almacenara los productos de la tienda
products = {}

#Creamos una variable para almacenar la opcion del usuario
option = 0

#Creamos una funcion que se encargara de mostrar el menu de opciones
def menu():
    print("Menu:")
    print("1. Add product")
    print("2. Add sale")
    print("3. Show sales")
    print("4. Exit")

#Creamos una funcion para pedir el nombre del producto
def ask_name():

    #Pedimos al usuario que introduzca el nombre del producto
    name = input("Introduce the name of the product: ")

    #Devolvemos el nombre del producto
    return name

#Creamos una funcion para pedir el numero de ventas del producto
def ask_sale():

    #Pedimos al usuario que introduzca el numero de ventas del producto
    sale = int(input("Introduce the number of sales of the product: "))

    #Devolvemos el numero de ventas del producto
    return sale

#Creamos una funcion para añadir un producto
def add_product(name):

    #Creamos una variable para almacenar si el producto se ha añadido o no
    added = False

     #Si el producto no se encuentra entre los productos lo añadimos
    if name not in products:

        #Añadimos el producto al diccionario
        products[name] = 0

        #Asignamos que el producto se ha añadido
        added = True
    
    #Devolvemos si el producto se ha añadido
    return added
        
#Creamos un bucle while para que hasta que el usuario no desee salir seguir en el programa 
while option != 4:

    #Llamamos al menu de opciones
    menu()

    #Preguntamos al usuario que opcion desea
    option = int(input("Introduce a option: "))

    #Creamos un switch case para que depende de la opcion del usuario se realize una funcion u otra
    match option:

        #Si la opcion es 1 añadimos un producto
        case 1:

            #Llamamos a la funcion para obtener el nombre del producto
            name = ask_name()

            #Llamamos a la funcion para añadir el producto
            done = add_product(name)

            #Si se ha realizado informamos al usuario
            if done:

                #Informamos al usuario que se ha añadido el producto
                print("The product has been added")

            #Si no se ha realizado informamos al usuario
            else:

                #Informamos al usuario que el producto ya existe
                print("The product already exists")

        #Si la opcion es 2 registramos las ventas del producto
        case 2:

            #Llamamos a la funcion para obtener el nombre del producto
            name = ask_name()

            #Si el nombre se encuentra entre los productos registramos las ventas
            if name in products:
                
                #Preguntamos al usuario las ventas del producto
                sale = ask_sale()

                #Registramos las ventas del producto
                products[name] += sale

            #Si el producto no se encuentra informamos al usuario
            else:
                
                #Informamos al usuario de que el producto no se ha encontrado
                print("The product is not found")
        
        #Si la opcion es 3 mostramos las ventas del producto
        case 3:

            #Llamamos a la funcion para obtener el nombre del producto
            name = ask_name()

            #Si el nombre se encuentra entre los productos mostramos el numero de ventas del producto
            if name in products:
                
                #Mostramos el numero de ventas del producto
                print("The number of sales of the product is", products[name], "sales")

            #Si el producto no se encuentra informamos al usuario
            else:
                
                #Informamos al usuario de que el producto no se ha encontrado
                print("The product is not found")

        #Si la opcion es 4 informamos al usuario de que ha salido del programa
        case 4:
            print("You have left the program")

        #Si la opcion introducida por el usuario no es ninguna de las anteriores informamos al usuario de que no es valida
        case _:
            print("The option entered is not valid")