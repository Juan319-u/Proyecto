from material import Material
class Audio(Material):
    tipo_de_material=int
    cantate=str
    productor=str
    año_grabacion=int

    def __init__(self, titulo="", asignatura_topografica="", numero_inventario=0, estado=1,coleccion=0,tipo_de_material=4):
        super().__init__(titulo=titulo, asignatura_topografica=asignatura_topografica, numero_inventario=numero_inventario, estado=estado,coleccion=coleccion)
        self.tipo_de_material=tipo_de_material

    def pedir_datos_h(self):
            self.cantate=input("cantante ")
            self.productor=input("productor ")
            while True:
                try:
                    self.año_grabacion=int(input("año de grabacion "))
                    if self.año_grabacion>10000:
                        print("Error numero mayor a 10000")
                    else:
                        break
                except:
                    print("Error")
