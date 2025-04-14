#1. función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: “Hola Mundo!”

def imprimir_hola_mundo():
    print("Hola mundo!")

# Programa Principal     
imprimir_hola_mundo()

#2.función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado.
#Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. 

def saludar_usuario(nom):
    print(f"Hola {nom}!")

# Programa Principal     
nombre = input("Ingresa tu nombre: ")

saludar_usuario(nombre)

#3. función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima: “Soy
#[nombre] [apellido], tengo [edad] años y vivo en [residencia]”

def informacion_personal (nom, apellido, edad, res):
    print(f"Soy {nom} {apellido}, tengo {edad} años y vivo en {res}.")

# Programa Principal 
nombre = input("Por favor, ingrese su nombre: ")
apellido = input("Por favor, ingrese su apellido: ")
edad = int(input("Por favor, ingrese su edad: "))
residencia = input("Por favor, ingrese su lugar de residencia: ")

informacion_personal(nombre,apellido,edad,residencia)

#4.dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. calcular_perimetro_
#circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas
#funciones para mostrar los resultados. 
import math

def calcular_area_circulo(radio):
    area = round ((math.pi * (radio ** 2)),2 )
    return area

def calcular_perimetro_circulo(radio):
    perimetro = round((2 * math.pi * radio), 2)
    return perimetro

# Programa Principal 
r = float(input("Por favor, ingrese el radio del círculo: "))

area = calcular_area_circulo(r)
perimetro = calcular_perimetro_circulo(r)

print(f"El área del círculo es de {area} y un perímetro es de {perimetro}")

#5.función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la cantidad de horas correspondientes.

def segundos_a_horas(segundos):
    horas = round(segundos /3600, 2)
    return horas

# Programa Principal 
seg = int(input("Por favor, ingrese la cantidad de segundos (>0): "))
horas = segundos_a_horas(seg)

print(f"\n El equivalente a {seg} segundos son {horas} horas.")

#6.función llamada tabla_multiplicar(numero) que reciba un número como parámetro y imprima la tabla de multiplicar de ese
#número del 1 al 10. Pedir al usuario el número y llamar a la función. 

def tabla_multiplicar(num):
    print(f"\nTABLA DE MULTIPLICAR DEL NÚMERO {num}\n")
    for i in range (1, 11):
        resul = num * i
        print (f"{num} x {i} = {resul}")

# Programa Principal 
n = int(input("Por favor, ingrese un número entero: "))

tabla_multiplicar(n)

#7.función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y devuelva una tupla con el resultado
#de sumarlos, restarlos, multiplicarlos y dividirlos 

def operaciones_basicas(a,b):
    suma = a + b
    resta = a - b
    multi = a * b
    div = round(a / b, 2)
    return (suma,resta,multi,div)
    
# Programa Principal 
num1 = float(input("Por favor, ingrese el primero número: "))
num2 = float(input("Por favor, ingrese el segundo número que no sea 0: "))

while num2 == 0:
    print("Error! El segundo número fué 0")
    num2 = float(input("Por favor, ingrese el segundo número que no sea 0: "))
    
suma , resta,multi,div = operaciones_basicas(num1,num2)

print(f"\nOPERACIONES\n\nSuma: {suma}\nResta: {resta}\nMultiplicación: {multi}\nDivisión: {div:.1f}")

#8.función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, y devuelva el índice de masa corporal (IMC) 

def calcular_imc(peso, altura):
    imc = round(peso/(altura ** 2), 2)
    return imc

# Programa Principal    
peso = float(input("Por favor, ingresa tu peso en Kilogramos: "))  
while peso <=0:
    peso = float(input("Por favor, ingresa tu peso distinto de 0: "))
    
altura = float(input("Por favor, ingresa tu altura en metros: "))
while altura <=0:
    altura = float(input("Por favor, ingresa tu altura distinta de 0: "))

imc = calcular_imc(peso,altura)
print(f"\nSu índice de masa corporal (IMC) es: {imc}")

#9.función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente en
#Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función. 

def celsius_a_fahrenheit(celsius):
    fahr = round((9/5) * celsius + 32, 2)
    return fahr

# Programa Principal 
cel = float(input("Por favor, ingrese una temperatura en °C: "))
fahrenheit = celsius_a_fahrenheit(cel)

print(f"\n* {cel:.1f}°C grados Celsius equivalen a {fahrenheit}°F grados Fahrenheit")

#10. función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos.

def calcular_promedio(a, b, c):
    prom = round((a + b + c) /3, 2)
    return prom

# Programa Principal 
num1 = float(input("Por favor, ingrese el primer número: "))
num2 = float(input("Por favor, ingrese el segundo número: "))
num3 = float(input("Por favor, ingrese el tercer número: "))

promedio = calcular_promedio(num1,num2,num3)
print(f"\nEl promedio de los números ingresados es: {promedio}")