# Escribir un programa que contenga una función 
# que reciba una lista de palabras y devuelva la más larga.
#  Imprimir por pantalla la palabra resultante.


from p import palabra_mas_larga


def lista(palabralarga):
    palabra_mas_larga = []
    for i in palabralarga:
        palabra_mas_larga.append((len(i), i))
        palabra_mas_larga.sort()
        return palabra_mas_larga
def main():
    palabralarga = [ 'estoy' , 'haciendo', 'una', 'lista' , 'de' , 'palabras',
    'para' ,  'ver' , 'cual' , 'es' , 'la', 'mas', 'larga']
    print(palabra_mas_larga(palabralarga))
if __name__ == '__main__':
    main()