from consultorio import *

nombre_paciente=input("Ingrese el nombre del paciente: ")
peso = float(input("Ingrese peso del paciente: "))
altura = float(input("Ingrese altura del paciente: "))
temperatura = float(input("Ingrese temperatura del paciente: "))
presion_sistolica = float(input("Ingrese presión sistólica: "))
presion_diastolica = float(input("Ingrese presión diastólica: "))

diagnostico = cargar_consultas(nombre_paciente, peso, altura, temperatura, presion_sistolica, presion_diastolica)
print(diagnostico)

