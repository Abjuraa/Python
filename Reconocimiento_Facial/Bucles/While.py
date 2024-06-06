#Bucle while
import math

numero = int(input('Escriba un numero: '))

while numero < 0:
    print('Ingrese un numero positivo')
    numero = int(input('Escriba un numero: '))

print(f"El resultado de la raiz cuadrda es: {math.sqrt(numero):.2f}")