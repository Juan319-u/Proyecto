'''
Este codigo fue creado el 1/05/2024
Creadores
-Juan Felipe Corrales Toro
-Edwin Daniel Martinez Gaviria
-Daniel Medina Julio
Ultima Actualizacion 1/05/2024
'''
class Estudiante():#esta clase para crear el objeto empleado
    programa_academico=str
    codigo=int

    def __init__(self,programa_academico="",codigo=0):
        self.programa_academico=programa_academico
        self.codigo=codigo
    
    def pedir_estudiante_datos(self):# este metodo sirve para pedir los datos del objeto
        self.programa_academico=input(f"Ingresa tu programa academico ")
        self.codigo=int(input(f"Codigo\n "))