import pandas as pd
df_pokemon = pd.read_csv('pokemon.csv')
# Visualiz as 8 últimas linhas do DataFrame
print(df_pokemon.tail(8))