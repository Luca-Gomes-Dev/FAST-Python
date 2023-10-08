def media(nota1, nota2):
    media = (nota1 + nota2)/2
    return media

def conceito(media):
    if media > 6:
        print('Aprovado')
    elif media >= 4 and media <= 6:
        print('Verificação Suplementar')
    else:
        print('Reprovado')

    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))

    media = (nota1 + nota2)
    conceito = (media)