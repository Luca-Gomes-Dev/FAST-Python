import numpy as np

# Dados de notas dos alunos (suponha que cada linha representa um aluno)
notas = np.array([
    [7.5, 8.0, 6.5],
    [8.5, 7.0, 9.0],
    [6.0, 6.5, 7.0],
    [9.0, 7.5, 8.5],
    [7.5, 6.0, 6.0]
])

# Calcular a média das notas dos três primeiros alunos (linhas 0, 1 e 2)
media_tres_primeiros_alunos = np.mean(notas[:3, :])

# Verificar quais alunos tiraram notas acima de 7
notas_acima_de_7 = notas > 7

# Exibir os resultados
print(f"Média das notas dos três primeiros alunos: {media_tres_primeiros_alunos:.2f}")
print("Alunos que tiraram notas acima de 7:")
for i in range(len(notas)):
    if np.any(notas_acima_de_7[i]):
        print(f"Aluno {i + 1}: {notas[i]}")