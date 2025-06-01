#Ejercicio1
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

num = int(input("Ingrese un número entero:"))
for i in range(1, num):
    print(f"El factorial de {i} es {factorial(i)} ")


#Ejercicio2
def fibonacci(n):
    if n in resultados:
        return resultados[n]
    else:
        resultados[n] = fibonacci(n-1)+ fibonacci(n-2)
        return resultados[n]
      
resultados = {0: 0, 1: 1}
n = int(input("Ingrese el valor de la serie de fibonacci:"))
print(fibonacci(n))
position = int(input("Ingrese la posicion hasta que desea mostrar la serie:"))
print([fibonacci(n) for n in range(position)])


#Ejercicio3
def potencia(base, exponente):
    global res
    if base == 0 or base == 1:
        return base
    elif exponente > 0:
        res *= base
        return potencia(base, exponente-1)
    return res
res = 1
base = int(input("Ingrese un número entero:"))
exponente = int(input("Ingrese un exponente entero:"))
print(potencia(base, exponente))
    

#Ejercicio4
ls =[]
def num_to_binary(num):
    if num != 0:
        ls.append(num%2)
        return num_to_binary(num//2)
    else:
        return "".join(map(str,ls[::-1]))

num = int(input("Ingrese un numero en base decimal:"))
print(f"El numero equivale a {num_to_binary(num)} en base binaria")


#Ejercicio5
def es_palindromo(palabra):
    global invertida, length
    invertida += palabra[length]
    if length == 0:
        if palabra == invertida:
            return True
        else:
            return False
    else:
        length -= 1
        return es_palindromo(palabra)

palabra = input("Ingrese una palabra:")
length = len(palabra)-1
invertida = ''
print(es_palindromo(palabra))


#Ejercicio6
def suma_digitos(n):
    global suma
    suma += n % 10
    if n % 10 == n:
        return suma
    return suma_digitos(n//10)
    
n = int(input("Ingrese un número:"))
suma = 0
print(suma_digitos(n))


#Ejercicio7
def contar_bloques(n):
    if n == 1 or n == 0:
        return n
    else:
        return n + contar_bloques(n-1)

n = int(input("Ingrese el número de bloques:"))
print(contar_bloques(n))


#Ejercicio8
def contar_digito(numero, digito):
    global count
    if numero >= 1 and digito in range(0, 10): 
        if numero % 10 == digito:           
            count += 1
        if numero % 10 == numero:
            return count
        return contar_digito(numero // 10, digito)
    else:
        return("Ingrese valores válidos")
    
count = 0
numero = int(input("Ingrese un número entero positivo:"))
digito = int(input("Ingrese un dígito del 0-9:")) 
print(contar_digito(numero, digito))