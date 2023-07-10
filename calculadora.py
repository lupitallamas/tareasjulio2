"""Escribe un programa que emule el funcionamiento de una calculadora simple. 
Este es un posible ejemplo de la ejecución del programa en una terminal:"""


def suma(numero1:float, numero2:float):
    cuenta=numero2 + numero1
    return cuenta

def restar(numero1:float, numero2:float):
    cuenta=numero2 - numero1
    return cuenta

def dividir(numero1:float, numero2:float):
    cuenta=numero2 / numero1
    return cuenta

def multiplicar(numero1:float, numero2:float):
    cuenta=numero2 * numero1
    return cuenta

    
sigue="C"
numero1=0.0
numero2=0.0
numero_convertir=""

while sigue in ["C"] :
    numero=input("$")
    numero1=0

    numero_convertir=numero.replace("+","")
    numero_convertir=numero_convertir.replace("-","") 
    numero_convertir=numero_convertir.replace("*","")
    numero_convertir=numero_convertir.replace("/","")
    
    print(numero_convertir)
    numero1=float(numero_convertir)
    
    if numero.find("+")>-1:
        resultado=suma(numero1,numero2)
    elif numero.find("-")>-1:
        resultado=restar(numero1,numero2)
    elif numero.find("*")>-1:
        resultado=multiplicar(numero1,numero2)
    elif numero.find("/")>-1:
        resultado=dividir(numero1,numero2)
    elif numero.find("C") > -1:
        sigue="S"       
    else:
        resultado=float(numero)
        numero2=float(numero)
    
    numero2=resultado
    print(resultado)