from libro import Libro
from video import Video
from audio import Audio
from revista import Revista
from usuario import Usuario
from prestar import Prestar
from estudiante import Estudiante
from empleado import Empleado


class App(Libro,Video,Audio,Revista,Prestar):

    def crear_nuevo_material(self):
            while True:
                try:
                    self.tipo_de_material=int(input("1) para libro \n2) para video \n3) para revista \n4) para audio\n"))
                    match self.tipo_de_material:
                        case 1:
                            material=Libro()
                            material.pedir_datos()
                            material.pedir_datos_h()
                            break
                        case 2:
                            material=Video()
                            material.pedir_datos()
                            material.pedir_datos_h()
                            break
                        case 3:
                            material=Revista()
                            material.pedir_datos()
                            material.pedir_datos_h()
                            break
                        case 4:
                            material=Audio()
                            material.pedir_datos()
                            material.pedir_datos_h()
                            break
                        case _:
                            print("Error ")
                except:
                    print("Error ")

p1=App()
p1.crear_nuevo_material()
print(p1.tipo_de_material)