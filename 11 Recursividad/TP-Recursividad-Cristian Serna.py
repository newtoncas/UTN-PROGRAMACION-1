#1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa función para calcular y mostrar en pantalla el factorial de todos los números enteros entre 1 y el número que indique el usuario

def factorial(n):
    if n == 0 or n == 1:    # Caso base: factorial de 0 o 1 es 1
        return 1
    else:                   # Caso recursivo: n! = n * (n-1)!
        return n * factorial(n - 1)
    
num = int(input("\nIngrese un número entero para calcular su factorial: "))     #Se solicita un número entero
fact = factorial(num)     #se llama a la funcion recursiva con el número ingresado

print(f"El factorial de {num} es: {fact}")      #Se muestra el factorial del número ingresado

#2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario especifique.

def fibonacci(n):
    if n == 0: return 0      # Caso base 1
    elif n == 1: return 1    # Caso base 2  
    else: return fibonacci(n-1) + fibonacci(n-2)  # Recursión

posicion = int(input("\nIngrese la posición hasta la que desea ver la serie de Fibonacci: "))     #Se solicita una posición

print(f"\nSérie de Fibonacci hasta la posición {posicion}:")      #Se muestra el resultado
for i in range(posicion + 1):
    print(fibonacci(i), end=" ")

#3) Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, utilizando la fórmula 𝑛𝑚= 𝑛∗𝑛(𝑚−1). Prueba esta función en un algoritmo general.

def potencia(base, exponente):
    if exponente == 0:
        return 1  # Caso base: cualquier número elevado a 0 es 1
    else:
        return base * potencia(base, exponente - 1)

base = int(input("\nIngrese la base: "))              #Se solicita la base
exponente = int(input("Ingrese el exponente: "))      #Se solicita el exponente

resultado = potencia(base, exponente)                 #se llama a la funcion recursiva con la base y el exponente ingresado
print(f"\nResultado: {base} elevado a la {exponente} es igual a {resultado}")     #Se muestra el resultado

#4) Crear una función recursiva en Python que reciba un número entero positivo en base decimal y devuelva su representación en binario como una cadena de texto.

def decimal_a_binario(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

num = int(input("Ingrese un número entero positivo: "))       #Se solicita un número positivo

if num >= 0:  
    binario = decimal_a_binario(num)                          #se llama a la funcion recursiva con el número ingresado
    print(f"El número {num} en binario es: {binario}")        #Se muestra el resultado
else:
    print("¡Error!. Debe ingresar un número entero positivo.")
    
#5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es

def es_palindromo(palabra):
    # Caso base: si la palabra tiene 0 o 1 letras, es palíndromo
    if len(palabra) <= 1:
        return True
    # Comparar primera y última letra
    if palabra[0] != palabra[-1]:
        return False
    # Llamada recursiva con la palabra sin la primera y última letra
    return es_palindromo(palabra[1:-1])

palabra = str(input("Ingrese una palabra sin espacios ni tildes: ")).lower()      #Se solicita un número entero. Agregre .lower para unificar las letras a minusculas

palindromo = es_palindromo(palabra)       #se llama a la funcion recursiva con el parametro ingresado y se guarda en la variable palindromo

print(palindromo)     #Se muestra el resultado

#6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un número entero positivo y devuelva la suma de todos sus dígitos.

def suma_digitos(n):
    # Caso base: si el número es menor a 10, es un solo dígito, se devuelve tal cual
    if n < 10:
        return n
    # Paso recursivo: sumar el último dígito con la suma de los restantes
    return (n % 10) + suma_digitos(n // 10)

num = int(input("\nIngrese un número positivo: "))      #Se solicita un número entero

suma = suma_digitos(num)      #se llama a la funcion recursiva con el parametro ingresado y se guarda en la variable suma

print(f"La suma de todos los digitos del número {num} es: {suma}")      #Se muestra el resultados

#7) Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el nivel más bajo y devuelva el total de bloques que necesita para construir toda la pirámide.

def contar_bloques(n):
    # Caso base: si solo hay un nivel, se necesita un solo bloque
    if n == 1:
        return 1
    # Paso recursivo: sumar los bloques del nivel actual con los necesarios para los niveles superiores
    return n + contar_bloques(n - 1)

num_block = int(input("\nIngrese el número de bloques del nivel más bajo: "))   #Se solicita el número base de bloques 

total_bock = contar_bloques(num_block)      #se llama a la funcion recursiva con el parametro ingresado y se guarda en la varaible total block

print(f"{total_bock}")      #Se muestra el resultado

#8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces aparece ese dígito dentro del número.

def contar_digito(numero, digito):
    # Caso base: si el número es 0, no hay más dígitos que contar
    if numero == 0:
        return 0
    # Verificar si el último dígito del número coincide con el buscado
    if numero % 10 == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)
    
num = int(input("\nIngresa un número entero positivo: "))       #Se solicita un número entero positivo
digito = int(input("Ingresa un digito (entre 0 y 9): "))        #Se solicita un dígito

total_digito = contar_digito(num,digito)        #se llama a la funcion recursiva con el número y digito ingresado

print(f"En el número {num} el dígito {digito} aparece {total_digito} veces")        #Se muestra el resultado


