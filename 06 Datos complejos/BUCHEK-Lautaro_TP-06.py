#Ejercicio1
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

#Ejercicio2
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

#Ejercicio3
#lista que contenga solo las frutas
solo_frutas = list(precios_frutas.keys())


#Ejercicio4
numeros = {}
for i in range(1, 6):
    nombre = input(f"Ingrese el nombre del contacto {i}: ")
    telefono = int(input(f"Ingrese el número de teléfono del contacto {i}: "))
    numeros[nombre] = telefono
cual_nombre = input("Ingrese una persona de su lista de contactos: ")
if cual_nombre in numeros.keys():
    print(f"El número de {cual_nombre} es {numeros[cual_nombre]}")
else:
    print("El nombre ingresado no se encuentra en la lista de contactos")


#Ejercicio5
frase = (input("Ingrese una frase: ").split())
recuento = {}
for palabra in frase:
    if palabra not in recuento:
        recuento[palabra] = 1
    else:
        recuento[palabra] += 1

print(set(frase))
print(recuento)


#Ejercicio6
alumnos = {}
for i in range(1,4):
    alumno = input(f"Ingrese el nombre del alumno {i}:")
    notas = input(f"Ingrese tres notas del alumno {i} seguidas (ej.789): ")
    alumnos[alumno] = tuple(notas)
for i in alumnos.keys():
    promedio = 0
    for nota in alumnos[i]:
        promedio += int(nota)
    promedio /= 3
    print(f"El promedio de {i} es de {promedio}")


#Ejercicio7
list1 = []
list2 = []
aprobaron2 = []
aprobaron1 = []
for i in list1:
    if list1[i] in list2:
        aprobaron2.append(list1[i])
    else:
        aprobaron1.append(list1[i])
for i in list2:
    if list2[i] not in list1:
        aprobaron1.append(list2[i])
print(aprobaron1, aprobaron2)


#Ejercicio8
productos = {'remeras': 20, 'pantalones': 30, 'buzos': 15}
consulta = input("Ingrese el producto a consultar: ")
if consulta in productos.keys():
    print(f"El stock del producto ingresado es de {productos[consulta]} unidades")
    unidades = int(input(f"Cuantas unidades desea agregar de {consulta}: "))
    productos[consulta] += unidades
else:
    print("El producto no existe")
    nuevo_producto = input("Ingrese el producto que desea agregar: ")
    nuevo_producto_stock = int(input("Ingrese el stock del nuevo producto: "))
    productos[nuevo_producto] = nuevo_producto_stock
print(productos)


#Ejercicio9
agenda = {
    ("lunes", "10:00"): "Reunion",
    ("martes", "15:00"): "Clase 1",
    ("miercoles", "11:00"): "Clase 2",
}
consulta_actividad = input("Ingrese la actividad que desea consultar: ")


#Ejercicio10
original = {"Argentina": "buenos aires", "Chile": "santiago" , "Brasil": "brasilia"}
invertido = {}
for pais in original.keys():
    invertido[original[pais]] = pais
print(invertido)