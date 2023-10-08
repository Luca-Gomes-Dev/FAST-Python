import numpy as np

vendas = []

for i in range (5):
    venda = float(input(f'Digite a vendas{i+1}: '))
    vendas.append(venda)

vendas = np.array(vendas)
    
media_vendas = np.mean(vendas[:10])

vendas_acima_de_1000 = vendas[:10] > 1000

print(f"Média de vendas nos primeiros 10 dias: {media_vendas:.2f}")
if np.any(vendas_acima_de_1000):
    print("Houve pelo menos um dia com vendas acima de 1000.")
else:
    print("Não houve nenhum dia com vendas acima de 1000.")