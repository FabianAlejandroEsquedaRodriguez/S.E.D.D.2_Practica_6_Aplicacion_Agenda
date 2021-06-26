
#Clase Entrada -> Estudiante
class Entrada:
    def __init__(self,nombre="", apellido="", codigo="", carrera=""):
        self.__nombreA = nombre
        self.__apellidoA = apellido
        self.__codigo_carrera = codigo
        self.__carreraA = carrera


    @property
    def nombre(self):
        return self.__nombreA

    @property
    def apellido(self):
        return self.__apellidoA

    @property
    def codigo(self):
        return self.__codigo_carrera

    @property
    def carrera(self):
        return self.__carreraA

    def leer_entrada(self, archivoAgregar):
        print("\n\tAGREGAR ESTUDIANTE\n")

        nombre = input("NOMBRE: ")
        apellido = input("APELLIDO: ")
        codigo = input("CÓDIGO: ")
        carrera = input("CARRERA: ")

        estudiante = Entrada(nombre, apellido, codigo, carrera)

        archivoAgregar.write('\n')
        archivoAgregar.write(nombre)
        archivoAgregar.write('\n')
        archivoAgregar.write(apellido)
        archivoAgregar.write('\n')
        archivoAgregar.write(codigo)
        archivoAgregar.write('\n')
        archivoAgregar.write(carrera)
        archivoAgregar.write('\n')

        return estudiante

    def imprimirAlumnos(self):
        print("NOMBRE: ", self.__nombreA)
        print("APELLIDO: ", self.__apellidoA)
        print("CÓDIGO: ", self.__codigo_carrera)
        print("CARRERA: ", self.__carreraA)
        print("\n")