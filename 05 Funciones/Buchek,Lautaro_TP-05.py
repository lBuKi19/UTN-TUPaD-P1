#Ejercicio 1
def imprimir_hola_mundo():
    print("hola mundo")
imprimir_hola_mundo()


#Ejercicio 2
def saludar_usuario(nombre):
    print(f"Hola {nombre}")
nombre = input("Ingrese su nombre:")
saludar_usuario(nombre)


#Ejercicio 3
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")
nombre = input("Ingrese su nombre:")
apellido = input("Ingrese su apellido:")
edad = input("Ingrese su edad:")
residencia = input("Ingrese su lugar de residencia:")
informacion_personal(nombre, apellido, edad, residencia)


#Ejercicio 4
import math
def calcular_area_circulo(radio):
    return math.pi * (radio**2)
def calcular_perimetro_circulo(radio):
    return (2*math.pi)* radio

radio = float(input("Ingrese un radio:"))
print(f"El area es {calcular_area_circulo(radio)}")
print(f"El perimetro es {calcular_perimetro_circulo(radio)}")


#Ejercicio 5
def segundos_a_horas(segundos):
    return segundos / 60
segundos = float(input("Ingrese una cantidad de segundos:"))
print(f"Los segundos equivalen a {segundos_a_horas(segundos)} horas")


#Ejercicio 6
def tabla_multiplicar(numero):
    for i in range (1,11):
        print(f"{numero}x{i} = {numero*i}")
numero = float(input("Ingrese un número:"))
tabla_multiplicar(numero)


#Ejercicio 7
def operaciones_basicas(a, b):
    tupla = []
    tupla.append(a + b)
    tupla.append(a - b)
    tupla.append(a * b)
    tupla.append(a / b)
    return tuple(tupla)
a = float(input("Ingrese un número:"))
b = float(input("Ingrese otro número:"))
operaciones = ["suma", "resta", "multiplicación", "división"]
tup = operaciones_basicas(a, b)
for i in range(len(tup)):
    print(f"El resultado de la {operaciones[i]} es {tup[i]}")


#Ejercicio 8
def calcular_imc(peso, altura):
    return peso/(altura**2)

peso = float(input("Ingrese su peso en kilogramos:"))
altura = float(input("Ingrese su altura en metros:"))
print(f"El índice IMC es {calcular_imc(peso, altura)}")


#Ejercicio 9
def celsius_a_fahrenheit(celsius):
    return (celsius*(9/5)) + 32
celsius = float(input("Ingrese una temperatura en grados Celsius:"))
print(f"La temperatura equivale a {celsius_a_fahrenheit(celsius)} grados Fahrenheit")


#Ejercicio 10
def calcular_promedio(a, b, c):
    return (a+b+c) / 3
a = float(input("Ingrese un número:"))
b = float(input("Ingrese un segundo número:"))
c = float(input("Ingrese un tercer número:"))
print(f"El promedio entre los números es {calcular_promedio(a, b, c)}")