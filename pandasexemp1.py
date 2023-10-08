import pandas as pd

estados_nordeste = [['Alagoas', 'AL', '3,4 milhoes', 'Maceio'],
                    ['Bahia', 'BA', '15,4 milhoes', 'Salvador'],
                    ['Ceará', 'CE', '9,2 milhoes', 'Fortaleza'],
                    ['Maranhão', 'CE', '9,2 milhoes', 'Fortaleza'],
                    ['Paraiba', 'PB', '4,0 milhoes', 'João Pessoa'],
                    ['Pernambuco', 'PE', '9,7 milhoes', 'Recife'],
                    ['Piaui', 'PI', '3,3 milhoes', 'Terezina'],
                    ['Rio Grande do Norte', 'RN', '3,5 milhoes', 'Natal'],
                    ['Sergipe', 'SE', '2.3 milhoes', 'Aracaju']]
                    
df = pd.DataFrame(estados_nordeste,columns=['Estado','Sigla', 'População', 'Capital'])  
idh = [0.631, 0.632, 0.682, 0.639, 0.658, 0.673, 0.646, 0.684, 0.665]
df['IDH'] = idh

#print(df.loc[0:2])

print(df.iloc[0:6,0:4])