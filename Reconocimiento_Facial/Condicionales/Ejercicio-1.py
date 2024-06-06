#Ejercicio 1

n1 = int(input("Ingrese un número: "))
n2 = int(input("Ingrese otro número: "))

if n1 % 2 == 0 and n2 % 2 == 0:
    print("Ambos son pares")

elif n1 % 2 == 0 and n2 % 2 != 0:
    print(f"{n1} es un numero par")

elif n1 % 2 != 0 and n2 % 2 == 0:
    print(f"{n2} es un numero par")

else:
    print("Ninguno de los dos es par")