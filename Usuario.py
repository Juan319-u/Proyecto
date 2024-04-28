'''
Este codigo fue creado el 28/04/2024
Creadores
-Juan Felipe Corrales Toro
-Edwin
-Daniel
Ultima Actualizacion 28/04/2024
'''

class Usuario(): #esta clase tiene la finalidad de manejar la creacion de usuarios y modificarlos
    tipo_usuario=int
    programa_academico=str
    codigo=int
    dependencia=str
    año_ingreso=int


    def __init__(self,tipo_usuario=0,programa_academico="",codigo=0,dependencia="",año_ingreso=0): #constructo con valores predeterminados a los atributos
        self.tipo_usuario=tipo_usuario
        self.programa_academico=programa_academico
        self.codigo=codigo
        self.dependencia=dependencia
        self.año_ingreso=año_ingreso
        pass

    def pedirDatos(self): #con esta funcion podemos modificar los datos de cada objeto
        año_ingreso=-1
        while True:

            self.tipo_usuario=int(input(f"1 Estudiante \n2 Empleado\n "))

            if self.tipo_usuario==1:
                self.programa_academico=input(f"Ingresa tu programa academico ")
                self.codigo=int(input(f"Codigo\n "))
                print("-----------------------------------------------------")
                print("Usuario registrado exitosamente!! ")
                break

            elif self.tipo_usuario==2:
                self.codigo=int(input(f"Codigo\n "))
                self.dependencia=input("Dependencia\n ")
                while año_ingreso<=-1:
                    año_ingreso=int(input("Año de ingreso\n "))
                    if año_ingreso>=0:
                        self.año_ingreso=año_ingreso
                    else:
                        print("Error")
                print("-----------------------------------------------------")
                print("Usuario registrado exitosamente!! ")
                break

            else:
                print("Error al registrar")

pepito=Usuario()
pepito.pedirDatos()