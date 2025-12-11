import math
from datetime import datetime

    # definicion de variable

fecha_actual = datetime.today()
fecha_actual2 = datetime.now()
print("Fecha actual:", fecha_actual2.strftime("%d/%m/%Y %H:%M:%S"))
ventas_colombia = float(input("Ingrese las ventas de Colombia: "))
ventas_peru = float(input("Ingrese las ventas de Peru: "))
ventas_ecuador = float(input("Ingrese las ventas de Ecuador: "))
ventas_venezuela = float(input("Ingrese las ventas de Venezuela: "))

    # operaciones matematicas basicas

total_ventas = ventas_ecuador + ventas_peru + ventas_colombia + ventas_venezuela
promedio_ventas = total_ventas / 4
if ventas_colombia > 15000000: 
    print("¡Las ventas en Colombia superan los 15 millones!")
else:
    print("Las ventas en Colombia no superan los 15 millones.")
    # mostrar resultados

print("___________________________________________  ")
print("El total de las ventas de todos los paises es:", total_ventas)
print("El promedio de las ventas de todos los paises es:", promedio_ventas)
print("___________________________________________  ")
print("El total de ventas de Colombia es:", ventas_colombia)
print("El total de ventas de Venezuela es:", ventas_venezuela)
print("El total de ventas de Peru es:", ventas_peru)
print("El total de ventas de Ecuador es:", ventas_ecuador)
print("___________________________________________  ")
print("La mayor de las ventas es:", max(ventas_colombia, ventas_ecuador, ventas_peru, ventas_venezuela))
print("La menor de las ventas es:", min(ventas_colombia, ventas_ecuador, ventas_peru, ventas_venezuela))
print("___________________________________________  ")
print("Redondeando las ventas de Venezuela:", round(ventas_venezuela, 2))
print("Redondeando las ventas de Ecuador:", round(ventas_ecuador, 2))
print("Redondeando las ventas de Peru:", math.ceil(ventas_peru))
print("Redondeando las ventas de Peru con Floor:", math.floor(ventas_peru))
print("Ventas de Colombia en formato entero:", int(ventas_colombia))
