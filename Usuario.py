'''
Este codigo fue creado el 28/04/2024
Creadores
-Juan Felipe Corrales Toro
-Edwin
-Daniel
Ultima Actualizacion 28/04/2024
'''
from Estudiantes import Estudiante
from Empleado import Empleado
class Usuario():
    tipo_usuario=int
    obj=object
    def pedir_datos(self):
        
        while True:

            self.tipo_usuario=int(input(f"1 Estudiante \n2 Empleado\n "))
            if self.tipo_usuario==1:
               self.obj=Estudiante()
               self.obj.pedir_datos()
            elif self.tipo_usuario==2:
                self.obj=Empleado()
                self.obj.pedir_datos()
            else:
                print("Error al registrar")
