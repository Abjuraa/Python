#Ejercicio 2

saldo = 2000

print("1. Ingreso de dinero")
print("2. Retiro de dinero")
print("3. Mostrar saldo")
print("4. Salir")

seleccion = int(input("Elija una opción: "))

if seleccion == 1:
    ingreso = float(input("Dinero a ingresar: "))
    saldo = saldo + ingreso
    print(f"El saldo actual es: {saldo}")
elif seleccion == 2:
    salida = float(input("Dinero a retirar: "))
    if salida > saldo:
        print("Saldo insuficiente")
    else:
        saldo = saldo - salida
        print(f"El saldo actual es: {saldo}")
elif seleccion == 3:
    print(f"Saldo disponible {saldo}")
elif seleccion == 4:
    print("Hasta pronto")
else:
    print("Opcion incorrecta")