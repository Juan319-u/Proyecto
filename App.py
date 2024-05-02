'''
Este codigo fue creado el 1/05/2024
Creadores
-Juan Felipe Corrales Toro
-Edwin Daniel Martinez Gaviria
-Daniel Medina Julio
Ultima Actualizacion 1/05/2024
'''
import numpy as np
from Usuario import Usuario
from Estudiante import Estudiante
from Empleado import Empleado
from Fechas import fechas
from Material import Material
class AppBiblioteca:

    material = np.ndarray
    usuario = np.ndarray

    cont_material = int
    cont_usario = int

    # Estas constantes indica el tope de usuarios y material que se pueden almacenar
    MAX_USUARIOS = 50
    MAX_MATERIALES = 100
    MAX_PRESTADOS = 100

    def __init__(self): #Este metodo tiene la finaliza de construir los dos arreglos principales para la app
        # Se inicializa el arreglo de objetos con el valor None en todas su casillas
        self.usuario = np.full((self.MAX_USUARIOS), fill_value=Usuario, dtype=object)
        self.material = np.full((self.MAX_MATERIALES), fill_value=Material, dtype=object)

        # Cuando se crea la aplicación el número de usuarios y materiales es de cero
        self.cont_material = 0
        self.cont_usuario = 0


    def buscador(self):#Este metodo busca apartir de un titulo dado la coincidencia los titulos de los objetos guardados
        try:
            x = input("ingrese el titulo ")
            for i in range(0,len(self.material),1):
                if (self.material[i].titulo == x):
                    self.codigo_prestador=x
                    return i
        except:
            print("Error")

    def buscador_usuario(self):#Este metodo busca apartir de un codigo la coincidencia con los codigos de los objetos guardados
        try:
            x = int(input("ingrese su codigo "))
            for i in range(0,len(self.usuario),1):
                if (self.usuario[i].codigo == x):
                    return i
        except:
            print("Error")

    def procesar(self):#metodo principal de la app con un menu y diferentes metodos para cumplir los requerimientos 

        # Esta variable nos ayuda a controlar el menú
        menu = int
        menu = 0

        while (menu!=8):# en esta parte pedimos que el ciclo continue a excepcion de que el user marque la opcion 8
                print("\n*************************************\nBiblioteca Garage-U - Menú de opciones\n*************************************")
                print("1. Registrar un usuario \n2. ingresar nuevo material  \n3. Buscar un recurso  \n4. prestar un recurso \n5. lista de recursos prestados \n6. lista de recursos por tipo o coleccion  \n7. actualizar estado \n8. salir del programa ")
                try:# con este try intentamos evitar errores del usuario
                    menu = int(input("Seleccione una opción del menú: "))
                    match(menu):

                        case 1:
                            # Se verifica si hay capacidad para almacenar nuevos usuarios
                            if (self.cont_usuario < self.MAX_USUARIOS):
                                # Se crea un objeto consulta
                                nuevo_usuario = Usuario()
                                # Se piden los datos de la consulta
                                nuevo_usuario.pedir_datos()
                                # Se almacena la consulta al arreglo
                                self.usuario[self.cont_usuario] = nuevo_usuario
                                # Se aumenta el contador de consultas
                                self.cont_usuario += 1
                                input("Usuario Registrado Correctamente")

                        case 2:
                            if (self.cont_material < self.MAX_MATERIALES):
                                # Se crea un objeto consulta
                                nuevo_material = Material()
                                # Se piden los datos de la consulta
                                nuevo_material.crear_nuevo_material()
                                # Se almacena la consulta al arreglo
                                self.material[self.cont_material] = nuevo_material
                                # Se aumenta el contador de consultas
                                self.cont_material += 1
                                input("Material Registrado Correctamente")


                        case 3:
                            x = int(input("ingrese 1 para buscar por numero de inventario o 2 para buscar por titulo "))
                            if (x == 1):
                                c = input("ingrese el numero de inventario que quiere prestar ")
                                for i in range(0,len(self.material),1):#con este ciclo buscamos en todas las opciones del arreglo
                                    if (self.material[i].numero_inventario == c):#validamos la coincidencia del titulo con lo escrito por el user 
                                        print("\n")
                                        print(f"resultado: ")
                                        print(f"numero de inventario: {self.material[i].numero_inventario}")
                                        print(f"titulo: {self.material[i].titulo}")
                                        print(f"asignatura topografica: {self.material[i].asignatura_topografica}")
                                        print(f"coleccion: {self.material[i].coleccion}")
                                        print(f"estado: {self.material[i].estado}")
                                        print(f"tipo de material: {self.material[i].tipo_de_material}")
                                        if (self.material[i].tipo_de_material == 1):#libro
                                            print(f"ISBN: {self.material[i].isbn}" )
                                            print(f"Autor: {self.material[i].autor}")
                                            print(f"numero de edicion {self.material[i].numero_edicion}")
                                        elif (self.material[i].tipo_de_material == 2):#video
                                            print(f"productor: {self.material[i].productor}")
                                            print(f"Director: {self.material[i].director}" )
                                            print(f"año de grabacion: {self.material[i].año_grabacion}")
                                            print(f"genero: {self.material[i].genero}")
                                        elif (self.material[i].tipo_de_material == 4):#audios
                                            print(f"Material: {self.material[i].cantante}")
                                            print(f"Productor: {self.material[i].productor}" )
                                            print(f"Año de grabacion: {self.material[i].año_grabacion}")
                                        elif (self.material[i].tipo_de_material == 3):#revista
                                            print(f"ISSN: {self.material[i].issn}")
                                            print(f"Editorial: {self.material[i].editorial}")
                                            print(f"Volumen: {self.material[i].volumen}")
                                            print(f"Numero: {self.material[i].numero}")
                                            print(f"Año de publicacion: {self.material[i].año_publicacion}")
                                else:
                                        print("el material no esta disponible actualmente en la Biblioteca")
                            elif (x==2):
                                c = input("ingrese el titulo del material que quiere prestar ")
                                for i in range(0,len(self.material),1):
                                    if c == self.material[i].titulo:
                                        print("\n")
                                        print(f"resultado: ")
                                        print(f"numero de inventario: {self.material[i].numero_inventario}")
                                        print(f"titulo: {self.material[i].titulo}")
                                        print(f"asignatura topografica: {self.material[i].asignatura_topografica}")
                                        print(f"coleccion: {self.material[i].coleccion}")
                                        print(f"estado: {self.material[i].estado}")
                                        print(f"tipo de material: {self.material[i].tipo_de_material}")
                                        if (self.material[i].tipo_de_material == 1):#libro
                                            print(f"ISBN: {self.material[i].isbn}" )
                                            print(f"Autor: {self.material[i].autor}")
                                            print(f"numero de edicion {self.material[i].numero_edicion}")
                                        elif (self.material[i].tipo_de_material == 2):#video
                                            print(f"productor: {self.material[i].productor}")
                                            print(f"Director: {self.material[i].director}" )
                                            print(f"año de grabacion: {self.material[i].año_grabacion}")
                                            print(f"genero: {self.material[i].genero}")
                                        elif (self.material[i].tipo_de_material == 4):#audios
                                            print(f"Material: {self.material[i].cantante}")
                                            print(f"Productor: {self.material[i].productor}" )
                                            print(f"Año de grabacion: {self.material[i].año_grabacion}")
                                        elif (self.material[i].tipo_de_material == 3):#revista
                                            print(f"ISSN: {self.material[i].issn}")
                                            print(f"Editorial: {self.material[i].editorial}")
                                            print(f"Volumen: {self.material[i].volumen}")
                                            print(f"Numero: {self.material[i].numero}")
                                            print(f"Año de publicacion: {self.material[i].año_publicacion}")
                                else:
                                        print("el material no esta disponible actualmente en la Biblioteca")
                        case 4:
                            x = self.buscador()
                            y = self.buscador_usuario()

                            if (self.material[x].estado == 1 & self.usuario[y].tipo_usuario == 1):#estudiante, verificamos estado y otorgamos la fecha de devolucion
                                self.material[x].prestar_material(self.material[x].tipo_de_material,self.material[x].coleccion)
                            elif (self.material[x].estado == 1 & self.usuario[y].tipo_usuario == 2):#empleado, verificamos estado y otorgamos la fecha de devolucion
                                self.material[x].prestar_material(self.material[x].tipo_de_material,self.material[x].coleccion)
                            else:
                                print("error, el recurso no esta disponible para prestar")
                        case 5:
                            print("los materiales que han sido prestados son: ")
                            for i in range(len(self.material)):
                                if (self.material[i].estado == 2):#prestado
                                    print(f"numero de inventario: {self.material[i].numero_inventario}")
                                    print(f"el usuario que lo posee: {self.usuario[y].codigo}")
                                    print(f"titulo: {self.material[i].titulo}")
                                    print(f"Sera devuelvo en la fecha {self.material[i].fecha_inicial}\n")
                        case 6:#Generar un listado por tipo de recurso o por colección en el que se debe mostrar el título del recurso, su  signatura topográfica y su estado.
                            x = int(input("1 para una lista por tipo de recurso y 2 para una lista por coleccion \n"))
                            if (x == 1 or x == 2):
                                if(x==1):
                                    y = int(input("de que tipo quiere hacer la lista: \n1 para libro \n2 para video \n3 para revista \n4 para audio \n"))
                                    match (y):
                                        case 1:
                                            for i in range(len(self.material)):
                                                if(self.material[i].tipo_de_material == 1):
                                                    print(f"titulo: {self.material[i].titulo}")
                                                    print(f"asignatura topografica: {self.material[i].asignatura_topografica}")
                                                    print(f"estado: {self.material[i].estado}")
                                        case 2:
                                            for i in range(len(self.material)):
                                                if(self.material[i].tipo_de_material == 2):
                                                    print(f"titulo: {self.material[i].titulo}")
                                                    print(f"asignatura topografica: {self.material[i].asignatura_topografica}")
                                                    print(f"estado: {self.material[i].estado}")
                                        case 3:
                                            for i in range(len(self.material)):
                                                if(self.material[i].tipo_de_material == 3):
                                                    print(f"titulo: {self.material[i].titulo}")
                                                    print(f"asignatura topografica: {self.material[i].asignatura_topografica}")
                                                    print(f"estado: {self.material[i].estado}")
                                        case 4:
                                            for i in range(len(self.material) == 4):
                                                if(self.material[i].tipo_de_material == 1):
                                                    print(f"titulo: {self.material[i].titulo}")
                                                    print(f"asignatura topografica: {self.material[i].asignatura_topografica}")
                                                    print(f"estado: {self.material[i].estado}")
                        case 7:
                            x = int(input("ingrese 1. para devolver un recurso, 2. para enviarlo a reparacion, 3. para eliminarlo del inventario "))
                            if (x == 1):
                                y = self.buscador()
                                self.material[y].estado = 1
                                print("el estado del material ya ah sido actualizado con exito")
                            elif (x == 2):
                                y = self.buscador()
                                self.material[y].estado = 3
                                print("el estado del material ya ah sido actualizado con exito")
                            elif (x == 3):
                                y = self.buscador()
                                self.material[y] = object
                                print("el material ah sido eliminado del inventario correctamente")
                        case 8:
                            print("Programa Finalizado")
                            break
                        case _:
                            print("Error de seleccion ")
                except:
                    print("Error")

inventario=AppBiblioteca()
inventario.procesar()