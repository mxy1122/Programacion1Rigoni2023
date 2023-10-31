"""8)Diseñar una función que calcule el área y el perímetro de una circunferencia.
Utiliza dicha función en un programa principal que lea el radio de una circunferencia y muestre su área y perímetro
"""
import math

def funcion(radio):

    perimetro = 2 * math.pi * radio

    area = math.pi * (radio * radio)

    return (perimetro,area)


print("ingrese el radio de una circunferencia")
radio=int(input(":"))
print("El area y el perimetro de la circunferencia con radio ",radio," es perimetro y radio :",funcion(radio))

"""9. Crear una subrutina llamada “login”, 
que recibe un nombre de usuario y una contraseña y
te devuelve Verdadero si el nombre de usuario es “usuario1” y la contraseña es “asdasd”.
Además recibe el número de intentos que se ha intentado hacer login y si no se ha podido hacer login incremente este valor.
Crear un programa principal donde se pida un nombre de usuario y una contraseña y se intente hacer login, 
solamente tenemos tres oportunidades para intentarlo.
"""
def login(usuario,contraseña,intentos):
    if usuario == "usuario1" and contraseña == "asdasd":
        return True,intentos
    else:
        intentos += 1
        return False,intentos
intentos = 0
while intentos < 3:
    usuario = input("Ingrese el nombre de usuario :")   
    contraseña = input("Ingrese el nombre de usuario :")  
    entrada,intentos= login(usuario,contraseña,intentos)
    cont = (3 - intentos)
    if entrada == True:
        print("felicidade ha ingresado correctamente")
        break
    else:
        print("la contraseña o el usuario es incorrecto pruebe de nuevo ")
    if intentos < 3 :
        print("le queda ",cont,"intentos pruebe otra vez")
    else:
        print("se ha quedado sin intentos mala suerte")           

#13)Escribir una función que calcule el módulo de un vector.

import math

def module_vector(x, y):
    module = math.sqrt(x*2 + y*2)
    return module

x =int(input("ingrese un valor para x:"))
y =int(input("ingrese un valor para y:"))
module = module_vector(x, y)
print("El módulo del vector x =", x, "y y =", y, "es", module)

#14)Requerir al usuario que ingrese un número entero e informar si es primo o no, utilizando una función booleana que lo decida.


def even_or_odd(x):

    if x < 0:
        print("ingrese un numero valido")
    else:
        if x % 2==0 :
            return True
        else:
            return False

x = int(input("ingrese un numero:"))

Number = even_or_odd(x)
print(Number)
