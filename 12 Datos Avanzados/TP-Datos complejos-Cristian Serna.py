#1) Dado el diccionario precios_frutas  Añadir las siguientes frutas con sus respectivos precios

precios_frutas = {      # Diccionario inicial
    'Banana': 1200,
    'Ananá': 2500,
    'Melón': 3000,
    'Uva': 1450
}

precios_frutas['Naranja'] = 1200    # Agregar nuevas frutas y precios
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

# print(precios_frutas)       # Se muestra el resultado

#2) actualizar los precios de las siguientes frutas: Banana, Manzana, Melon

precios_frutas = {      # Diccionario inicial
    'Banana': 1200,
    'Ananá': 2500,
    'Melón': 3000,
    'Uva': 1450
}

precios_frutas['Naranja'] = 1200    # Agregar nuevas frutas y precios
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

precios_frutas['Banana'] = 1330     # Se actualizan los precios
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print("Precios actualizados:\n")
for fruta, precio in precios_frutas.items():
    print(f"{fruta}: {precio}")

#3) crear una lista que contenga únicamente las frutas sin los precios.

precios_frutas = {      # Diccionario inicial
    'Banana': 1200,
    'Ananá': 2500,
    'Melón': 3000,
    'Uva': 1450
}

precios_frutas['Naranja'] = 1200    # Agregar nuevas frutas y precios
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

lista_frutas = list(precios_frutas.keys())      # Crear la lista solo con las frutas (las claves)

print(lista_frutas)     # Mostrar la lista

#4) Escribí un programa que permita almacenar y consultar números telefónicos.

contactos = {}     #se crea diccionario vacio

print("Ingresa 5 contactos con sus respectivos números:\n")    
for i in range(5):
    nombre = input(f"Ingresá el nombre del contacto {i+1}: ")       #sE solicita un nombre de contacto
    numero = int(input(f"Ingresá el número de {nombre}: "))         #Se solicita el numero del contacto ingresado
    contactos[nombre] = numero      #Se asocia el número al nombre de contacto ingresado
nombre_busqueda = input("\nIngrese el nombre que quieres buscar: ") #Se solicita el nombre para buscar el número 

if nombre_busqueda in contactos:        #Condicional para comprobar si el nombre esta en la lista de contacto o no
    print(f"El número de {nombre_busqueda} es: {contactos[nombre_busqueda]}")   #Se muestra los resultados
else:
    print(f"{nombre_busqueda} no es un contacto agendado.")                     #Se informa que el nombre del contacto ingresado no esta agendado


#5) Solicita al usuario una frase e imprime:Las palabras únicas (usando un set). Un diccionario con la cantidad de veces que aparece cada palabra.

frase = input("Ingrese una frase: ")    #Se solicita una frase

palabras = frase.split()                #se usa .split() separar en palabras la frase

palabras_unicas = set(palabras)         #Se obtienen palabras únicas con set

recuento = {}                           #Se crea una lista vacia

for palabra in palabras:                #Se itera palabra por palabra verificando con el condicional
    if palabra in recuento:
        recuento[palabra] += 1
    else:
        recuento[palabra] = 1


print("\nLas palabras únicas de la frase son:", palabras_unicas)  #Se muestran las palabras unicas
print("Recuento de las palabras:", recuento)                #Se muestra el recuento

#6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. Luego, mostrá el promedio de cada alumno.

alumnos = {}

#Doble estructuras for anidadas
for i in range(3):  
    nombre = str(input(f"\nIngresa el nombre del alumno {i+1}: "))  #Se solicita el ingreso de nombre de cada alumno
    notas=[]    
    for j in range(3):
        nota = int(input(f"Ingresa la nota {j+1}: "))   #Se solicita la nota del alumno
        notas.append(nota)                              #Se guarda la nota siguiente de la anterior
    alumnos[nombre] = tuple(notas)
print("\nPROMEDIOS DE NOTAS DE ALUMNOS\n")

for nombre, notas in alumnos.items():       #Doble estructuras fo anidades para mostrar el promedio de cada alumno
    suma = 0
    cantidad = 0
    for nota in notas:
        suma += nota
        cantidad += 1
    promedio = suma / cantidad
    print(f"{nombre}: {promedio:.2f}")

