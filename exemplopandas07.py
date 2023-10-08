import pandas as pd
df_pokemon = pd.read_csv('pokemon.csv')
# Ordenar pokemons por nomes
print(df_pokemon.sort_values (['Name','Type 1']))