"""Escribe una función qué reciba varios números y devuelva el mayor de ellos."""

def numero_mayor(lista_numeros):
    #encuentra el número mayor de una lista
    mayor = 0
    mayor =lista_numeros[0]
    for item in range(0,len(lista_numeros)):
        if lista_numeros[item] > mayor :
            mayor = lista_numeros[item]
    return mayor

numeros =[]
sigue ="S"
num_mayor=0
while sigue in ["S","s"]:
    dato="D"
    while dato.isdigit() ==False:
        dato=input('Dame un número: ')
    numeros.append(int(dato))
    sigue =input('Deseas continuar (S/N) : ')
num_mayor =numero_mayor(numeros)
print('\n\t\t El número mayor de tu lista es: ',num_mayor,"\n\n")        
            