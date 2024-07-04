'''
Centro de Biotecnologia Agropecuaria
fecha: 06/05/2024
aprendiz: Julian Daniel Camacho Aguilar
ficha: 2877795
version: 3.12.3
'''


#importamos el modulo random
import random

# definimos la respuesta del usuario
def user_answer():
    answer = input("¿Desea generar una lista aleatoria (si/no)?: ")
    return answer.lower()

# creamos la funcion principal del programa
def arrays():
    array = []  # ponemos la lista principal aqui
    total = 0 # ponemos esta variable para no usar la funcion sum()
    pair = []  # creamos la lista de numeros pares
    inpair = []  # creamos la lista de numeros impares

# creamos la logica para que se detenga con el cero y para que imprima las listas
    while True:
        numero_aleatorio = random.randint(0, 20)

        if numero_aleatorio!= 0:
            array.append(numero_aleatorio)
            if numero_aleatorio % 2 == 0:
                pair.append(numero_aleatorio) 
            else:
                inpair.append(numero_aleatorio)
        else:
            print("La lista generada es: ", array)
            print("--------------------------------")
            print(f"Los numeros totales de la lista son: {len(array)}")
            print("--------------------------------")
            for i in array:
                total += i
            print("la suma de los numeron generados es: ",total)
            print("--------------------------------")
            print(f"el promedio de la lista generada es: {total / len(array)}")
            print("--------------------------------")
            print("Los números pares de la lista son: ", pair)
            print("Los números impares de la lista son: ", inpair)
            break