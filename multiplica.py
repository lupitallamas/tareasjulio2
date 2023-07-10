"""Escribe una función que permita multiplicar varios números"""

def multiplicar (*args:list):
    """multiplica un numero infinitos"""
    result=1
    for argument in args:
        result *=argument
    return result

sigue = "S"

print("\n \t\t Resultado: ",multiplicar(1,2,3,4,5,6,7,8,9))   