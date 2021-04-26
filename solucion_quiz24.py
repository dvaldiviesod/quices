# -*- coding: utf-8 -*-
import string
# Ejercicio 1
n = int(input("Ingrese el tamaño del arreglo"))
m = int(input("Ingrese el número de múltiplos"))
a = []
for i in range(1, n + 1):
    a.append(i * m)
print(a)
# Ejercicio 2
A = int(input("Ingresa el tamaño de los arreglos: "))
B = []
C = []
for i in range(0, A):
    B.append(input("Ingresa el nombre de las personas: "))
print("Los nombres ingresados son:", B)
for j in range(0, A):
    C.append(len(B[j]))
print("La longitud de los nombres {} es de {} caracteres.".format(B, C))
# Ejercicio 3
materias = ["Matemáticas", "Física", "Química", "Historia", "Lenguaje"]
notas = []
for materia in materias:
    nota = input("¿Qué nota sacaste en " + materia + "? ")
    notas.append(nota)
for i in range(len(notas)):
    print("Sacaste " + notas[i] + " en " + materias[i])
# Ejercicio 4
datos = [4, 5, 9, 10]
for i in range(0, 4):
    print(datos[i], end=" ")
print()

datos[2] = -10
for i in range(0, len(datos)):
    print(datos[i], end=" ")
print()

datos.insert(1, 11)
for i in range(0, len(datos)):
    print(datos[i], end=" ")
print()

datos.remove(5)
for i in range(0, len(datos)):
    print(datos[i], end=" ")
print()

datos = datos + [21, 22]
for i in range(0, len(datos)):
    print(datos[i], end=" ")
print()
# Ejercicio 5
alphabet = [string.ascii_lowercase]
for i in range(len(alphabet), 1, -1):
    if i % 3 == 0:
        alphabet.pop(i - 1)
print(alphabet)
# Ejercicio 6


def palindromo(palabra):
    if palabra == palabra[::-1]:
        print("La palabra ingresada es un palíndromo")
    else:
        print("La palabra ingresada no es un palíndromo")


word = input("Ingresa una palabra: ")
palindromo(word)
# Ejercicio 7
vocales = "A", "E", "I", "O", "U", "a", "e", "i", "o", "u"
nombres = []
while True:
    nombre = input("Ingrese un nombre (0 para salir): ")
    nombres.append(nombre)
    if nombre == "0":
        break
    if nombre.startswith(vocales):
        nombres.remove(nombre)
print(nombres)
