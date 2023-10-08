import pandas as pd
tabela = pd.read_csv('ClientesBanco.csv', encoding="latin1")
tabela = tabela.drop('CLIENTNUM', axis=1)
#print(tabela)
tabela = tabela.dropna()
quant_categoria = tabela ['Categoria'].value_counts()
print(quant_categoria)
quant_categoria_perc = tabela ['Categoria'].value_counts(normalize=True)
print(quant_categoria_perc)

#import plotly.express as px

#for coluna in tabela:
   
    #grafico = px.histogram(tabela, x='Idade', color='Categoria')
    #grafico.show()


#print(tabela.info())
#print(tabela.describe().round(1))