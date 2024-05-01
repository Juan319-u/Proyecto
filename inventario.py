from Usuario import Usuario
class Inventario():
    obj=Usuario
    listado_empleados={}
    listado_estudiantes={}
    def listado(self):
        de=1
        while de==1:
            de=int(input("1) Agregar \n2)No\n"))
            if de==1:
                obj=Usuario()
                obj.pedirDatos()
                if self.obj.tipo_usuario==2:
                    self.listado_empleados.append(obj)
                else:
                    self.listado_estudiantes.append(obj)
            
    
    def mostrar(self):
        print(self.listado_empleados)
        print(self.listado_estudiantes)

p=Inventario()
p.listado()
p.mostrar()