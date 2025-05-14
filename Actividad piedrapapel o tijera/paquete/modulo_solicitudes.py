def validar_texto_vacio(texto: str) -> bool:
    es_valido = True
    if texto.strip() == "":
        es_valido = False
    return es_valido

def preguntar_texto(mensaje: str) -> str:
    """
    Función para ingresar textos, valida que no sean vacío y retorna el texto ingresado
    """
    texto = input(mensaje).strip()
    while not validar_texto_vacio(texto):
        print("Debe ingresar texto, no dejar vacío")
        texto = input(mensaje).strip()
    return texto

def preguntar_entero(mensaje: str) -> int:
    numero = int(input(mensaje))
    return numero

def preguntar_int_positivo(mensaje: str) -> int:
    numero = int(input(mensaje))
    while numero < 1:
        print("Ingrese un entero positivo")
        numero = int(input(mensaje))
    return numero

def preguntar_decimal_positivo(mensaje: str) -> float:
    numero = float(input(mensaje))
    while numero < 1:
        print("Ingrese un número positivo")
        numero = float(input(mensaje))
    return numero

def preguntar_int_en_rango(mensaje: str, min: int, max=None) -> int:
    numero = preguntar_entero(mensaje)
    if max is None:
        while numero < min:
            print(f"Ingrese número mayor o igual a {min}")
            numero = preguntar_entero(mensaje)
    else:
        while numero < min or numero > max:
            print(f"Ingrese valor dentro del rango {min} y {max}")
            numero = preguntar_entero(mensaje)
    return numero

def preguntar_numero_legajo() -> str:
    n_legajo = preguntar_texto("Ingrese número de legajo de 4 cifras: ")
    while n_legajo[0] == "0" or len(n_legajo) > 4:
        print("Legajo incorrecto: sin ceros a la izquierda o más de 4 cifras")
        n_legajo = preguntar_texto("Ingrese número de legajo de 4 cifras:")
    return n_legajo

def obtener_estado_civil(numero_estado) -> str:
    if numero_estado == 1:
        estado = "Soltero/a"
    elif numero_estado == 2:
        estado = "Casado/a"
    elif numero_estado == 3:
        estado = "Divorciado/a"
    else:
        estado = "Viudo/a"
    return estado
