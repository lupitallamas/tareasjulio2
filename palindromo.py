"""Escribe un programa que pueda identificar si una palabra o frase es un palíndromo"""

def is_palindromo(word_pal:str):
    word_pal=word_pal.lower()
    reversa=len(word_pal)-1
    for i in range(0,len(word_pal)):
        if word_pal[i] == word_pal[reversa]:
            reversa -= 1
        else:
            return False
    return True


continua="S"

while continua in["S","s","N","n"]:
    palabra=input("\n\n Dame Tu palabra: ")
    if is_palindromo(palabra)== True:
        print(".....La palabra: ",palabra," es un palindromo")
    else:
        print(".....La palabra: ", palabra, " No es un palindromo") 
    continua= input("Deseas chechar otra palabra? (S/N):")