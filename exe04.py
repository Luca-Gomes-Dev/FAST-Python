import numpy as np

# Dados de vendas nos primeiros 10 dias (substitua com seus próprios dados)
vendas = np.array([800, 1100, 900, 750, 1200, 950, 1050, 980, 800, 1300])

# Calcular a média de vendas nos primeiros 10 dias
media_vendas = np.mean(vendas[:10])

# Verificar se houve algum dia em que as vendas foram maiores que 1000
vendas_acima_de_1000 = vendas[:10] > 1000

# Exibir os resultados
print(f"Média de vendas nos primeiros 10 dias: {media_vendas:.2f}")
if np.any(vendas_acima_de_1000):
    print("Houve pelo menos um dia com vendas acima de 1000.")
else:
    print("Não houve nenhum dia com vendas acima de 1000.")
    
