import pandas as pd

alunos = [['Luiz',8.5],
          ['Rickson',7.8],
          ['João',5.5], 
          ['Luciano',6.5], 
          ['Maria',8.9]]

df_alunos = pd.DataFrame(alunos, columns=['Nome', 'Media'])
status = ['Aprovado', 'Aprovado', 'Reprovado', 'Reprovado', 'Aprovado']
df_alunos['Status'] = status 

df_aprovados = df_alunos[df_alunos['Status'] == 'Aprovado']
print(df_aprovados)
