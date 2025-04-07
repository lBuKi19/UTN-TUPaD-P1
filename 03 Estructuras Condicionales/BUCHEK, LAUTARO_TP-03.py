#PRÁCTICO 3 - ESTTUCTURAS CONDICIONALES - Buchek, Lautaro

#Ejercicio 1
edad =int(input("Ingrese su edad: "))
if edad > 18:
    print("Es mayor de edad")


#Ejercicio 2
nota = float(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")


#Ejercicio 3
check = 1
#uso de loop hasta que el resto del módulo sea 0
while check == 1:
    num = int(input("Ingrese un numero par: "))
    check = num % 2
    if check == 0:
        print("Ha ingresado un número par")


#Ejercicio 4
edad =int(input("Ingrese su edad: "))
if edad < 12:
    print("El usuario pertenece a la categoría Niño")
elif edad >= 12 and edad < 18:
    print("El usuario pertenece a la categoría Adolescente")
elif edad >= 18 and edad < 30:
    print("El usuario pertenece a la categoría Adulto joven")
else:
    print("El usuario pertenece a la categoría Adulto")


#Ejercicio 5
check = 0
#uso de loop mientras contraseña sea de longitud incorrecta
while check < 8 or check > 14:
    contraseña = input("Ingrese una contraseña de entre 8 y 14 caracteres inclusive: ")
    check = len(contraseña)
    if check >= 8 and check <= 14:
        print("Ha ingresado una contraseña correcta")
    

#Ejercicio 6
import random
from statistics import mode, median, mean
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
mean_list = mean(numeros_aleatorios)
mode_list = mode(numeros_aleatorios)
median_list = median(numeros_aleatorios)
print(f"Mean = {mean_list}, Mode = {mode_list}, Median = {median_list}")
if mean_list > median_list and median_list > mode_list:
    print("Hay sesgo positivo")
elif mean_list < median_list and median_list < mode_list:
    print("Hay sesgo negativo")
elif mean_list == mode_list and mode_list == median_list:
    print("No hay sesgo")


#Ejercicio 7
string = input("Ingrese una palabra o frase: ")
vocal = ["a", "e", "i", "o", "u"]
#check si ultima letra del string esta en la lista de vocales
if (string[-1]).lower() in vocal:
    string = string + "!"

print(string)


#Ejercicio 8
nombre = input("Ingrese su nombre: ")
num = int(input("Ingrese 1, 2 o 3 según la opción que desee:\n 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. \n 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.\n  3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro : "))
if num == 1:
    print(nombre.upper())
elif num == 2:
    print(nombre.lower())
elif num == 3:
    print(nombre.title())


#Ejercicio 9
magnitud = float(input("Ingrese la magnitud de un terremoto: "))
if magnitud < 3:
    print("Muy leve")
elif magnitud >= 3 and magnitud < 4:
    print("Leve")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte")
elif magnitud >= 6 and magnitud < 7:
    print("Muy fuerte")
else:
    print("Extremo")


#Ejercicio 10
#importe de libreria para poder convertir input de usuario a formato fecha
from datetime import date  
hm = input("Ingrese en cuál hemisferio se encuentra (N/S): ")
mes = int(input("Ingrese el numero de mes (ej. 1=enero 2=febrero ...): "))
dia = int(input("Ingrese el día: "))
#incializo fecha compuesta por inputs ingresados, al no pedir año, ingreso valor arbitrario
fecha = date(2025, mes, dia)
#formato fecha en string para poder compararla con operadores relacionales
if fecha <= date(2025, 6, 20) and fecha >= date(2025, 3, 21):
    if hm.upper() == "N":
        print("El usuario se encuentra en primavera")
    else:
        print("El usuario se encuentra en otoño")
elif fecha <= date(2025, 9, 20) and fecha >= date(2025, 6, 21):
    if hm.upper() == "N":
        print("El usuario se encuentra en verano")
    else:
            print("El usuario se encuentra en invierno")
elif fecha <= date(2025, 12, 20) and fecha >= date(2025, 9, 21):
    if hm.upper() == "N":
        print("El usuario se encuentra en otoño")
    else:
        print("El usuario se encuentra en primavera")
else:
    #ultimo caso sin condicional if, (21/12 al 20/3) ya que al cruzar de diciembre a marzo, variaria el año y traeria problemas a la hora de comparar fechas
    if hm.upper() == "N":
        print("El usuario se encuentra en invierno")
    else:
        print("El usuario se encuentra en verano")




