'''
Autores:
Juan Felipe Corrales Toro
Edwin Daniel Martinez Gaviria
ultima modificacion 03/06/2024
'''
class Usuario():
    codigo=int
    tipo_usuario=int

    def __init__(self,codigo=0):
        self.codigo=codigo

    def pedir_datos(self):
        while True:
            try:
                self.codigo=int(input("Ingresa el codigo \n"))
                break
            except:
                print("Error ")
