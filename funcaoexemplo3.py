def soma (n1, n2):
    return n1+n2
def subtracao (n1, n2):
    return n1-n2
def multiplicacao (n1, n2):
    return n1*n2
def divisao (n1, n2):
    if n1>n2:
        return n1/n2
    else:
        return n2/n1
    
continuar = input('Deseja realizar uma operação? [S] ou [N] : ').upper()
    
while continuar == "S":

    num1 = int(input('Digite o primeiro valor: '))
    num2 = int(input('Digite o segundo valor: '))
    print('\n[S] Soma [B] Subtração [M] Mutiplicação [D] Divisão')
    opcao = input('Digite a opção desejada:').upper()

    if opcao == "S":
        print(soma(num1, num2))
    elif opcao == "B":
        print(subtracao(num1, num2))
    elif opcao == "M":
        print(multiplicacao(num1, num2)) 
    else:
        print(divisao(num1, num2))  

    continuar = input('Deseja realizar uma operação? [S] ou [N] : ').upper()


    
