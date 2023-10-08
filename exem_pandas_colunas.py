import pandas as pd

df_pokemon = pd.read_csv('pokemon.csv')
# Criar coluna Total e somando os valores
df_pokemon['total'] = df_pokemon['HP'] + df_pokemon['Attack'] + df_pokemon['Defense'] + df_pokemon['Sp. Atk'] + df_pokemon['Sp. Def'] + df_pokemon['Speed']

print(df_pokemon['total'])
print(df_pokemon)
