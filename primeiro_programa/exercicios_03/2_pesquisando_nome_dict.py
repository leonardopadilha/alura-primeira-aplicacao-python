idades = {'Júlia': 16, 'Carol': 23, 'Alberto': 19}

try:
  nome = input('Digite um nome: ')
  idade = idades[nome]
except Exception as e:
  print(type(e), f'Desculpe, tente novamente!')
except KeyError:
  print(f'Erro: O nome {nome} não foi encontrado')
else:
  print(f'A idade do(a) {nome} é {idade} anos')