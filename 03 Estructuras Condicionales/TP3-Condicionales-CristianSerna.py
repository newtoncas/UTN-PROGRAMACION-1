#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

#Se crea la variable mayor de edad
MAYOR_EDAD = 18

# Solicitar al usuario la edad
edad = int(input("Cual es tu edad?: "))

if edad > MAYOR_EDAD:
    print("Eres mayor de edad")
else:
    print("No eres mayor de edad")
    
#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”.

# Se crea la variable Aprobado
APROBADO = 6

# Solicitar al usuario la nota
nota = float(input("Escriba su nota: "))

if nota >= APROBADO:
    print("Felicitaciones, estas aprobado!")
else:
    print("Estas desaprobado")
    
#3) Escribir un programa que permita ingresar solo números pares.

# Solicitar al usuario un numero
num = int(input("Ingrese un numero par: "))

if num % 2 == 0:
    print("Ha ingresado un numero par")
else:
    print("Por favor ingrese un número par")

#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál categorías pertenece

# Solicitar al usuario su edad
edad = int(input("Ingrese su edad: "))

if edad < 12:
    print("Eres niño/a")
    
elif edad >= 12 and edad < 18:
    print("Eres adolescente")
    
elif edad >= 18 and edad < 30:
    print("Eres adulto/a joven")
    
else:
    print("Eres adulto")

#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres

# Solicitar al usuario una contraseña
passw = input("Ingrese una contraseña de entre 8 y 14 caracteres: ")

if len(passw) >= 8 and len(passw) <= 14:
    print("Ha ingresado una contraseña correcta!")
else:
    print("Por favor ingrese una contraseña de entre 8 y 14 caracteres")

#6) escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare

# Importar las funciones
from statistics import mode, median, mean
import random

# Crear numero aleatorios del 1 al 100
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# Calcular la moda, media y mediana de los numero aleatorios
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

if media > mediana and mediana > moda:
    print("Hay sesgo postivo o a la derecha")
    
elif media < mediana and mediana < moda:
    print("Hay sesgo negativo o a la izquierda")
    
elif media == mediana == moda:
    print("No hay sesgo")
    
else:
    print("No se pudo determinar el sesgo")

#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por pantalla; en caso contrario, dejar el string tal cual lo ingresó

# Solicitar al usuario una palabra o frase
cadena = (input("Ingrese una palabra o una frase: "))

# Seleccionar la ultima letra de la frase o palabra
ultima_letra = cadena[-1]

# Se crea la variable con las vocales en mayusculas y minusculas
VOCAL = ["A","a","E","e","I","i","O","o","U","u"]

if ultima_letra in VOCAL:
    print(f"{cadena}!")
else:
    print(cadena)

#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee

# Solicitar al usuario su nombre
nombre = input("Ingrese su nombre: ")

# Mostrar el menu con las opciones
print("\n1. Si quiere su nombre en mayúsculas \n2. Si quiere su nombre en minúsculas \n3. Si quiere su nombre con la primera letra en mayuscula")

# Solicitar al usuario la opcion elegida
opcion = input("\nIngrese el número de la opcion elegida (1, 2 o 3): ")

if opcion == "1":
    print(nombre.upper())
elif opcion == "2":
    print(nombre.lower())
elif opcion == "3":
    print(nombre.title())
else:
    print("\nLa opcion elegida no es correcta")

#9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las categorías según la escala de Richter

# Solicitar al usuario la magnitud del terremoto
magnitud = int(input("Ingrese la magnitud del terremoto: "))

# Clasificar el terremoto según su magnitud
if magnitud < 3:
    categoria = "Muy leve (imperceptible)"
elif magnitud >= 3 and magnitud < 4:
    categoria = "Leve (ligerametne imperceptible)"
elif magnitud >= 4 and magnitud < 5:
    categoria = "Moderado (sentido por personas, pero generalmente no causa daños)"
elif magnitud >= 5 and magnitud < 6:
    categoria  = "Fuerte (puede causar daños en estructuras débiles)"
elif magnitud >= 6 and magnitud < 7:
    categoria = "Muy fuerte (puede causar daños significativos)"
else:
    categoria = "Extremo (puede causar graves daños a gran escala)"

#Mostrar resultado

print(f"\nEl terremoto es de categoria: {categoria}")

#10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año

# Solicitar informacion al usuario

hemisferio = input("En que hemisferio te encuentras? (Norte o Sur): ").lower()
mes = int(input("Ingrese el mes (1-12): "))
dia = int(input("Ingrese el dia : "))

if (dia > 21 and mes == 12) or (dia <= 20 and mes == 3):
    if hemisferio == "norte":
        estacion = "Estas en Invierno"
    elif hemisferio == "sur":
        estacion = "Estas en Verano"
elif (dia > 21 and mes == 3) or (dia <= 20 and mes == 6):
    if hemisferio == "norte":
        estacion = "Estas en Primavera"
    elif hemisferio == "sur":
        estacion = "Estas en Otoño"
elif (dia > 21 and mes == 6) or (dia <= 20 and mes == 9):
    if hemisferio == "norte":
        estacion = "Estas en Verano"
    elif hemisferio == "sur":
        estacion = "EStas en Invierno"       
elif (dia > 21 and mes == 9) or (dia <= 20 and mes == 12):
    if hemisferio == "norte":
        estacion = "Estas en Otoño"
    elif hemisferio == "sur":
        estacion = "Estas en Primavera"
else:
    estacion = "Fechas no validas"
    
# Mostar resultado
print(estacion)