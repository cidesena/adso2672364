from cuenta import *
class Persona:
    __telefono="1234"
    __correo="a@a.com"
    
    def __init__(self,nombre,documento):
        self.__nombre=nombre
        self.__documento=documento
                
class Empleado(Persona):
    def __init__(self, nombre, documento,cargo,cuenta):
        super().__init__(nombre, documento)
        self.__cargo=cargo
        self.__cuenta=cuenta

c1=Cuenta(12345,"ahorros")
Luisito=Empleado("Luis Diaz",112233,"Gerente",c1)
print(Luisito.__dict__)
del Luisito
#print(Luisito.__dict__)
print(type(c1))