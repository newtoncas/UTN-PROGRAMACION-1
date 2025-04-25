# 1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range.

lista = list (range (4,101,4))
print(lista)

# 2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el penúltimo.

lista = ["a", "b", "c", "d", "e"]
print(lista[-2])

# 3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por pantalla

lista=[]

lista.append("lunes")
lista.append("martes")
lista.append("miercoles")

print(lista)

# 4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, respectivamente. Imprimir la lista resultante por pantalla.

animales=["perro", "gato", "conejo", "pez"]

animales[1]="loro"
animales[-1]="oso"

print(animales)

# 5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.

#Se inicia la lista llamada números con los siguientes números: 8, 15, 3, 22, 7
#Con la función "max" se indentifica el número más grande de la lista
#Con la función "remove" se elimina de la lista el número mas grande.
#Se imprime por pantalla la lista "números" con los valores: 8, 15, 3, 7


# 6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por pantalla los dos primeros.

lista = list (range (10,31,5))
print(lista)

# 7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores cualesquiera.

autos = ["sedan","polo","suran","gol"]

autos[1]="ferrari"
autos[2]="mclaren"

print(autos)

# 8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append directamente. Imprimir la lista resultante por pantalla

dobles=[]

dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)

print(dobles)

# 9) Dada la lista “compras”, Agregar "jugo" a la lista del tercer cliente usando append. Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
# Eliminar "pan" de la lista del primer cliente. Imprimir la lista resultante por pantalla

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

compras[2].append("jugo")

compras[1][1] = "tallarines"

compras[0].remove("pan")

print(compras)

# 10) Elaborar una lista anidada llamada “lista_anidada”

lista_anidada = [15, True, [25.5, 57.9, 30.6], False]

print(lista_anidada)
