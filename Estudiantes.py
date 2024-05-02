class Estudiante():
    programa_academico=str
    codigo=int

    def __init__(self,programa_academico="",codigo=0):
        self.programa_academico=programa_academico
        self.codigo=codigo
    
    def pedir_estudiante_datos(self):
        self.programa_academico=input(f"Ingresa tu programa academico ")
        self.codigo=int(input(f"Codigo\n "))