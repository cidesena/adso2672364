import random
lista=[]
print(type(lista))
lista=100
print(type(lista))

#indentación
def fillList(lista,tam):
    for i in range(tam):
        num=random.randrange(100)
        lista.append(num)
    return lista

mylist=[]
fillList(mylist,10)
print(mylist)

def funcioncita():
    print('Hola mundo')

funcioncita()

#desventaja lenguajes no tipados
def calcular_mitad1(temperaturas):
    mitad1 = temperaturas[:15]
    promedio_mitad1 = sum(mitad1) / len(mitad1)
    return promedio_mitad1

m='hola'
calcular_mitad1(m)