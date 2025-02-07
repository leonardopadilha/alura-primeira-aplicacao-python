notas_turma = ['João', 8.0, 9.0, 10.0, 'Maria', 9.0, 7.0, 6.0, 'José', 3.4, 7.0, 7.0, 'Cláudia', 5.5, 6.6, 8.0, 'Ana', 6.0, 10.0, 9.5]

nomes = []
notas = []

for i in range(len(notas_turma)):
  if i % 4 == 0:
    nomes.append(notas_turma[i])
  else:
    notas.append(notas_turma[i])

lista_de_notas = []
for i in range(0, len(notas), 3):
  lista_de_notas.append([notas[i], notas[i + 1], notas[i + 2]])

print(lista_de_notas)