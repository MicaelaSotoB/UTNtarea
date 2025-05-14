def cargar_consultas(nombre_paciente: str, peso: float, altura: float, temperatura: float, 
                    presion_sistolica: float, presion_diastolica: float):
    analisis_imc = calc_imc(peso, altura)
    fiebre = calc_temp(temperatura)
    presion = calc_presion(presion_sistolica, presion_diastolica)
    
    diagnostico = f"""
    Diagnóstico del paciente {nombre_paciente}:
    Peso: {analisis_imc}
    Temperatura: {fiebre}
    Presión:{presion}"""
    return diagnostico


def calc_temp(temperatura):

    """Esta funcion toma el valor de la temperatura 
    y la retorna el string"""

    if temperatura > 41:
        fiebre = "Muy alta"
    elif temperatura > 39:
        fiebre = "Alta"
    elif temperatura >=38:
        fiebre = "Fiebre moderada"
    elif temperatura > 37.3:
        fiebre= "Febrícula"
    else:
        fiebre = "Temperatura normal"
    return fiebre

def calc_imc(peso, altura):

    """"Calcula el indice de masa corporal"""
    imc = peso / (altura**2)
    if imc < 18.5:
        analisis_imc = "Es necesario aumentar ingesta calórica."
    elif imc < 25:
        analisis_imc = "Peso equilibrado."
    else:
        analisis_imc = "Es necesario disminuir ingesta calórica."
    return analisis_imc

def calc_presion(presion_sis, presion_dias):

    """"Calcula la presión"""

    if presion_sis < 90 or presion_dias < 60:
        presion = "Baja"
    elif presion_sis > 140 or presion_dias < 90:
        presion = "Alta"
    else:
        presion = "Normal"
    return presion


# diagnostico = cargar_consultas("Emiliano", 40, 1.62, 38, 80, 50)
# print(diagnostico)