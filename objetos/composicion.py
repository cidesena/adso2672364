from cuenta import *
class Persona:
    __telefono="1234"
    __correo="a@a.com"
    
    def __init__(self,nombre,documento):
        self.__nombre=nombre
        self.__documento=documento
                
class Empleado(Persona):
    def __init__(self, nombre, documento,cargo):
        super().__init__(nombre, documento)
        self.__cargo=cargo
    
    def crearCuenta(self,numero,tipo):
        self.__cuenta=Cuenta(numero,tipo)


c1=Cuenta(12345,"ahorros")
luisito=Empleado("Luis Diaz",112233,"Gerente")
print(luisito.__dict__)
luisito.crearCuenta(111222,"corriente")
print(luisito.__dict__)
del luisito
