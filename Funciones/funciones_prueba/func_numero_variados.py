def num_entero():


    """
    Ingrese un numero entero y lo retorna
    """

    num=int(input("Ingrese un numero: "))

    return num

def num_float():
    """
    Ingresa un numero y retorna un decimal
    """

    num=float(input("Ingrese un número: "))

    return num

def cadenita():
    """
    Ingresa algo y lo retorna como string
    Para mostrarlo, coloquelo en un print.
    """
    cadena=input("Ingrese lo que quiera: ")

    return cadena

def area_rectangulo(base, altura):

    """
    Ingresa la bae y altura de un rectangulo y retorna su área
    Para mostrarlo debe estar en un print con las medidas
    """
    area=base*altura

    return area

def area_circulo(radio):
    """
    Calcula el area de un circulo
    """
    area=3.1416*(radio*radio)

    return area

def es_par_o_impar(numero):
    """
    Verifica si un numero es par o impar
    """
    if numero%2==0:
        resultado=f"El {numero} es par"
    else:
        resultado=f"El {numero} no es par"

    return resultado

def par_o_impar_bool(numero):
    """
    Indica si un numero es par o no retornando un booleano
    """
    if numero%2==0:
        resultado=True
    else:
        resultado=False
    
    return resultado

def mayor_de_tres(n1, n2, n3):
    """
    Ingresa tres numeros e indica el mayor de los tres
    """
    if n1>n2 and n1>n3:
        mayor=f"El mayor es {n1}"
    elif n2>n1 and n2>n3:
        mayor=f"El mayor es: {n2}"
    else:
        mayor=f"El mayor es:{n3}"
    return mayor

def potencia(base, exponente):
    """
    Da el resultado de una potencia determinando la base y el exponente
    """
    resultado=base ** exponente

    return resultado

def tabla_de_multiplicar(base, multiplicador):
    """
    Muestra la tabla de un numero pero determinando hasta cuanto
    """
    for i in range(multiplicador+1):
        print(f"""
        {base}x{i}={i*base}""")

tabla_de_multiplicar(5,10)