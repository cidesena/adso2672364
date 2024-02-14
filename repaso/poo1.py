class explicacion:
    __direccion='123'   
    def __init__(self,nombre,edad):
        #print('Se activo el constructor')
        self.__nombre=nombre
        self.edad=edad    
    def getNombre(self):
        return self.__nombre
    def setNombre(self,nombre):
        self.__nombre=nombre
    def getDireccion(self):
        return self.__direccion
    # def metodo(self):
    #     print("Soy un método de la clase explicación") 

objeto=explicacion('pepe',20)
print(objeto.getNombre())
objeto.setNombre('Jose Perez')
print(objeto.getNombre())
print(objeto.getDireccion())
#objeto.metodo()
#print(type(objeto))


# def function():
#     pass
# print(type(function))


