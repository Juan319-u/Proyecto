'''
Este codigo fue creado el 28/04/2024
Creadores
-Juan Felipe Corrales Toro
-Edwin
-Daniel
Ultima Actualizacion 28/04/2024
'''
from datetime import date,timedelta
class fechas():
    fecha_inicial=date
    def Fecha_inicial(self,dias_prestamo):
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
       