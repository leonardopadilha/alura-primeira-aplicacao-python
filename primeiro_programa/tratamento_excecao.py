notas = {'Joao': [8.0, 9.0, 10.0], 'Maria': [9.0, 7.0, 6.0]}
# nome = input('Digite o nome do(a) aluno(a): ')

'''
try -> Código a ser executado. Caso uma exceção seja lançada, pare imediatamente.
except -> Se uma exceção for lançada no try, rode esse código, senão, pule esta etapa.
else -> Se não houver uma exceção lançada pelo try, rode essa parte.
finally -> Rode essa parte (com ou sem exceção)


try:
  resultado = notas[nome]
  print(f'O aluno(a) {nome} obteve média {resultado}')
except Exception as e:
  print(type(e), f'Erro: O nome {e} não foi encontrado')


try:
  resultado = notas[nome]
  print(f'O aluno(a) {nome} obteve média {resultado}')
except KeyError:
  print('Estudante não matriculado(a) na turma')


try:
  nome = input('Digite o nome do(a) aluno(a): ')
  resultado = notas[nome]
except KeyError:
  print('Estudante não matriculado(a) na turma')
else:
  print(f'O aluno(a) {nome} obteve média {resultado}')

'''


try:
  nome = input('Digite o nome do(a) aluno(a): ')
  resultado = notas[nome]
except KeyError:
  print('Estudante não matriculado(a) na turma')
else:
  print(f'O aluno(a) {nome} obteve média {resultado}')
finally:
  print('Fim do programa!')
