#introduccion a listas 
#array.insert(2, "Baloncesto") inserta un elemento en una posicion determinada
#array.append(100) agrega un elemento al final de la lista
#array.extend([1,88,True,100]) agrega un bloque de datos al final de la lista
#array.remove(100) elimina un elemento de la lista
#array.pop(1) elimina un elemento en una posicion determinada
#array.clear() elimina todos los elementos de la lista
#array.index("Pc") devuelve la posicion de un elemento
#array.reverse() invierte la lista
#array.sort() ordena la lista de menor a mayor
#array.sort(reverse=True) ordena la lista de mayor a menor

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////

#print(array.index("Pc")) Busca el indice de un elemento
#print(array.count("Pc")) Cuenta cuantas veces aparece un elemento
#print("Pc" in array) busca si un elemento esta en la lista

array = ["Futbol", "Pc", 18.6, 18, [6,7,10.4], True, False]

print(array.count("Pc"))