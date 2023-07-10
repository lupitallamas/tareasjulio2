""" Escribir un script que permita ordenar la siguiente lista de tuplas por el segudo valor
  de cada tupla manera ascendente y descendente
     
pair_numbers = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
resultado esperado [(2,1),(1,2),(2,3),(4,4),(2,5])]
y [(2,5),(4,4),(2,3),(1,2),(2,1)]"""

def get_value(tupla):
  return tupla[1]
                      
pair_numbers = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]                
print(pair_numbers)

pair_numbers.sort(key=get_value)
print(pair_numbers)
pair_numbers.sort(key=get_value,reverse=True)
print(pair_numbers)
    
         
