# Para Contar a frequência de cada palavra em uma frase, utilize o seguinte código:

frase = 'Python se tornou uma das linguagens de programação mais populares do mundo nos últimos anos.'

contagem_palavra = {}
palavras = frase.split()

for palavra in palavras:
  contagem_palavra[palavra] = contagem_palavra.get(palavra, 0) + 1
print(contagem_palavra)

# ----------------------------------------------

pessoa = {'nome': 'Teste da Silva', 'idade': 100}

if 'nome' in pessoa:
  print(pessoa.get('nome'))
else:
  print('Não existe esse dado')