"""Escribe una función que permita identificar si un número dado es primo o no."""

def es_primo(primo:int):
    for i in range(2,primo):
        if primo%i== 0:
            return False
        return True    

sigue = 'S'
dato=" "
while sigue in['S','s']:
    dato="d"
    while dato.isdigit()==False:
        dato=input("\n\n\t\t\ Dame el número a checar: ")
    if es_primo(int(dato)):
        print('\n\t\t\t El número: ',dato," Es un número primo")
    else:
        print('\n\t\t\tEl número: ',dato," No es un número primo")
    
    sigue=input("-----Deseas checar otro número (S/N): ")    
        