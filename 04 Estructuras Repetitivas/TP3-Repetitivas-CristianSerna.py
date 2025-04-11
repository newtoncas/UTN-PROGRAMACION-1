#1)Programa que imprima en pantalla todos los números enteros desde 0 hasta 100. (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for i in range (101):       #bucle que itera de 1 a 100 y muestra por pantalla cada iteración
    print(i)                #SE MUESTRA EL RESULTADO POR PANTALLA

#2)Programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.   

num = int(input("Ingrese un número entero: "))          #Se pide al usuario un numero entero

if num < 0:                                             #Si el numero es negativo se pasa a positivo
    num2 = -num                
    digitos = len(str(num2))                            #Con la funcion "str"se convierte la variable num a cadena. Con la funcion "len" se calcula la cantidad de digitos de la cadena
    print(f"El numero {num} tiene: {digitos} digitos")  #SE MUESTRA POR PANTALLA SI EL RESULTADO ES NEGATIVO
else:                
    digitos = len(str(num))                        
    print(f"El numero {num} tiene: {digitos} digitos")  #SE MUESTRA POR PANTALLA SI EL RESULTADO ES POSITIVO
    
#3)Programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.

num1 = int(input("Ingrese el primer número: "))  #Se pide al usuario un numero entero
num2 = int(input("Ingrese el segundo número: ")) #Se pide al usuario otro numero entero
total = 0                                        #Se declara la variable total con un valor incial 0
i = num1                                         #Se declara contador y se inicializa con el valor del primer numero

if num1 < num2:
    
    while i < num2 -1:
        i = i + 1
        total = total + i
else:
    i = num2
    while i < num1 -1:
        i = i + 1
        total = total + i

print(f"La suma de los valores comprendidos entre {num1} y {num2} es: {total}")  #SE MUESTRAN LOS RESULTADOS POR PANTALLA

#4)Programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

num = int(input("Ingrese un número (distino de 0): "))              #Se pide al usuario un numero entero

if num != 0:                                                        #Se inicia las operaciones si el número es diferente a 0
    total = num
    while num != 0:                                                 #bucle que itera hasta que el usuario ingrese "0"
        num = int(input("Ingrese un número (distino de 0): "))
        total = total + num                                         #Acumulador de todos los numero ingresados por el usuario
    print(f"\nEl valor total acumulado es: {total}")                #SE MUESTRA POR PANTALLA EL RESULTADO TOTAL
else:
    print("No se ingresaron valores para acumular")
  
#5)Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
import random

aleatorio = random.randint(0, 9)                                       #Se generan un numero aleatorio del 0 al 9
intentos = 1

num = int(input("Ingrese el posible número (0 - 9): "))                #Se solicita al usuario un numero para compararlo con el numero a adivinar                                                                                  #Se inicializa el contador

while num != aleatorio:                                                 #Mientras no coincida el numero aleatorio con el ingresado por el usuario se iterará 
      num = int(input("Ingrese el posible numero (0 - 9): "))
      intentos = intentos + 1

print(f"\n¿Felicidades! el número era {num} y te costó {intentos} intentos")    #SE MUESTRAN RESULTADOS POR PANTALLA

#6)Programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.

for i in range (100,-1,-1):  #Iteracion desde 100 hasta 0 decrementandose el valor inicial en 1 con cada iteración    
    if i%2 == 0:            #Se verifica si el número es par
        print(i)            #SE MUESTAN POR PANTALLA SI EL NÚMERO ES PAR

#7)Programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.

num = int(input("Ingrese un número: "))                                     #Se solicita un número al usuario

if num > 0:
    i = 0                                                                       #Se declara el contador con valor 0
    total = 0                                                                   #Se declara el acumulador con valor 0

    while i < num:                                                              #Iteracion mientras el contador sea menor que el numero dado por el usuario
        i = i +1                                                                #Incremento del contador
        total = total + i                                                       #Incremento del acumulador

    print(f"La suma de los números comprendidos entre 0 y {num} es: {total}")   #SE MUESTRAN RESULTADOS POR PANTALLA
else:
    print("Error: Debe ingresar un número entero positivo mayor que cero.")
    
#8)Programa que permita al usuario ingresar 100 números enteros . . .

par = 0                                                 #INICIACION DE VARIABLES
impar = 0
neg = 0
pos = 0

for i in range (1,101):                                 #Iteracion de 1 a 100
    num = int(input("Ingrese un número entero: "))      #Se solicita un número al usuario
    
    if num%2 == 0:                                      #Se verifica si el número es par
        par = par + 1                                   #Incremento a acumulador
    else:
        impar = impar + 1
    
    if num > 0:                                         #Se verifica si el número es positivo
        pos = pos + 1
    elif num < 0:                                       #Se verifica si el número es negativo
        neg = neg + 1

print(f"Números pares: {par}")                          #SE MUESTRAN RESULTADOS POR PANTALLA
print(f"Números impares: {impar}")
print(f"Números Positivos: {pos}")
print(f"Números Negativos: {neg}")

#9)Programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores
media = 0                                                   #Se declaran variables con valor 0
total = 0

for i in range (1,101):                                     #bucle que iterará de 1 a 100
    num = int(input("Ingrese un número entero: "))          #Se solicita un número al usuario
    total = total + num                                     #Acumulador de los números ingresados

media = total / 100                                         #Se calcula y se guarda la media
    
print(f"La media de los números ingresados es: {media}")    #SE MUESTRA EL RESULTADO POR PANTALLA

#10)Programa que invierta el orden de los dígitos de un número ingresado por el usuario.

num = int(input("Ingrese un número: "))             #Se solicita un número al usuario

num_invertido = 0                                   #Se declara la variable con valor 0

if num < 0:                                         #Se convierte a positivo si el número es negativo
    num = -num
    
while num != 0:                                     #Mientras el número no sea 0 se ejecuta el bucle
    digito = num % 10
    num_invertido = num_invertido * 10 + digito
    num = num // 10
    
print(f"Número invertido: {num_invertido}")         #SE MUESTRA EL RESULTADO POR PANTALLA  
  