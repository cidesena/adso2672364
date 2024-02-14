import random

def llenar_lista():
    temperaturas = [random.randint(10, 30) for _ in range(30)]
    return temperaturas
def calcular_mitad1(temperaturas):
    mitad1 = temperaturas[:15]
    promedio_mitad1 = sum(mitad1) / len(mitad1)
    return promedio_mitad1
def calcular_mitad2(temperaturas):
    mitad2 = temperaturas[15:]
    promedio_mitad2 = sum(mitad2) / len(mitad2)
    return promedio_mitad2
def calcular_tercio1(temperaturas):
    tercio1 = temperaturas[:10]
    promedio_tercio1 = sum(tercio1) / len(tercio1)
    return promedio_tercio1
def calcular_tercio2(temperaturas):
    tercio2 = temperaturas[10:20]
    promedio_tercio2 = sum(tercio2) / len(tercio2)
    return promedio_tercio2
def calcular_tercio3(temperaturas):
    tercio3 = temperaturas[20:]
    promedio_tercio3 = sum(tercio3) / len(tercio3)
    return promedio_tercio3
temperaturas_mes = llenar_lista()
print(temperaturas_mes)
promedio_mes = sum(temperaturas_mes) / len(temperaturas_mes)
promedio_mitad_1 = calcular_mitad1(temperaturas_mes)
promedio_mitad_2 = calcular_mitad2(temperaturas_mes)
promedio_tercio_1 = calcular_tercio1(temperaturas_mes)
promedio_tercio_2 = calcular_tercio2(temperaturas_mes)
promedio_tercio_3 = calcular_tercio3(temperaturas_mes)
print(f"Promedio de temperatura del mes: {promedio_mes}")
print(f"Promedio de temperatura de la primera mitad del mes: {promedio_mitad_1}")
print(f"Promedio de temperatura de la segunda mitad del mes: {promedio_mitad_2}")
print(f"Promedio de temperatura del primer tercio del mes: {promedio_tercio_1}")
print(f"Promedio de temperatura del segundo tercio del mes: {promedio_tercio_2}")
print(f"Promedio de temperatura del tercer tercio del mes: {promedio_tercio_3}")