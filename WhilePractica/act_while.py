# Mostrar 10 repeticiones de números ascendentes desde el 1 al 10.

# numero=1
# while numero!=11:
#     print(numero)
#     numero+=1

# Mostrar 10 repeticiones de números descendentes desde el 10 al 1.

# numero=10
# while numero!=0:
#     print(numero)
#     numero-=1

# Mostrar la suma de los números desde el 1 hasta el 10.

# sumados=0

# while sumados<10:
#     print(sumados+1)
#     sumados+=1

# Mostrar la suma de los números pares desde el 1 hasta el 10.

# numero = 1
# pares=0
# while numero<10:
#     if numero%2==0:
#         pares+=numero
#         print(f"Suma de par:{pares}")
#     numero+=1


# Solicitar el ingreso de 5 números, calcular la suma de los números ingresados y el promedio. 
# Mostrar la suma y el promedio por pantalla.

# vueltas=0
# suma=0
# while vueltas<5:
#     numeros=int(input("Ing. un numero"))
#     suma+=numeros
#     vueltas+=1
# print("El promedio es ", suma/vueltas, "Y la suma es: ", suma)

# Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). 
# Calcular la suma de los números ingresados y el promedio de los mismos.


# print("""Ingrese el numero correspondiente de la opción que desea realizar
#         1.Sumar números
#         2.Finalizar programa.""")
# opcion=int(input("Ingrese la opcion: "))
# vueltas=0
# suma=0
# while opcion==1:
#     numero=int(input("Ingrese un numero: "))
#     suma+=numero
#     vueltas+=1
#     opcion=int(input("""Ingrese 1 si desea seguir
# Ingrese 2 si quiere salir
# Elija su opción: """))

# promedio=suma/vueltas
# print(f"Su promedio es de: {promedio}")

# Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). 
# Calcular la suma de los números positivos y el producto de los negativos.

# positivo=0
# negativos_prod=1
# numero=int(input("Ingrese un número: "))
# print("Si no quiere ingresar más numeros, ingrese 0")
# while numero!=0:
#     if numero>0:
#         positivo+=numero
#         numero=int(input("Ingrese un número: "))
#     elif numero<0:
#         negativos_prod*=numero
#         numero=int(input("Ingrese un número: "))
# print(f"Producto de los negativos insertados: {negativos_prod}. Suma de los positivos insertados: {positivo}")


# Ingresar 10 números enteros. Determinar el máximo y el mínimo.

vueltas=0
mayor=int(input("Ingrese un número: "))
menor=mayor
while vueltas<5:
    numeros=int(input("Ingrese un número: "))
    if numeros<mayor:
        vueltas+=1
    else:
        mayor=numeros
        vueltas+=1

    if numeros < menor:
        menor = numeros
print(f"Numero menor: {menor}. Numero mayor: {mayor}")