from random import randint

lista = ['Pedro', 'Júlia', 'Otávio', 'Eduardo']

def gera_codigo():
  return str(randint(0, 999))

nomes_estudantes = []

for i in range(len(lista)):
  nomes_estudantes.append((lista[i][0] + gera_codigo(), lista[i]))

print(nomes_estudantes)

lista_de_tuplas = []
for i in range(len(lista)):
  lista_de_tuplas.append((i, lista[i]))
print(lista_de_tuplas)