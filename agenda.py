
#Clase Agenda
from entrada import Entrada

class Agenda:
    def __init__(self):
        self.__estudiantes = []#Lista para almacenar estudiantes

    def agregar_registro(self):#Usar append
        archivoAgregar = open("Estudiantes.txt", 'a')

        e = Entrada()
        estudiante = e.leer_entrada(archivoAgregar)

        self.__estudiantes.append(estudiante)

        archivoAgregar.close()

    def mostrarListaAlumnos(self):
        print("\n\tALUMNOS REGISTRADOS\n")
        for estudiante in self.__estudiantes:
            estudiante.imprimirAlumnos()

    def buscar_por_codigo(self, codigoEntrada):
        # Esta haciendo una busqueda lineal directo en la lista
        encontrado = False
        for est in self.__estudiantes:
            if codigoEntrada == est.codigo:
                print("\n\tESTUDIANTE ENCONTRADO\n")
                print("Nombre: ", est.nombre)
                print("Apellido: ", est.apellido)
                print("Código: ", est.codigo)
                print("Carrera: ", est.carrera)
                encontrado = True
        
        if encontrado == False:
            print(f"\nEl alumno con el codigo {codigoEntrada}, no fue encontrado\n")

    def busqueda_por_nombre(self, nombreEnt, apellidoEnt):
        # Esta haciendo una busqueda lineal directo en la lista
        encontrado = False
        for est in self.__estudiantes:
            if (nombreEnt == est.nombre) and (apellidoEnt == est.apellido):
                print("\n\tESTUDIANTE ENCONTRADO\n")
                print("Nombre: ", est.nombre)
                print("Apellido: ", est.apellido)
                print("Código: ", est.codigo)
                print("Carrera: ", est.carrera)
                encontrado = True

        if encontrado == False:
            print(f"\nEl alumno con el nombre {nombreEnt} {apellidoEnt}, no fue encontrado\n")

    def cargar_agenda(self):#Recuperar desde el archivo
        archivoEntrada = open("Estudiantes.txt", 'r')

        for e in archivoEntrada:
            nombre = archivoEntrada.readline().replace("\n", "")#Reemplaza los saltos de linea por una espacio en blanco
            apellido = archivoEntrada.readline().replace("\n", "")
            codigo = archivoEntrada.readline().replace("\n", "")
            carrera = archivoEntrada.readline().replace("\n", "")

            e = Entrada(nombre, apellido, codigo, carrera)
            self.__estudiantes.append(e)
        
        archivoEntrada.close()

    def borrar_registro_Codigo(self, codigoEliminar):
        encontrado = False
        for est in self.__estudiantes:
            if codigoEliminar == est.codigo:
                print("\n\tESTUDIANTE ENCONTRADO PARA ELIMINAR\n")
                print("Nombre: ", est.nombre)
                print("Apellido: ", est.apellido)
                print("Código: ", est.codigo)
                print("Carrera: ", est.carrera)
                encontrado = True

                self.__estudiantes.remove(est)#Eliminar el registro encontrado en la lista
        
        archivoR = open("RespaldoEstudiantes.txt", 'w')#Abrr el respaldo en modo de escritura
        for e in self.__estudiantes:
            #Escribir en el respaldo la lista de estudiantes, una vez sea eliminado el que queremos
            archivoR.write('\n')
            archivoR.write(e.nombre+'\n')
            archivoR.write(e.apellido+'\n')
            archivoR.write(e.codigo+'\n')
            archivoR.write(e.carrera+'\n')

        archivoR.close()
    
        if encontrado == False:
            print(f"\nEl alumno con el nombre {codigoEliminar}, no fue encontrado\n")
        else:
            #Abrir el respaldo en modo de lectura 
            archivoResp = open("RespaldoEstudiantes.txt", 'r')
            #Abrir el original en modo de escritura
            archivoOrig = open("Estudiantes.txt", 'w')
            #Copiar lo del respaldo al original
            for lineaR in archivoResp:
                archivoOrig.write(lineaR)
            
            #Cerrar los archivos
            archivoOrig.close()
            archivoResp.close()

            print("\nAlumno eliminado...")

    def borrar_registro_NombreApellido(self, nombreEliminar, apellidoEliminar):
        encontrado = False
        for est in self.__estudiantes:
            if (nombreEliminar == est.nombre) and (apellidoEliminar == est.apellido):
                print("\n\tESTUDIANTE ENCONTRADO PARA ELIMINAR\n")
                print("Nombre: ", est.nombre)
                print("Apellido: ", est.apellido)
                print("Código: ", est.codigo)
                print("Carrera: ", est.carrera)
                encontrado = True

                self.__estudiantes.remove(est)#Eliminar el registro encontrado en la lista
        
        archivoR = open("RespaldoEstudiantes.txt", 'w')#Abrr el respaldo en modo de escritura
        for e in self.__estudiantes:
            #Escribir en el respaldo la lista de estudiantes, una vez sea eliminado el que queremos
            archivoR.write('\n')
            archivoR.write(e.nombre+'\n')
            archivoR.write(e.apellido+'\n')
            archivoR.write(e.codigo+'\n')
            archivoR.write(e.carrera+'\n')

        archivoR.close()

        if encontrado == False:
            print(f"\nEl alumno con el nombre {nombreEliminar} {apellidoEliminar}, no fue encontrado\n")
        else:
            #Abrir el respaldo en modo de lectura 
            archivoResp = open("RespaldoEstudiantes.txt", 'r')
            #Abrir el original en modo de escritura
            archivoOrig = open("Estudiantes.txt", 'w')
            #Copiar lo del respaldo al original
            for lineaR in archivoResp:
                archivoOrig.write(lineaR)
            
            #Cerrar los archivos
            archivoOrig.close()
            archivoResp.close()

            print("\nAlumno eliminado...")
