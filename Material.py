from datetime import date,timedelta
class Material():
    tipo_de_material=int
    numero_inventario=int
    titulo=str
    asignatura_topografica=str
    coleccion=int
    estado=int
    autor=str
    ISBN=int
    editorial=str
    numero_edicion=int
    productor=str
    director=str
    año_grabacion=int
    genero=int
    ISSN=int
    volumen=int
    año_publicacion=int
    numero_publicacion=int
    cantate=str
    fecha_inicial=date
    fecha_final=date

    def __init__(self):
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
                    self.director=input("productor ")
                    self.año_grabacion=int(input("año de grabacion "))
                    while True:
                        genero=int(input("1) para documental\n 2) para comedia\n 3) para terror\n 4)para accion\n"))
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
        if self.estado==1:#disponible
            pass
        elif self.estado==2:
            pass
