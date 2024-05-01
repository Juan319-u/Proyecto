from datetime import date,timedelta
from Fechas import fechas
class Material():
    tipo_de_material=int
    numero_inventario=int
    titulo=str
    asignatura_topografica=str
    coleccion=int
    genero=int
    autor=str
    ISBN=int
    editorial=str
    numero_edicion=int
    productor=str
    director=str
    año_grabacion=int
    ISSN=int
    volumen=int
    año_publicacion=int
    numero_publicacion=int
    cantate=str
    fecha_inicial=str
    fecha_final=str

    def __init__(self,titulo="",codigo=0,estado=1,tipo_material=0):
        self.titulo=titulo
        self.codigo=codigo
        self.estado=estado
        self.tipo_de_material=tipo_material
        pass

    def crear_nuevo_material(self):
        self.estado=1
        self.numero_inventario=int(input("Numero de inventario "))
        self.titulo=input("Titulo ")
        self.asignatura_topografica=input("Asignatura topografica ")
        while True:
            coleccion=int(input("1) General \n2) Reserva \n3)Hemeroteca \n"))
            match coleccion:
                case 1:
                    self.coleccion=coleccion
                    break
                case 2:
                    self.coleccion=coleccion
                    break
                case 3:
                    self.coleccion=coleccion
                    break
                case _:
                    print("Error")

        while True:
            self.tipo_de_material=int(input("1) para libro\n 2) para video\n 3) para revista\n 4) para audio\n"))
            match self.tipo_de_material:
                case 1:
                    self.autor=input("Autor ")
                    self.ISBN=input("ISBN ")
                    self.editorial=input("Editorial ")
                    self.numero_edicion=int(input("Numero de edicion "))
                    break

                case 2:
                    self.productor=input("productor ")
                    self.director=input("director ")
                    self.año_grabacion=int(input("año de grabacion "))
                    while True:
                        genero=int(input("1) para documental \n2) para comedia \n3) para terror \n4)para accion\n"))
                        match genero:
                            case 1:
                                self.genero=genero
                                break
                            case 2:
                                self.genero=genero
                                break
                            case 3:
                                self.genero=genero
                                break
                            case 4:
                                self.genero=genero
                                break
                            case _: print("Error")
                    break
                case 3:
                    self.editorial=input("editorial ")
                    self.ISSN=int(input("ISSN "))
                    self.volumen=int(input("volumen "))
                    self.año_publicacion=int(input("Año de publicacion "))
                    self.numero_publicacion=int(input("Numero de publicacion "))
                    break
                case 4:
                    self.cantate=input("cantante ")
                    self.productor=input("productor ")
                    self.año_grabacion=int(input("año de grabacion "))
                    break
                case _:
                    print("Error ")

    def prestar_material(self):
        while True:
            if self.estado==1:#disponible
                print("Disponible para prestar ")
                

                while True:#organizar
                    tipo=int(input("1 Estudiante \n2 Empleado\n "))
                    coleccion=int(input("1) General \n2) Reserva \n3)Hemeroteca \n"))
                    if tipo==1:
                        while True:
                            if coleccion==1:
                                self.fecha_inicial=fechas.Fecha_inicial(self,15)
                                self.estado=2
                            elif coleccion==2:
                                self.fecha_inicial=fechas.Fecha_inicial(self,1)
                                self.estado=2
                            elif coleccion==3:
                                self.fecha_inicial=fechas.Fecha_inicial(self,3)
                                self.estado=2
                            else:
                                print("Error ")
                            break
                    elif tipo==2:
                        while True:
                            if coleccion==1:
                                self.fecha_inicial=fechas.Fecha_inicial(self,30)
                                self.estado=2
                            elif coleccion==2:
                                self.fecha_inicial=fechas.Fecha_inicial(self,15)
                                self.estado=2
                            elif coleccion==3:
                                self.fecha_inicial=fechas.Fecha_inicial(self,3)
                                self.estado=2
                            else:
                                print("Error ")
                    else:
                        print("Error ")
                
                    print(f"debes devolver el articulo en la fecha {self.fecha_inicial}")
                    break
                break
            elif self.estado==2:#prestado
                print(f"El articulo ya esta prestado y sera devuelto {self.fecha_final}")
            elif self.estado==3:#reparacion
                print("El articulo se encuentra reparando ")
            elif self.estado==4:#Inactivo
                print("El articulo fue eliminado ")
            else:
                print("Error")
