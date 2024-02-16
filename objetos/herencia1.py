class Persona:
    __telefono="1234"
    __correo="a@a.com"
    __cont=0
    def __init__(self,nombre,documento):
        self.__nombre=nombre
        self.__documento=documento
        self.__cont+=1

    def setTelefono(self,telefono):
        self.__telefono=telefono
    
    def getTelefono(self):
        return self.__telefono
    def getContador(self):
        return self.__cont

class Empleado(Persona):
    def __init__(self, nombre, documento,cargo):
        super().__init__(nombre, documento)
        self.__cargo=cargo

emp1=Empleado("Evelio Suarez",12345,"instructor")
print(type(emp1))
print(emp1.__dict__)

p10=Persona('Ana Jimenez',4321)
p20=Persona('john Jimenez',432)
p30=Persona('juan Jimenez',321)
#p.setTelefono(311111111)
# print(type(p))
# print(p.__dict__)
#print('------',p.getTelefono())
print(p20.getContador())

