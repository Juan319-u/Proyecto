'''
Este codigo fue creado el 1/05/2024
Creadores
-Juan Felipe Corrales Toro
-Edwin Daniel Martinez Gaviria
-Daniel Medina Julio
Ultima Actualizacion 1/05/2024
'''
from datetime import date,timedelta
class fechas():
    fecha_inicial=date
    def Fecha_inicial(self,dias_prestamo): #este metodo sirve para pedirle al usuario la fecha que se realiza el prestamo y retornar la fecha de devolucion
            while True:
                dia=int(input("ingresa el dia "))
                mes=int(input("ingresa el mes "))
                año=int(input("ingresa el año "))
                if 1 <= mes <= 12 and 1 <= dia <= 31 and año >= 0:
                    self.fecha_inicial=date(año,mes,dia)
                    break
                else:
                    print("Error de fecha")

            if dias_prestamo >= 0:
                fecha_final = self.fecha_inicial + timedelta(days=dias_prestamo)
                fecha_final=str(fecha_final)
            else:
                print("Error en la cantidad de dias")
            return fecha_final
       