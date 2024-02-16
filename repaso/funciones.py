def cuadrado(num):
    return num*num

print(cuadrado(10))


square = lambda x: x ** 2
print(square(100))

lambda_func = lambda x: True if x**2 >= 10 else False
print(lambda_func(2))
print(lambda_func(5))

class prueba:
    def __init__(self) -> None:
        pass

def add(a, b) -> int:
    return a + b
print(add(2, 3))
print(add.__annotations__)


def add(a,b):
    return a+b



print(add(2, 3))
print(add.__annotations__)

#   int addNumbers(int x, int y){
#         return x+y;
#     }