'''
Autores:
Juan Felipe Corrales Toro
Edwin Daniel Martinez Gaviria
ultima modificacion 03/06/2024
'''
class Material():
    titulo=str
    asignatura_topografica=str
    numero_inventario=int
    estado=int
    coleccion=int
    fecha_devolucion=str
    c_usuario = int
    tipo_de_material=int
    
    def __init__(self, titulo="", asignatura_topografica="", numero_inventario=0, estado=1,coleccion=0, c_usuario = 0,fecha_devolucion="",tipo_de_material=0 ):
        self.titulo = titulo
        self.asignatura_topografica = asignatura_topografica
        self.numero_inventario = numero_inventario
        self.estado = estado
        self.coleccion=coleccion
        self.c_usuario = c_usuario
        self.fecha_devolucion = fecha_devolucion
        self.tipo_de_material=tipo_de_material
    def pedir_datos(self):
        self.titulo = input("Ingresa el titulo de la obra \n")
        self.asignatura_topografica = input("Ingresa la asignatura topografica de la obra \n")
        while True:
            try:
                self.numero_inventario = int(input("Ingresa el numero de inventario \n"))
                break
            except ValueError:
                print("Por favor, ingresa un número entero válido para el número de inventario.")
        while True:
                try:
                    coleccion=int(input("1) General \n2) Reserva \n3) Hemeroteca\n"))
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
                except:
                    print("Error ")
