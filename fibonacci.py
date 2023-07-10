"""Escribe una función que genere una lista con los números de la serie de fibonacci. 
La función debe recibir la cantidad de números a genera"""

def fibonacci(contador:int):
    resultado1= 0
    resultado2=1
    number_fibonacci=[]
    for contador in range(0,contador):      
        number_fibonacci.append(resultado1 + resultado2)
        resultado1 = resultado2
        resultado2 = number_fibonacci[contador]
    return number_fibonacci   
        
continuar = "S"

while continuar  in ["S","s"]:
    contador=" "
    while contador.isdigit() == False:        
        contador =input('Cuantos numeros fibonacci quieres generar: ')
       
    fibonaccis=fibonacci(int(contador))
    print("\n\nSerie fibonancci de :", contador, "numeros")
    print("\n\n ",fibonaccis)   
    continuar= input("\n\n\n\t\t Deseas generar otra serie fibonacci? (S/N):")
    print(continuar)