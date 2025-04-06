#1)Programa que imprima por pantalla el mensaje: “Hola Mundo!”

print(Hola Mundo!)

#2)Programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado

nombre = input("¿Cual es tu nombre?: ")
print(f"Hola {nombre} como estas!")

#3)Programa que pida al usuario su nombre, apellido, edad y lugar de residencia

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
residencia = input("Ingrese su lugar de residencia: ")

print(f"\nSoy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

#4)Programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.

radio = float(input("Ingrese el valor del radio: "))
area = 3.14 * (radio ** 2)
perimetro = 2 * 3.14 * radio

print(f"\nEl valor del área del cirulo es: {area:.2f} y su perimetro: {perimetro:.2f}")


#5)Programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale

segundos =int(input("Ingrese la cantidad de segundos: "))
horas = segundos /3600

print(f"\n {segundos} segundos son {horas:.2f} horas")

#6)Programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.

num = int(input("Ingrese un numero: "))
print(f"\nTABLA DE MULTIPLICAR DEL NÚMERO {num}\n")

for i in range (1, 11):
    resul = num * i
    print (f" {num} x {i} = {resul}")

#7)Programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

num1 = int(input("Ingrese el primero número que no sea 0: "))
num2 = int(input("Ingrese el segundo número que no sea 0: "))

suma = num1 + num2
resta = num1 - num2
multi = num1 * num2
div = num1 / num2

print(f"\nSuma: {suma}\nResta: {resta}\nMultiplicación: {multi}\nDivisión: {div:.1f}") 

#8)Programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal

altura = float(input("Ingrese su altura en m: "))
peso = float(input("Ingrese su peso en Kg: "))
imc = peso/(altura ** 2)

print(f"\nSu índice de masa corporal (IMC) es: {imc:.1f}")

#9)Programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit

celsius = float(input("Ingrese el valor de la temperatura en grados Celsius: "))
fahr = (9/5) * celsius + 32

print(f"\n* {celsius:.1f} grados Celsius equivalen a {fahr:.1f} grados Fahrenheit")

#10)Programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

prom = (num1 + num2 + num3) /3

print(f"\nEl promedio es: {prom:.1f}")

