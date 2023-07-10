"""Escribe un programa tipo "Caja registradora", que permita introducir una lista de artículos, 
cantidad y precio. Al final debe mostrarle 
al usuario la cantidad de artículos y la cantidad a cobrar (editado) """
def valida_int(pregunta:str)->int:
    dato=" "
    while dato.isdigit() == False:
        dato=input(pregunta)
    return int(dato)

def valida_float(pregunta:str):
    dato=" "
    #while dato.isdecimal() == False:
    dato=input(pregunta)
    return float(dato)

compra=[]
sub_total= 0.0
iva = 0.0
total =0.0
num_articulos = 0
articulo =""
cantidad = 0
precio = 0.0
finish ='C'
contador=0
valida_entrada=""
print('\n\n\n\t\t\t ------CAJA REGISTRADORA------ ')
print('....Para terminar tu cuenta oprime T/t en los dos puntos ":"')
while finish not in [ 'T','t']:
    articulo=input('Articulo: ')
    cantidad=valida_int('Cantidad: ')
    precio=valida_float('Precio: ')
    compra.append({"Articulo":articulo,"Cantidad":cantidad,"Precio":precio})
    finish=input("\n :")

lista=""

compra1={}
print("\n\nARTICULO        CANTIDAD        PRECIO      SUBTOTAL")
for item in compra:
    #compra1=item  
    #print(compra1.values())
    for k,v in item.items():
        lista=lista+"     " +str(v)+"      "
        if k=="Cantidad":
            cantidad=v
        elif k=="Precio":
            precio=v
            
    print(lista,"%.2f" % cantidad*precio)
    sub_total=sub_total+(cantidad*precio)
    lista=""  
    
iva=sub_total * 0.16
total =sub_total*1.16  

print("\nTotal de Articulos:\t ",len(compra))
print("SubTotal:\t\t ","%.2f" % sub_total)
print("Iva:\t\t\t","%.2f" % iva)
print("Total:\t\t\t","%.2f" % total)