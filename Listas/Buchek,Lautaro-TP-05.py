#Ejercicio 1
lista = list(range(4, 100, 4))

#Ejercicio 2
lista = [1, 2, 3, 4, 5]
print(lista[-2])

#Ejercicio 3
lista = []
lista.append("Hola", "Mundo", "Chau")
lista.append("Mundo")
lista.append("Chau")
print(lista)

#Ejercicio 4
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[-1] = "oso"
print(animales)

#Ejercicio 5
#El programa primero inicializa una lista compuesta por cinco números.
#Con el método remove borra un item de la lista, en este caso el número más grande (con el método max())
#Finalmente, hace un print con la actualizada, que ahora tendrá únicamente 4 elementos.

#Ejercicio 6
lista = list(range(10, 31, 5))
print(lista[0:2])

#Ejercicio 7
autos = ["sedan", "polo", "suran", "gol"]
autos[1] = "golf"
autos[2] = "nivus"

#Ejercicio 8
dobles = []
dobles.append(10)
dobles.append(20)
dobles.append(30)
print(dobles)

#Ejercicio 9
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")
print(compras)

#Ejercicio 10 
lista_anidada = [[15], [True], [25.5, 57.9, 30.6], [False]]
print(lista_anidada)