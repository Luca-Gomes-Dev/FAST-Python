def inverte_numero(numero):
    # Converte o número em uma lista de dígitos
    lista_digitos = list(str(numero))
    
    # Inverte a lista de dígitos usando o método reverse()
    lista_digitos.reverse()
    
    # Converte a lista invertida de dígitos de volta para um número
    numero_invertido = int("".join(lista_digitos))
    
    return numero_invertido

# Solicita ao usuário um número inteiro
numero = int(input("Digite um número inteiro: "))

# Chama a função e exibe o número invertido
numero_invertido = inverte_numero(numero)
print("Número invertido:", numero_invertido)