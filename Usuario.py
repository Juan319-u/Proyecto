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
    d=1
    tipo_usuario=int
    codigo=int
    obj=Estudiante,Empleado
    def pedir_datos(self):
        
        while self.d==1:

            self.tipo_usuario=int(input(f"1 Estudiante \n2 Empleado\n "))
            if self.tipo_usuario==1:
               self.obj=Estudiante()
               self.obj.pedir_estudiante_datos()
               self.codigo=self.obj.codigo
               self.d=2
            elif self.tipo_usuario==2:
                self.obj=Empleado()
                self.obj.pedir_empleado_datos()
                self.codigo=self.obj.codigo
                self.d=2
            else:
                print("Error al registrar")


