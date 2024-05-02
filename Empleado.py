'''
Este codigo fue creado el 1/05/2024
Creadores
-Juan Felipe Corrales Toro
-Edwin Daniel Martinez Gaviria
-Daniel Medina Julio
Ultima Actualizacion 1/05/2024
'''
class Empleado():#esta clase para crear el objeto empleado
    codigo=int
    dependencia=str
    año_ingreso=int

    def __init__(self,dependencia="",codigo=0,año_ingreso=-1):
        self.dependencia=dependencia
        self.codigo=codigo
        self.año_ingreso=año_ingreso

    def pedir_empleado_datos(self): # este metodo sirve para pedir los datos del objeto
        año_ingreso=-1
        self.codigo=int(input(f"Codigo\n "))
        self.dependencia=input("Dependencia\n ")
        while año_ingreso<=-1:
            año_ingreso=int(input("Año de ingreso\n "))
            if año_ingreso>=0:
                self.año_ingreso=año_ingreso
            else:
                print("Error")