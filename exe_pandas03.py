import pandas as pd

df_pokemon = pd.read_csv('pokemon.csv')

df_pokemon['Combined_Types'] = df_pokemon['Type 1'] + '-' + df_pokemon['Type 2']

df_pokemon = df_pokemon[['Name','Combined_Types' ]]
print(df_pokemon.tail(5))
#print(df_pokemon[['Name', 'Combined_Types']].tail(5))