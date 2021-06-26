from agenda import Agenda
from entrada import Entrada
#Menu de opciones

agenda = Agenda()#Objeto de la clase Agenda

#Se llama al metodo para cargar la lista, con la informacion que hay en la agenda
agenda.cargar_agenda()

while True:#Menu de opciones
    print("\n\tMENU DE OPCIONES\n")
    print("(1) AGREGAR ESTUDIANTE")
    print("(2) MOSTRAR LISTA DE ESTUDIANTES")
    print("(3) BUSCAR ESTUDIANTE")
    print("(4) ELIMINAR ESTUDIANTE")
    print("(0) SALIR")

    opc = input("\n-> ")

    if opc == '1':
        agenda.agregar_registro()


    if opc == '2':
        agenda.mostrarListaAlumnos()


    if opc == '3':
        print("\n\tBUSCAR ALUMNO")
        print("\n(1) Buscar por nombre")
        print("(2) Buscar por código")
                
        op = input("-> ")
        print("\n")

        if op == '1':
            print("\tBUSCAR ALUMNO POR NOMBRE\n")

            nombre = input("Digita el nombre del alumno a buscar: ")
            apellido = input("Digita el apellido del alumno a buscar: ")

            agenda.busqueda_por_nombre(nombre, apellido)

        if op == '2':
            print("\tBUSCAR ALUMNO POR CÓDIGO\n")

            codigo = input("Digita el código del alumno a buscar: ")
            agenda.buscar_por_codigo(codigo)


    if opc == '4':
        #Para copiar todo lo que hay en el archivo original, al de respaldo
        archivoOriginal = open("Estudiantes.txt", 'r')#Abrir el original en modo de lectura
        archivoRespaldo = open("RespaldoEstudiantes.txt", 'w')#Abrir el respaldo en modo de escritura

        for linea in archivoOriginal:
            archivoRespaldo.write(linea)#Copiar lo que tiene el archivo original al archivo de respaldo

        #Cerrar ambos archivos
        archivoOriginal.close()
        archivoRespaldo.close()

        print("\n\tELIMINAR ALUMNO")
        print("\n(1) Eliminar por nombre")
        print("(2) Eliminar por código")
                
        op = input("-> ")
        print("\n")

        if op == '1':
            print("\tELIMINAR ALUMNO POR NOMBRE\n")

            nombre = input("Digita el nombre del alumno a eliminar: ")
            apellido = input("Digita el apellido del alumno a eliminar: ")

            agenda.borrar_registro_NombreApellido(nombre, apellido)

        if op == '2':
            print("\tELIMINAR ALUMNO POR CÓDIGO\n")

            codigo = input("Digita el código del alumno a eliminar: ")
            agenda.borrar_registro_Codigo(codigo)
            

    if opc == '0':
        break
