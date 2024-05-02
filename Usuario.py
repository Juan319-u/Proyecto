'''
Este codigo fue creado el 1/05/2024
Creadores
-Juan Felipe Corrales Toro
-Edwin Daniel Martinez Gaviria
-Daniel Medina Julio
Ultima Actualizacion 1/05/2024
'''
from Estudiantes import Estudiante
from Empleado import Empleado
class Usuario():
    
    tipo_usuario=int
    codigo=int
    obj=Estudiante,Empleado
    def pedir_datos(self):
        d=1
        while d == 1:
            try:
                self.tipo_usuario = int(input("1 Estudiante \n2 Empleado\n "))
        
                if self.tipo_usuario == 1:
                    self.obj = Estudiante()
                    self.obj.pedir_estudiante_datos()
                    self.codigo = self.obj.codigo
                    d = 2
                elif self.tipo_usuario == 2:
                    self.obj = Empleado()
                    self.obj.pedir_empleado_datos()
                    self.codigo = self.obj.codigo
                    d = 2
                else:
                    print("Error al registrar")
            except ValueError:
                print("Por favor, ingresa un número entero.")



