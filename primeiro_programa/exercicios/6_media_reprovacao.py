# Para atender a uma demanda de uma instituição de ensino para a análise do desempenho de seus(suas)
# estudantes, você precisa criar uma função que recebe uma lista de 4 notas e retore:
# Maior nota
# Menor nota
# Média
# Situação (Aprovado(a)) ou Reprovado(a))

notas = []
for i in range(1, 5):
  nota = float(input(f"Digite a {i}ª nota: "))
  notas.append(nota)

def media_alunos(notas):
  media = round(sum(notas) / len(notas), 1)
  situacao = "Aprovado" if media > 6 else "Reprovado"
  return f'O(a) estudante obteve uma média de {media}, com a maior nota de {max(notas)} pontos e a menor nota de {min(notas)} pontos e foi {situacao}'

print(media_alunos(notas))