'''
Autores:
Juan Felipe Corrales Toro
Edwin Daniel Martinez Gaviria
ultima modificacion 03/06/2024
'''
import numpy as np
from libro import Libro
from video import Video
from audio import Audio
from revista import Revista
from usuario import Usuario
from prestar import Prestar
from estudiante import Estudiante
from empleado import Empleado
from material import Material


class App():
    '''Este bloque sirve para inicializar los array que vamos a utilizar para almacenar nuestros objetos'''
    materiales = np.ndarray 
    usuarios = np.ndarray
    cont_material = int
    cont_usario = int
    '''aqui le damos lo parametros a usar'''
    MAX_USUARIOS = 50
    MAX_MATERIALES = 100
    MAX_PRESTADOS = 100

    def __init__ (self):
        self.usuarios = np.full((self.MAX_USUARIOS), fill_value=Usuario, dtype=Usuario)
        self.materiales = np.full((self.MAX_MATERIALES), fill_value=Material, dtype=Material)
        self.cont_material = 0
        self.cont_usuario = 0
    
    def cargar_datos(self):
        '''Cargar los datos de los arreglos desde un archivo npz'''
        try:
            data = np.load('datos.npz', allow_pickle=True)
            self.materiales = data['materiales']
            self.usuarios = data['usuarios']
            self.cont_material = data['cont_material'].item()
            self.cont_usuario = data['cont_usuario'].item()
            print("Datos cargados exitosamente")
        except FileNotFoundError:
            print("No se encontró el archivo de datos. Se iniciará con arreglos vacíos.")

    def crear_nuevo_material(self):
            '''este metodo nos sirve para crear los nuevos materiales
            esta funcion va ser llamada mas adelante'''
            material = Material()
            tipo_de_material = int
            while True:
                try:
                    tipo_de_material=int(input("1) para libro \n2) para video \n3) para revista \n4) para audio\n"))
                    match tipo_de_material:
                        case 1:
                            x=Libro()
                            x.pedir_datos()
                            x.pedir_datos_h()
                            material = x
                            break
                        case 2:
                            x=Video()
                            x.pedir_datos()
                            x.pedir_datos_h()
                            material = x
                            break
                        case 3:
                            x=Revista()
                            x.pedir_datos()
                            x.pedir_datos_h()
                            material = x
                            break
                        case 4:
                            x=Audio()
                            x.pedir_datos()
                            x.pedir_datos_h()
                            material = x

                            break
                        case _:
                            print("Error ")
                except:
                    print("Error ")
            return material
    
    def crear_nuevo_usuario(self):
            '''este metodo tiene la funcion de crear los nuevos usuarios y almacenarlos en el arreglo
            al igual que el metodo anterior'''
            usuario = Usuario()
            while True:
                try:
                    self.tipo_usuario=int(input("1) para Estudiante \n2) para Empleado\n"))
                    match(self.tipo_usuario):
                        case 1:
                            estudiante=Estudiante()
                            estudiante.pedir_datos()
                            estudiante.pedir_datos_estudiante()
                            estudiante.tipo_usuario=1
                            usuario = estudiante
                            break
                        case 2:
                            empleado=Empleado()
                            empleado.pedir_datos()
                            empleado.pedir_datos_empleado()
                            empleado.tipo_usuario=2
                            usuario = empleado
                            break
                        case _:
                            print("Error ")
                except:
                    print("Error ")
            
            return usuario
    def buscador(self):
        '''este metodo sirve para buscar los materiales en el array materiales '''
        try:
            x = input("ingrese el titulo \n")
            for i in range(0,len(self.materiales),1):
                if (self.materiales[i].titulo == x):
                    return i
                else:
                    return -1
        except:
            print("Error")

    def buscador_usuario(self):
        '''este metodo sirve para buscar los usuarios en el array usuarios'''
        try:
            x = int(input("ingrese su codigo \n"))
            for i in range(0,len(self.usuarios),1):
                if (self.usuarios[i].codigo == x):
                    return i
                else:
                    return -1
        except:
            print("Error")
    
    def procesar(self):#metodo principal de la app con un menu y diferentes metodos para cumplir los requerimientos 

        # Esta variable nos ayuda a controlar el menú
        menu = int
        menu = 0
        self.cargar_datos()
        try:
            while (menu!=8):# en esta parte pedimos que el ciclo continue a excepcion de que el user marque la opcion 8
                        print("\n*************************************\nBiblioteca Garage-U - Menú de opciones\n*************************************")
                        print("1. Registrar un usuario \n2. ingresar nuevo material  \n3. Buscar un recurso  \n4. prestar un recurso \n5. lista de recursos prestados \n6. lista de recursos por tipo o coleccion  \n7. actualizar estado \n8. salir del programa ")
                        menu = int(input("Seleccione una opción del menú: \n"))
                        match(menu):
                            case 1:
                                if (self.cont_usuario < self.MAX_USUARIOS):
                                    # Se crea un objeto consulta
                                    usuario = self.crear_nuevo_usuario()
                                    # Se almacena la consulta al arreglo
                                    self.usuarios[self.cont_usuario] = usuario
                                    # Se aumenta el contador de consultas
                                    self.cont_usuario += 1
                                    print("Usuario Registrado Correctamente")
                            case 2:
                                if (self.cont_material < self.MAX_MATERIALES):
                                    # Se crea un objeto consulta
                                    material = self.crear_nuevo_material()
                                    # Se almacena la consulta al arreglo
                                    self.materiales[self.cont_material] = material
                                    # Se aumenta el contador de consultas
                                    self.cont_material += 1
                                    print("Material Registrado Correctamente")
                            case 3:
                                x = int(input("ingrese 1 para buscar por numero de inventario o 2 para buscar por titulo \n"))
                                if (x == 1):
                                    c = int(input("ingrese el numero de inventario que quiere buscar \n"))
                                    for i in range(0,len(self.materiales),1):#con este ciclo buscamos en todas las opciones del arreglo
                                        if (self.materiales[i].numero_inventario == c):#validamos la coincidencia del titulo con lo escrito por el user 
                                            print("\n")
                                            print(f"resultado: ")
                                            print(f"numero de inventario: {self.materiales[i].numero_inventario}")
                                            print(f"titulo: {self.materiales[i].titulo}")
                                            print(f"asignatura topografica: {self.materiales[i].asignatura_topografica}")
                                            print(f"coleccion: {self.materiales[i].coleccion}")
                                            print(f"estado: {self.materiales[i].estado}")
                                            print(f"tipo de material: {self.materiales[i].tipo_de_material}")
                                            if (self.materiales[i].tipo_de_material == 1):#libro
                                                print(f"ISBN: {self.materiales[i].isbn}" )
                                                print(f"Autor: {self.materiales[i].autor}")
                                                print(f"numero de edicion {self.materiales[i].numero_edicion}")
                                            elif (self.materiales[i].tipo_de_material == 2):#video
                                                print(f"productor: {self.materiales[i].productor}")
                                                print(f"Director: {self.materiales[i].director}" )
                                                print(f"año de grabacion: {self.materiales[i].año_grabacion}")
                                                print(f"genero: {self.materiales[i].genero}")
                                            elif (self.materiales[i].tipo_de_material == 4):#audios
                                                print(f"Material: {self.materiales[i].cantante}")
                                                print(f"Productor: {self.materiales[i].productor}" )
                                                print(f"Año de grabacion: {self.materiales[i].año_grabacion}")
                                            elif (self.materiales[i].tipo_de_material == 3):#revista
                                                print(f"ISSN: {self.materiales[i].issn}")
                                                print(f"Editorial: {self.materiales[i].editorial}")
                                                print(f"Volumen: {self.materiales[i].volumen}")
                                                print(f"Numero: {self.materiales[i].numero}")
                                                print(f"Año de publicacion: {self.materiales[i].año_publicacion}")
                                    #else:
                                        #print("el material no esta disponible actualmente en la Biblioteca")
                                elif (x==2):
                                    c = input("ingrese el titulo del material que quiere buscar \n")
                                    for i in range(0,len(self.materiales),1):
                                        if (c == self.materiales[i].titulo):
                                            print("\n")
                                            print(f"resultado: ")
                                            print(f"numero de inventario: {self.materiales[i].numero_inventario}")
                                            print(f"titulo: {self.materiales[i].titulo}")
                                            print(f"asignatura topografica: {self.materiales[i].asignatura_topografica}")
                                            print(f"coleccion: {self.materiales[i].coleccion}")
                                            print(f"estado: {self.materiales[i].estado}")
                                            print(f"tipo de material: {self.materiales[i].tipo_de_material}")
                                            if (self.materiales[i].tipo_de_material == 1):#libro
                                                print(f"ISBN: {self.materiales[i].isbn}" )
                                                print(f"Autor: {self.materiales[i].autor}")
                                                print(f"numero de edicion {self.materiales[i].numero_edicion}")
                                            elif (self.materiales[i].tipo_de_material == 2):#video
                                                print(f"productor: {self.materiales[i].productor}")
                                                print(f"Director: {self.materiales[i].director}" )
                                                print(f"año de grabacion: {self.materiales[i].año_grabacion}")
                                                print(f"genero: {self.materiales[i].genero}")
                                            elif (self.materiales[i].tipo_de_material == 4):#audios
                                                print(f"Material: {self.materiales[i].cantante}")
                                                print(f"Productor: {self.materiales[i].productor}" )
                                                print(f"Año de grabacion: {self.materiales[i].año_grabacion}")
                                            elif (self.materiales[i].tipo_de_material == 3):#revista
                                                print(f"ISSN: {self.materiales[i].issn}")
                                                print(f"Editorial: {self.materiales[i].editorial}")
                                                print(f"Volumen: {self.materiales[i].volumen}")
                                                print(f"Numero: {self.materiales[i].numero}")
                                                print(f"Año de publicacion: {self.materiales[i].año_publicacion}")     
                            case 4:
                                x = self.buscador()
                                y = self.buscador_usuario()
                                prestar = Prestar()
                                dias_prestamo = int
                                p = str

                                if (self.materiales[x].estado == 1 & self.usuarios[y].tipo_usuario == 1):#estudiante, verificamos estado y otorgamos la fecha de devolucion
                                    self.materiales[x].c_usuario = self.usuarios[y].codigo
                                    if (self.materiales[x].coleccion == 1):
                                        p = prestar.fecha(dias_prestamo=15)
                                        self.materiales[x].fecha_devolucion = p
                                        self.materiales[x].estado = 2
                                        print(f"debes devolver el material en la sigueinte fecha: {p}")
                                    elif (self.materiales[x].coleccion == 2):
                                        p = prestar.fecha(dias_prestamo=1)
                                        self.materiales[x].fecha_devolucion = p
                                        self.materiales[x].estado = 2
                                        print(f"debes devolver el material en la sigueinte fecha: {p}")
                                    elif (self.materiales[x].coleccion == 3):
                                        p = prestar.fecha(dias_prestamo=3)
                                        self.materiales[x].fecha_devolucion = p
                                        self.materiales[x].estado = 2
                                        print(f"debes devolver el material en la sigueinte fecha: {p}")
                                elif (self.materiales[x].estado == 1 & self.usuarios[y].tipo_usuario == 2):#empleado, verificamos estado y otorgamos la fecha de devolucion
                                    self.materiales[x].c_usuario = self.usuarios[y].codigo
                                    if (self.materiales[x].coleccion == 1):
                                        p = prestar.fecha(dias_prestamo=30)
                                        self.materiales[x].fecha_devolucion = p
                                        self.materiales[x].estado = 2
                                        print(f"debes devolver el material en la sigueinte fecha: {p}")
                                    elif (self.materiales[x].coleccion == 2):
                                        p = prestar.fecha(dias_prestamo=15)
                                        self.materiales[x].fecha_devolucion = p
                                        self.materiales[x].estado = 2
                                        print(f"debes devolver el material en la sigueinte fecha: {p}")
                                    elif (self.materiales[x].coleccion == 3):
                                        p = prestar.fecha(dias_prestamo=22)
                                        self.materiales[x].fecha_devolucion = p
                                        self.materiales[x].estado = 2
                                        print(f"debes devolver el material en la sigueinte fecha: {p}")
                                else:
                                    print("error, el recurso no esta disponible para prestar")   
                            case 5:
                                print("los materiales que han sido prestados son: ")
                                for i in range(len(self.materiales)):
                                    if (self.materiales[i].estado == 2):#prestado
                                        print(f"numero de inventario: {self.materiales[i].numero_inventario}")
                                        print(f"el usuario que lo posee: {self.materiales[i].c_usuario}")
                                        print(f"titulo: {self.materiales[i].titulo}")
                                        print(f"Sera devuelto en la fecha {self.materiales[i].fecha_devolucion}\n")
                            case 6:
                                x = int(input("1 para una lista por tipo de recurso y 2 para una lista por coleccion \n"))
                                if (x == 1 or x == 2):
                                    
                                    if(x==1):
                                        y = int(input("de que tipo quiere hacer la lista: \n1 para libro \n2 para video \n3 para revista \n4 para audio \n"))
                                        match (y):
                                            case 1:
                                                for i in range(len(self.materiales)):
                                                    if(self.materiales[i].tipo_de_material== 1):
                                                        print(f"titulo: {self.materiales[i].titulo}")
                                                        print(f"asignatura topografica: {self.materiales[i].asignatura_topografica}")
                                                        print(f"estado: {self.materiales[i].estado}")
                                            case 2:
                                                for i in range(len(self.materiales)):
                                                    if(self.materiales[i].tipo_de_material == 2):
                                                        print(f"titulo: {self.materiales[i].titulo}")
                                                        print(f"asignatura topografica: {self.materiales[i].asignatura_topografica}")
                                                        print(f"estado: {self.materiales[i].estado}")
                                            case 3:
                                                for i in range(len(self.materiales)):
                                                    if(self.materiales[i].tipo_de_material == 3):
                                                        print(f"titulo: {self.materiales[i].titulo}")
                                                        print(f"asignatura topografica: {self.materiales[i].asignatura_topografica}")
                                                        print(f"estado: {self.materiales[i].estado}")
                                            case 4:
                                                for i in range(len(self.materiales) == 4):
                                                    if(self.materiales[i].tipo_de_material == 1):
                                                        print(f"titulo: {self.materiales[i].titulo}")
                                                        print(f"asignatura topografica: {self.materiales[i].asignatura_topografica}")
                                                        print(f"estado: {self.materiales[i].estado}")
                                    elif(x==2):
                                        y = int(input("de que coleccion quiere hacer la lista: \n1 para general \n2 para reserva \n3 para hemeroteca\n"))
                                        match (y):
                                            case 1:
                                                for i in range(len(self.materiales)):
                                                    if(self.materiales[i].coleccion == 1):
                                                        print(f"titulo: {self.materiales[i].titulo}")
                                                        print(f"asignatura topografica: {self.materiales[i].asignatura_topografica}")
                                                        print(f"estado: {self.materiales[i].estado}")
                                            case 2:
                                                for i in range(len(self.materiales)):
                                                    if(self.materiales[i].coleccion == 2):
                                                        print(f"titulo: {self.materiales[i].titulo}")
                                                        print(f"asignatura topografica: {self.materiales[i].asignatura_topografica}")
                                                        print(f"estado: {self.materiales[i].estado}")
                                            case 3:
                                                for i in range(len(self.materiales)):
                                                    if(self.materiales[i].coleccion == 3):
                                                        print(f"titulo: {self.materiales[i].titulo}")
                                                        print(f"asignatura topografica: {self.materiales[i].asignatura_topografica}")
                                                        print(f"estado: {self.materiales[i].estado}")
                                else:
                                    print("error")

                            case 7:
                                x = int(input("ingrese \n1. para devolver un recurso, \n2. para enviarlo a reparacion, \n3. para eliminarlo del inventario \n"))
                                if (x == 1):
                                    y = self.buscador()
                                    self.materiales[y].estado = 1
                                    self.materiales[y].fecha_devolucion = ""
                                    self.materiales[y].c_usuario = 0
                                    print("el estado del material ya ah sido actualizado con exito")
                                elif (x == 2):
                                    y = self.buscador()
                                    self.materiales[y].estado = 3
                                    print("el estado del material ya ah sido actualizado con exito")
                                elif (x == 3):
                                    y = self.buscador()
                                    self.materiales[y] = object
                                    print("el material ah sido eliminado del inventario correctamente")
                            case 8:
                                print("Programa Finalizado")
                                np.savez('datos.npz', materiales=self.materiales, usuarios=self.usuarios, cont_material=self.cont_material, cont_usuario=self.cont_usuario)
                                break
                            case _:
                                print("Error de seleccion ")
        except:
            print("Error ")


p1=App()
p1.procesar()
