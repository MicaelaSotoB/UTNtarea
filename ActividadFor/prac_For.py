# Mostrar los números ascendentes desde el 1 al 10

# for i in range(1,11):
#     print(i)

# Mostrar los números descendentes desde el 10 al 1
# desc=10
# for i in range(1, 11):
#     print(desc)
#     desc-=1


# Ingresar un número. Mostrar los números desde 0 hasta el número ingresado.

# num=int(input("Ingrese un numerito: "))
# contador=0
# for i in range(num+1):
#     print(contador)
#     contador+=1

# Ingresar un número y mostrar la tabla de multiplicar de ese número. Por ejemplo si se ingresa el numero 5:

# 	5 x 0 = 0
# 	5 x 1  = 5
# 	5 x 2 = 10
# 	5 x 3  = 15 …

# num=int(input("Ingrese un numero para mostrar su tabla: "))

# for i in range(11):
#     print(f"{num} x {i}={num*i}")


# Se ingresan un máximo de 10 números o hasta que el usuario ingrese el número 0. 
# Mostrar la suma y el promedio de todos los números.
# suma=0
# for i in range(11):
#     numeros=int(input("Ingrese un numero a sumar: "))
#     if numeros != 0:
#         suma+=numeros
#     else:
#         break

# promedio=suma/i
# print(promedio)

# Imprimir los números múltiplos de 3 entre el 1 y el 10.


# for i in range(1, 11):
#     print(f"3 x {i}={3*i}")
#     if i%3==0:
#         print(f"{i} es múltiplo de 3")


# Mostrar los números pares que hay desde la unidad hasta el número 50.

# for i in range(1, 51):
#     if i%2==0:
#         print(f"{i} Es número par")

# Realizar un programa que permita mostrar una pirámide de números. 
# Por ejemplo: si se ingresa el numero 5, la salida del programa será la siguiente:

# num=int(input("Ingrese un numero para empear la piramide: "))
# for i in range(num):
#     for j in range(1, i+2):
#         print(j, end='')
#     print()

# Ingresar un número. Mostrar todos los divisores que hay desde el 1 hasta el número ingresado. 
# Mostrar la cantidad de divisores encontrados.

# num=int(input("Ingrese un numero: "))
# for i in range(1, num):
#     print(i)
#     if num%i==0:
#         print(f"{i} es divisor de {num}")

# Ingresar un número. Determinar si el número es primo o no.

# num=int(input("Ingrese para saber si es un numero primo: "))
# cant_divisores=2
# for i in range(2, num):
#     if num % i ==0:
#         cant_divisores+=1
# if cant_divisores==2:
#     print("Es primo")


# Ingresar un número. Mostrar cada número primo que hay entre el 1 y el número ingresado.
# Informar cuántos números primos se encontraron.

# num=int(input("Ingrese para saber si es un numero primo: "))
# cant_divisores=2
# cant_primos=0
# for i in range(2, num):
#     if num % i ==0:
#         cant_divisores+=1
#         cant_primos+=1
#     if num% i== 0 and cant_divisores==2:
#         # cant_primos+=1
#         print(f"El {i} es primo en el recorrido hasta {num}")
# print(f"Se encontraron{cant_primos} mintras llegabamos a {num}")

# Me falta arreglar este, toy cansado por hoy