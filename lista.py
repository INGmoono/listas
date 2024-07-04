'''
Centro de Biotecnologia Agropecuaria
fecha: 06/05/2024
aprendiz: Julian Daniel Camacho Aguilar
ficha: 2877795
version: 3.12.3
'''

from funciones import *

#creamos la funcion para seguir o parar segun la respuesta del usuario
def main():
    while True:
        answer = user_answer()
        if answer == "si":
            arrays()
        elif answer == "no":
            print("---Fin del programa---")
            break
        else:
            print("---Caracter invalido, intente de nuevo.")

# corremos el programa
if __name__ == "__main__":
    main()

