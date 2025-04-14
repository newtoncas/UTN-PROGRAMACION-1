#1. función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: “Hola Mundo!”

def imprimir_hola_mundo():      #Se define la función
    print("Hola mundo!")

#P rograma Principal     
imprimir_hola_mundo()           #Se llama la función

#2.función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado.

def saludar_usuario(nom):               #Se define la función
    print(f"Hola {nom}!")

# Programa Principal     
nombre = input("Ingresa tu nombre: ")   #Se solicita datos al usuario

saludar_usuario(nombre)                 #Se llama a la función pasando el parametro

#3. función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima: “Soy
#[nombre] [apellido], tengo [edad] años y vivo en [residencia]”

def informacion_personal (nom, apellido, edad, res):                    #Se define la función
    print(f"Soy {nom} {apellido}, tengo {edad} años y vivo en {res}.")

# Programa Principal 
nombre = input("Por favor, ingrese su nombre: ")                        #Se solicita datos al usuario
apellido = input("Por favor, ingrese su apellido: ")
edad = int(input("Por favor, ingrese su edad: "))
residencia = input("Por favor, ingrese su lugar de residencia: ")

informacion_personal(nombre,apellido,edad,residencia)                   #Se llama a la función pasando el parametro

#4.dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. calcular_perimetro_
#circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. 

import math #Se importa la libreria math donde esta la función math.pi para abstraer el valor de PI

def calcular_area_circulo(radio):                   #Se define la función 
    area = round ((math.pi * (radio ** 2)),2 ) 
    return area

def calcular_perimetro_circulo(radio):              #Se define la función 
    perimetro = round((2 * math.pi * radio), 2)
    return perimetro

# Programa Principal 
r = float(input("Por favor, ingrese el radio del círculo: "))   #Se solicita datos al usuario

area = calcular_area_circulo(r)                                 #Se llama a la función pasando el parametro
perimetro = calcular_perimetro_circulo(r)                       

print(f"El área del círculo es de {area} y un perímetro es de {perimetro}")     #Se muestra por pantalla el resultado

#5.función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la cantidad de horas correspondientes.

def segundos_a_horas(segundos):             #Se define la función
    horas = round(segundos /3600, 2)
    return horas

# Programa Principal 
seg = int(input("Por favor, ingrese la cantidad de segundos (>0): "))   #Se solicita datos al usuario
horas = segundos_a_horas(seg)                                           #Se llama a la función pasando el parametro

print(f"\n El equivalente a {seg} segundos son {horas} horas.")         #Se muestra por pantalla el resultado


#6.función llamada tabla_multiplicar(numero) que reciba un número como parámetro y imprima la tabla de multiplicar de ese
#número del 1 al 10. Pedir al usuario el número y llamar a la función. 

def tabla_multiplicar(num):                                 #Se define la función
    print(f"\nTABLA DE MULTIPLICAR DEL NÚMERO {num}\n")
    for i in range (1, 11):
        resul = num * i
        print (f"{num} x {i} = {resul}")

# Programa Principal 
n = int(input("Por favor, ingrese un número entero: "))     #Se solicita datos al usuario

tabla_multiplicar(n)                                        #Se llama a la función pasando el parametro

#7.función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y devuelva una tupla con el resultado
#de sumarlos, restarlos, multiplicarlos y dividirlos 

def operaciones_basicas(a,b):           #Se define la función            
    suma = a + b
    resta = a - b
    multi = a * b
    div = round(a / b, 2)
    return (suma,resta,multi,div)
    
# Programa Principal 
num1 = float(input("Por favor, ingrese el primero número: "))                   #Se solicita datos al usuario
num2 = float(input("Por favor, ingrese el segundo número que no sea 0: "))

while num2 == 0:                                                                #Bucle por si el usuario ingresa 0, se le vuelva a pedir ingresar otro numero distinto
    print("Error! El segundo número fué 0")
    num2 = float(input("Por favor, ingrese el segundo número que no sea 0: "))  #Se solicita de nuevo datos al usuario
    
suma , resta,multi,div = operaciones_basicas(num1,num2)                         #Se llama a la función pasando el parametro

print(f"\nOPERACIONES\n\nSuma: {suma}\nResta: {resta}\nMultiplicación: {multi}\nDivisión: {div:.1f}")   #Se muestra por pantalla el resultado

#8.función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, y devuelva el índice de masa corporal (IMC) 

def calcular_imc(peso, altura):                                             #Se define la función
    imc = round(peso/(altura ** 2), 2)
    return imc

# Programa Principal    
peso = float(input("Por favor, ingresa tu peso en Kilogramos: "))           #Se solicita datos al usuario

while peso <=0:                                                             #Bucle por si el usuario ingresa 0, se le vuelva a pedir ingresar otro numero distinto
    peso = float(input("Por favor, ingresa tu peso distinto de 0: "))       #Se solicita de nuevo datos al usuario
    
altura = float(input("Por favor, ingresa tu altura en metros: "))           #Se solicita datos al usuario

while altura <=0:                                                           #Bucle por si el usuario ingresa 0, se le vuelva a pedir ingresar otro numero distinto
    altura = float(input("Por favor, ingresa tu altura distinta de 0: "))   #Se solicita de nuevo datos al usuario

imc = calcular_imc(peso,altura)                                             #Se llama a la función pasando el parametro
print(f"\nSu índice de masa corporal (IMC) es: {imc}")                      #Se muestra por pantalla el resultado

#9.función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente en
#Fahrenheit. 

def celsius_a_fahrenheit(celsius):                                                      #Se define la función
    fahr = round((9/5) * celsius + 32, 2)
    return fahr

# Programa Principal 
cel = float(input("Por favor, ingrese una temperatura en °C: "))                        #Se solicita datos al usuario
fahrenheit = celsius_a_fahrenheit(cel)                                                  #Se llama a la función pasando el parametro

print(f"\n* {cel:.1f}°C grados Celsius equivalen a {fahrenheit}°F grados Fahrenheit")   #Se muestra por pantalla el resultado

#10. función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos.

def calcular_promedio(a, b, c):                                 #Se define la función
    prom = round((a + b + c) /3, 2)
    return prom

# Programa Principal 
num1 = float(input("Por favor, ingrese el primer número: "))    #Se solicita datos al usuario
num2 = float(input("Por favor, ingrese el segundo número: "))
num3 = float(input("Por favor, ingrese el tercer número: "))

promedio = calcular_promedio(num1,num2,num3)                        #Se llama a la función pasando los parametros
print(f"\nEl promedio de los números ingresados es: {promedio}")    #Se muestra por pantalla el resultado


