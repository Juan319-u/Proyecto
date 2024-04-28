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
    fecha_final=date

    def fecha_inicial(self):
            while True:
                dia=int(input("ingresa el dia "))
                mes=int(input("ingresa el mes "))
                año=int(input("ingresa el año "))
                if 1 <= mes <= 12 and 1 <= dia <= 31 and año >= 0:
                    self.fecha_inicial=date(año,mes,dia)
                    break   
                else:
                    print("Error de fecha")

    def calcular_fecha_final(self):
        dias_prestamo = int(input("¿Cuántos días se le prestará? "))
        if dias_prestamo >= 0:
            fecha_final = self.fecha_inicial + timedelta(days=dias_prestamo)
            self.fecha_inicial=fecha_final
        else:
            print("Error en la cantidad de dias")