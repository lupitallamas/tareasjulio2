"""Escribe una función para verificar que un número se encuentra en un rango de números determinado. 
El resultado de esa función debe ser booleano"""




def esta_en_rango(numero,**kwargs):
       
    if numero >= kwargs["minimo"] and numero <= kwargs["maximo"]:
        return True
    return False
 
dato ="v"
rango = {}
num=0
contador=1   

      
while contador < 3:
    dato=""
    if contador ==1:
        num_letra="--Dame tu mínimo: "
    else:
        num_letra="--Dame tu maximo: " 
        
    while dato.isdigit() == False:        
        dato = input(num_letra)
    numero=int(dato)
               
         
    if contador == 1:
        rango["minimo"]=numero
        contador = contador + 1
    else:
        if rango["minimo"] < numero:
            rango["maximo"]=numero
            contador =contador + 1
            #print("contador: ",contador)
        else:
            print("\t \t.....El número maximo debe ser mayor al Mínimo")   
   
print("\n \t \t ",rango) 
dato ="D"       
while dato.isdigit() == False:        
    dato = input("Número a Verificar que se encuentre en el rango: ")
num=int(dato)

if esta_en_rango(num,**rango) == True:
    print('El numero:' ,num,' Se encuentra del rango: ',rango)  
else:
    print('El numero:' ,num,' NO Se encuentra en el rango: ',rango)
  