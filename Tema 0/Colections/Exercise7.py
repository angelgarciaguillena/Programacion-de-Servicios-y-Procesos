#Creamos un diccionario que almacenara los contactos del usuario
agenda = {}

#Creamos una variable para almacenar la opcion del usuario
option = 0

#Creamos una funcion que se encargara de mostrar el menu de opciones
def menu():
    print("Menu:")
    print("1. Add contact")
    print("2. Delete contact")
    print("3. Search contact")
    print("4. Exit")

#Creamos una funcion para pedir el nombre del contacto al usuario
def ask_name():

    #Pedimos al usuario que introduzca el nombre del contacto
    name = input("Introduce the name of the contact: ")

    #Devolvemos el nombre del contacto
    return name

#Creamos una funcion para pedir el telefono del contacto al usuario
def ask_phone():

    #Pedimos al usuario que introduzca el telefono del contacto
    phone = input("Introduce the phone of the contact: ")

    #Devolvemos el numero de telefono del contacto
    return phone

#Creamos una funcion para añadir un contacto a la agenda
def add_contact(name, phone):

    #Creamos una variable para almacenar si el contacto se ha añadido o no
    added = False

     #Si el contato no se encuentra en la agenda lo añadimos
    if name not in agenda:

        #Añadimos el contacto al diccionario
        agenda[name] = phone

        #Asignamos que el contacto se ha añadido
        added = True
    
    #Devolvemos si el contacto se ha añadido
    return added

#Creamos una funcion para eliminar un contacto de la agenda
def delete_contact(name):

    #Creamos una variable para almacenar si el contacto se ha eliminado o no
    removed = False

     #Si el contato se encuentra en la agenda lo eliminamos
    if name in agenda:

        #Eliminamos el contacto del diccionario
        del agenda[name]

        #Asignamos que el contacto se ha eliminado
        removed = True
    
    #Devolvemos si el contacto se ha eliminado
    return removed 

#Creamos un bucle while para que hasta que el usuario no desee salir seguir en el programa 
while option != 4:

    #Llamamos al menu de opciones
    menu()

    #Preguntamos al usuario que opcion desea
    option = int(input("Introduce a option: "))

    #Creamos un switch case para que depende de la opcion del usuario se realize una funcion u otra
    match option:

        #Si la opcion es 1 añadimos a un contacto
        case 1:

            #Llamamos a la funcion para obtener el nombre del contacto
            name = ask_name()

            #LLamamos a la funcion para obtener el telefono del contacto
            phone = ask_phone()

            #Llamamos a la funcion para añadir al contacto
            done = add_contact(name, phone)

            #Si se ha realizado informamos al usuario
            if done:

                #Informamos al usuario que se ha añadido el contacto
                print("The contact has been added to the agenda")

            #Si no se ha realizado informamos al usuario
            else:

                #Informamos al usuario que el contacto ya existe en la agenda
                print("The contact already exists in the agenda")

        #Si la opcion es 2 eliminamos a un contacto
        case 2:

            #Llamamos a la funcion para obtener el nombre del ucontacto
            name = ask_name()

            #Eliminamos el contacto del diccionario llamando a la funcion
            done = delete_contact(name)

            #Si se ha eliminado al contacto informamos al usuario
            if done:

                #Informamos al usuario que se ha eliminado el contacto
                print("The contact has been removed from the agenda")

            #Si no se ha eliminado informamos al usuario
            else:

                #Informamos al usuario que el contacto no existe en la agenda
                print("The contact does not exist in the agenda")

        #Si la opcion es 3 buscamos al contacto y mostramos la informacion
        case 3:

            #Llamamos a la funcion para obtener el nombre del contacto
            name = ask_name()

            #Si el nombre se encuentra en la agenda mostramos la informacion del contacto
            if name in agenda:
                
                #Mostramos el nombre del contacto
                print("Name:", name)

                #Mostramos el telefono del contacto
                print("Phone:", agenda[name])

            #Si el contacto no se encuentra en la agenda informamos al usuario
            else:
                
                #Informamos al usuario de que el contacto no se encuentra en la agenda
                print("The contact is not found in the agenda")

        #Si la opcion es 4 informamos al usuario de que ha salido del programa
        case 4:
            print("You have left the program")

        #Si la opcion introducida por el usuario no es ninguna de las anteriores informamos al usuario de que no es valida
        case _:
            print("The option entered is not valid")