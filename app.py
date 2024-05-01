import numpy as np
from Usuario import Usuario
from Estudiantes import Estudiante
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

    def __init__(self):
        # Se inicializa el arreglo de objetos con el valor None en todas su casillas
        self.usuario = np.full((self.MAX_USUARIOS), fill_value=None, dtype=object)
        self.material = np.full((self.MAX_USUARIOS), fill_value=None, dtype=object)

        # Cuando se crea la aplicación el número de usuarios y materiales es de cero
        self.cont_material = 0
        self.cont_usuario = 0

    def buscador(self):
        x = input("ingrese el titulo")
        for i in range(len(self.material)):
            if (Material.tiutlo == x):
                return i

    def buscador_usuario(self):
        x = input("ingrese su codigo")
        for i in range(len(self.usuario)):
            if (self.usuario.codigo == x):
                return i

    def procesar(self):
        # Esta variable nos ayuda a controlar el menú
        menu = int
        menu = 0

        while (menu >= 0 & menu < 7):
            print("\n*************************************\nBiblioteca Garage-U - Menú de opciones\n*************************************")
            print("1. Registrar un usuario \n2. ingresaar nuevo material  \n3. Buscar un recurso  \n4. prestar unrecurso \n5. lista de recursos prestados \n6. lista de recursos po tipo o coleccion  \n7. salir del programa ")
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
                    x = int(input("ingrese 1 para buscar por codigo o 2 para buscar por titulo"))
                    if (x == 1):
                        c = int(input("ingrese el codigo del material que quiere prestar"))
                        for i in range(len(self.material)):
                           if (Material.codigo == c):
                                print(f"resultado: ")
                                print(f"numero de inventario: {Material.numero_inventario}")
                                print(f"titulo: {Material.titulo}")
                                print(f"asignatura topografica: {self.material.asignatura_topografica}")
                                print(f"coleccion: {Material.coleccion}")
                                print(f"estado: {Material.estado}")
                                print(f"tipo de material: {Material.tipo_material}")
                                if (Material.tipo_material == 1):#libro
                                    print(f"autor: {Material.autor}")
                                    print(f"ISBN: {Material.isbn}" )
                                    print(f"Autor: {Material.autor}")
                                    print(f"numero de edicion {Material.num_edicion}")
                                elif (Material.tipo_material == 2):#video
                                    print(f"productor: {Material.productor}")
                                    print(f"Director: {Material.director}" )
                                    print(f"año de grabacion: {Material.año_grabacion}")
                                    print(f"genero: {Material.genero}")
                                elif (Material.tipo_material == 4):#audios
                                    print(f"Material: {Material.cantante}")
                                    print(f"Productor: {Material.productor}" )
                                    print(f"Año de grabacion: {Material.año_grabacion}")
                                elif (Material.tipo_material == 3):#revista
                                    print(f"ISSN: {Material.issn}")
                                    print(f"Editorial: {Material.editorial}")
                                    print(f"Volumen: {Material.volumen}")
                                    print(f"Numero: {Material.numero}")
                                    print(f"Año de publicacion: {Material.año_publicacion}")
                    elif (self.x==2):
                        self.c = int(input("ingrese el titulo del material que quiere prestar"))
                        for i in range(len(self.material)):
                           if (Material.titulo == c):
                                print(f"resultado: ")
                                print(f"numero de inventario: {Material.numero_inventario}")
                                print(f"titulo: {Material.titulo}")
                                print(f"asignatura topografica: {self.material.asignatura_topografica}")
                                print(f"coleccion: {Material.coleccion}")
                                print(f"estado: {Material.estado}")
                                print(f"tipo de material: {Material.tipo_material}")
                                if (Material.tipo_material == 1):#libro
                                    print(f"autor: {Material.autor}")
                                    print(f"ISBN: {Material.isbn}" )
                                    print(f"Autor: {Material.autor}")
                                    print(f"numero de edicion {Material.num_edicion}")
                                elif (Material.tipo_material == 2):#video
                                    print(f"productor: {Material.productor}")
                                    print(f"Director: {Material.director}" )
                                    print(f"año de grabacion: {Material.año_grabacion}")
                                    print(f"genero: {Material.genero}")
                                elif (Material.tipo_material == 4):#audios
                                    print(f"Material: {Material.cantante}")
                                    print(f"Productor: {Material.productor}" )
                                    print(f"Año de grabacion: {Material.año_grabacion}")
                                elif (Material.tipo_material == 3):#revista
                                    print(f"ISSN: {Material.issn}")
                                    print(f"Editorial: {Material.editorial}")
                                    print(f"Volumen: {Material.volumen}")
                                    print(f"Numero: {Material.numero}")
                                    print(f"Año de publicacion: {Material.año_publicacion}")
                case 4:
                    x = self.buscador(self)
                    y = self.buscador_usuario(self)
                    m = Material()

                    if (self.material[x].estado == 1 & self.usuario[y].tipo_usuario == 1):#estudiante
                        m.prestar_material()
                    elif (self.material[x].estado == 1 & self.usuario[y].tipo_usuario == 2):#empleado
                        m.presar_material()
                    else:
                        print("error, el recurso no esta disponible para prestar")
                case 5:
                    print("los materiales que han sido prestados son: ")
                    for i in range(len(self.material)):
                        if (self.material[i].estado == 2):#prestado
                            print(f"numero de inventario: {self.material[i].num_inventario}")
                            print(f"titulo: {self.material[i].titulo}")
                            print(f"Usuario que lo posee: {self.material[i].codigo_prestamo}")#como sabemos que usuario lo presto?
                case 6:#Generar un listado por tipo de recurso o por colección en el que se debe mostrar el título del recurso, su  signatura topográfica y su estado.
                    x = int(input("1 para una lista por tipo de recurso y 2 para una lista por coleccion"))
                    if (x == 1 or x == 2):
                        if(x==1):
                            y = int(input("de que tipo quiere hacer la lista: \n1 para libro \n2 para video \n3 para revista \n4 para audio"))
                            match (y):
                                case 1:
                                    for i in range(len(self.material)):
                                        if(self.material[i].tipo_material == 1):
                                            print(f"titulo: {self.material[i].titulo}")
                                            print(f"asignatura topografica: {self.material[i].asignatura_topografica}")
                                            print(f"estado: {self.material[i].estado}")
                                case 2:
                                    for i in range(len(self.material)):
                                        if(self.material[i].tipo_material == 2):
                                            print(f"titulo: {self.material[i].titulo}")
                                            print(f"asignatura topografica: {self.material[i].asignatura_topografica}")
                                            print(f"estado: {self.material[i].estado}")
                                case 3:
                                    for i in range(len(self.material)):
                                        if(self.material[i].tipo_material == 3):
                                            print(f"titulo: {self.material[i].titulo}")
                                            print(f"asignatura topografica: {self.material[i].asignatura_topografica}")
                                            print(f"estado: {self.material[i].estado}")
                                case 4:
                                    for i in range(len(self.material) == 4):
                                        if(self.material[i].tipo_material == 1):
                                            print(f"titulo: {self.material[i].titulo}")
                                            print(f"asignatura topografica: {self.material[i].asignatura_topografica}")
                                            print(f"estado: {self.material[i].estado}")
                case 7:
                    print("Programa Finalizado")
                    break