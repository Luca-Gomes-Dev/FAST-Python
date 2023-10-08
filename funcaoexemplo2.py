from random import randint

def sorteia():
    numeros = []
    for i in range(5):
        numeros.append(randint(0, 99))
    print(f'\nSorteando {len(numeros)} valores da lista')

    for i in numeros:
        print(f'{i}', end=' ')
        return numeros
    
def soma_par(lista_numeros):
    pares = []
    for i in lista_numeros:
            if i%2==0:
                pares.append(i)
    print(f'\nOs valores pares da lista sâo {pares}')
    print(f'E a soma deles é: {sum(pares)}\n')

soma_par(sorteia())