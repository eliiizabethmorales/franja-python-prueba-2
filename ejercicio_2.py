# Escriba un programa que pida dos palabras y diga si riman o no.
#  Si coinciden las últimas tres letras tiene que decir que riman. 
# Si coinciden sólo las últimas dos tiene que decir que riman un poco. 
# Y si no coinciden, decir que no riman. 
# Validar que las palabras tengan al menos tres letras. Nota: Utilizar slices


def main():
    palabra1 = input("hola ingrese una palabra: ")
    palabra1 = palabra1.upper()
    palabra2 = input("ingrese otra palabra: ")
    palabra2 = palabra2.upper()

    if palabra1[-3:] == palabra2[-3:]:
        print("las palabras si riman")
    elif palabra1[-2:] == palabra2[-2:]:
        print("las palabras riman poco")
    else:
        print("las palabras no riman")

if __name__ == '__main__':
    main()