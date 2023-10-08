import pandas as pd

data = {
    'Aluno': ['Aluno1', 'Aluno2', 'Aluno3', 'Aluno4', 'Aluno5'],
    
   
    'Disciplina1': [7.5, 8.0, 6.5, 4.0, 9.0],
    'Disciplina2': [6.0, 6.5, 7.0, 5.5, 8.5],
    'Disciplina3': [8.0, 7.5, 6.0, 4.5, 9.5]
}

df = pd.DataFrame(data)


df['Média'] = df[['Disciplina1', 'Disciplina2', 'Disciplina3']].mean(axis=1)

alunos_abaixo_da_media = df[df['Média'] < 7.0]

print(df)
print('Alunos com média abaixo de 7 :', alunos_abaixo_da_media)