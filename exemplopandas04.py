import pandas as pd
df_pokemon = pd.read_csv('pokemon.csv' )
# Visualizar as informações da linhas
#print(df_pokemon.index)
print(df_pokemon.info())