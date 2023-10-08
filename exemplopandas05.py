import pandas as pd
df_pokemon = pd.read_csv('pokemon.csv')
# Visualizar por Nomes
#print(df_pokemon['Name'])
# Visualizar por Nomes e Tipos
print(df_pokemon[['Name','Type 1']])