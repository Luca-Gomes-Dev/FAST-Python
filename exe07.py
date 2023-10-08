import numpy as np
despesas = np.array([
    [2000, 2200, 1800],
    [2100, 2400, 1900],
    [1900, 2300, 1700],
    [2050, 2450, 1750],
    [2200, 2550, 1950]
])

media_anual = np.mean(despesas)

media_mensal = np.mean(despesas, axis=0)

meses_despesas_altas = (media_mensal > 2 * media_anual)[0]

print(f"Média anual de despesas: {np.round(media_anual,2)} ")
print(f"Média de despesas por mês:{media_mensal}")
print("Meses com despesas superiores ao dobro da média anual:", meses_despesas_altas + 1)