notas = [[8.0, 9.0, 10.0], [9.0, 7.0, 6.0], [3.4, 7.0, 7.0], [5.5, 6.6, 8.0], [6.0, 10.0, 9.5]]

def media(lista: list = [0]) -> float:
  return sum(lista) / len(lista)

medias = [round(media(nota), 1) for nota in notas]
print(medias)

nomes = [('João', 'J720'), ('Maria', 'M205'), ('José', 'J371'), ('Cláudia', 'C546'), ('Ana', 'A347')]
medias = [9.0, 7.3, 5.8, 6.7, 8.5]

# Gerando a lista de nomes (extraindo da tupla)
# nomes = [exp for item in lista]
nomes = [nome[0] for nome in nomes]
print(nomes)

estudantes = list(zip(nomes, medias))
print(estudantes)

medias_alunos_zip = [f'{n1} - {m1}' for n1, m1 in zip(nomes, medias)]
print(medias_alunos_zip)

candidatos = [estudante[0] for estudante in estudantes if estudante[1] > 8.0]
print(candidatos)