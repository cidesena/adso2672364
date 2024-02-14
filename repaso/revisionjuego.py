import random

def juego():

    numero2 = random.randint(1,100)
    print(numero2)
    numero1 = int(input("Ingrese un numero del 1 al 100: ")) 
    intentos = 0

    while (numero1 < numero2):
        print("EL NUMERO QUE INGRESASTE ES MENOR QUE EL NUMERO CORRECTO")
        intentos = intentos + 1
        numero1 = int(input("Ingrese un numero del 1 al 100: "))

        if (numero1 > numero2):
            print("EL NUMERO QUE INGRESASTE ES MAYOR QUE EL NUMERO CORRECTO")
            intentos = intentos + 1
            numero1 = int(input("Ingrese un numero del 1 al 100: "))
        
        if (numero1 == numero2):
            intentos = intentos + 1
            print("HAS ADIVINADO EL NUMERO EN ",intentos," INTENTOS")

        if (intentos == 10):
            intentos = intentos + 1
            print("PERDISTE")


juego()