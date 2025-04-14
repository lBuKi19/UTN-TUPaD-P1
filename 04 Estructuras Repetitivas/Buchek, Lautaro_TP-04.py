#PRÁCTICO 4 - ESTRUCTURAS REPETITIVAS - Buchek, Lautaro

#Ejercicio 1
for i in range(1, 101):
    print(i)


#Ejercicio 2
num = input("Ingrese un número entero: ")
print(len(num))


#Ejercicio 3
min = int(input("Ingrese un valor mínimo: "))
max = int(input("Ingrese un valor máximo: "))
sum = 0
for i in range(min+1, max):
    sum += i

print(sum)


#Ejercicio 4  
check = 1
sum = 0
while check != 0:
    num = int(input("Ingrese un número entero: "))
    sum += num
    check = num 

print(f"El total acumulado es {sum}")


#Ejercicio 5
from random import randint
intentos = 0
check = 100
random = randint(0, 9)
while check != random:
    check = int(input("Adivine el número aleatorio entre 0 y 9: "))
    intentos += 1
print(f"Has intentado {intentos} veces para adivinar el número")


#Ejercicio 6
for i in range(100, 0, -2):
    print(i)


#Ejercicio 7
check, sum = 0, 0
while check <= 0:
    num = int(input("Ingrese un número entero positivo: "))
    check = num 
for i in range(num):
    sum += i
print(f"La suma de los valores comprendidos entre 0 y el valor ingresado es {sum}")


#Ejercicio 8
pos, neg, par, impar = 0, 0, 0, 0
for i in range(100):
    num = int(input("Ingrese un número entero: "))
    if num > 0:
        pos += 1
    elif num < 0:
        neg += 1
    #otra estrucutura condicional ya que sino el programa cuenta una sola condicion(ej. es positivo, pero a la vez no sera par/impar)
    if num % 2 == 0 and num != 0:
        par += 1
    elif num != 0:
        impar += 1

print(f"La cantidad de números positivos ingresados es {pos}")
print(f"La cantidad de números negativos ingresados es {neg}")
print(f"La cantidad de números pares ingresados es {par}")
print(f"La cantidad de números impares ingresados es {impar}")


#Ejercicio 9
media = 0
valor = 100
for i in range(valor):
    num = int(input("Ingrese un número entero: "))
    media += num
media = media / valor
print(f"La media de los valores ingresados es {media}")


#Ejercicio 10
num = input("Ingrese un número")
invertido = ""
for i in range(len(num)-1, -1, -1):
    #utilizando solo digitos en caso de que el ususario ingrese un num con decimales
    if num[i].isnumeric():
        invertido += num[i]

print(int(invertido))
     
    
