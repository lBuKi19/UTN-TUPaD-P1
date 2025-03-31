#TRABAJO PRÁCTICO 1 - TECNICATURA EN PROGRMACIÓN - BUCHEK, LAUTARO

#Ejercicio 1
print ("Hola mundo")

#Ejercicio 2
nombre = input("Escribe tu nombre: ")
print (f"Hola {nombre}!")

#Ejercicio 3
nombre = input("Escribe tu nombre: ")
apellido = input("Escribe tu apellido: ")
edad = input("Escribe tu edad: ")
residencia = input("Escribe tu lugar de residencia: ")

print (f"Soy {nombre} {apellido}, tengo {edad} y vivo en {residencia}")

#Ejercicio 4
import math
radio = input("Ingrese el radio de un circulo: ")
area = math.pi * (float(radio) ** 2)
perimetro = (2 * math.pi) * float(radio)

print (f"El area es igual a {area} y el perimetro es {perimetro}")

#Ejercicio 5
segundos = input("Ingrese una cantidad de segundos: ")
hs =int(segundos) / 3600

print (f"La cantidad de segundos equivale a {hs} horas")

#Ejercicio 6
num = input("Ingrese un numero: ")
num = int(num)
for x in range(1, 11):
    resultado = x * num
    print (f"{num} x {x} = {resultado}")

#Ejercicio 7
num, num1 = 0, 0

while num == 0:
    num = int( input("Ingrese un numero entero: "))

while num1 == 0:
    num1 = int(  input("Ingrese otro numero entero: "))

suma = num + num1
resta = num - num1
m = num * num1
d = num / num1

print(f"La suma entre los numeros ingresados es {suma}")  
print(f"La resta entre los numeros ingresados es {resta}")  
print(f"El producto entre los numeros ingresados es {m}")  
print(f"La division entre los numeros ingresados es {d}")  

#Ejercicio 8
altura =  float( input("Ingrese su altura: "))
peso = float(input("Ingrese su peso: "))
imc = peso / (altura ** 2)

print(f"Su indice de masa corporal es {imc}")  

#Ejercicio 9
gradosC = float(input("Ingrese una temperatura en grados Celsius: "))
gradosF = gradosC * (9/5) + 32

print(f"La temperatura ingresada equivale a {gradosF} grados Fahrenheit")   

#Ejercicio 10
n1 = float(input("Ingrese un numero: "))
n2 = float(input("Ingrese un segundo numero: "))
n3 = float(input("Ingrese un tercer numero: "))
promedio = (n1 + n2 + n3) / 3
print(f"El promedio entre los numeros ingresados es {promedio}")  
 