class Empleado():
    codigo=int
    dependencia=str
    año_ingreso=int

    def __init__(self,dependencia="",codigo=0,año_ingreso=-1):
        self.dependencia=dependencia
        self.codigo=codigo
        self.año_ingreso=año_ingreso

    def pedir_empleado_datos(self):
        año_ingreso=-1
        self.codigo=int(input(f"Codigo\n "))
        self.dependencia=input("Dependencia\n ")
        while año_ingreso<=-1:
            año_ingreso=int(input("Año de ingreso\n "))
            if año_ingreso>=0:
                self.año_ingreso=año_ingreso
            else:
                print("Error")