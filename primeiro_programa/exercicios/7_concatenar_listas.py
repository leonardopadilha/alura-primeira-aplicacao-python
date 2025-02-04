# Você recebeu uma demanda para tratar 2 listas com os nomes e sobrenomes de cada estudante
# concatenando-as para apresentar seus nomes completos na forma Nome e Sobrenome. As listas são:
nomes = ["João", "Maria", "José"]
sobrenomes = ["Silva", "Souza", "Tavares"]

nome_sobrenome_lambda = list(map(lambda n1, n2: f'{n1} {n2}', nomes, sobrenomes))
print(nome_sobrenome_lambda)

# Usa zip para combinar as listas e list comprehension para concatenar
# zip(nomes1, nomes2) -> Combina os elementos das duas listas em pares
nome_sobrenome_zip = [f'{n1} {n2}' for n1, n2 in zip(nomes, sobrenomes)]
print(nome_sobrenome_zip)

nome_completo = list(map(lambda nome, sobrenome: f'{nome} {sobrenome}', nomes, sobrenomes))
for i in range(len(nome_completo)):
  print(f'Nome completo: {nome_completo[i]}')