#7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2

# Datos de ejemplo 
aprobados_parcial1 = {10, 15, 18, 11, 12}
aprobados_parcial2 = {15, 17, 18, 13, 15}

ambos_parciales = aprobados_parcial1 & aprobados_parcial2   # Estudiantes que aprobaron ambos parciales 
print(f"Aprobaron ambos parciales: {ambos_parciales}")

solo_uno = aprobados_parcial1 ^ aprobados_parcial2          # Estudiantes que aprobaron solo uno (diferencia simétrica)
print(f"Aprobaron solo un parcial: {solo_uno}")

total_aprobados = aprobados_parcial1 | aprobados_parcial2   # Lista total de aprobados en al menos un parcial (unión)
print(f"Total de aprobados (al menos uno): {total_aprobados}")


#8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. 

# Stock inicial con productos y cantidades de cada uno
productos_stock = {
    "monitor": 100,
    "teclado": 55,
    "mouse": 33,
    "impresora": 20    
}

# Menu de operaciones
while True:
    print("\n\n******* GESTION DE STOCK *******")
    print("\n1. Consultar el stock de un producto. ")
    print("2. Agregar unidades al stock si el producto ya existe.")
    print("3. Agregar un nuevo producto si no existe.")
    print("4. Salir\n")

    try:
        opcion = int(input("Selecciona una opción (1-4): "))    #Se solicita el ingreso de la opcion comprendida entre 1 y 4
    except ValueError:
        print("Error! Ingresa una opcion válida (1-4)")         # Se muestra error si la opcion ingresada no esta comprendida entre 1 y 4
        continue
    # Se compara las opciones seleccionadas
    if opcion == 1:
        producto = input("\nIngresa el producto a consultar: ").lower() #Se solicita el ingreso del nombre del producto a consultar
        if producto in productos_stock:
            print(f"- {producto}: {productos_stock[producto]} unidades") #Se muestra el producto y las cantidades en stock
        else:
            print("Stock vacío.")
    
    elif opcion == 2:
        producto = input("\nIngresa el producto para agregar unidades de stock: ").lower()  #Se solicita el ingreso del nombre del producto para agregar al stock
        if producto in productos_stock:
            cantidad = int(input(f"Ingresa la cantidad de {producto} a agregar: "))         #Se solicita la cantidad de producto para agregar al stock
            productos_stock[producto] += cantidad
        else:
            print("Sin stock")
    
    elif opcion == 3:
        nuevo_producto = input("\nIngresa el nombre del nuevo producto: ").lower()      #Se solicita el nombre del nuevo producto para agregar al stock
        if nuevo_producto in productos_stock:
            print("El producto ya existe")
        else:
            cantidad = int(input(f"Ingresa la cantidad de {nuevo_producto}: "))        #Se solicita la cantidad de producto 
            productos_stock[nuevo_producto] = cantidad
    
    elif opcion == 4:
        print("Saliendo")       #Se sale del programa
        break
    
    else:
        print("Opción no válida. Elige una opcion (1-4)")  



#9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos

agenda = {                                  # Diccionario inicial
    ("lunes", "10:00"): "Reunion",
    ("martes", "15:00"): "Clase de ingles"
}

def consultar_evento(dia, hora):        # funcion para agendar y visualizar los eventos segun el dia y la hora
    evento = agenda.get((dia.lower(), hora))
    if evento:
        print(f"El {dia} a las {hora} tienes: {evento}")
    else:
        print(f"No hay eventos programados el {dia} a las {hora}.")
        
consultar_evento("lunes", "10:00")   # Muestra el evento del lunes a las 10:00 "Reunión"
consultar_evento("martes", "09:00")  # No muestra eventos



#10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo diccionario donde

original = {                        # Diccionario inicial
    "Argentina": "Buenos Aires", 
    "Chile": "Santiago",
    "Colombia": "Bogota"
}


invertido = {capital: pais for pais, capital in original.items()}

print(invertido)